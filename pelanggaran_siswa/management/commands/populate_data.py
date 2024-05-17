import os
import django
from faker import Faker
import random
from django.utils import timezone
from django.core.management.base import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from pelanggaran_siswa.models import Sekolah, Kelas, Siswa, User, PelanggaranKategori, Pelanggaran

class Command(BaseCommand):
    help = 'Populate database with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # def create_sekolah(n=5):
        #     for _ in range(n):
        #         Sekolah.objects.create(
        #             nama=fake.company(),
        #             alamat=fake.address(),
        #             kota=fake.city(),
        #             provinsi=fake.state(),
        #             no_telp=fake.phone_number(),
        #             email=fake.email(),
        #             website=fake.url(),
        #             catatan=fake.text(max_nb_chars=199)
        #         )

        # def create_kelas(n=20):
        #     sekolahs = list(Sekolah.objects.all())
        #     for _ in range(n):
        #         Kelas.objects.create(
        #             sekolah=random.choice(sekolahs),
        #             nama=fake.word().capitalize(),
        #             tingkat=random.randint(1, 12),
        #             catatan=fake.text(max_nb_chars=199)
        #         )

        def create_siswa(n=100):
            sekolahs = list(Sekolah.objects.all())
            kelass = list(Kelas.objects.all())
            for _ in range(n):
                Siswa.objects.create(
                    sekolah=random.choice(sekolahs),
                    nis=fake.unique.random_number(digits=5),
                    nama=fake.name(),
                    kelas=random.choice(kelass),
                    nama_ortu=fake.name(),
                    hp_ortu=fake.phone_number(),
                    email_ortu=fake.email(),
                    catatan=fake.text(max_nb_chars=199)
                )

        # def create_user(n=10):
        #     sekolahs = list(Sekolah.objects.all())
        #     for _ in range(n):
        #         User.objects._create_user(
        #             username=fake.user_name(),
        #             password='password123',
        #             nama=fake.name(),
        #             email=fake.email(),
        #             no_hp=fake.phone_number(),
        #             sekolah=random.choice(sekolahs),
        #             jabatan=fake.job(),
        #             catatan=fake.text(max_nb_chars=199)
        #         )

        # def create_pelanggaran_kategori(n=10):
        #     sekolahs = list(Sekolah.objects.all())
        #     for _ in range(n):
        #         PelanggaranKategori.objects.create(
        #             sekolah=random.choice(sekolahs),
        #             nama=fake.word().capitalize(),
        #             poin=random.randint(1, 10),
        #             pesan=fake.sentence(),
        #             catatan=fake.text(max_nb_chars=199)
        #         )

        # def create_pelanggaran(n=50):
        #     sekolahs = list(Sekolah.objects.all())
        #     users = list(User.objects.all())
        #     siswas = list(Siswa.objects.all())
        #     kelass = list(Kelas.objects.all())
        #     kategoris = list(PelanggaranKategori.objects.all())
        #     for _ in range(n):
        #         Pelanggaran.objects.create(
        #             sekolah=random.choice(sekolahs),
        #             tgl_jam=fake.date_time_this_year(before_now=True, after_now=False, tzinfo=timezone.get_current_timezone()),
        #             petugas=random.choice(users),
        #             siswa=random.choice(siswas),
        #             kelas=random.choice(kelass),
        #             kategori=random.choice(kategoris),
        #             poin=random.randint(1, 10),
        #             catatan=fake.text(max_nb_chars=199)
        #         )

        # print("Populating Sekolah...")
        # create_sekolah()
        # print("Populating Kelas...")
        # create_kelas()
        # print("Populating Siswa...")
        create_siswa()
        print("Populating User...")
        # create_user()
        # print("Populating Pelanggaran Kategori...")
        # create_pelanggaran_kategori()
        # print("Populating Pelanggaran...")
        # create_pelanggaran()
        print("Done!")
