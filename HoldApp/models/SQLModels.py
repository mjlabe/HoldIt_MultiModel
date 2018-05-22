# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Caseinfo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=10, blank=True, null=True)  # Field name made lowercase.
    summary = models.CharField(db_column='Summary', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CaseInfo'


class Device(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Device'


class Report(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=10, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Report'


class Typed(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    typedinfo = models.ForeignKey('Typedinfo', models.DO_NOTHING, db_column='TypeDInfo')  # Field name made lowercase.
    typedattributes = models.ForeignKey('Typedattributes', models.DO_NOTHING, db_column='TypeDAttributes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeD'


class Typedassociation(models.Model):
    id = models.ForeignKey(Device, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    device = models.CharField(db_column='Device', max_length=10)  # Field name made lowercase.
    caseinfo = models.ForeignKey(Caseinfo, models.DO_NOTHING, db_column='CaseInfo', blank=True, null=True)  # Field name made lowercase.
    report = models.ForeignKey(Report, models.DO_NOTHING, db_column='Report', blank=True, null=True)  # Field name made lowercase.
    typed = models.ForeignKey(Typed, models.DO_NOTHING, db_column='TypeD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeDAssociation'


class Typedattributes(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    attributes = models.CharField(db_column='Attributes', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeDAttributes'


class Typedinfo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeDInfo'


class Typeh(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    typehinfo = models.ForeignKey('Typehinfo', models.DO_NOTHING, db_column='TypeHInfo')  # Field name made lowercase.
    typehdata = models.ForeignKey('Typehdata', models.DO_NOTHING, db_column='TypeHData')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeH'


class Typehassociation(models.Model):
    id = models.ForeignKey(Device, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    device = models.CharField(db_column='Device', max_length=10)  # Field name made lowercase.
    caseinfo = models.ForeignKey(Caseinfo, models.DO_NOTHING, db_column='CaseInfo', blank=True, null=True)  # Field name made lowercase.
    report = models.ForeignKey(Report, models.DO_NOTHING, db_column='Report', blank=True, null=True)  # Field name made lowercase.
    typeh = models.ForeignKey(Typeh, models.DO_NOTHING, db_column='TypeH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeHAssociation'


class Typehdata(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    data = models.CharField(db_column='Data', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeHData'


class Typehinfo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeHInfo'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
