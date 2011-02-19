from django.db import models

class Type(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=15, unique=True)
        class Meta:
                verbose_name_plural = "Types"
                db_table = "Type"
                
class Library(models.Model):
        id = models.AutoField(primary_key=True)
        year = models.CharField(max_length=5)
        code = models.CharField(max_length=10)
        type = models.ForeignKey(Type, to_field='name')
        particulars = models.CharField(max_length=2000)
        project  = models.CharField(max_length=2000)
        issue = models.CharField(max_length=2000)
        event = models.CharField(max_length=2000)
        general = models.CharField(max_length=2000)
        resource = models.CharField(max_length=200)
        
        class Meta:
                verbose_name_plural = "Library"
                db_table = "Library"

class Abbreviation(models.Model):
        id = models.AutoField(primary_key=True)
        Abbreviation = models.CharField(max_length=20)
        project  = models.CharField(max_length=2000)

        class Meta:
                verbose_name_plural = "Abbreviations"
                db_table = "Abbreviation"
