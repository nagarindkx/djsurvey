from django.db import models

# Create your models here.


class Survey(models.Model):
    fullname = models.CharField(
        verbose_name="ชื่อ",
        max_length=255,  blank=False)
    email = models.EmailField(
        verbose_name="อีเมล",
        blank=False)
    gender = models.CharField(
        verbose_name="เพศ",
        max_length=1,    blank=False,
        choices=[('F', 'หญิง'), ('M', 'ชาย')],
        default='F',
    )
    birthdate = models.DateField(
        verbose_name="วันเดือนปีเกิด",
        auto_now=False,  blank=False)
    fruit = models.CharField(
        verbose_name="ผลไม้ที่ท่านชอบ",
        max_length=1,    blank=False,
        choices=[('a', 'แอปเปิ้ล'), ('b', 'มะละกอ'),
                 ('c', 'กล้วย'), ('d', 'ส้ม')],
        default='c',
    )
    comment = models.TextField(
        verbose_name="ข้อเสนอแนะ",
        blank=True)
