from django.db import models

class Type(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=15, unique=True)
        def __unicode__(self):
                return self.name
        
        class Meta:
                verbose_name_plural = "Types"
                db_table = "Type"
                
class Library(models.Model):
        id = models.AutoField(primary_key=True)
        year = models.CharField(max_length=5)
        code = models.CharField(max_length=10)
        type = models.ForeignKey(Type, to_field='name')
        particulars = models.CharField(max_length=2000)
        project  = models.CharField(max_length=2000, blank=True)
        issue = models.CharField(max_length=2000, blank=True)
        event = models.CharField(max_length=2000, blank=True)
        general = models.CharField(max_length=2000, blank=True)
        resource = models.CharField(max_length=200, blank=True)
        ByCCORREA = models.BooleanField()
        
        def __unicode__(self):
                return self.code        
        class Meta:
                verbose_name_plural = "Library"
                db_table = "Library"
                ordering = ['-year']

class Abbreviation(models.Model):
        id = models.AutoField(primary_key=True)
        Abbreviation = models.CharField(max_length=20, unique=True)
        project  = models.CharField(max_length=2000)

        def __unicode__(self):
                return '{0}-{1}'.format(self.id, self.Abbreviation)

        class Meta:
                verbose_name_plural = "Abbreviations"
                db_table = "Abbreviation"
