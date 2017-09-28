from factory.alchemy import SQLAlchemyModelFactory
import factory
from pcornet import models, common_session, configuration
from pcornet import generation_utils as gu
from pcornet.factories import DemographicFactory, EncounterFactory
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()


class DiagnosisFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Diagnosis
        sqlalchemy_session = common_session.Session

    class Params:
        Length = 8

    diagnosisid = factory.LazyAttribute(lambda o: gu.random_with_N_digits(o.Length))
    encounterid = factory.SubFactory(EncounterFactory)
    patid = factory.SubFactory(DemographicFactory)
    raw_dx_type = factory.Iterator(['ICD-9-CM', 'ICD-10-CM'])
    @factory.lazy_attribute
    def raw_dx(self):
        if self.raw_dx_type=='ICD-9-CM':
            return gu.generate_icd9_dx()
        elif self.raw_dx_type=='ICD-10-CM':
            return gu.generate_icd10_dx()
    @factory.lazy_attribute
    def raw_sedi_diagnosis_date(self):
        temp = self.encounterid.admit_date
        # TODO this needs to be a configuration parameter
        temp += timedelta(days=fake.random_digit())
        return temp
