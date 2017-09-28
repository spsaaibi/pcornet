from pcornet import models, common_session
from sqlalchemy import func, and_, or_

session = common_session.Session


def booleans_from_list_of_dicts(tablename, dictt):
    """
    A helper function to parse a dictionary and generate sqlalchemy booleans for a suquery
    :param tablename: PCORnet table name
    :param dictt: python dictionary with key as column name and value is list of exact match values
    :return: sqlalchemy boolean object
    """
    temp = []
    for x in dictt:
        temp2 = []
        for key, value in x.items():
            temp2.append(getattr(getattr(models, tablename), key).in_(value))
        temp.append(and_(*temp2))
    return or_(*temp)


def booleans_from_list_of_dicts_likes(tablename, dictt):
    """
    A helper function to parse a dictionary and generate sqlalchemy booleans for a suquery
    :param tablename: PCORnet table name
    :param dictt: python dictionary with key as column name and value is list of like match values
    :return: sqlalchemy boolean object
    """
    temp = []
    for x in dictt:
        temp2 = []
        for key, value in x.items():
            temp3 = []
            for val in value:
                temp3.append(func.lower(getattr(getattr(models, tablename), key)).like(val))
            temp2.append(or_(*temp3))
        temp.append(and_(*temp2))
    return or_(*temp)
