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
    
    def get_health_multiplier_indicator_score(self):
        W_BMI_score = self.W_BMI*self.get_multiplier()
        C_UW_score = self.C_UW*self.get_multiplier()
        AN_W_score = self.AN_W*self.get_multiplier()
        AN_C_score = self.AN_C*self.get_multiplier()
        AHC_ANC_score = self.AHC_ANC*self.get_multiplier()
        AHC_Full_ANC_score = self.AHC_Full_ANC*self.get_multiplier()
        AHC_PNC_score = self.AHC_PNC*self.get_multiplier()
        AHC_HI_score = self.AHC_HI*self.get_multiplier()
        
        ind_arr = [
            W_BMI_score,C_UW_score,
            AN_W_score,AN_C_score,
            AHC_ANC_score, AHC_Full_ANC_score, AHC_PNC_score,
            AHC_HI_score
            ]
        rounded_ind_arr = [round(value, 3) for value  in ind_arr]
     
        return rounded_ind_arr
    
    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()
    
    def get_health_norm_ind_score(self):
        districts = self.get_all_objects()
        W_BMI_score=[]
        C_UW_score=[]
        AN_W_score=[]
        AN_C_score=[]
        AHC_ANC_score=[]
        AHC_Full_ANC_score=[]
        AHC_PNC_score=[]
        AHC_HI_score=[]
        arr=[   W_BMI_score,C_UW_score,
                AN_W_score,AN_C_score,
                AHC_ANC_score, AHC_Full_ANC_score, AHC_PNC_score,
                AHC_HI_score
                ]
        
        for district in districts:
            W_BMI_score.append(district.get_health_multiplier_indicator_score()[0]),
            C_UW_score.append(district.get_health_multiplier_indicator_score()[1]),
            AN_W_score.append(district.get_health_multiplier_indicator_score()[2]),
            AN_C_score.append(district.get_health_multiplier_indicator_score()[3]),
            AHC_ANC_score.append(district.get_health_multiplier_indicator_score()[4]),
            AHC_Full_ANC_score.append(district.get_health_multiplier_indicator_score()[5]),
            AHC_PNC_score.append(district.get_health_multiplier_indicator_score()[6]),
            AHC_HI_score.append(district.get_health_multiplier_indicator_score()[7]),
        max_arr=[]
        min_arr=[]
        for i in arr:
            max_val = max(i, default=0)
            min_value=min(i, default=0)
            max_arr.append(max_val)
            min_arr.append(min_value)
        
        arr=self.get_health_multiplier_indicator_score()
        norm_arr=[]
        for i in range(0,8):
            ans=((max_arr[i]-arr[i])/(max_arr[i]-min_arr[i]))
            norm_arr.append(round(ans,3))
        return norm_arr
    
    def get_health_ind_score(self):
        W_BMI_score=self.get_health_norm_ind_score()[0]
        C_UW_score=self.get_health_norm_ind_score()[1]
        AN_W_score=self.get_health_norm_ind_score()[2]
        AN_C_score=self.get_health_norm_ind_score()[3]
        AHC_ANC_score=self.get_health_norm_ind_score()[4]
        AHC_Full_ANC_score=self.get_health_norm_ind_score()[5]
        AHC_PNC_score=self.get_health_norm_ind_score()[6]
        AHC_HI_score=self.get_health_norm_ind_score()[7]

        ind_arr = [
            [W_BMI_score,C_UW_score],
            [AN_W_score,AN_C_score],
            [AHC_ANC_score, AHC_Full_ANC_score, AHC_PNC_score],
            [AHC_HI_score]
            ]
        ind_score=[]
        for i in ind_arr:
            ans=0
            p=0
            for j in i:
                ans+=j
                p=p+1
            ind_score.append(ans/p)
        return ind_score
    
    def get_health_score(self):
        get_health_ind_score_values=self.get_health_ind_score()
        sum=0
        j=0
        for i in get_health_ind_score_values:
            sum+=i
            j=j+1
        return (sum/j)
    
    def get_education_norm_ind_score(self):
        
        
        districts = self.get_all_objects()
        for district in districts:
            Enrollment = district.Enrollment
            Equity =district.Equity
            E_DropRate =district.E_DropRate
            arr=[   Enrollment,Equity,E_DropRate
                ]
            max_arr=[]
            min_arr=[]
            for i in arr:
                max_val = max(i, default=0)
                min_value=min(i, default=0)
                max_arr.append(max_val)
                min_arr.append(min_value)
        norm_arr=[]
        for i in range(0,8):
            ans=((max_arr[i]-arr[i])/(max_arr[i]-min_arr[i]))
            norm_arr.append(round(ans,3))
        return norm_arr



    def get_education_score(self):
        get_education_ind_score_values=self.get_education_norm_ind_score()
        sum=0
        j=0
        for i in get_education_ind_score_values:
            sum+=i
            j=j+1
        return (sum/j)
    
    # def get_sol_norm_ind_score(self):
    #     districts = self.get_all_objects()
    #     S_CoFu = self.S_CoFu
    #     S_DrWa = self.S_DrWa
    #     S_Sani = self.S_Sani
    #     S_Elec = self.S_Elec

    #     arr=[   S_CoFu,S_DrWa,S_Sani,S_Elec
    #             ]
        
    #     for district in districts:
    #         max_arr=[]
    #         min_arr=[]
    #         for i in arr:
    #             max_val = max(i, default=0)
    #             min_value=min(i, default=0)
    #             max_arr.append(max_val)
    #             min_arr.append(min_value)
    #     norm_arr=[]
    #     for i in range(0,8):
    #         ans=((max_arr[i]-arr[i])/(max_arr[i]-min_arr[i]))
    #         norm_arr.append(round(ans,3))
    #     return norm_arr



    # def get_sol_score(self):
    #     get_sol_ind_score_values=self.get_sol_norm_ind_score()
    #     sum=0
    #     j=0
    #     for i in get_sol_ind_score_values:
    #         sum+=i
    #         j=j+1
    #     return (sum/j)
    
    
            
                








        
    
