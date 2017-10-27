from os.path import dirname, join
import pandas as pd

module_path = dirname(__file__)


def load_icd9_gems():
    icd9_gems = pd.read_fwf(join(module_path, '2017_I9gem.txt'),
                            [(0,6),(6,14),(14,19)],
                            header=None,
                            names=['icd9_diagnosis', 'icd10_diagnosis', 'map_key'],
                            converters={'icd9_diagnosis':str,
                                        'icd10_diagnosis':str,
                                        'map_key':str}
                            )
    return icd9_gems


def load_icd10_gems():
    icd10_gems = pd.read_fwf(join(module_path, '2017_I10gem.txt'),
                             [(0,8),(8,14),(14,19)],
                             header=None,
                             names=['icd10_diagnosis','icd9_diagnosis', 'map_key'],
                             converters={'icd10_diagnosis': str,
                                         'icd9_diagnosis': str,
                                         'map_key': str}
                             )
    return icd10_gems


def load_labs():
    df = pd.read_csv(join(module_path, 'labs.txt'))

    return df


def load_icd9_procedure():
    """
    Generate ICD9 procedure codes
    :return: pandas.DataFrame
    """
    df = pd.read_fwf(join(module_path, 'ICD9_SG.txt'),
                     widths=[5, 100],
                     names=['icd9_px', 'desc'])
    return df


def load_icd9_diagnosis():
    """
    Generate ICD9 Diagnosis Codes
    :return: pandas.DataFrame
    """
    df = pd.read_fwf(join(module_path, 'ICD9_DX.txt'),
                     widths=[6, 100],
                     names=['icd9_dx', 'desc'])
    return df


def load_icd10_diagnosis():
    """
    Generate ICD10 Diagnosis Codes
    :return: pandas.DataFrame
    """
    df = pd.read_fwf(join(module_path, 'ICD10_DX.txt'),
                     widths=[8, 100],
                     names=['icd10_dx', 'desc'])
    return df


def load_medications():
    """
    List of comprehensive Medications taken from: https://www.fda.gov/drugs/informationondrugs/ucm142438.htm
    Which is the NDC Database File - Text Version last updated 9/1/2017
    :return: pandas.DataFrame with two columns: proprietaryname and nonproprietaryname
    """
    df = pd.read_csv(
        join(module_path, 'newmeds.txt')
        )

    return df
