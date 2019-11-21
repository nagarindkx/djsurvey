from django.db import models

# Create your models here.

class Survey(models.Model):
    fullname    = models.CharField(max_length=255,  blank=False)
    email       = models.EmailField(                blank=False)
    gender      = models.CharField(max_length=1,    blank=False,
                            choices=[('F','หญิง'),('M','ชาย')],
                            default='F',
                        )
    birthdate   = models.DateField(auto_now=False,  blank=False)
    fruit       = models.CharField(max_length=1,    blank=False,
                            choices=[('a','แอปเปิ้ล'),('b','มะละกอ'),('c','กล้วย'),('d','ส้ม')],
                            default='c',
                        )
    comment     = models.TextField(                 blank=True)