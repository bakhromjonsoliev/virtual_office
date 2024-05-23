from django.db import models
from django.contrib.auth.models import User

class Murojaat(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Korib chiqilmoqda'),
        ('accepted', 'Qabol qilindi'),
        ('rejected', 'Rad etildi'),
        ('answered', 'Javob berildi'),
    ]

    VILOYAT_CHOICES = [
        ('Andijon', 'Andijon'),
        ('Buxoro', 'Buxoro'),
        ('Jizzax', 'Jizzax'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Navoiy', 'Navoiy'),
        ('Namangan', 'Namangan'),
        ('Samarqand', 'Samarqand'),
        ('Surxondaryo', 'Surxondaryo'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Toshkent', 'Toshkent'),
        ('Fargona', 'Fargona'),
        ('Xorazm', 'Xorazm'),
        ('Qoraqalpogiston', 'Qoraqalpogiston'),
    ]

    MUROJAAT_CHOICES = [
        ('murojaat', 'Murojaat'),
        ('taklif', 'Taklif'),
        ('shikoyat', 'Shikoyat'),
        ('talabnoma', 'Talabnoma'),
        ('bosh_ish_orin', 'Bosh_ish_orin'),
        ('rahbariyat_qabuli', 'Rahbariyat_qabuli'),
        ('sayt_mamuriyatiga', 'Sayt_mamuriyatiga'),
    ]

    fish = models.CharField(max_length=255)
    ish_joyi = models.CharField(max_length=255)
    telefon = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    hudud = models.CharField(max_length=255, choices=VILOYAT_CHOICES)
    manzil = models.CharField(max_length=255)
    passport = models.CharField(max_length=255)
    murojaat_turi = models.CharField(max_length=255, choices=MUROJAAT_CHOICES)
    murojaat_mavzusi = models.CharField(max_length=255)
    murojaat_matni = models.CharField(max_length=255)
    murojaat_fayli = models.FileField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.fish} {self.murojaat_turi} {self.murojaat_mavzusi}'
