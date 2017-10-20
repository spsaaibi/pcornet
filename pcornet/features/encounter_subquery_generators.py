from pcornet import models, common_session
from sqlalchemy import func, and_, case, or_, tuple_, between
from pcornet.features.utils import booleans_from_list_of_dicts, booleans_from_list_of_dicts_likes

session = common_session.Session


def generate_a_yes_no_count_by_encounterid_with_dict(varlabel, tablename, list_of_dicts):
    """
    A subquery generator that gives count of column yes no according to a list of dicts. Each dict should contain a key
    that is a pcornet.models.columname and a value that is a list of acceptable inputs.
    For example, [{'raw_dx': ['410.10', '410.11'], 'raw_dx_type': ['ICD-9-CM']}, {'raw_dx': ['I21.4'], 'raw_dx_type':
    ['ICD-10-CM']}]. This would give a count of yes/no that match with AND's in the dicts and ORs between list elements.
    :param varlabel: str: resulting varaible name
    :param tablename: str: corresponding to a pcornet.model
    :param list_of_dicts: a list of strings that return yes (1); otherwise no (0)
    :return: a sqlalchemy.query.subquery that executes conditions above with both patid and encounterid
    """
    temp = session.query(
        getattr(models, tablename).patid,
        getattr(models, tablename).encounterid,
        func.sum(case(
                    [
                        (booleans_from_list_of_dicts(tablename, list_of_dicts), 1)
                    ],
                    else_=0
                )
        ).label(varlabel))\
    .group_by(
        getattr(models, tablename).patid,
        getattr(models, tablename).encounterid
    )\
    .subquery()

    return temp


def generate_a_yes_no_by_encounterid_with_dicts(varlabel, tablename, list_of_dicts):
    """
    A subquery generator that gives 0 or 1 column according to a list of dicts. Each dict should contain a key
    that is a pcornet.models.columname and a value that is a list of acceptable inputs.
    For example, [{'raw_dx': ['410.10', '410.11'], 'raw_dx_type': ['ICD-9-CM']}, {'raw_dx': ['I21.4'], 'raw_dx_type':
    ['ICD-10-CM']}]. This would give a count of yes/no that match with AND's in the dicts and ORs between list elements.
    :param varlabel: str: resulting varaible name
    :param tablename: str: corresponding to a pcornet.model
    :param list_of_dicts: a list of strings that return yes (1); otherwise no (0)
    :return: a sqlalchemy.query.subquery that executes conditions above with both patid and encounterid
    """
    temp = generate_a_yes_no_count_by_encounterid_with_dict(varlabel, tablename, list_of_dicts)

    temp2 = session.query(
        temp.c.patid,
        temp.c.encounterid,
        case([
            (getattr(temp.c, varlabel)>0, 1)
        ], else_=0).label(varlabel)
        )\
        .subquery()

    return temp2


def generate_a_cumulative_sum_by_encounterid_with_dicts(varlabel, tablename, list_of_dicts):
    """
    A subquery generator that gives a cumulative sum of match criteria by encounterid ordered by admit date.
    Each dict should contain a key that is a pcornet.models.columname and a value that is a list of acceptable inputs.
    For example, [{'raw_dx': ['410.10', '410.11'], 'raw_dx_type': ['ICD-9-CM']}, {'raw_dx': ['I21.4'], 'raw_dx_type':
    ['ICD-10-CM']}]. This would give a cumulative sum that match with AND's in the dicts and ORs between list elements.
    :param varlabel: str: resulting varaible name
    :param tablename: str: corresponding to a pcornet.model
    :param list_of_dicts: a list of strings that return yes (1); otherwise no (0)
    :return: a sqlalchemy.query.subquery that executes conditions above with patid, encounterid, Encounter.admit_date
    """
    temp = session.query(
        getattr(models, tablename).patid,
        getattr(models, tablename).encounterid,
        models.Encounter.admit_date,
        func.sum(case(
            [
                (booleans_from_list_of_dicts(tablename, list_of_dicts), 1)
            ],
            else_=0
        )
        ).label('temp')) \
        .join(models.Encounter) \
        .group_by(
        getattr(models, tablename).patid,
        models.Encounter.admit_date,
        getattr(models, tablename).encounterid
    ) \
        .subquery()

    temp2 = session.query(
        temp.c.patid,
        temp.c.encounterid,
        temp.c.admit_date,
        func.sum(temp.c.temp).over(
            #TODO: not sure if this is returning the correct cumulative sum if several dates are the same with 0 and 1.
            order_by=tuple_(
                temp.c.patid,
                temp.c.admit_date,
                temp.c.encounterid
            ),
            partition_by=tuple_(
                temp.c.patid
            )
        ).label(varlabel)) \
        .subquery()

    return temp2


def generate_allvalues_between_admit_discharge_date_with_subset(
        varlabel,
        tablename,
        date_var,
        time_var,
        value_var,
        list_of_dicts = None):
    """
    This will create a window function that will allow us to pull all occurances of a match within a window
    of an encounter. In other words, all occurances where admit_date <= date_var <= discharge_date. This is a useful
    function when no encounterid is available. This occurs in tables like lab_result_cm.
    :param varlabel:
    :param tablename:
    :param list_of_dicts:
    :param date_var:
    :param time_var:
    :param value_var:
    :return: a sqlalchemy.query.subquery that executes conditions above with both patid, admit_date, discharge_date, date_var
    """
    myfilter = booleans_from_list_of_dicts(tablename, list_of_dicts)

    temp = session.query(
        getattr(models, tablename).patid,
        getattr(getattr(models, tablename), date_var).label('date'),
        func.to_date(
            func.to_char(
                getattr(getattr(models, tablename), date_var), 'DD-MON-YY')
                + ' '
                + getattr(getattr(models,tablename), time_var),
                'DD-MON-YY HH24:MI').label('datetime'),
        getattr(getattr(models, tablename), value_var).label(value_var))\
        .filter(myfilter)\
        .subquery()

    temp2 = session.query(
        models.Encounter.patid,
        models.Encounter.encounterid,
        models.Encounter.admit_date,
        temp.c.datetime,
        models.Encounter.discharge_date,
        getattr(temp.c, value_var).label(varlabel)) \
        .join(temp, and_(
        models.Encounter.patid == temp.c.patid)) \
        .filter(between(temp.c.date,
                        models.Encounter.admit_date,
                        models.Encounter.discharge_date)) \
        .order_by(models.Encounter.patid, models.Encounter.encounterid, temp.c.datetime).subquery()

    return temp2

def generate_allvalues_between_admit_discharge_date(
        varlabel,
        tablename,
        date_var,
        time_var,
        value_var):
    """
    This will create a window function that will allow us to pull all occurances of a match within a window
    of an encounter. In other words, all occurances where admit_date <= date_var <= discharge_date. This is a useful
    function when no encounterid is available. This occurs in tables like lab_result_cm.
    :param varlabel:
    :param tablename:
    :param list_of_dicts:
    :param date_var:
    :param time_var:
    :param value_var:
    :return: a sqlalchemy.query.subquery that executes conditions above with both patid, admit_date, discharge_date, date_var
    """

    temp = session.query(
        getattr(models, tablename).patid,
        getattr(getattr(models, tablename), date_var).label('date'),
        func.to_date(
            func.to_char(
                getattr(getattr(models, tablename), date_var), 'DD-MON-YY')
                + ' '
                + getattr(getattr(models,tablename), time_var),
                'DD-MON-YY HH24:MI').label('datetime'),
        getattr(getattr(models, tablename), value_var).label(value_var)) \
        .filter(getattr(getattr(models, tablename), value_var).isnot(None)) \
        .subquery()

    temp2 = session.query(
        models.Encounter.patid,
        models.Encounter.encounterid,
        models.Encounter.admit_date,
        temp.c.datetime,
        models.Encounter.discharge_date,
        getattr(temp.c, value_var).label(varlabel)) \
        .join(temp, and_(
        models.Encounter.patid == temp.c.patid)) \
        .filter(between(temp.c.date,
                        models.Encounter.admit_date,
                        models.Encounter.discharge_date)) \
        .order_by(models.Encounter.patid, models.Encounter.encounterid, temp.c.datetime).subquery()

    return temp2


def generate_first_value_between_admit_discharge_date(
        varlabel,
        tablename,
        date_var,
        time_var,
        value_var,
        list_of_dicts = None):
    """
    This will create a window function that will allow us to pull the first occurance of a match within a window
    of an encounter. In other words, the first occurance where admit_date <= date_var <= discharge_date. This is a useful
    function when no encounterid is available. This occurs in tables like lab_result_cm.
    :param varlabel:
    :param tablename:
    :param list_of_dicts:
    :param date_var:
    :param time_var:
    :param value_var:
    :return: a sqlalchemy.query.subquery that executes conditions above with both patid, admit_date, discharge_date, date_var
    """
    if list_of_dicts is None:
        all = generate_allvalues_between_admit_discharge_date(
            varlabel,
            tablename,
            date_var,
            time_var,
            value_var
        )
    else:
        all = generate_allvalues_between_admit_discharge_date_with_subset(
            varlabel,
            tablename,
            date_var,
            time_var,
            value_var,
            list_of_dicts
        )

    temp3 = session.query(
        all.c.patid,
        all.c.encounterid,
        func.min(all.c.datetime).label('min_datetime')
        ).group_by(all.c.patid, all.c.encounterid).subquery()

    temp4 = session.query(
        all
        ).filter(and_(
            all.c.patid == temp3.c.patid,
            all.c.encounterid == temp3.c.encounterid,
            all.c.datetime == temp3.c.min_datetime
        )).subquery()
    return temp4
