# sekolah_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  UserViewSet, SekolahViewSet, KelasViewSet, SiswaViewSet, PelanggaranKategoriViewSet, PelanggaranViewSet 
from .views import UserDetail, UserRegistration, UserLogin, UserLogout

router = DefaultRouter()
router.register(r'sekolah', SekolahViewSet)
router.register(r'kelas', KelasViewSet)
router.register(r'siswa', SiswaViewSet)
# router.register(r'petugas', PetugasViewSet)
router.register(r'pelanggaran_kategori', PelanggaranKategoriViewSet)
router.register(r'pelanggaran', PelanggaranViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('me/', UserDetail.as_view(), name='me'),
]

# urls.py
# from django.urls import path
# from .views import UserRegistration, UserLogin, UserLogout

# urlpatterns = [
#     path('register/', UserRegistration.as_view(), name='register'),
#     path('login/', UserLogin.as_view(), name='login'),
#     path('logout/', UserLogout.as_view(), name='logout'),
#     # Add URLs for other user types if needed
# ]