from pcornet import models, common_session
from sqlalchemy import func, and_, case
from pcornet.features.utils import booleans_from_list_of_dicts, booleans_from_list_of_dicts_likes

session = common_session.Session


def generate_a_yes_no_count_by_patid_with_dict_of_likes(varlabel, tablename, list_of_dicts):
    """
    A subquery generator that gives count of column yes no according to a list of dicts. Each dict should contain a key
    that is a pcornet.models.columname and a value that is a list of non-exact acceptable inputs (i.e. LIKE '%HDL%').
    For example, [{'raw_rx_med_name': ['%hydrochlorothiazide%', '%chlorthalidon%', '%metoprolol%']}]. This would give
    a count of yes/no that match with AND's in the dicts and ORs between list elements.
    :param varlabel: str: resulting varaible name
    :param tablename: str: corresponding to a pcornet.model
    :param list_of_dicts: a list of strings that return yes (1); otherwise no (0)
    :return: a sqlalchemy.query.subquery that executes conditions above
    """
    temp = session.query(
        getattr(models, tablename).patid,
        func.sum(case(
                    [
                        (booleans_from_list_of_dicts_likes(tablename, list_of_dicts), 1)
                    ],
                    else_=0
                )
        ).label(varlabel))\
    .group_by(getattr(models, tablename).patid)\
    .subquery()

    return temp


def generate_a_yes_no_count_by_patid(varlabel, tablename, columnname, listcode):
    """
    A subquery generator that gives count of column yes no if in listcode by patid
    :param varlabel: str: resulting varaible name
    :param tablename: str: corresponding to a pcornet.model
    :param columnname: str: corresponding to a pcornet.model.columname
    :param listcode: a list of strings that return yes (1); otherwise no (0)
    :return: a sqlalchemy.query.subquery that executes conditions above
    """
    temp = session.query(getattr(models, tablename).patid,
                            func.sum(case(
                                        [
                                            (getattr(getattr(models, tablename), columnname).in_(listcode), 1)
                                        ],
                                        else_=0
                                    )
                            ).label(varlabel))\
    .group_by(getattr(models, tablename).patid)\
    .subquery()

    return temp


def generate_an_average_by_patid(varlabel, tablename, columnname, listcode):
    """
    A subquery generator that gives an average of a column by patid
    :param varlabel: str: resulting varaible name
    :param tablename: str: corresponding to a pcornet.model
    :param columnname: str: corresponding to a pcornet.model.columname
    :param listcode: a list of strings that return yes (1); otherwise no (0)
    :return: a sqlalchemy.query.subquery that executes conditions above
    """
    temp = session.query(getattr(models, tablename).patid,
                            func.avg(getattr(getattr(models, tablename), columnname).in_(listcode)).label(varlabel))\
    .group_by(getattr(models, tablename).patid)\
    .subquery()

    return temp


def generate_a_yes_no_count_by_patid_with_dict(varlabel, tablename, list_of_dicts):
    """
    A subquery generator that gives count of column yes no according to a list of dicts. Each dict should contain a key
    that is a pcornet.models.columname and a value that is a list of acceptable inputs.
    For example, [{'raw_dx': ['410.10', '410.11'], 'raw_dx_type': ['ICD-9-CM']}, {'raw_dx': ['I21.4'], 'raw_dx_type':
    ['ICD-10-CM']}]. This would give a count of yes/no that match with AND's in the dicts and ORs between list elements.
    :param varlabel: str: resulting varaible name
    :param tablename: str: corresponding to a pcornet.model
    :param list_of_dicts: a list of strings that return yes (1); otherwise no (0)
    :return: a sqlalchemy.query.subquery that executes conditions above
    """
    temp = session.query(getattr(models, tablename).patid,
                        func.sum(case(
                                    [
                                        (booleans_from_list_of_dicts(tablename, list_of_dicts), 1)
                                    ],
                                    else_=0
                                )
                        ).label(varlabel))\
    .group_by(getattr(models, tablename).patid)\
    .subquery()

    return temp


def generate_most_recent_value_by_patid(varlabel, tablename, datecolumnname, valuecolumnname):
    """
    A subquery generator to return the most recent value of column by patid. If there is more than one last value (e.g.
    two values that occur on the same day), an average will be returned.
    :param varlabel: str: resulting varaible name
    :param tablename: str: corresponding to a pcornet.model
    :param valuecolumnname: str: corresponding to a pcornet.model.columname with the value
    :param datecolumnname: str: corresponding to a pcornet.model.columname with the date
    :return: a sqlalchemy.query.subquery that executes conditions above
    """
    vital_max_date_valid_ht = session.query(
        getattr(models, tablename).patid,
        func.max(getattr(getattr(models, tablename), datecolumnname)).label('maxdate')) \
        .filter(
        getattr(getattr(models, tablename), valuecolumnname).isnot(None)
        ) \
        .group_by(models.Vital.patid) \
        .subquery()

    vital_current_ht = session.query(
        getattr(models, tablename).patid,
        getattr(getattr(models, tablename), valuecolumnname).label('recent_ht'),
        vital_max_date_valid_ht.c.maxdate
        ) \
        .join(
        vital_max_date_valid_ht,
        and_(
            getattr(models, tablename).patid == vital_max_date_valid_ht.c.patid,
            getattr(getattr(models, tablename), datecolumnname) == vital_max_date_valid_ht.c.maxdate,
        )) \
        .filter(getattr(getattr(models, tablename), valuecolumnname).isnot(None)) \
        .subquery()

    temp = session.query(
        vital_current_ht.c.patid,
        func.avg(vital_current_ht.c.recent_ht).label(varlabel)) \
        .group_by(vital_current_ht.c.patid) \
        .subquery()

    return temp
