from marshmallow_sqlalchemy import ModelSchema, fields
from marshmallow import fields, post_dump
from pcornet import models
import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import timedelta


class VitalModelSchema(ModelSchema):
    Start = fields.Method('get_start')
    Finish = fields.Method('get_finish')
    Task = fields.Str('Vital')
    Resource = fields.Str('Vital')

    def get_finish(self, obj):
        temp = obj.measure_date + timedelta(days=1)
        return temp.strftime('%Y-%m-%d')

    def get_start(self, obj):
        temp = obj.measure_date.strftime('%Y-%m-%d')
        return temp

    class Meta:
        model = models.Vital
        fields = ('Start', 'Finish', 'Task', 'Resource')


class ProceduresModelSchema(ModelSchema):
    Start = fields.Method('get_start')
    Finish = fields.Method('get_finish')
    Task = fields.Str('Procedures')
    Resource = fields.Str('Procedures')

    def get_finish(self, obj):
        temp = obj.px_date + timedelta(days=1)
        return temp.strftime('%Y-%m-%d')

    def get_start(self, obj):
        temp = obj.px_date.strftime('%Y-%m-%d')
        return temp

    class Meta:
        model = models.Procedures
        fields = ('Start', 'Finish', 'Task', 'Resource')


class PrescribingModelSchema(ModelSchema):

    Start = fields.Method('get_start', allow_none=True)
    Finish = fields.Method('get_finish', allow_none=True)
    Task = fields.Str('Prescribing')
    Resource = fields.Str('Prescribing')

    def get_finish(self, obj):
        if obj.rx_end_date is None:
            temp = obj.rx_start_date + timedelta(days=30)
            return temp.strftime('%Y-%m-%d')
        else:
            temp = obj.rx_end_date
            return temp.strftime('%Y-%m-%d')

    def get_start(self, obj):
        temp = obj.rx_start_date
        return temp.strftime('%Y-%m-%d')

    class Meta:
        model = models.Prescribing
        fields = ('Start', 'Finish', 'Task', 'Resource')


class MedReconciliationModelSchema(ModelSchema):

    Start = fields.Method('get_start')
    Finish = fields.Method('get_finish')
    Task = fields.Str('MedReconciliation')
    Resource = fields.Str('MedReconciliation')

    def get_finish(self, obj):
        temp = obj.rx_review_date + timedelta(days=1)
        return temp.strftime('%Y-%m-%d')

    def get_start(self, obj):
        temp = obj.rx_review_date.strftime('%Y-%m-%d')
        return temp

    class Meta:
        model = models.Med_Reconciliation
        fields = ('Start', 'Finish', 'Task', 'Resource')


class LabResultModelSchema(ModelSchema):

    Start = fields.Method('get_start')
    Finish = fields.Method('get_finish')
    Task = fields.Str('Labs')
    Resource = fields.Str('Labs')

    def get_finish(self, obj):
        temp = obj.specimen_date + timedelta(days=1)
        return temp.strftime('%Y-%m-%d')

    def get_start(self, obj):
        temp = obj.specimen_date.strftime('%Y-%m-%d')
        return temp

    class Meta:
        model = models.Lab_Result_CM
        fields = ('Start', 'Finish', 'Task', 'Resource')


class DiagnosisModelSchema(ModelSchema):

    Start = fields.Method('get_start')
    Finish = fields.Method('get_finish')
    Task = fields.Str('Diagnosis')
    Resource = fields.Str('Diagnosis')

    def get_finish(self, obj):
        temp = obj.raw_sedi_diagnosis_date + timedelta(days=1)
        return temp.strftime('%Y-%m-%d')

    def get_start(self, obj):
        temp = obj.raw_sedi_diagnosis_date.strftime('%Y-%m-%d')
        return temp

    class Meta:
        model = models.Diagnosis
        fields = ('Start', 'Finish', 'Task', 'Resource')



class EncounterModelSchema(ModelSchema):
    diagnosis = fields.Nested(DiagnosisModelSchema, many=True)
    procedures = fields.Nested(ProceduresModelSchema, many=True)
    prescribing = fields.Nested(PrescribingModelSchema, many=True)
    diagnosis = fields.Nested(DiagnosisModelSchema, many=True)

    Start = fields.Method('get_start', allow_none=True)
    Finish = fields.Method('get_finish', allow_none=True)
    Task = fields.Str('Encounter')
    Resource = fields.Str('Encounter')

    def get_finish(self, obj):
        if obj.discharge_date is None:
            temp = obj.admit_date + timedelta(days=30)
            return temp.strftime('%Y-%m-%d')
        elif obj.discharge_date==obj.admit_date:
            temp = obj.admit_date + timedelta(days=1)
            return temp.strftime('%Y-%m-%d')
        else:
            temp = obj.discharge_date
            return temp.strftime('%Y-%m-%d')

    def get_start(self, obj):
        temp = obj.admit_date
        return temp.strftime('%Y-%m-%d')

    class Meta:
        model = models.Prescribing
        fields = ('Start', 'Finish', 'Task', 'Resource')


    class Meta:
        model = models.Encounter
        fields = ('Start', 'Finish', 'Task', 'Resource', 'diagnosis', 'procedures',
                  'prescribing')


class PlotlyGnattSchema(ModelSchema):
    patid = fields.String()
    age = fields.Method("get_age")
    sex = fields.String()
    hispanic = fields.String()
    encounter = fields.Nested(EncounterModelSchema, many=True)
    lab_result_cm = fields.Nested(LabResultModelSchema, many=True)
    med_reconciliation = fields.Nested(MedReconciliationModelSchema, many=True)
    vital = fields.Nested(VitalModelSchema, many=True)

    class Meta:
        model = models.Demographic
        fields = ('patid', 'age', 'sex', 'hispanic', 'encounter', 'lab_result_cm', 'med_reconciliation', 'vital')

    def get_age(self, obj):
        return relativedelta(dt.datetime.now().date(), obj.birth_date).years

    @post_dump
    def flatten(self, data):
        newdata = []
        for datum in data['encounter']:
            newdict = {'Start': datum['Start'],
                       'Finish': datum['Finish'],
                       'Task': datum['Task'],
                       'Resource': datum['Resource']}
            newdata.append(newdict)
            for x in datum['diagnosis']:
                newdata.append(x)
            for x in datum['prescribing']:
                newdata.append(x)
            for x in datum['procedures']:
                newdata.append(x)
        for x in data['lab_result_cm']:
            newdata.append(x)
        for x in data['med_reconciliation']:
            newdata.append(x)
        for x in data['vital']:
            newdata.append(x)
        final = list({(v['Start'], v['Finish'], v['Task']): v for v in newdata}.values())
        newdict = {
            'patid': data['patid'],
            'age': data['age'],
            'sex': data['sex'],
            'hispanic': data['hispanic'],
            'df': final
        }
        return newdict
