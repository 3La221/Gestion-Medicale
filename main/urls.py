from django.urls import path
from . import views


urlpatterns = [
    path("doctor/",views.getDoctors , name="list-doctors"),
    path("doctor/<str:pk>",views.getDoctor,name="list-doctor"),
    
    path("profile/",views.getProfiles , name="list-profiles"),
    path("profile/<str:pk>",views.getProfile,name="list-profile"),
    
    
    path("labo/",views.getLabos , name="list-labos"),
    path("labo/<str:pk>",views.getLabo,name="list-labo"),
    
    path("radio/",views.getRadios , name="list-radios"),
    path("radio/<str:pk>",views.getRadio,name="list-radio"),
    
    path("report/",views.getReports , name="list-reports"),
    path("report/<str:pk>",views.getReport,name="list-report"),
    
    path("maladie/",views.getMaladies , name="list-maladies"),
    
    path("medicament/", views.getMedicament , name ="list-medicaments")
    
]
