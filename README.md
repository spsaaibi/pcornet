# pcornet_tools
A "batteries included" approach to data science projects that utlize the [PCORnet common data model](http://www.pcornet.org/pcornet-common-data-model/).

## How do I install?
```
git clone https://vlp-gitlab.dhe.duke.edu/nn31/pcornet_tools.git
cd ./pcornet_tools
pip install .
```

## How do I use?
There are many tools included in this package for handling the PCORnet data model. We will go through several
things possible

### Instantiate the PCORnet common data model (no data inserted)
```
from sqlalchemy import create_engine
from pcornet import Base
engine = create_engine('postgresql+psycopg2://django_pcornet:django_pcornet_password@localhost/django_pcornet')
Base.metadata.create_all(engine)
```

### Load some test data for a 'hands on' experience
**Note if starting a new python session from here, first set up an engine (see above)**
```
from pcornet import factories
from itertools import chain
import random
from pcornet.common_session import Session
session = Session(bind=engine)
demos = factories.DemographicFactory.create_batch(10)
encounters = [factories.EncounterFactory.create_batch(random.randint(1,12),
                                                      demographic=demo,
                                                      patid=demo) for demo in demos]
encounters = list(chain(*encounters))                                                    
diagnoses = [factories.DiagnosisFactory.create_batch(random.randint(1,12),
                                                     demographic=encounter.demographic,
                                                     patid=encounter.patid,
                                                     encounter=encounter,
                                                     encounterid=encounter) for encounter in encounters]
vital = [factories.VitalFactory.create_batch(random.randint(0,12),
                                                     demographic=encounter.demographic,
                                                     patid=encounter.patid,
                                                     encounter=encounter,
                                                     encounterid=encounter) for encounter in encounters]
                                                     
prescribing = [factories.PrescribingFactory.create_batch(random.randint(0,12),
                                                     demographic=encounter.demographic,
                                                     patid=encounter.patid,
                                                     encounter=encounter,
                                                     encounterid=encounter) for encounter in encounters]

labs = [factories.LabResultCMFactory.create_batch(random.randint(0,12),
                                                     demographic=encounter.demographic,
                                                     patid=encounter.patid,
                                                     encounter=encounter,
                                                     encounterid=encounter) for encounter in encounters]

med_recs = [factories.MedRecFactory.create_batch(random.randint(1,45),
                                                     demographic=demo,
                                                     patid=demo) for demo in demos]

session.commit()
```

### Generate Features for the Framingham 30 year CVD Risk 
**NOTE**: we use another library which contains implemented versions of clinical algorithms. You may need to install to actually score the test data.
```
from pcornet import models
from sqlalchemy.sql import func, select, text, and_, case, not_, or_
from sqlalchemy import create_engine, and_
import pandas as pd
from pcornet.features.subquery_generators import *
from pcornet.features.feature_metadata import TRTBP, DIABETES, SMOKER

recent_height = generate_most_recent_value_by_patid('recent_ht', 'Vital', 'measure_date', 'ht')
recent_weight = generate_most_recent_value_by_patid('recent_wt', 'Vital', 'measure_date', 'wt')
trtbp_count = generate_a_yes_no_count_by_patid_with_dict_of_likes('trtbp_count', 'Prescribing', TRTBP['prescribing'])
diabetes_count = generate_a_yes_no_count_by_patid_with_dict('diab_count', 'Diagnosis', DIABETES['diagnosis'])
smoking_count = generate_a_yes_no_count_by_patid_with_dict('smoking_count', 'Vital', SMOKER['vital'])

#Custom Subqueries can be used
avg_sbp = session.query(
    models.Vital.patid,
    func.avg(models.Vital.systolic).label('sbp_avg')
    )\
    .group_by(models.Vital.patid)\
    .subquery()
    
#Put it all together:
#Note, some of these features, implicitly impute 0. Ensure this is okay.
features = session.query(models.Demographic.patid,
                         (func.current_date()-models.Demographic.birth_date).label('age'),
                         case(
                             [
                                 (models.Demographic.sex == 'M', 1),
                                 (models.Demographic.sex == 'F', 0)
                             ],
                             else_=None
                         ).label('male'),
                         avg_sbp.c.sbp_avg,
                         smoking_count.c.smoking_count,
                         trtbp_count.c.trtbp_count,
                         diabetes_count.c.diab_count,
                         recent_height.c.recent_ht,
                         recent_weight.c.recent_wt)\
    .outerjoin(avg_sbp, models.Demographic.patid==avg_sbp.c.patid)\
    .outerjoin(smoking_count, models.Demographic.patid==smoking_count.c.patid)\
    .outerjoin(trtbp_count, models.Demographic.patid==trtbp_count.c.patid)\
    .outerjoin(diabetes_count, models.Demographic.patid==diabetes_count.c.patid)\
    .outerjoin(recent_height, models.Demographic.patid==recent_height.c.patid)\
    .outerjoin(recent_weight, models.Demographic.patid==recent_weight.c.patid)
    
df = pd.read_sql(features.statement, session.bind)
```
Now, we'll pull in the Framingham 30 year (BMI) CVD Risk model
```
from clapton.cython import fram30_bmi
import numpy as np
#Examine the signature of the function
print(fram30_bmi.fram30_bmi.__doc__)

def bmi_calc(height, weight):
    wt_convert = weight*0.45
    ht_convert = np.square(np.multiply(height, 0.025))
    bmi = np.divide(wt_convert, ht_convert)
    return bmi

#don't need counts, so generate yes/no variables
def count_2_yesno(count_variable):
    if pd.isnull(count_variable):
        pass
    else:
        if count_variable>0:
            return 1
        else:
            return 0
df['bmi'] = df.apply(lambda row: bmi_calc(row['recent_ht'], row['recent_wt']), axis=1)
df['trtbp_yesno'] = df.apply(lambda row: count_2_yesno(row['trtbp_count']), axis=1)
df['smoke_yesno'] = df.apply(lambda row: count_2_yesno(row['smoking_count']), axis=1)
df['diabetes_yesno'] = df.apply(lambda row: count_2_yesno(row['diab_count']), axis=1)

fram30_bmi_variables = ['male', 'age', 'sbp_avg', 'bmi', 'smoke_yesno', 'trtbp_yesno', 'diabetes_yesno']

df['fram30_bmi_risk'] = fram30_bmi.fram30_bmi(df[fram30_bmi_variables].as_matrix())

```


### Serialize patient data
```
import pprint
from pcornet import models
from pcornet.serializers import PlotlyGnattSchema
patients = session.query(models.Demographic).limit(7)
#Demographics Only
pprint.pprint(PlotlyGnattSchema().dump(patients, many=True).data)
```
Now, use this serialization to hook up to a plotly graphic to develop an interactive timeline
into a patient's history:
```
import plotly.offline as py
import plotly.figure_factory as ff


colors = dict(Vital = 'rgb(46, 137, 205)',
              Procedures = 'rgb(114, 44, 121)',
              Prescribing = 'rgb(198, 47, 105)',
              MedReconciliation = 'rgb(58, 149, 136)',
              Labs = 'rgb(107, 127, 135)',
              Diagnosis = 'rgb(255,0,0)',
              Encounter = 'rgb(0,255,0)')
              
data = PlotlyGnattSchema().dump(patients[0]).data

fig = ff.create_gantt(data['df'], colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
py.plot(fig, filename='gantt-group-tasks-together.html')
```