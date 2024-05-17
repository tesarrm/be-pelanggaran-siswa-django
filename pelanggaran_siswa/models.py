# pelanggaran_siswa/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Sekolah(models.Model):
    nama = models.CharField(max_length=99)
    alamat = models.CharField(max_length=199, blank=True, null=True)
    kota = models.CharField(max_length=99, blank=True, null=True)
    provinsi = models.CharField(max_length=99, blank=True, null=True)
    no_telp = models.CharField(max_length=19, blank=True, null=True)
    email = models.EmailField(max_length=99, blank=True, null=True)
    website = models.URLField(max_length=99, blank=True, null=True)
    catatan = models.CharField(max_length=199, blank=True, null=True)

    def __str__(self):
        return self.nama

class Kelas(models.Model):
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)
    nama = models.CharField(max_length=99)
    tingkat = models.PositiveSmallIntegerField()
    catatan = models.CharField(max_length=199, blank=True, null=True)

    def __str__(self):
        return self.nama

class Siswa(models.Model):
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)
    nis = models.CharField(max_length=19)
    nama = models.CharField(max_length=99)
    kelas = models.ForeignKey(Kelas, on_delete=models.SET_NULL, null=True, blank=True)
    nama_ortu = models.CharField(max_length=99, blank=True, null=True)
    hp_ortu = models.CharField(max_length=19, blank=True, null=True)
    email_ortu = models.EmailField(max_length=99, blank=True, null=True)
    catatan = models.CharField(max_length=199, blank=True, null=True)

    def __str__(self):
        return self.nama

class UserManager(BaseUserManager):
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)

    def _create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

# class Petugas(models.Model):
#     sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)
#     nama = models.CharField(max_length=99)
#     jabatan = models.CharField(max_length=99, blank=True, null=True)
#     no_hp = models.CharField(max_length=19, blank=True, null=True)
#     email = models.EmailField(max_length=99, blank=True, null=True)
#     catatan = models.CharField(max_length=199, blank=True, null=True)

#     # ketika diubah menjadi string maka akan muncul nama
#     def __str__(self):
#         return self.nama

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=49, unique=True)
    nama = models.CharField(max_length=99, blank=True, null=True)
    email = models.EmailField(max_length=99, blank=True, null=True)
    no_hp = models.CharField(max_length=19, blank=True, null=True)
    catatan = models.CharField(max_length=199, blank=True, null=True)
    last_login = models.DateTimeField(null=True, blank=True)
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)
    jabatan = models.CharField(max_length=99, blank=True, null=True)
    catatan = models.CharField(max_length=199, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nama', 'email', 'no_hp']

    objects = UserManager()

    def __str__(self):
        return self.username

class PelanggaranKategori(models.Model):
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)
    nama = models.CharField(max_length=99)
    poin = models.PositiveIntegerField()
    pesan = models.CharField(max_length=199, blank=True, null=True)
    catatan = models.CharField(max_length=199, blank=True, null=True)

    def __str__(self):
        return self.nama

class Pelanggaran(models.Model):
    sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE)
    tgl_jam = models.DateTimeField()
    petugas = models.ForeignKey(User, on_delete=models.CASCADE)
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    kategori = models.ForeignKey(PelanggaranKategori, on_delete=models.CASCADE)
    poin = models.PositiveIntegerField()
    catatan = models.CharField(max_length=199, blank=True, null=True)

    def __str__(self):
        return f'{self.siswa} - {self.kategori}'
