# sekolah_app/serializers.py
from rest_framework import serializers
from .models import Sekolah, Kelas, Siswa, PelanggaranKategori, Pelanggaran, User

class SekolahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sekolah
        fields = '__all__'

class KelasSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Kelas
        fields = ['id', 'nama', 'tingkat', 'sekolah', 'catatan', 'count']

class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = '__all__'

class PelanggaranKategoriSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)
    class Meta:
        model = PelanggaranKategori
        fields = ['id', 'nama', 'poin', 'pesan', 'catatan', 'count']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'

class PelanggaranSerializer(serializers.ModelSerializer):
    sekolah = SekolahSerializer()
    petugas = UserSerializer()  # Assuming Petugas is a User, update this if different
    siswa = SiswaSerializer()
    kelas = KelasSerializer()
    kategori = PelanggaranKategoriSerializer()

    class Meta:
        model = Pelanggaran
        fields = '__all__'
