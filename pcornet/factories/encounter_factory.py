from factory.alchemy import SQLAlchemyModelFactory
import factory
from pcornet import models, common_session, configuration
from pcornet import generation_utils as gu
from pcornet.factories import DemographicFactory
from datetime import datetime, timedelta
from faker import Faker
from dateutil.relativedelta import relativedelta

fake = Faker()


class EncounterFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Encounter
        sqlalchemy_session = common_session.Session

    class Params:
        Length = 8
        ENC_TYPE = configuration.ENC_TYPE

    encounterid = factory.LazyAttribute(lambda o: gu.random_with_N_digits(o.Length))
    patid = factory.SubFactory(DemographicFactory)

    @factory.lazy_attribute
    def admit_date(self):
        temp = self.patid.birth_date
        # TODO this needs to be a configuration parameter
        temp2 = temp + relativedelta(years=fake.random_digit())
        return temp2
    admit_time = '00:00'
    @factory.lazy_attribute
    def discharge_date(self):
        temp = self.admit_date
        # TODO this needs to be a configuration parameter
        temp += timedelta(days=fake.random_digit())
        return temp
    discharge_time = '00:00'
    providerid = factory.LazyAttribute(lambda o: gu.random_with_N_digits(o.Length))
    # facility_location
    raw_enc_type = factory.LazyAttribute(lambda o: gu.generate_a_choice_configuration(o.ENC_TYPE))

    @factory.lazy_attribute
    def enc_type(self):
        if self.raw_enc_type in ['11', 'OFFICE VISIT']:
            return 'AV'
        elif self.raw_enc_type in ['12', 'INOUT_BILLING_CODE=0, ED_FLAG=Y']:
            return 'ED'
        elif self.raw_enc_type in ['13', 'INOUT_BILLING_CODE=I, ED_FLAG=Y']:
            return 'EI'
        elif self.raw_enc_type in ['10', 'INOUT_BILLING_CODE=I, ED_FLAG=N']:
            return 'IP'
        elif self.raw_enc_type in ['ALLIED HEALTH', 'ANCILLARY ORDERS', 'ANESTHESIA', 'ANESTHESIA EVENT',
                                   'ANTI-COAG VISIT', 'APPOINTMENT', 'BILLING ENCOUNTER', 'CLINICAL SOCIAL WORK',
                                   'COUNSELING', 'CRC RESEARCH ENCOUNTER', 'DOCUMENTATION', 'HOSPITAL ENCOUNTER',
                                   'INFUSION', 'INITIAL CONSULT', 'INITIAL PRENATAL', 'INOUT_BILLING_CODE=0, ED_FLAG=N',
                                   'LAB', 'LAB REQUISITION', 'NURSE ONLY', 'NUTRITION', 'OFF SITE SURGERY',
                                   'OPH TESTING', 'ORDER TRANSCRIPTION', 'ORDERS ONLY', 'PATIENT EMAIL',
                                   'PATIENT HOME VISIT', 'PATIENT OUTREACH', 'PHARMACY VISIT', 'POST OP',
                                   'POSTPARTUM VISIT', 'PRE-ANESTHESIA', 'PRE-EVALUATION', 'PROCEDURE VISIT',
                                   'PT/OT OFFICE VISIT', 'RESEARCH ENCOUNTER', 'ROUTINE PRENATAL', 'SURGICAL CONSULT',
                                   'TELEMEDICINE']:
            return 'OT'
    # facilityid
    # discharge_disposition
    # discharge_status
    # raw_drg_type
    # drg
    # drg_type
    # admitting_source
    # raw_siteid
    # raw_discharge_disposition
    # raw_discharge_status
    # raw_admitting_source
    # raw_sedi_ed_los_hours
    # raw_sedi_inpt_los_days
    # raw_sedi_total_los_days
    # raw_sedi_depart_ed_date
    # raw_sedi_depart_ed_time
    # raw_sedi_ed_prov_key
    # raw_sedi_admit_prov_key
    # raw_sedi_refer_prov_key
    # raw_sedi_disch_prov_specialty
    # raw_sedi_admit_prov_specialty
    # raw_sedi_refer_prov_specialty
    # raw_sedi_perf_prov_specialty
    # raw_sedi_admit_dept
    # raw_sedi_admit_service
    # raw_sedi_discharge_dept
    # raw_sedi_discharge_service
    # raw_sedi_discharge_disp_desc
    # raw_sedi_outpt_los_hours
    # raw_sedi_clinic_dept
    # raw_sedi_clinic_loc
    # raw_sedi_clinic_svc_specialty
    # raw_sedi_clinic_visit_reason
    # raw_sedi_clinic_visit_type
    # raw_sedi_clinic_visit_catg
