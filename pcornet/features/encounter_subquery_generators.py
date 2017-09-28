from pcornet import models, common_session
from sqlalchemy import func, and_, case, or_
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




