from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from enum import Enum
import uuid 
from django.utils import timezone



class Specialite(Enum):
    CARDIOLOGIE = 'Cardiologie'
    DERMATOLOGIE = 'Dermatologie'
    GASTRO_ENTEROLOGIE = 'Gastro-entérologie'
    NEUROLOGIE = 'Neurologie'
    PEDIATRIE = 'Pédiatrie'
    PSYCHIATRIE = 'Psychiatrie'
    RADIOLOGIE = 'Radiologie'
    CHIRURGIE = 'Chirurgie'
    AUTRE = 'Autre'

class Doctor(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField()
    address = models.CharField(max_length=100, null=True, blank=True)
    specialite = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in Specialite])
    numero_tel = models.CharField(max_length=20, null=True, blank=True)
    isPrivee = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    
    @property 
    def get_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.get_name
    
class BloodType(Enum):
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    B_POSITIVE = 'B+'
    B_NEGATIVE = 'B-'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'

class Profile(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    carte_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField()
    numero_tel = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    blood_type = models.CharField(max_length=3, choices=[(tag.value, tag.name) for tag in BloodType])
    gender = models.CharField(max_length=10, choices=[(tag.value, tag.name) for tag in Gender])
    image = models.ImageField(blank=True, null=True)
    emergency_numbers = models.JSONField(default=list)    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email","carte_id"]

    objects = CustomUserManager()
    
    @property
    def get_name(self):
        return f'{self.first_name} {self.last_name}'    
    
    def __str__(self) -> str:
        return self.get_name


class Labo(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True,null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    numero_tel = models.CharField(max_length=20, blank=True, null=True)
    isLabo = models.BooleanField(default = True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email","carte_id"]

    objects = CustomUserManager()
    
    
    def __str__(self) -> str:
        return self.name


class TypeRadiologie(Enum):
    RADIOGRAPHIE = "Radiographie"
    SCAN = "Tomodensitométrie (TDM)"
    IRM = "Imagerie par Résonance Magnétique (IRM)"
    TEP = "Tomographie par Émission de Positons (TEP)"
    ÉCHOGRAPHIE = "Échographie"
    MAMMOGRAPHIE = "Mammographie"
    FLUOROSCOPIE = "Fluoroscopie"
    MÉDECINE_NUCLÉAIRE = "Imagerie en Médecine Nucléaire"
    AUTRE = "Autre"
    
    
class Radio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    radio_type = models.CharField(max_length=80,choices=[(tag.value,tag.name) for tag in TypeRadiologie])
    radio_file = models.FileField(upload_to='radio_files/', blank=True, null=True)
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='radios',null=True)
    labo = models.ForeignKey(Labo , on_delete = models.SET_NULL,related_name="radios",null=True)

    def __str__(self) -> str:
        return f'{self.patient} {self.labo} Radio'


class TypeMaladie(Enum):
    CARDIOVASCULAIRE = "Maladie cardiovasculaire"
    RESPIRATOIRE = "Maladie respiratoire"
    INFECTIEUSE = "Maladie infectieuse"
    AUTOIMMUNE = "Maladie auto-immune"
    MENTALE = "Maladie mentale"
    GENETIQUE = "Maladie génétique"
    CANCER = "Cancer"
    METABOLIQUE = "Trouble métabolique"
    NEUROLOGIQUE = "Trouble neurologique"
    AUTRE = "Autre"

class Maladie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,blank=True,null= True)
    isChronic = models.BooleanField(default=False)
    maladie_type = models.CharField(max_length=80,choices=[(tag.name,tag.value) for tag in TypeMaladie])
    
    
class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(default=timezone.now,blank=True,null=True)
    maladie = models.ForeignKey(Maladie,on_delete=models.SET_NULL,null=True)
    patient = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name ="reports")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name ="reports",null=True)
    

    
class Ordonance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report = models.OneToOneField(Report,on_delete = models.SET_NULL,blank=True , 
                                null = True,related_name="ordonance")



class Medicament(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)    



class MedicamentDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ratio = models.IntegerField(default=1)
    duree = models.IntegerField(default=7)
    notes = models.TextField(blank=True, null = True)
    isChronic = models.BooleanField(default=False)
    medicament = models.ForeignKey(Medicament,null=True,blank=True , on_delete=models.CASCADE)
    ordonance = models.ForeignKey(Ordonance , on_delete = models.CASCADE , null = True , blank =True,related_name="medicaments")
    

class TypeOperation(Enum):
    CHIRURGIE_CARDIAQUE = "Chirurgie cardiaque"
    CHIRURGIE_ORTHOPEDIQUE = "Chirurgie orthopédique"
    CHIRURGIE_ESTHETIQUE = "Chirurgie esthétique"
    CHIRURGIE_DIGESTIVE = "Chirurgie digestive"
    CHIRURGIE_VASCULAIRE = "Chirurgie vasculaire"
    CHIRURGIE_NEUROLOGIQUE = "Chirurgie neurologique"
    CHIRURGIE_UROLOGIQUE = "Chirurgie urologique"
    CHIRURGIE_GYNECOLOGIQUE = "Chirurgie gynécologique"
    CHIRURGIE_THORACIQUE = "Chirurgie thoracique"
    CHIRURGIE_OPHTALMOLOGIQUE = "Chirurgie ophtalmologique"
    AUTRE = "Autre"

class Operation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    name = models.CharField(max_length=100,blank=True,null=True)
    operation_type = models.CharField(max_length=100 , choices = [(tag.name,tag.value) for tag in TypeOperation])
    patient = models.ForeignKey(Profile,on_delete=models.CASCADE , related_name="operations")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE , related_name="operations" )