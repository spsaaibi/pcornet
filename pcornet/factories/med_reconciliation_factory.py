from factory.alchemy import SQLAlchemyModelFactory
import factory
from pcornet import models, common_session, configuration
from pcornet.factories import DemographicFactory
from pcornet import generation_utils as gu
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()


class MedRecFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Med_Reconciliation
        sqlalchemy_session = common_session.Session

    class Params:
        Length = 15

    medreconid = factory.LazyAttribute(lambda o: gu.random_with_N_digits(o.Length))
    patid = factory.SubFactory(DemographicFactory)
    @factory.lazy_attribute
    def medication_name(self):
        return gu.generate_prop_meds()

    @factory.lazy_attribute
    def rx_review_date(self):
        temp = self.patid.birth_date
        # TODO this needs to be a configuration parameter
        temp += timedelta(days=fake.random_digit())
        return temp