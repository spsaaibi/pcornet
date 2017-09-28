from sqlalchemy import Column, ForeignKey, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Demographic(Base):
    __tablename__ = 'demographic'

    patid = Column(String(300), primary_key=True)
    birth_date = Column(Date)
    birth_time = Column(String(15))
    sex = Column(String(6))
    sexual_orientation = Column(String(6))
    gender_identity = Column(String(6))
    hispanic = Column(String(6))
    race = Column(String(6))
    biobank_flag = Column(String(3))
    raw_sex = Column(String(150))
    raw_sexual_orientation = Column(String(150))
    raw_gender_identity = Column(String(150))
    raw_hispanic = Column(String(150))
    raw_race = Column(String(150))
    raw_sedi_religion = Column(String(150))
    raw_sedi_employment_sts = Column(String(150))
    raw_sedi_language_name = Column(String(150))
    raw_sedi_current_marital_sts = Column(String(150))
    raw_sedi_partial_flag = Column(String(3))

    def __repr__(self):
        return "<Demographic(patid=%s)>" % self.patid


class Encounter(Base):
    __tablename__ = 'encounter'

    encounterid = Column(String(300), primary_key=True)
    patid = Column(String(300), ForeignKey('demographic.patid'))
    admit_date = Column(Date)
    admit_time = Column(String(15))
    discharge_date = Column(Date)
    discharge_time = Column(String(15))
    providerid = Column(String(300))
    facility_location = Column(String(9))
    enc_type = Column(String(6))
    facilityid = Column(String(300))
    discharge_disposition = Column(String(6))
    discharge_status = Column(String(6))
    drg = Column(String(9))
    drg_type = Column(String(6))
    admitting_source = Column(String(6))
    raw_siteid = Column(String(150))
    raw_enc_type = Column(String(150))
    raw_discharge_disposition = Column(String(150))
    raw_discharge_status = Column(String(150))
    raw_drg_type = Column(String(150))
    raw_admitting_source = Column(String(150))
    raw_sedi_ed_los_hours = Column(String(150))
    raw_sedi_inpt_los_days = Column(String(150))
    raw_sedi_total_los_days = Column(String(150))
    raw_sedi_depart_ed_date = Column(Date)
    raw_sedi_depart_ed_time = Column(String(15))
    raw_sedi_ed_prov_key = Column(String(150))
    raw_sedi_admit_prov_key = Column(String(150))
    raw_sedi_refer_prov_key = Column(String(150))
    raw_sedi_disch_prov_specialty = Column(String(300))
    raw_sedi_admit_prov_specialty = Column(String(300))
    raw_sedi_refer_prov_specialty = Column(String(300))
    raw_sedi_perf_prov_specialty = Column(String(300))
    raw_sedi_admit_dept = Column(String(300))
    raw_sedi_admit_service = Column(String(300))
    raw_sedi_discharge_dept = Column(String(300))
    raw_sedi_discharge_service = Column(String(300))
    raw_sedi_discharge_disp_desc = Column(String(150))
    raw_sedi_outpt_los_hours = Column(String(300))
    raw_sedi_clinic_dept = Column(String(300))
    raw_sedi_clinic_loc = Column(String(300))
    raw_sedi_clinic_svc_specialty = Column(String(300))
    raw_sedi_clinic_visit_reason = Column(String(300))
    raw_sedi_clinic_visit_type = Column(String(300))

    demographic = relationship("Demographic", backref=backref('encounter'))

    def __repr__(self):
        return "<Encounter(encounterid=%s)>" % self.encounterid
#
#
# class Enrollment(Base):
#     __tablename__ = 'enrollment'
#     id = Column(Integer, primary_key=True)
#     patid = Column(Integer, ForeignKey(Demographic.patid))
#     enr_start_date = Column(Date)
#     enr_end_date = Column(Date)
#     chart = Column(String)
#     enr_basis = Column(String)
#
#     class Meta:
#         unique_together = ('patid',
#                            'enr_start_date',
#                            'enr_basis',)
#
#     def __str__(self):
#         return "<Enrollment(patid=%s, enr_start_date=%s, enr_basis=%s)>" %\
#                (self.patid, self.enr_start_date, self.enr_basis)


class Diagnosis(Base):
    __tablename__ = 'diagnosis'

    diagnosisid = Column(String(300), primary_key=True)
    patid = Column(String(300), ForeignKey('demographic.patid'), index=True)
    encounterid = Column(String(300), ForeignKey('encounter.encounterid'))
    enc_type = Column(String(6))
    admit_date = Column(Date)
    providerid = Column(String(300))
    dx = Column(String(54))
    dx_type = Column(String(6))
    dx_source = Column(String(6))
    dx_origin = Column(String(6))
    pdx = Column(String(6))
    raw_dx = Column(String(300), index=True)
    raw_dx_type = Column(String(150), index=True)
    raw_dx_source = Column(String(150))
    raw_dx_origin = Column(String(150))
    raw_pdx = Column(String(150))
    raw_sedi_diagnosis_date = Column(Date)
    raw_sedi_diagnosis_group = Column(String(600))
    raw_sedi_diagnosis_name = Column(String(600))
    raw_sedi_coding_context_key = Column(String(150))
    raw_sedi_coding_context_desc = Column(String(300))

    demographic = relationship("Demographic", backref=backref('diagnosis'))
    encounter = relationship("Encounter", backref=backref('diagnosis'))

    def __repr__(self):
        return "<Diagnosis(diagnosisid=%s)>" % self.diagnosisid
#
#
# # noinspection PyPep8Naming
# class Emerg_Contact(Base):
#     __tablename__ = 'emerg_contact'
#     id = Column(Integer, primary_key=True)
#     patid = Column(Integer, ForeignKey(Demographic.patid))
#     contact_flag = Column(String)
#
#     def __str__(self):
#         return "<Emerg_Contact(id=%s)>" % self.id


class Procedures(Base):
    __tablename__ = 'procedures'

    proceduresid = Column(String(300), primary_key=True)
    patid = Column(String(300), ForeignKey('demographic.patid'))
    encounterid = Column(String(300), ForeignKey('encounter.encounterid'))
    enc_type = Column(String(6))
    admit_date = Column(Date)
    providerid = Column(String(300))
    px_date = Column(Date)
    px = Column(String(33))
    px_type = Column(String(6))
    px_source = Column(String(6))
    raw_px = Column(String(150))
    raw_px_type = Column(String(150))
    raw_px_source = Column(String(150))
    raw_sedi_px_desc = Column(String(600))
    raw_sedi_px_seq = Column(String(150))
    raw_sedi_px_rank = Column(String(150))
    raw_sedi_px_loc = Column(String(300))
    raw_sedi_px_provider_key = Column(String(150))

    demographic = relationship("Demographic", backref=backref('procedures'))
    encounter = relationship("Encounter", backref=backref('procedures'))

    def __repr__(self):
        return "<Procedures(proceduresid=%s)>" % self.proceduresid


class Vital(Base):
    __tablename__ = 'vital'

    vitalid = Column(String(300), primary_key=True)
    patid = Column(String(300), ForeignKey('demographic.patid'), index=True)
    encounterid = Column(String(300), ForeignKey('encounter.encounterid'))
    measure_date = Column(Date)
    measure_time = Column(String(15))
    vital_source = Column(String(6))
    ht = Column(Numeric(15, 8))
    wt = Column(Numeric(15, 8))
    diastolic = Column(Numeric(15, 8))
    systolic = Column(Numeric(15, 8))
    original_bmi = Column(Numeric(15, 8))
    bp_position = Column(String(6))
    smoking = Column(String(6))
    tobacco = Column(String(6))
    tobacco_type = Column(String(6))
    raw_diastolic = Column(String(150))
    raw_systolic = Column(String(150))
    raw_bp_position = Column(String(150))
    raw_smoking = Column(String(300))
    raw_tobacco = Column(String(300))
    raw_tobacco_type = Column(String(300))
    raw_encounterid = Column(String(150))

    demographic = relationship("Demographic", backref=backref('vital'))
    encounter = relationship("Encounter", backref=backref('vital'))

    def __repr__(self):
        return "<Vital(vitalid=%s)>" % self.vitalid
#
#
# class Dispensing(Base):
#     __tablename__ = 'dispensing'
#
#     dispensingid = Column(String, primary_key=True)
#     patid = Column(Integer, ForeignKey(Demographic.patid))
#     prescribingid = Column(String)
#     dispense_date = Column(Date)
#     ndc = Column(String)
#     dispense_sup = Column(Numeric(15, 8))
#     dispense_amt = Column(Numeric(15, 8))
#     raw_ndc = Column(String)
#
#     def __str__(self):
#         return "<Dispensing(dispensingid=%s)>" % self.dispensingid


# noinspection PyPep8Naming
class Lab_Result_CM(Base):
    __tablename__ = 'lab_result_cm'

    lab_result_cm_id = Column(String(300), primary_key=True)
    patid = Column(String(300), ForeignKey('demographic.patid'), index=True)
    encounterid = Column(String(300), ForeignKey('encounter.encounterid'))
    lab_name = Column(String(30))
    specimen_source = Column(String(30))
    lab_loinc = Column(String(30))
    priority = Column(String(6))
    result_loc = Column(String(6))
    lab_px = Column(String(33))
    lab_px_type = Column(String(6))
    lab_order_date = Column(Date)
    specimen_date = Column(Date)
    specimen_time = Column(String(15))
    result_date = Column(Date)
    result_time = Column(String(15))
    result_qual = Column(String(36))
    result_num = Column(Numeric(15, 8))
    result_modifier = Column(String(6))
    result_unit = Column(String(33))
    norm_range_low = Column(String(30))
    norm_modifier_low = Column(String(6))
    norm_range_high = Column(String(30))
    norm_modifier_high = Column(String(6))
    abn_ind = Column(String(6))
    raw_lab_name = Column(String(300))
    raw_lab_code = Column(String(900))
    raw_panel = Column(String(900))
    raw_result = Column(String(900))
    raw_unit = Column(String(150))
    raw_order_dept = Column(String(300))
    raw_facility_code = Column(String(150))
    raw_specimen_source = Column(String(300))
    raw_result_loc = Column(String(300))
    raw_lab_px_type = Column(String(300))
    raw_result_qual = Column(String(150))
    raw_result_modifier = Column(String(150))
    raw_norm_modifier_low = Column(String(150))
    raw_norm_modifier_high = Column(String(150))
    raw_abn_ind = Column(String(300))
    raw_encounterid = Column(String(150))
    raw_sedi_test_desc = Column(String(600), index=True)
    raw_sedi_base_name = Column(String(300))
    raw_sedi_common_name = Column(String(300))

    demographic = relationship("Demographic", backref=backref('lab_result_cm'))
    encounter = relationship("Encounter", backref=backref('lab_result_cm'))

    def __repr__(self):
        return "<Lab_Result_Cm(lab_result_cm_id=%s)>" % self.lab_result_cm_id


# noinspection PyPep8Naming
class Med_Reconciliation(Base):
    __tablename__ = 'med_reconciliation'

    medreconid = Column(String(300), primary_key=True)
    patid = Column(String(300), ForeignKey('demographic.patid'))
    rx_review_date = Column(Date)
    medication_name = Column(String(900))
    taking_yn = Column(String(30))

    demographic = relationship("Demographic", backref=backref('med_reconciliation'))

    def __repr__(self):
        return "<Med_Reconciliation(medreconid=%s)>" % self.medreconid
#
#
# # noinspection PyPep8Naming
# class Patient_Address(Base):
#     __tablename__ = 'patient_address'
#     id = Column(Integer, primary_key=True)
#     patient_address_id = Column(String)
#     patid = Column(Integer, ForeignKey(Demographic.patid))
#     addressid = Column(String)
#     address_type = Column(String)
#     pat_addr_current_flag = Column(String)
#     pataddr_effective_date = Column(Date)
#     pataddr_expiration_date = Column(Date)
#     street_address = Column(String)
#     city = Column(String)
#     prim_postal_code = Column(String)
#     secn_postal_code = Column(String)
#     county = Column(String)
#     state = Column(String)
#     verified_flag = Column(String)
#     std_street_line1 = Column(String)
#     std_street_line2 = Column(String)
#     std_city = Column(String)
#     std_state = Column(String)
#     std_zip = Column(String)
#     std_zip4 = Column(String)
#     std_county_name = Column(String)
#     std_country_code = Column(String)
#     geo_result_code = Column(String)
#     geo_latitude = Column(Numeric(15, 8))
#     geo_longitude = Column(Numeric(15, 8))
#     geo_county_fips_code = Column(String)
#     geo_tract_fips_code = Column(String)
#     geo_blockgrp_fips_code = Column(String)
#     geo_block_fips_code = Column(String)
#     geo_mcd_fips_code = Column(String)
#     geo_msa_cmsa_fips_code = Column(String)
#     geo_pmsa_fips_code = Column(String)
#     geo_cbsa_fips_code = Column(String)
#
#
# class Condition(Base):
#     __tablename__ = 'condition'
#
#     conditionid = Column(String, primary_key=True)
#     patid = Column(Integer, ForeignKey(Demographic.patid))
#     encounterid = Column(Integer, ForeignKey(Encounter.encounterid))
#     report_date = Column(Date)
#     resolve_date = Column(Date)
#     onset_date = Column(Date)
#     condition_status = Column(String)
#     condition = Column(String)
#     condition_type = Column(String)
#     condition_source = Column(String)
#     raw_condition_status = Column(String)
#     raw_condition = Column(String)
#     raw_condition_type = Column(String)
#     raw_condition_source = Column(String)
#     raw_sedi_condition_name = Column(String)
#     raw_sedi_condition_group = Column(String)
#     raw_sedi_chronic_problem = Column(String)
#     raw_sedi_principal_problem = Column(String)
#     raw_sedi_hospital_problem = Column(String)
#     raw_sedi_imo_term_id = Column(String)
#
#     def __str__(self):
#         return "<Condition(conditionid=%s)>" % self.conditionid
#
#
# # noinspection PyPep8Naming
# class Pro_cm(Base):
#     __tablename__ = 'pro_cm'
#
#     pro_cm_id = Column(String, primary_key=True)
#     patid = Column(Integer, ForeignKey(Demographic.patid))
#     encounterid = Column(Integer, ForeignKey(Encounter.encounterid))
#     pro_item = Column(String)
#     pro_loinc = Column(String)
#     pro_date = Column(Date)
#     pro_time = Column(String)
#     pro_response = Column(Numeric(15, 8))
#     pro_method = Column(String)
#     pro_mode = Column(String)
#     pro_cat = Column(String)
#     raw_pro_code = Column(String)
#     raw_pro_response = Column(String)
#
#     def __str__(self):
#         return "<Pro_cm(pro_cm_id=%s)>" % self.pro_cm_id


class Prescribing(Base):
    __tablename__ = 'prescribing'

    prescribingid = Column(String(300), primary_key=True)
    patid = Column(String(300), ForeignKey('demographic.patid'), index=True)
    encounterid = Column(String(300), ForeignKey('encounter.encounterid'))
    rx_providerid = Column(String(300))
    rx_order_date = Column(Date)
    rx_order_time = Column(String(15))
    rx_start_date = Column(Date)
    rx_end_date = Column(Date)
    rx_quantity = Column(Numeric(15, 8))
    rx_quantity_unit = Column(String(6))
    rx_refills = Column(Numeric(15, 8))
    rx_days_supply = Column(Numeric(15, 8))
    rx_frequency = Column(String(6))
    rx_basis = Column(String(6))
    rxnorm_cui = Column(Numeric(15, 8))
    raw_rx_med_name = Column(String(600), index=True)
    raw_rx_frequency = Column(String(300))
    raw_rxnorm_cui = Column(String(300))
    raw_rx_quantity = Column(String(150))
    raw_rx_ndc = Column(String(150))
    raw_rx_basis = Column(String(300))
    raw_sedi_brand_name = Column(String(900))
    raw_sedi_duke_therapeut_class = Column(String(300))
    raw_sedi_administration_route = Column(String(300))
    raw_sedi_drug_form = Column(String(300))
    raw_sedi_drug_strength = Column(String(300))
    raw_sedi_units_per_dose = Column(String(150))
    raw_sedi_discrete_dose_units = Column(String(150))
    raw_sedi_discrete_dose_amount = Column(String(150))
    raw_sedi_pat_ns_loc_key = Column(String(150))
    raw_sedi_pat_clinic_loc_key = Column(String(150))
    raw_sedi_ordering_prov_key = Column(String(150))
    raw_sedi_order_prov_specialty = Column(String(300))

    demographic = relationship("Demographic", backref=backref('prescribing'))
    encounter = relationship("Encounter", backref=backref('prescribing'))

    def __repr__(self):
        return "<Prescribing(prescribingid=%s)>" % self.prescribingid
#
#
# # noinspection PyPep8Naming
# class Pcornet_trial(Base):
#     __tablename__ = 'pcornet_trial'
#     id = Column(Integer, primary_key=True)
#     patid = Column(Integer, ForeignKey(Demographic.patid))
#     trialid = Column(String)
#     participantid = Column(String)
#     trial_siteid = Column(String)
#     trial_enroll_date = Column(Date)
#     trial_end_date = Column(Date)
#     trial_withdraw_date = Column(Date)
#     trial_invite_code = Column(String)
#
#     class Meta:
#         unique_together = ('patid',
#                            'trialid',
#                            'participantid',)
#
#     def __str__(self):
#         return "<Pcornet_trial(patid=%s, trialid=%s, participantid=%s)>" %\
#                (self.patid, self.trialid, self.participantid)
#
#
# class Death(Base):
#     __tablename__ = 'death'
#     id = Column(Integer, primary_key=True)
#     patid = Column(Integer, ForeignKey(Demographic.patid))
#     death_date = Column(Date)
#     death_date_impute = Column(String)
#     death_source = Column(String)
#     death_match_confidence = Column(String)
#     raw_death_date = Column(String)
#     raw_death_date_impute = Column(String)
#     raw_death_source = Column(String)
#     raw_death_match_confidence = Column(String)
#
#     class Meta:
#         unique_together = ('patid',
#                            'death_source',)
#
#     def __str__(self):
#         return "<Death(patid=%s, death_source=%s)>" % (self.patid, self.death_source)
#
#
# # noinspection PyPep8Naming
# class Death_cause(Base):
#     __tablename__ = 'death_cause'
#     id = Column(Integer, primary_key=True)
#     patid = Column(Integer, ForeignKey(Demographic.patid))
#     death_cause = Column(String)
#     death_cause_code = Column(String)
#     death_cause_type = Column(String)
#     death_cause_source = Column(String)
#     death_cause_confidence = Column(String)
#
#     class Meta:
#         unique_together = ('patid',
#                            'death_cause',
#                            'death_cause_code',
#                            'death_cause_type',
#                            'death_cause_source',)
#
#     def __str__(self):
#         return "<Death_cause(patid=%s, death_cause=%s, death_cause_code=%s," \
#                "death_cause_type=%s, death_cause_source=%s)>" % \
#                (self.patid, self.death_cause, self.death_cause_code, self.death_cause_type, self.death_cause_source)
#
#
# class Harvest(Base):
#     __tablename__ = 'harvest'
#     id = Column(Integer, primary_key=True)
#     networkid = Column(String)
#     network_name = Column(String)
#     datamartid = Column(String)
#     datamart_name = Column(String)
#     datamart_platform = Column(String)
#     cdm_version = Column(Numeric(15, 8))
#     datamart_claims = Column(String)
#     datamart_ehr = Column(String)
#     birth_date_mgmt = Column(String)
#     enr_start_date_mgmt = Column(String)
#     enr_end_date_mgmt = Column(String)
#     admit_date_mgmt = Column(String)
#     discharge_date_mgmt = Column(String)
#     px_date_mgmt = Column(String)
#     rx_order_date_mgmt = Column(String)
#     rx_start_date_mgmt = Column(String)
#     rx_end_date_mgmt = Column(String)
#     dispense_date_mgmt = Column(String)
#     lab_order_date_mgmt = Column(String)
#     specimen_date_mgmt = Column(String)
#     result_date_mgmt = Column(String)
#     measure_date_mgmt = Column(String)
#     onset_date_mgmt = Column(String)
#     report_date_mgmt = Column(String)
#     resolve_date_mgmt = Column(String)
#     pro_date_mgmt = Column(String)
#     refresh_demographic_date = Column(Date)
#     refresh_enrollment_date = Column(Date)
#     refresh_encounter_date = Column(Date)
#     refresh_diagnosis_date = Column(Date)
#     refresh_procedures_date = Column(Date)
#     refresh_vital_date = Column(Date)
#     refresh_dispensing_date = Column(Date)
#     refresh_lab_result_dm_date = Column(Date)
#     refresh_condition_date = Column(Date)
#     refresh_pro_dm_date = Column(Date)
#     refresh_prescribing_date = Column(Date)
#     refresh_pcornet_trial_date = Column(Date)
#     refresh_death_date = Column(Date)
#     refresh_death_cause_date = Column(Date)
#
#     class Meta:
#         unique_together = ('networkid',
#                            'datamartid',)
#
#     def __str__(self):
#         return "<Harvest(networkid='%s', datamartid='%s')>" % (self.networkid, self.datamartid)
