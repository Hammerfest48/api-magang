from django.db import models
from django.db .models.fields import DateTimeField, SlugField


class Lowongan(models.Model):
    nama_instansi = models.TextField(null=True, blank=True)
    jenis_pekerjaan = models.TextField(max_length=200)
    tanggal = DateTimeField(auto_now_add=True, null=True)
    deskripsi = models.TextField(max_length=300)

    def __str__(self):
        return self.nama_instansi


