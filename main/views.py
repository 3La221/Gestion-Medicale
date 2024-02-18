from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (Doctor,Profile,Maladie,Medicament,MedicamentDetails,
                    Ordonance,Report,Radio,Labo,Operation)
from .serializers import (DoctorSerializer,ProfileSerializer,
LaboSerialzier,RadioSerializer,ReportSerializer , MaladieSeriailzer, MedicamentSerializer)
# Create your views here.


@api_view(['GET','POST'])
def getDoctors(request):
    if request.method == "GET":
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        if 'password' not in request.data:
            return Response({'password': ['This field is required.']}, status=status.HTTP_400_BAD_REQUEST)
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET','PUT','DELETE'])
def getDoctor(request,pk):
    try:
        doctor = Doctor.objects.get(id=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #GET
    if request.method == "GET":
        serializer = DoctorSerializer(doctor,many=False,context= {'docor_id':pk})
        return Response(serializer.data)
    #PUT
    elif request.method == "PUT":
        serializer = DoctorSerializer(doctor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET','POST'])
def getProfiles(request):
    if request.method == "GET":
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        if 'password' not in request.data:
            return Response({'password': ['This field is required.']}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET','PUT','DELETE'])
def getProfile(request,pk):
    try:
        profile = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #GET
    if request.method == "GET":
        serializer = ProfileSerializer(profile,many=False)
        return Response(serializer.data)
    #PUT
    elif request.method == "PUT":
        serializer = ProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def getLabos(request):
    if request.method == "GET":
        labos = Labo.objects.all()
        serializer = LaboSerialzier(labos,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        if 'password' not in request.data:
            return Response({'password': ['This field is required.']}, status=status.HTTP_400_BAD_REQUEST)
        serializer = LaboSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET','PUT','DELETE'])
def getLabo(request,pk):
    
    try:
        labo = Labo.objects.get(id=pk)
    except Labo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #GET
    if request.method == "GET":
        serializer = LaboSerialzier(labo,many=False,context={'labo_id':pk})
        return Response(serializer.data)
    #PUT
    elif request.method == "PUT":
        serializer = LaboSerialzier(labo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        labo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



    
@api_view(['GET','POST'])
def getRadios(request):
    if request.method == "GET":
        radios = Radio.objects.all()
        serializer = RadioSerializer(radios,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = RadioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET','PUT','DELETE'])
def getRadio(request,pk):
    try:
        radio = Radio.objects.get(id=pk)
    except Radio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == "GET":
        serializer = RadioSerializer(radio,many=False)
        return Response(serializer.data)
    #PUT
    elif request.method == "PUT":
        serializer = RadioSerializer(radio,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #delete
    if request.method == "DELETE":
        radio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST','DELETE'])
def getReports(request):
    if request.method == "GET":
        reports = Report.objects.all()
        serializer = ReportSerializer(reports,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        reports = Report.objects.all()
        reports.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
@api_view(['GET','PUT','DELETE'])
def getReport(request,pk):
    try:
        report = Report.objects.get(id=pk)
    except Radio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == "GET":
        serializer = ReportSerializer(report,many=False)
        return Response(serializer.data)
    #PUT
    elif request.method == "PUT":
        serializer = ReportSerializer(report,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #delete
    if request.method == "DELETE":
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def getMaladies(request):
    if request.method == "GET":
        maladies = Maladie.objects.all()
        serializer = MaladieSeriailzer(maladies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def getMedicament(request):
    if request.method == "GET":
        medicaments = Medicament.objects.all()
        serializer = MedicamentSerializer(medicaments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)