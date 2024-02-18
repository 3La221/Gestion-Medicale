from rest_framework import serializers
from .models import (Doctor, Profile , Labo , Radio ,
                    Report, Maladie , Medicament , Ordonance ,
                    MedicamentDetails)

class DoctorSerializer(serializers.ModelSerializer):
    patients = serializers.SerializerMethodField()
    
    def get_patients(self,obj):
        try:
            doctor_id = self.context['doctor_id']
            reports_of_docor = Report.objects.filter(doctor=doctor_id)
            patients = set(report.patient.id for report in reports_of_docor)
            return list(patients)
        except :
            return []
    
    class Meta:
        model = Doctor
        exclude = ['password']
        
        
        
class LaboSerialzier(serializers.ModelSerializer):
    patients = serializers.SerializerMethodField()
    
    def get_patients(self,obj):
        try:
            labo_id = self.context['labo_id']
            print(labo_id)
            radio_of_labo = Radio.objects.filter(labo=labo_id)
            print(radio_of_labo)
            patients = set(radio.patient.id for radio in radio_of_labo)
            return list(patients)
        except:
            return []
    
    class Meta:
        model = Labo
        fields = ['id','email','name','address','numero_tel','isLabo','patients']
        
        

class RadioSerializer(serializers.ModelSerializer):
        
        
    class Meta:
        model = Radio
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        fields = ['id', 'carte_id', 'email', 'first_name',
                'last_name', 'birth_date', 'numero_tel', 
                'address', 'blood_type', 'gender', 'image',
                'emergency_numbers',]

    
    

class RadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radio
        fields = '__all__'

class MedicamentSerializer(serializers.ModelSerializer):
    
        
    class Meta:
        model = Medicament
        fields = '__all__'

class MedicamentDetailsSerializer(serializers.ModelSerializer):
    medicament = MedicamentSerializer()
    
    class Meta :
        model = MedicamentDetails
        exclude = ['ordonance','id']    
        
    def create(self, validated_data):
        medicament_data = validated_data["medicament"]
        medicament , _ = Medicament.objects.get_or_create(**medicament_data)
        medicament_details  = MedicamentDetails.objects.create(medicament = medicament , **validated_data)
        return medicament_details
        
        
class OrdonanceSerializer(serializers.ModelSerializer):
    medicaments = MedicamentDetailsSerializer(many=True)
    
    class Meta:
        model = Ordonance
        fields = ['medicaments']   

        
        
            

class ReportSerializer(serializers.ModelSerializer):
    ordonance = OrdonanceSerializer()
    class Meta:
        model = Report
        fields = '__all__'
        
        
class MaladieSeriailzer(serializers.ModelSerializer):
    class Meta:
        model = Maladie
        fields = '__all__'





    

class ReportSerializer(serializers.ModelSerializer):
    maladie = MaladieSeriailzer()
    ordonance = OrdonanceSerializer(required=False)
    
    class Meta:
        model = Report
        fields = '__all__'
        
    def create(self,validated_data):
        maladie_data = validated_data.pop("maladie")
        maladie,_ = Maladie.objects.get_or_create(**maladie_data)
        ordonance_data = validated_data.pop("ordonance")
        medicaments_data = ordonance_data.pop("medicaments")
        
    
        report = Report.objects.create(maladie=maladie  ,**validated_data)
        ordonance = Ordonance.objects.create(report=report)
        
        for med in medicaments_data:
            
            medicament_name = med.pop("medicament")
            print("Name",medicament_name)
            print("Med",med)
            medicament , _ = Medicament.objects.get_or_create(name=medicament_name["name"])
            
            medicaments = MedicamentDetails.objects.create(medicament = medicament , ordonance = ordonance ,**med)
            report.ordonance.medicaments.add(medicaments)
        
        
        return report
