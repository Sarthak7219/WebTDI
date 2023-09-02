from django.db import models

# Create your models here.
class Tribe_Image(models.Model):
    image=models.ImageField(upload_to='images')
    location=models.CharField(max_length=50)
    date=models.DateField()

class Tribe(models.Model):
    name=models.CharField(max_length=50)
    # image=models.ForeignKey(Tribe_Image, on_delete=models.CASCADE, related_name='tribe_image', null=True, blank=True)
    H_DI=models.IntegerField()
    E_DI=models.IntegerField()
    SOL_DI=models.IntegerField()
    C_DI=models.IntegerField()
    G_DI=models.IntegerField()
    incidence=models.FloatField(null=True, blank=True)
    intensity=models.FloatField(null=True, blank=True)
    tdi=models.FloatField(null=True, blank=True)

class Health(models.Model):
    HH_size=models.IntegerField(blank=True,null=True)
    HH_score_H_CD=models.BooleanField(blank=True,null=True)
    HH_score_H_IMM=models.BooleanField(blank=True,null=True)
    HH_score_H_MC=models.BooleanField(blank=True,null=True)
    HH_score_H_U5C=models.BooleanField(blank=True,null=True)
    HH_score_H_FS=models.BooleanField(blank=True,null=True)
    total_indicator=models.IntegerField(blank=True,null=True)
    developed_indicator=models.IntegerField(blank=True,null=True)
    Weightage=models.FloatField(blank=True,null=True)
    score=models.FloatField(blank=True,null=True)
    Is_Developed=models.BooleanField(blank=True,null=True)
    H_incidence=models.FloatField(blank=True,null=True)
    H_intensity=models.FloatField(blank=True,null=True)
    H_H_members_of_developed_HHs=models.IntegerField(blank=True,null=True)



    


