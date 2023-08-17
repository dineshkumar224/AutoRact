from django.db import models

# Create your models here.


class details(models.Model):
    # img = models.BooleanField(default=True)
    name = models.CharField(max_length=122, null=True, blank=True)
    # fname = models.CharField(max_length=122, null=True, blank=True)
    gender = models.CharField(max_length=122, null=True, blank=True)
    id_no = models.CharField(max_length=122, null=True, blank=True)
    dob = models.CharField(max_length=122, null=True, blank=True)
    # id_type = models.CharField(max_length=122, null=True, blank=True)

    def __str__(self):
        return self.name
