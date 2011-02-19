from django.db import models

class Particular(models.Model):
        id = models.AutoField(primary_key=True)
        year = models.CharField(max_length=5)
        code = models.CharField(max_length=10)
        type = models.CharField(max_length=10)
        title = models.CharField(max_length=2000)
        particulars = models.CharField(max_length=2000)
        project  = models.CharField(max_length=2000)
        issue = models.CharField(max_length=2000)
        event = models.CharField(max_length=2000)
        general = models.CharField(max_length=2000)

        #def __unicode__(self):
        #        return self.name
        class Meta:
                verbose_name_plural = "Particulars"
                db_table = "Particular"

class Journal(models.Model):
        id = models.AutoField(primary_key=True)
        year = models.CharField(max_length=5)
        code = models.CharField(max_length=10)
        type = models.CharField(max_length=10)
        particulars = models.CharField(max_length=2000)
        project  = models.CharField(max_length=2000)
        general = models.CharField(max_length=2000)

        #def __unicode__(self):
        #        return self.name
        class Meta:
                verbose_name_plural = "Journals"
                db_table = "Journal"

class Book(models.Model):
        id = models.AutoField(primary_key=True)
        year = models.CharField(max_length=5)
        code = models.CharField(max_length=10)
        type = models.CharField(max_length=10)
        particulars = models.CharField(max_length=2000)
        Bycorrea = models.BooleanField()

        #def __unicode__(self):
        #        return self.name
        class Meta:
                verbose_name_plural = "Books"
                db_table = "Book"

class Abbreviation(models.Model):
        id = models.AutoField(primary_key=True)
        Abbreviation = models.CharField(max_length=20)
        project  = models.CharField(max_length=2000)

        #def __unicode__(self):
        #        return self.name
        class Meta:
                verbose_name_plural = "Abbreviations"
                db_table = "Abbreviation"	

#class Drawings(models.Model):	
