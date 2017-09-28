from factory.alchemy import SQLAlchemyModelFactory
import factory
from pcornet import models, common_session, configuration
from pcornet import generation_utils as gu


class DemographicFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Demographic
        sqlalchemy_session = common_session.Session

    class Params:
        Length = 7
        SEX = configuration.SEX
        HISPANIC = configuration.HISPANIC
        RELIGION = configuration.RELIGION
        RACE = configuration.RACE
        LANGUAGE = configuration.LANGUAGE
        EMPLOYMENT_STS = configuration.EMPLOYMENT_STS
        MARITAL_STS = configuration.MARITAL_STS

    patid = factory.LazyAttribute(lambda o: gu.random_with_N_digits(o.Length))
    birth_date = factory.LazyFunction(gu.generate_date_between)
    birth_time = '00:00'
    raw_sex = factory.LazyAttribute(lambda o: gu.generate_a_choice_configuration(o.SEX))

    @factory.lazy_attribute
    def sex(self):
        if self.raw_sex == 'INDETERMINATE':
            return 'A'
        elif self.raw_sex == 'FEMALE':
            return 'F'
        elif self.raw_sex == 'MALE':
            return 'M'
        elif self.raw_sex == 'UNKNOWN':
            return 'UN'
    # raw_sexual_orientation =
    sexual_orientation = 'NI'
    # raw_gender_identity =
    gender_identity = 'NI'
    raw_hispanic = factory.LazyAttribute(lambda o: gu.generate_a_choice_configuration(o.HISPANIC))

    @factory.lazy_attribute
    def hispanic(self):
        if self.raw_hispanic in ['HISPANIC MEXICAN', 'HISPANIC PUERTO RICAN', 'HISPANIC OTHER', 'HISPANIC CUBAN',
                                 'HISPANIC OR LATINO']:
            return 'Y'
        elif self.raw_hispanic in ['UNAVAILABLE', None]:
            return 'NI'
        elif self.raw_hispanic in ['Declined', 'NOT REPORTED/DECLINED']:
            return 'R'
        elif self.raw_hispanic in ['OTHER']:
            return 'OT'
        elif self.raw_hispanic in ['NOT HISPANIC/LATINO']:
            return 'N'

    raw_race = factory.LazyAttribute(lambda o: gu.generate_a_choice_configuration(o.RACE))

    @factory.lazy_attribute
    def race(self):
        if self.raw_race in ['ALASKAN NATIVE', 'AMERICAN INDIAN', 'AMERICAN INDIAN OR ALASKAN NATIVE']:
            return '01'
        elif self.raw_race in ['ASIAN']:
            return '02'
        elif self.raw_race in ['BLACK OR AFRICAN AMERICAN']:
            return '03'
        elif self.raw_race in ['HAWAII-PACIFIC', 'NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER']:
            return '04'
        elif self.raw_race in ['CAUCASIAN/WHITE', 'WHITE OR CAUCASIAN']:
            return '05'
        elif self.raw_race in ['2 OR MORE RACES', 'MULTIRACIAL']:
            return '06'
        elif self.raw_race in ['DECLINED', 'NOT REPORTED/DECLINED']:
            return '07'
        elif self.raw_race in ['UNAVAILABLE', None]:
            return 'NI'
        elif self.raw_race in ['OTHER']:
            return 'OT'
        elif self.raw_race in ['UNKNOWN']:
            return 'UN'
    # biobank_flag = factory.Iterator()
    raw_sedi_religion = factory.LazyAttribute(lambda o: gu.generate_a_choice_configuration(o.RELIGION))
    raw_sedi_employment_sts = factory.LazyAttribute(lambda o: gu.generate_a_choice_configuration(o.EMPLOYMENT_STS))
    raw_sedi_language_name = factory.LazyAttribute(lambda o: gu.generate_a_choice_configuration(o.LANGUAGE))
    raw_sedi_current_marital_sts = factory.LazyAttribute(lambda o: gu.generate_a_choice_configuration(o.MARITAL_STS))
    # raw_sedi_partial_flag =
