# sekolah_app/serializers.py
from rest_framework import serializers
from .models import Sekolah, Kelas, Siswa, PelanggaranKategori, Pelanggaran, User

class SekolahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sekolah
        fields = '__all__'

class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = '__all__'

class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = '__all__'

class PelanggaranKategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = PelanggaranKategori
        fields = '__all__'

class PelanggaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggaran
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'
