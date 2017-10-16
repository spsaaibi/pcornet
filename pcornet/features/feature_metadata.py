DIABETES = {
        'diagnosis': [
        {
            'raw_dx' : ['249.00', '250.00', '250.01', '790.2', '790.21', '790.22', '790.29', '791.5', '791.6', 'V45.85',
                     'V53.91', 'V65.46', '249.01', '249.10', '249.11', '249.20', '249.21', '249.30', '249.31', '249.40',
                     '249.41', '249.50', '249.51', '249.60', '249.61', '249.70', '249.71', '249.80', '249.81', '249.90',
                     '249.91', '250.02', '250.03', '250.10', '250.11', '250.12', '250.13', '250.20', '250.21', '250.22',
                     '250.23', '250.30', '250.31', '250.32', '250.33', '250.40', '250.41', '250.42', '250.43', '250.50',
                     '250.51', '250.52', '250.53', '250.60', '250.61', '250.62', '250.63', '250.70', '250.71', '250.72',
                     '250.73', '250.80', '250.81', '250.82', '250.83', '250.90', '250.91', '250.92', '250.93'],
            'raw_dx_type' : ['ICD-9-CM']
        },
        {
            'raw_dx' : ['E08.21',  'E08.36',  'E09.638',  'R82.4',  'E09.628',  'E11.29',  'E10.29',  'E08.51',  'E09.40',
                      'E10.36',  'E10.51',  'E09.42',  'E13.44',  'E08.621',  'Z46.81',  'E10.311',  'E09.37X3',
                      'E09.319',  'E13.628',  'E08.37X2',  'R73.09',  'E13.40',  'E09.622',  'E08.9',  'E08.40',  'E08.620',
                      'E09.618',  'E09.649',  'E09.51',  'E09.610',  'E11.630',  'E08.39',  'E11.39',  'E10.11',  'E11.01',
                      'E08.622',  'E10.8',  'E09.311',  'E09.69',  'E13.49',  'E08.37X9',  'E08.641',  'E09.621',  'E08.43',
                      'E13.43',  'E11.21',  'E11.622',  'E09.9',  'E13.620',  'E13.8',  'E13.622',  'E11.00',  'E08.49',
                      'E13.59',  'E10.69',  'E11.649',  'E10.649',  'E10.622',  'E10.628',  'E11.621',  'E13.10', 'E09.641',
                      'E10.10',  'E10.638',  'E09.01',  'E08.618',  'E08.610',  'E10.9',  'E10.37X3',  'E10.620',  'E10.21',
                      'E10.630',  'E08.311',  'Z96.41',  'E10.65',  'E13.9',  'E13.649',  'E10.618',  'E09.39',  'E11.40',
                      'E10.37X9',  'E09.37X9',  'E09.65',  'E13.41',  'E11.620',  'E09.620',  'E08.65',  'E13.641',
                      'E09.37X2',  'E08.319',  'E13.69',  'E08.69',  'E11.36',  'E08.37X3',  'E08.630',  'E11.319',
                      'E08.37X1',  'E08.638',  'E08.44',  'E10.40',  'E11.311',  'E09.36',  'E09.11',  'E11.638',  'E11.65',
                      'E13.00',  'E09.21',  'E09.8',  'E09.37X1',  'E09.41',  'E10.37X1',  'E08.41',  'E08.01',  'E13.11',
                      'E10.621',  'E09.43',  'E13.39',  'R73.03',  'E09.49',  'E13.638',  'E08.8',  'E10.641',  'E10.37X2',
                      'E11.618',  'R73.02',  'E09.630',  'E13.65',  'E11.628',  'E09.44',  'E09.10',  'E11.51',  'E11.8',
                      'E11.69',  'E08.10',  'E08.42',  'E10.39',  'E11.9',  'E13.621',  'R73.01',  'E13.42',  'E10.319',
                      'R81.',  'E11.641',  'E08.11',  'E08.628'],
            'raw_dx_type' : ['ICD-10-CM']
        }
    ]
}

SMOKER = {
    'vital': [
        {
            'smoking': ['01', '02', '05', '07', '08']
        }
    ]
}

NSTEMI = {
    'diagnosis': [
        {
            'raw_dx': ['410.00', '410.01', '410.02', '410.10', '410.11', '410.12', '410.20', '410.21', '410.22', '410.30',
               '410.31', '410.32', '410.40', '410.41', '410.42', '410.50', '410.51', '410.52', '410.60', '410.61',
               '410.62', '410.70', '410.71', '410.72', '410.80', '410.81', '410.82', '410.90', '410.91', '410.92'],
            'raw_dx_type': ['ICD-9-CM']
        },
        {
            'raw_dx': ['I21.4', 'I22.2'],
            'raw_dx_type': ['ICD-10-CM']
        }
    ]
}

TRTBP = {
    'prescribing': [
        {
            'raw_rx_med_name': ['%hydrochlorothiazide%', '%chlorthalidon%', '%metoprolol%', '%carvedilol%', '%atenolol%', '%bisoprolol%',
                  '%nadolol%', '%captopril%', '%enalapril%', '%lisinopril%', '%ramipril%', '%candesartan%', '%losartan%',
                  '%valsartan%', '%irbesartan%', '%minoxidil%', '%hydralazine%', '%diltiazem%', '%amlodipine%',
                  '%verapamil%']
        }
    ]
}

CHB = {
    'diagnosis': [
        {
            'raw_dx': ['426.0'],
            'raw_dx_type': ['ICD-9-CM']
        },
        {
            'raw_dx': ['I44.2', 'I45.3'],
            'raw_dx_type': ['ICD-9-CM']
        }
    ],
    'procedures': [
        {
            'px': ['37.78', '37.71', '37.72', '37.73', '93.93'],
            'px_type': ['09']
        },
        {
            'px': ['5A1223Z', '5A1213Z'],
            'px_type': ['10']
        },
        {
            'px': ['C1785', '33213', 'C1895', '33237', '93734', '93286', '71090', 'C1777', '93733', '33206', '33234', 'C1722',
           '93623', '93732', '00530', 'C1786', '93731', 'C1896', '33208', 'C1898', '33210', '33235', 'A4627', '93724',
           '33212', '33233', '33222', 'C1727', 'C1764', '93735', '33214', '33200', 'C1899', '27345'],
            'px_type': ['CH']
        }
    ]
}

CARDIAC_ARREST = {
    'diagnosis': [
        {
            'raw_dx': ['427.5'],
            'raw_dx_type': ['ICD-9-CM']
        },
        {
            'raw_dx': ['Z86.74', 'I46.2', 'I46.8', 'I46.9'],
            'raw_dx_type': ['ICD-10-CM']
        }
    ]
}

VENTRICULAR_ARR = {
    'diagnosis': [
        {
            'raw_dx': ['427.41', '427.1', '427.42'],
            'raw_dx_type': ['ICD-9-CM']
        },
        {
            'raw_dx': ['I47.2', 'I49.01', 'I49.02'],
            'raw_dx_type': ['ICD-10-CM']
        }
    ]
}

ACUTE_PULMONARY_EDEMA = {
    'diagnosis': [
        {
            'raw_dx': ['518.4', '518.81', '518.84'],
            'raw_dx_type': ['ICD-9-CM']
        },
        {
            'raw_dx': ['R09.2', 'J96.00', 'J96.01', 'J96.02', 'J95.821', 'J95.822', 'J96.20', 'J96.90', 'J96.91'
                               'J96.92'],
            'raw_dx_type': ['ICD-10-CM']
        }
    ],
    'procedures': [
        {
            'px': ['96.04', '96.05', '93.99', '93.90', '93.91'],
            'px_type': ['09']
        },
        {
            'px': ['5A1945Z', '5A1955Z', '5A1935Z'],
            'px_type': ['10']
        }
    ]
}

CARDIOGENIC_SHOCK = {
    'procedures': [
        {
            'px': ['37.62', '37.61', '37.68', '37.41', '00.17'],
            'px_type': ['09']
        },
        {
            'px': ['5A15223'],
            'px_type': ['10']
        }
    ]
}

HEMATOCRIT = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['HCT', 'HEMATOCRIT', 'HEMATOCRIT     (BKR)', 'HEMATOCRIT     (BKR) ', 'HEMATOCRIT     (BKRAF)', 'HEMATOCRIT   (BKRREF)', 'HEMATOCRIT (LABCORP)', 'HEMATOCRIT - LABCORP', 'HEMATOCRIT, VENOUS', 'HEMATOCRIT, VENOUS     (BKR)', 'VENOUS HEMATOCRIT', 'HCT-PBPC BLOOD COUNT', 'DUAP HEMATOCRIT']
        }
    ]
}

HEMOGLOBIN = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['HGB', 'HEMOGLOBIN', 'HEMOGLOBIN     (BKR)', 'HEMOGLOBIN     (BKRAF)', 'HEMOGLOBIN - LABCORP', 'HEMOGLOBIN, VENOUS     (BKR)', 'VENOUS HEMOGLOBIN', 'HGB', 'DUAP HEMOGLOBIN', 'HEMOGLOBIN, VENOUS']
        }
    ]
}

PLATELET_COUNT = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['DUAP PLATELET COUNT /L', 'PLATELET COUNT', 'PLATELET COUNT     (BKR)', 'PLATELET COUNT     (BKRAF)', 'PLATELET COUNT - LABCORP', 'PLATELET COUNT /L', 'PLT CT', 'PLTS - LABCORP']
        }
    ]
}

WHITE_BLOOD_CELL = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['DUAP WBC', 'DUAP WHITE BLOOD CELL COUNT', 'WBC', 'WBC     (BKR)', 'WBC - LABCORP', 'WBC CORR', 'WBC CT', 'WHITE BLOOD CELL COUNT', 'WHITE BLOOD CELL COUNT     (BKR)', 'WHITE BLOOD CELL COUNT     (BKRAF)', 'WHITE BLOOD CELL COUNT - LABCORP', 'WHITE BLOOD COUNT']
        }
    ]
}

SODIUM = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['SODIUM', 'SODIUM     (BKR)', 'SODIUM     (BKRAF)', 'SODIUM - LABCORP', 'SODIUM, VENOUS', 'SODIUM, VENOUS     (BKR)', 'SODIUM, WHOLE BLOOD', 'SODIUM, WHOLE BLOOD     (BKR)']
        }
    ]
}

POTASSIUM = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['POTASSIUM', 'POTASSIUM     (BKR)', 'POTASSIUM     (BKRAF)', 'POTASSIUM - LABCORP', 'DUAP POTASSIUM', 'POTASSIUM, VENOUS', 'POTASSIUM, VENOUS     (BKR)', 'POTASSIUM,PRM', 'POTASSIUM. WHOLE BLOOD', 'POTASSIUM. WHOLE BLOOD     (BKR)']
        }
    ]
}

CHLORIDE = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['CHLORIDE', 'CHLORIDE     (BKR)', 'CHLORIDE     (BKRAF)', 'CHLORIDE - LABCORP', 'CHLORIDE-WHOLE BLOOD', 'CHLORIDE-WHOLE BLOOD     (BKR)']
        }
    ]
}

BICARBONATE = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['BICARBONATE', 'CARBON DIOXIDE', 'CARBON DIOXIDE - LABCORP', 'CARBON DIOXIDE-WHOLE BLOOD', 'CARBON DIOXIDE-WHOLE BLOOD     (BKR)', 'TOTAL CO2', 'CARBON DIOXIDE     (BKRAF)', 'CARBON DIOXIDE     (BKR)', 'HCO3 PRM', 'HCO3,PRIME']
        }
    ]
}

BUN = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['BLOOD UREA NITROGEN', 'BLOOD UREA NITROGEN - LABCORP', 'UREA NITROGEN', 'UREA NITROGEN     (BKR)', 'UREA NITROGEN     (BKRAF)', 'UREA NITROGEN-WHOLE BLOOD', 'UREA NITROGEN-WHOLE BLOOD     (BKR)']
        }
    ]
}

CREATININE = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['CREATINE', 'CREATININE', 'CREATININE     (BKR)', 'CREATININE     (BKRAF)', 'CREATININE  - LABCORP', 'CREATININE (MG/ML)   JAFFE     (BKR)', 'CREATININE - LABCORP', 'CREA BLD', 'CREATININE WHOLE BLOOD', 'CREATININE WHOLE BLOOD     (BKR)', 'CREATININE, SERUM', 'CREATINE, SERUM - LABCORP', 'CREATINE-SERUM/PLASMA', 'DUAP CREATININE']
        }
    ]
}

GLUCOSE = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['GLUCOSE', 'GLUCOSE     (BKR)', 'GLUCOSE     (BKRAF)', 'GLUCOSE    (BKR)', 'GLUCOSE    (BKRAF)', 'GLUCOSE WHOLE BLD BY GMD(POCT)', 'GLUCOSE, PLASMA - LABCORP', 'GLUCOSE, SERUM - LABCORP', 'GLUCOSE-SMB', 'GLUCOSE-WHOLE BLOOD', 'GLUCOSE-WHOLE BLOOD     (BKR)', 'DPC GLUCOSE', 'DPC GLUCOSE     (BKR)', 'DPC GLUCOSE 2', 'DUAP GLUCOSE']
        }
    ]
}

GFR = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['GFR', 'GFR(MDRD)', 'GFR-CREA', 'DUAP GFR(MDRD)', 'EGFR', 'EGFR(MDRD)     (BKR)', 'EGFR(MDRD)     (BKRAF)', 'EGFR-WB (MDRD)']
        }
    ]
}

CALCIUM = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['CALCIUM', 'CALCIUM     (BKR)', 'CALCIUM     (BKRAF)', 'CALCIUM - LABCORP', 'TOTAL CALCIUM']
        }
    ]
}

LDH = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['LACTATE DEHYDROGENASE', 'LACTATE DEHYDROGENASE     (BKR)', 'LACTATE DEHYDROGENASE (BKRREF)', 'LACTATE DEHYDROGENASE - LABCORP', 'LACTATE WHOLE BLOOD', 'LACTATE WHOLE BLOOD     (BKR)', 'LACTIC DEHYDROGENASE (LDH)', 'LDH']
        }
    ]
}

LACTIC_ACID = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['LACTIC ACID', 'LACTIC ACID BLOOD', 'LACTIC ACID BLOOD     (BKR)', 'ILACTATE', 'LACTATE WHOLE BLOOD', 'LACTATE WHOLE BLOOD     (BKR)']
        }
    ]
}

MAGNESIUM = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['MAGNESIUM', 'MAGNESIUM     (BKR)', 'MAGNESIUM     (BKRAF)', 'MAGNESIUM - LABCORP']
        }
    ]
}

BNP = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['BNP - LABCORP', 'BRAIN NATRIURETIC PEPTIDE', 'BRAIN NATRIURETIC PEPTIDE     (BKR)', 'BTYPE NATRIURETIC PEPTIDE DUAP']
        }
    ]
}

PRO_BNP = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['PRO BRAIN NATRIURETIC PEPTIDE', 'PRO BRAIN NATRIURETIC PEPTIDE     (BKR)']
        }
    ]
}

CREATININE_KINASE = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['CREATINE KINASE', 'CREATINE KINASE (CK)', 'CREATINE KINASE (CK)     (BKR)', 'CREATINE KINASE MB ISOENZYME', 'CREATINE KINASE TOTAL - LABCORP', 'CREATINE KINASE, TOTAL,SERUM', 'CREATINE KINASE,TOTAL   (BKRAF)', 'CREATINE KINASE,TOTAL,SERUM', 'CREATINE KINASE,TOTAL,SERUM     (BKR)', 'CREATINE KINASE,TOTAL,SERUM    (BKRREF)']
        }
    ]
}

CK_MB = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['CK-MB', 'CK-MB     (BKR)', 'CK-MB    (BKRREF)', 'CK-MB - LABCORP', 'CK-MB INDEX - LABCORP', 'CKMB', 'DUAP CKMB']
        }
    ]
}

MB_FRACTION = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['MB FRACTION', 'MB RELATIVE PERCENT   (BKR)']
        }
    ]
}

TROPONIN_T = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['TROPONIN T', 'TROPONIN T     (BKR)']
        }
    ]
}

TROPONIN_I = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['TROPONIN I', 'TROPONIN I     (BKR)', 'DUAP TROPONIN I']
        }
    ]
}

CHOLESTEROL = {
    'lab_result_cm': [
        {
            'raw_sedi_test_desc': ['HDL CHOLESTEROL', 'LDL Chol', 'Cholesterol, Total']
        }
    ]
}

