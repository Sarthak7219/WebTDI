from django.db import models
from django.utils.text import slugify

class District(models.Model):
    code = models.IntegerField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=30,unique=True)
    st_population = models.IntegerField()
    total_population = models.IntegerField()
    W_BMI = models.FloatField()
    C_UW = models.FloatField()
    AN_W = models.FloatField()
    AN_C = models.FloatField()
    AHC_ANC = models.FloatField()
    AHC_Full_ANC = models.FloatField()
    AHC_PNC = models.FloatField()
    AHC_HI = models.FloatField()
    Enrollment = models.FloatField()
    Equity = models.FloatField()
    E_DropRate = models.FloatField()
    S_Sani = models.FloatField()
    S_CoFu = models.FloatField()
    S_DrWa = models.FloatField()
    S_Elec = models.FloatField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(District, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    def get_multiplier(self):
        ans = self.st_population/self.total_population
        return ans
    
    def get_health_indicator_score(self):
        W_BMI_score = self.W_BMI*self.get_multiplier()
        C_UW_score = self.C_UW*self.get_multiplier()
        AN_W_score = self.AN_W*self.get_multiplier()
        AN_C_score = self.AN_C*self.get_multiplier()
        AHC_ANC_score = self.AHC_ANC*self.get_multiplier()
        AHC_Full_ANC_score = self.AHC_Full_ANC*self.get_multiplier()
        AHC_PNC_score = self.AHC_PNC*self.get_multiplier()
        AHC_HI_score = self.AHC_HI*self.get_multiplier()
        print()
        ind_arr = [
            ['W_BMI_score','C_UW_score'],
            ['AN_W_score','AN_C_score'],
            ['AHC_ANC_score', 'AHC_Full_ANC_score', 'AHC_PNC_score'],
            ['AHC_HI_score']
            ]
        ind_score = []

        for i in ind_arr:
            ans=0
            length=len(i)
            for j in i:
                ans+=j
            avg=ans/length
            ind_arr.append(avg)    
            print(ind_arr)
        return ind_arr


        
    
