from factory.alchemy import SQLAlchemyModelFactory
import factory
from pcornet import models, common_session, configuration
from pcornet.factories import DemographicFactory, EncounterFactory
from pcornet import generation_utils as gu
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()


class PrescribingFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Prescribing
        sqlalchemy_session = common_session.Session

    class Params:
        Length = 8

    prescribingid = factory.LazyAttribute(lambda o: gu.random_with_N_digits(o.Length))
    encounterid = factory.SubFactory(EncounterFactory)
    patid = factory.SubFactory(DemographicFactory)
    # rx_providerid
    # rx_order_date
    # rx_order_time
    # rx_start_date
    @factory.lazy_attribute
    def rx_start_date(self):
        temp = self.encounterid.admit_date
        # TODO this needs to be a configuration parameter
        temp += timedelta(days=fake.random_digit())
        return temp
    # def rx_end_date(self):
    #     temp = self.rx_start_date
    #     # TODO this needs to be a configuration parameter
    #     temp += timedelta(days=fake.random_digit())
    #     return temp
    # rx_quantity
    # rx_quantity_unit
    # rx_refills
    # rx_days_supply
    # rx_frequency
    # rx_basis
    # rxnorm_cui
    @factory.lazy_attribute
    def raw_rx_med_name(self):
        return gu.generate_nonprop_meds()
    # raw_rx_frequency
    # raw_rxnorm_cui
    # raw_rx_quantity
    # raw_rx_ndc
    # raw_rx_basis
    # raw_sedi_brand_name
    # raw_sedi_duke_therapeut_class
    # raw_sedi_administration_route
    # raw_sedi_drug_form
    # raw_sedi_drug_strength
    # raw_sedi_units_per_dose
    # raw_sedi_discrete_dose_units
    # raw_sedi_discrete_dose_amount
    # raw_sedi_pat_ns_loc_key
    # raw_sedi_pat_clinic_loc_key
    # raw_sedi_ordering_prov_key
    # raw_sedi_order_prov_specialty