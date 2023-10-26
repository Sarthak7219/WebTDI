from django.db import models
from django.utils.text import slugify
import math


class District(models.Model):
    code = models.IntegerField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=30,unique=True)
    st_population = models.IntegerField()
    total_population = models.IntegerField()
    #HEALTH
    W_BMI = models.FloatField()
    C_UW = models.FloatField()
    AN_W = models.FloatField()
    AN_C = models.FloatField()  
    AHC_ANC = models.FloatField()
    AHC_Full_ANC = models.FloatField()
    AHC_PNC = models.FloatField()
    AHC_HI = models.FloatField()
    
    #EDUCATION
    Enrollment = models.FloatField()
    Equity = models.FloatField()
    E_DropRate = models.FloatField()

    #SOL
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
    

    def get_indicator_st_scores(self):
        multiplier = self.get_multiplier()

        #HEALTH
        W_BMI_score = self.W_BMI*multiplier
        C_UW_score = self.C_UW*multiplier
        AN_W_score = self.AN_W*multiplier
        AN_C_score = self.AN_C*multiplier
        AHC_ANC_score = self.AHC_ANC*multiplier
        AHC_Full_ANC_score = self.AHC_Full_ANC*multiplier
        AHC_PNC_score = self.AHC_PNC*multiplier
        AHC_HI_score = self.AHC_HI*multiplier

        #EDUCATION
        Enrollment_score = self.Enrollment
        Equity_score = self.Equity
        E_DropRate_score = self.E_DropRate

        #SOL
        S_Sani_score = self.S_Sani*multiplier
        S_CoFu_score = self.S_CoFu*multiplier
        S_DrWa_score = self.S_DrWa*multiplier
        S_Elec_score = self.S_Elec*multiplier

        ind_arr = [
            W_BMI_score,C_UW_score,AN_W_score,AN_C_score,AHC_ANC_score,AHC_Full_ANC_score,AHC_PNC_score,AHC_HI_score,Enrollment_score, Equity_score, E_DropRate_score,S_Sani_score,S_CoFu_score,S_DrWa_score,S_Elec_score
            ]  #Index 0 to 6 are subindicators of health

        rounded_ind_arr = [round(value, 1) for value in ind_arr]
        return rounded_ind_arr
    
    #get all districts
    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()
    

    # Class-level variables to store the calculated values
    _max_arr = None
    _min_arr = None

    #Get max and min scores for all indicators/sub I
    def get_max_min_ind_scores(self):
        # Check if the values have already been calculated and stored
        if District._max_arr is not None and District._min_arr is not None:
            return District._max_arr, District._min_arr

        districts = self.get_all_objects()
        max_arr = [0.0] * 15
        min_arr = [0.0] * 15

        for i in range(15):
            one_ind_scores = []
            for district in districts:
                score = district.get_indicator_st_scores()[i]
                one_ind_scores.append(score)
            max_val = max(one_ind_scores)
            min_val = min(one_ind_scores)
            max_arr[i] = round(max_val,1)
            min_arr[i] = round(min_val,1)

        # Store the calculated values in class-level variables
        District._max_arr = max_arr
        District._min_arr = min_arr

        return [max_arr, min_arr]

        
    
    def get_normalized_ind_scores(self):

        max_arr = self.get_max_min_ind_scores()[0]
        min_arr = self.get_max_min_ind_scores()[1]
        norm_arr = [0.0]*15
        scores = self.get_indicator_st_scores()

        for i in range(15):
            max = max_arr[i]
            min = min_arr[i]
            act_val = scores[i]
            if(i>=0 and i<4 or i==9 or i==10):
                norm_value = (max-act_val)/(max-min)
            else:
                norm_value = (act_val-min)/(max-min)
            norm_arr[i] = norm_value
       

        x = 6  # Round off number

        norm_arr_final = [
            [round((norm_arr[0] + norm_arr[1]) / 2, x), round((norm_arr[2] + norm_arr[3]) / 2, x), round((norm_arr[4] + norm_arr[5] + norm_arr[6]) / 3, x), round(norm_arr[7], x)],
            [round(norm_arr[8], x), round(norm_arr[9], x), round(norm_arr[10], x)],
            [round(norm_arr[11], x), round(norm_arr[12], x), round(norm_arr[13], x), round(norm_arr[14], x)]
        ]

        return norm_arr_final
    
    def get_dimension_scores(self):
        norm_arr = self.get_normalized_ind_scores()
        dimension_arr = []
        for i in norm_arr:
            sum =0
            for j in i:
                sum += j
            avg = sum/len(i)
            dimension_arr.append(round(avg,3))

        return dimension_arr
    
    def get_tdi_score(self):
        dimension_scores = self.get_dimension_scores()
        total = sum(dimension_scores)
        length = len(dimension_scores)
        prod = 1

        for i in dimension_scores:
            prod = prod*i

        arithmetic_tdi = round(total/length,3)
        geometric_tdi = round(math.pow(prod, 1/length),3)

        return [arithmetic_tdi, geometric_tdi]


    def get_dimension_contribution_tdi(self):
        dimension_arr = self.get_dimension_scores()
        total = sum(dimension_arr)
        ans = [round((dimension_arr[0]/total)*100), round((dimension_arr[1]/total)*100), round((dimension_arr[2]/total)*100)]
        return ans


                






    
            
                








        
    
