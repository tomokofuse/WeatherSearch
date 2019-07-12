from django.db import models

class Tenki(models.Model):
    id = models.IntegerField(primary_key=True)
    area = models.CharField(max_length=10, blank=True, null=True)
    prefecture = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    label_1 = models.CharField(max_length=10, blank=True, null=True)
    day_1 = models.DateField(blank=True, null=True)
    telop_1 = models.CharField(max_length=100, blank=True, null=True)
    label_2 = models.CharField(max_length=10, blank=True, null=True)
    day_2 = models.DateField(blank=True, null=True)
    telop_2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenki'

    def __str__(self):
        return self.area
        
