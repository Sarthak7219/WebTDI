from django.db import models

# Create your models here.
class Tribe_Image(models.Model):
    image=models.ImageField(upload_to='images')
    location=models.CharField(max_length=50)
    date=models.DateField()

class Tribe(models.Model):
    name=models.CharField(max_length=50)
    # image=models.ForeignKey(Tribe_Image, on_delete=models.CASCADE, related_name='tribe_image', null=True, blank=True)
    incidence=models.FloatField(null=True, blank=True)
    intensity=models.FloatField(null=True, blank=True)
    tdi=models.FloatField(null=True, blank=True)
    # def get_dim_index(self):
    #      return (self.incidence)*(self.intensity)


class Health(models.Model):
    HH_size=models.IntegerField(blank=True,null=True)
    HH_Score_H_CD=models.BooleanField(blank=True,null=True)
    HH_Score_H_IMM=models.BooleanField(blank=True,null=True)
    HH_Score_H_MC=models.BooleanField(blank=True,null=True)
    HH_Score_H_U5C=models.BooleanField(blank=True,null=True)
    HH_Score_H_FS=models.BooleanField(blank=True,null=True)
    total_indicator=models.IntegerField(blank=True,null=True)
    developed_indicator=models.IntegerField(blank=True,null=True)
    Weightage=models.FloatField(blank=True,null=True)
    score=models.FloatField(blank=True,null=True)
    Is_Developed=models.BooleanField(blank=True,null=True)
    H_incidence=models.FloatField(blank=True,null=True)
    H_intensity=models.FloatField(blank=True,null=True)
    H_H_members_of_developed_HHs=models.IntegerField(blank=True,null=True)
    def get_dim_index(self):
         return (self.H_incidence)*(self.H_intensity)

class Education(models.Model):
    HH_size=models.IntegerField(blank=True,null=True)
    HH_Score_E_LE=models.BooleanField(blank=True,null=True)
    HH_Score_E_DRO=models.BooleanField(blank=True,null=True)
    total_indicator=models.IntegerField(blank=True,null=True)
    developed_indicator=models.IntegerField(blank=True,null=True)
    Weightage=models.FloatField(blank=True,null=True)
    score=models.FloatField(blank=True,null=True)
    Is_Developed=models.BooleanField(blank=True,null=True)
    E_H_members_of_developed_HHs=models.IntegerField(blank=True,null=True)
    E_incidence=models.FloatField(blank=True,null=True)
    E_intensity=models.FloatField(blank=True,null=True)
    def get_dim_index(self):
         return (self.E_incidence)*(self.E_intensity)

class SOL(models.Model):
    HH_size=models.IntegerField(blank=True,null=True)
    HH_Score_S_IC=models.BooleanField(blank=True,null=True)
    HH_Score_S_OWN=models.BooleanField(blank=True,null=True)
    HH_Score_S_SANI=models.BooleanField(blank=True,null=True)
    HH_Score_S_Fuel=models.BooleanField(blank=True,null=True)
    HH_Score_S_SoDrWa=models.BooleanField(blank=True,null=True)
    HH_Score_S_ELECTR=models.BooleanField(blank=True,null=True)
    HH_Score_S_ASS=models.BooleanField(blank=True,null=True)
    total_indicator=models.IntegerField(blank=True,null=True)
    developed_indicator=models.IntegerField(blank=True,null=True)
    Weightage=models.FloatField(blank=True,null=True)
    score=models.FloatField(blank=True,null=True)
    Is_Developed=models.BooleanField(blank=True,null=True)
    S_H_members_of_developed_HHs=models.IntegerField(blank=True,null=True)
    S_incidence=models.FloatField(blank=True,null=True)
    S_intensity=models.FloatField(blank=True,null=True)
    def get_dim_index(self):
         return (self.S_incidence)*(self.S_intensity)

class Culture(models.Model):
    HH_size=models.IntegerField(blank=True,null=True)
    HH_Score_C_L=models.BooleanField(blank=True,null=True)
    HH_Score_C_Arts=models.BooleanField(blank=True,null=True)
    total_indicator=models.IntegerField(blank=True,null=True)
    developed_indicator=models.IntegerField(blank=True,null=True)
    Weightage=models.FloatField(blank=True,null=True)
    score=models.FloatField(blank=True,null=True)
    Is_Developed=models.BooleanField(blank=True,null=True)
    C_H_members_of_developed_HHs=models.IntegerField(blank=True,null=True)
    C_incidence=models.FloatField(blank=True,null=True)
    C_intensity=models.FloatField(blank=True,null=True)
    def get_dim_index(self):
         return (self.C_incidence)*(self.C_intensity)
class Governence(models.Model):
    HH_size=models.IntegerField(blank=True,null=True)
    HH_Score_G_EV=models.BooleanField(blank=True,null=True)
    HH_Score_G_meeting=models.BooleanField(blank=True,null=True)
    total_indicator=models.IntegerField(blank=True,null=True)
    developed_indicator=models.IntegerField(blank=True,null=True)
    Weightage=models.FloatField(blank=True,null=True)
    score=models.FloatField(blank=True,null=True)
    Is_Developed=models.BooleanField(blank=True,null=True)
    G_H_members_of_developed_HHs=models.IntegerField(blank=True,null=True)
    G_incidence=models.FloatField(blank=True,null=True)
    G_intensity=models.FloatField(blank=True,null=True)
    def get_dim_index(self):
         return (self.G_incidence)*(self.G_intensity)