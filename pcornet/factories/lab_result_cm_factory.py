from factory.alchemy import SQLAlchemyModelFactory
import factory
from pcornet import models, common_session, configuration
from pcornet.factories import DemographicFactory, EncounterFactory
from pcornet import generation_utils as gu
from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker()

class LabResultCMFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Lab_Result_CM
        sqlalchemy_session = common_session.Session

    class Params:
        Length = 8

    lab_result_cm_id = factory.LazyAttribute(lambda o: gu.random_with_N_digits(o.Length))
    encounterid = factory.SubFactory(EncounterFactory)
    patid = factory.SubFactory(DemographicFactory)
    # lab_name
    # specimen_source
    # lab_loinc
    # priority
    # result_loc
    # lab_px
    # lab_px_type
    # lab_order_date
    # specimen_date
    @factory.lazy_attribute
    def specimen_date(self):
        temp = self.encounterid.admit_date
        # TODO this needs to be a configuration parameter
        temp += timedelta(days=fake.random_digit())
        return temp
    @factory.lazy_attribute
    def specimen_time(self):
        a = fake.date_time()
        return a.strftime('%H:%M')
    # result_date
    # result_time
    # result_qual
    @factory.lazy_attribute
    def result_num(self):
        return random.normalvariate(75.32, 11.31)
    # result_modifier
    # result_unit
    # norm_range_low
    # norm_modifier_low
    # norm_range_high
    # norm_modifier_high
    # abn_ind
    # raw_lab_name
    # raw_lab_code
    # raw_panel
    # raw_result
    raw_unit = 'mg/dl'
    # raw_order_dept
    # raw_facility_code
    # raw_specimen_source
    # raw_result_loc
    # raw_lab_px_type
    # raw_result_qual
    # raw_result_modifier
    # raw_norm_modifier_low
    # raw_norm_modifier_high
    # raw_abn_ind
    # raw_encounterid
    @factory.lazy_attribute
    def raw_sedi_test_desc(self):
        return gu.generate_lab_names()
    # raw_sedi_base_name
    # raw_sedi_common_name