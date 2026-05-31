from django.db import  models

class AgricultureRecord(models.Model):
    domain_code = models.CharField(max_length=20)
    domain = models.CharField(max_length=1000)
    area_code = models.CharField(max_length=20, db_index=True)
    area = models.CharField(max_length=1000, db_index=True)
    element_code = models.CharField(max_length=20)
    element = models.CharField(max_length=1000)
    item_code = models.CharField(max_length=20)
    item = models.CharField(max_length=1000)
    year_code = models.CharField(max_length=20)
    year = models.CharField(max_length=1000, db_index=True)
    unit = models.CharField(max_length=50)
    value = models.CharField(null=True, blank=True)
    flag = models.CharField()
    flag_description = models.TextField()
    note = models.TextField()
