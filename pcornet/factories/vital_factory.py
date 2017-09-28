from factory.alchemy import SQLAlchemyModelFactory
import factory
import numpy as np
from pcornet import models, common_session, configuration
from pcornet.factories import DemographicFactory, EncounterFactory
from pcornet import generation_utils as gu
from faker import Faker
import random
from dateutil.relativedelta import relativedelta

fake = Faker()

class VitalFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Vital
        sqlalchemy_session = common_session.Session

    class Params:
        Length = 8

    vitalid = factory.LazyAttribute(lambda o: gu.random_with_N_digits(o.Length))
    encounterid = factory.SubFactory(EncounterFactory)
    patid = factory.SubFactory(DemographicFactory)
    @factory.lazy_attribute
    def measure_date(self):
        temp = self.encounterid.admit_date
        # TODO this needs to be a configuration parameter
        temp2 = temp + relativedelta(days=fake.random_digit())
        # TODO this needs to be a configuration parameter
        return temp2
    measure_time = '00:00'
    vital_source = 'HC'
    @factory.lazy_attribute
    def ht(self):
        if fake.random.uniform(0, 1) > 0.5:
            return random.normalvariate(66.14, 4.3)
    @factory.lazy_attribute
    def wt(self):
        if fake.random.uniform(0,1)>0.5:
            return random.normalvariate(186.23, 53.10)
    @factory.lazy_attribute
    def diastolic(self):
        return random.normalvariate(75.32, 11.31)
    @factory.lazy_attribute
    def systolic(self):
        return random.normalvariate(126.32, 18.83)
    # @factory.lazy_attribute
    # def original_bmi(self):
    #     wt_convert = self.wt*0.45
    #     ht_convert = np.square(self.ht*0.025)
    #     bmi = np.divide(wt_convert, ht_convert)
    #     return bmi
    # bp_position =
    # smoking =
    # tobacco =
    # tobacco_type =
    # raw_diastolic =
    # raw_systolic =
    # raw_bp_position =
    # raw_smoking =
    # raw_tobacco =
    # raw_tobacco_type =
    # raw_encounterid =