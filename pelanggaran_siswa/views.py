# from django.shortcuts import render

# # Create your views here.# views.py
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from .models import User, Sekolah, Kelas, Siswa, PelanggaranKategori, Pelanggaran
from .serializers import UserSerializer, SekolahSerializer, KelasSerializer, SiswaSerializer,  PelanggaranKategoriSerializer, PelanggaranSerializer
from rest_framework.permissions import IsAuthenticated

# from .permissions import IsSuperAdmin, IsSuperAdminOrReadOnly, IsPetugasOrReadOnly, IsSiswaOrReadOnly, IsPetugas, IsSiswa

class SekolahViewSet(viewsets.ModelViewSet):
    queryset = Sekolah.objects.all()
    serializer_class = SekolahSerializer
    # permission_classes = [IsSuperAdminOrReadOnly]

class KelasViewSet(viewsets.ModelViewSet):
    queryset = Kelas.objects.annotate(count=Count('pelanggaran'))
    serializer_class = KelasSerializer
    # permission_classes = [IsSuperAdminOrReadOnly, IsPetugasOrReadOnly]


class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer
    # permission_classes = [IsSuperAdminOrReadOnly, IsPetugasOrReadOnly]

# class PetugasViewSet(viewsets.ModelViewSet):
#     queryset = Petugas.objects.all()
#     serializer_class = PetugasSerializer
#     permission_classes = [IsSuperAdminOrReadOnly]

class PelanggaranKategoriViewSet(viewsets.ModelViewSet):
    queryset = PelanggaranKategori.objects.all()
    serializer_class = PelanggaranKategoriSerializer
    # permission_classes = [IsSuperAdminOrReadOnly, IsPetugasOrReadOnly]

class PelanggaranViewSet(viewsets.ModelViewSet):
    queryset = Pelanggaran.objects.all()
    serializer_class = PelanggaranSerializer
    # permission_classes = [IsSuperAdminOrReadOnly, IsPetugasOrReadOnly]

class PelanggaranKategoriViewSet(viewsets.ModelViewSet):
    queryset = PelanggaranKategori.objects.annotate(count=Count('pelanggaran'))
    serializer_class = PelanggaranKategoriSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsSuperAdmin]


class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogout(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)