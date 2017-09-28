from random import randint
from numpy.random import choice
from faker import Faker
from datetime import datetime
from pcornet.datasets import load
import re
import random

fake = Faker()

icd9_dx = list(load.load_icd9_diagnosis()['icd9_dx'])
icd10_dx = list(load.load_icd10_diagnosis()['icd10_dx'])
icd9_px = list(load.load_icd9_procedure()['icd9_px'])
meds = list(load.load_medications()['NONPROPRIETARYNAME'])
medsp = list(load.load_medications()['PROPRIETARYNAME'])
labs = list(load.load_labs()['LAB_NAME'])


def generate_lab_names():
    if random.randint(0, 10) > 5:
        lab = 'HDL CHOLESTEROL'
    else:
        lab = choice(labs)
    return lab


def generate_nonprop_meds():
    med = choice(meds)
    return med


def generate_prop_meds():
    med = choice(medsp)
    return med


def icd9_insert_decimal_format(code):
    """
    Function that takes a code (ICD9) and returns a properly formatted string with decimal
    (i.e. one with a properly placed decimal).
    :param code: str: billing code
    :return: str: formatted
    """
    formatted_code = re.sub(r'(V\d{2}|E\d{3}|\d{3})(\d{1,2})', r'\1.\2', code)
    return formatted_code


def icd10_insert_decimal_format(code):
    """
    Function that takes a code (ICD10) and returns a properly formatted string with decimal
    (i.e. one with a properly placed decimal).
    :param code: str: billing code
    :return: str: formatted
    """
    formatted_code = re.sub(r'([A-TV-Z0-9][0-9][A-Z0-9])([A-Z0-9]{0,4})', r'\1.\2', code)
    return formatted_code


def generate_icd9_dx():
    code = choice(icd9_dx)
    formatted_code = icd9_insert_decimal_format(code)
    return formatted_code


def generate_icd10_dx():
    code = choice(icd10_dx)
    formatted_code = icd10_insert_decimal_format(code)
    return formatted_code


def random_with_N_digits(n):
    """
    A function to generate a numeric string with length n.
    :param n: length of string to be returned
    :return: str: of length n
    """
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))


def generate_date_between():
    """
    Randomly generates a date field
    :return:
    """
    z = fake.date_time_between_dates(datetime(1909, 9, 29, 7, 15, 25))
    return z.date()


def generate_a_choice_configuration(configuration_object):
    """
    Randomly generates a choice from a pcornet_tools.configuration object
    :param configuration_object: a python object from pcornet_tools.configuration
    :return: a value derived as a key from one of the pcornet_tools.configuration objects
    """
    values = list(configuration_object.keys())
    probs = list(configuration_object.values())
    return choice(values, 1, probs)[0]
