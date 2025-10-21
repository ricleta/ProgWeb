from django.db import models

class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='NAME') # Field name
    mpg = models.FloatField(db_column='MPG') # Field name
    cyl = models.IntegerField(db_column='CYL') # Field name
    disp = models.FloatField(db_column='DISP') # Field name
    hp = models.IntegerField(db_column='HP') # Field name
    wt = models.FloatField(db_column='WT') # Field name
    qsec = models.FloatField(db_column='QSEC') # Field name
    vs = models.IntegerField(db_column='VS') # Field name
    am = models.IntegerField(db_column='AM') # Field name
    gear = models.IntegerField(db_column='GEAR') # Field name

    class Meta:
        managed = True
        db_table = 'MTCars'
        ordering = ['id']

    def __str__(self):
        return self.name