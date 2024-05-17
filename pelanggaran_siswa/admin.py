# pelanggaran_siswa/admin.py
from django.contrib import admin
from .models import Sekolah, Kelas, Siswa, User, PelanggaranKategori, Pelanggaran

@admin.register(Sekolah)
class SekolahAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat', 'kota', 'provinsi', 'no_telp', 'email', 'website']
    search_fields = ['nama', 'kota', 'provinsi']
    list_filter = ['kota', 'provinsi']

@admin.register(Kelas)
class KelasAdmin(admin.ModelAdmin):
    list_display = ['nama', 'sekolah', 'tingkat']
    search_fields = ['nama', 'sekolah__nama']
    list_filter = ['sekolah', 'tingkat']

@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    list_display = ['nis', 'nama', 'sekolah', 'kelas', 'nama_ortu', 'hp_ortu']
    search_fields = ['nis', 'nama', 'sekolah__nama', 'kelas__nama']
    list_filter = ['sekolah', 'kelas']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'nama', 'email', 'no_hp', 'sekolah', 'jabatan', 'is_staff', 'is_superuser']
    search_fields = ['username', 'nama', 'email', 'sekolah__nama']
    list_filter = ['sekolah', 'is_staff', 'is_superuser']

@admin.register(PelanggaranKategori)
class PelanggaranKategoriAdmin(admin.ModelAdmin):
    list_display = ['nama', 'sekolah', 'poin']
    search_fields = ['nama', 'sekolah__nama']
    list_filter = ['sekolah', 'poin']

@admin.register(Pelanggaran)
class PelanggaranAdmin(admin.ModelAdmin):
    list_display = ['siswa', 'tgl_jam', 'kategori', 'poin', 'petugas', 'kelas', 'sekolah']
    search_fields = ['siswa__nama', 'kategori__nama', 'petugas__username', 'kelas__nama', 'sekolah__nama']
    list_filter = ['sekolah', 'kategori', 'kelas', 'tgl_jam']
