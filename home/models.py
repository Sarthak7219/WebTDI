from django.db import models
# from import_export import resources, fields
# from import_export.widgets import ForeignKeyWidget

# Create your models here.
class Tribe_Image(models.Model):
    image=models.ImageField(upload_to='images')
    location=models.CharField(max_length=50)
    date=models.DateField()


class Tribe(models.Model):

    name=models.CharField(max_length=50)
    image=models.ForeignKey(Tribe_Image, on_delete=models.CASCADE, related_name='tribe_image', null=True, blank=True)
    incidence=models.FloatField(null=True, blank=True)
    intensity=models.FloatField(null=True, blank=True)
    tdi=models.FloatField(null=True, blank=True)

    def get_total_tribals(self):
        cnt = 0
        households = self.household.all()  # Use the reverse relationship "household_set"
        for i in households:
            cnt = cnt + i.size
        return cnt

    def get_tribal_indicator_members(self):
        households = self.household.all() 
        CD_members =0
        IM_members =0
        MC_members =0
        CM_members =0
        FS_members =0
        LE_members =0
        DRO_members =0
        for i in households:
            sum = [i.CD_score*i.size+CD_members, i.IM_score*i.size+IM_members, i.MC_score*i.size+MC_members, i.CM_score*i.size+CM_members, i.FS_score*i.size+FS_members, i.LE_score*i.size+LE_members, i.DRO_score*i.size+DRO_members]
     
        ans = []
        total_members = self.get_total_tribals()
        for i in sum:
            percentage = (i/total_members)*100
            ans.append(percentage)

        return ans
          

            
            
            
        
       

        


    
class Household(models.Model):
    tribeID = models.ForeignKey(Tribe, on_delete=models.CASCADE, related_name="household", null=True, blank=True)
    tribe_name = models.CharField(max_length=20, null=True, blank=True)
    size = models.IntegerField(null= True, blank=True)

    # HEALTH
    CD_score = models.IntegerField(null = True, blank=True)
    IM_score = models.IntegerField(null = True, blank=True)
    MC_score = models.IntegerField(null = True, blank=True)
    CM_score = models.IntegerField(null = True, blank=True)
    FS_score = models.IntegerField(null = True, blank=True)

    # EDUCATION
    LE_score = models.BooleanField(null=True, blank=True)
    DRO_score = models.BooleanField(null=True, blank=True)

    #SOL
    IC_score = models.BooleanField(null=True, blank=True)
    OW_score = models.BooleanField(null=True, blank=True)
    SANI_score = models.BooleanField(null=True, blank=True)
    FUEL_score = models.BooleanField(null=True, blank=True)
    DRWA_score = models.BooleanField(null=True, blank=True)
    ELECTR_score = models.BooleanField(null=True, blank=True)
    ASS_score = models.BooleanField(null=True, blank=True)

    #CULTURE
    LAN_score = models.BooleanField(null=True, blank=True)
    ARTS_score = models.BooleanField(null=True, blank=True)

    #GOVERNANCE
    EV_score = models.BooleanField(null=True, blank=True)
    MEET_score = models.BooleanField(null=True, blank=True)


    def no_of_indicators(self):
        scores_H = [self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score]
        scores_E = [self.LE_score, self.DRO_score]
        scores_S = [self.IC_score, self.OW_score, self.SANI_score, self.FUEL_score, self.DRWA_score, self.ELECTR_score, self.ASS_score]
        scores_C =[self.LAN_score, self.ARTS_score]
        scores_G = [self.EV_score, self.MEET_score]

        scores = [scores_H, scores_E, scores_S, scores_C, scores_G]
        ans = []
        for i in scores:
            cnt = 0 
            for score in i:
                if score is not None:
                    cnt += 1
            ans.append(cnt)
        return ans
    
    def developed_indicators(self):
        scores_H = [self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score]
        scores_E = [self.LE_score, self.DRO_score]
        scores_S = [self.IC_score, self.OW_score, self.SANI_score, self.FUEL_score, self.DRWA_score, self.ELECTR_score, self.ASS_score]
        scores_C =[self.LAN_score, self.ARTS_score]
        scores_G = [self.EV_score, self.MEET_score]

        scores = [scores_H, scores_E, scores_S, scores_C, scores_G]
        ans = []
    
        for i in scores:
            cnt = 0 
            for score in i:
                if score is not None:
                    cnt += score
            ans.append(cnt)
        return ans

    
    def calculate_weightage(self):
        ans = []
        for i in range(0, 5):
            if self.no_of_indicators()[i]:
                cnt = 0.2 * (1 / self.no_of_indicators()[i])
            else:
                cnt = 0
            ans.append(round(cnt,2))

        return ans
    
    def D_DS(self):
        ans = []
        for i in range(0,5):
            weightage = self.calculate_weightage()[i]
            cnt = weightage * self.developed_indicators()[i]
            ans.append(round(cnt,2))
            
        return ans
    
    def is_developed(self):
        ans = []
        for i in range(0,5):
            if self.D_DS()[i] > 0.033 :
                cnt = 1
            else:
                cnt = 0
            ans.append(cnt)
        return ans
    
    
    def is_multidimensionally_developed(self):    ##--> TO be Updated!!!!
        ans = []
        for i in range(0,5):
            res = sum([self.developed_indicators()[i], self.developed_indicators()[i], self.developed_indicators()[i], self.developed_indicators()[i], self.developed_indicators()[i]])
            if res > 1:
                ans.append(1)
            else:
                ans.append(0)
        return ans

    def members_of_developed_households(self):
        ans = []
        for i in range(0,5):
            cnt = (int(self.is_developed()[i]))*(int(self.size))
            ans.append(round(cnt,2))
            
        return ans
    
    # def developed_indicators_members(self):
    #     scores_H = [self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score]
    #     scores_E = [self.LE_score, self.DRO_score]
    #     scores_S = [self.IC_score, self.OW_score, self.SANI_score, self.FUEL_score, self.DRWA_score, self.ELECTR_score, self.ASS_score]
    #     scores_C =[self.LAN_score, self.ARTS_score]
    #     scores_G = [self.EV_score, self.MEET_score]

    #     scores = [scores_H, scores_E, scores_S, scores_C, scores_G]
    #     ans = []
    
    #     for i in scores:
    #         cnt = 0 
    #         for score in i:
    #             if score is not None:
    #                 cnt += score*self.size
    #         ans.append(cnt)
    #     return ans

    

      
# class HouseholdResource(resources.ModelResource):
#     # Map the 'tribe' field in the Excel file to the 'tribe' ForeignKey field in the model.
#     tribe = fields.Field(
#         column_name='tribe',
#         attribute='tribe',
#         widget=ForeignKeyWidget(Tribe, 'name')
#     )

#     class Meta:
#         model = Household
#         skip_unchanged = True
#         report_skipped = False


        
        
        


    
    # def no_of_H_indicators(self):
    #     scores = [self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score]
    #     ans = 0
    #     for score in scores:
    #         if score is not None:
    #             ans += 1
    #     return ans
    
    # def H_developed_indicators(self):
    #     scores = [self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score]
    #     ans = 0
    #     for score in scores:
    #         if score is not None:
    #             ans += score
    #     return ans
    
    
    # def H_calculate_weightage(self):
    #     if self.no_of_H_indicators():
    #         ans = 0.2 * (1 / self.no_of_H_indicators())
    #         return round(ans,2)
    #     else:
    #         return 0
    
    # def H_DS(self):
    #     weightage = self.H_calculate_weightage()
    #     ans = weightage * self.H_developed_indicators()
    #     return round(ans,2)
    
    # def H_is_developed(self):
    #     if self.H_DS() > 0.033 :
    #         return 1
    #     else:
    #         return 0 
        
    

    # def H_is_multidimensionally_developed(self):
    #     res = sum([self.H_developed_indicators(), self.H_developed_indicators(), self.H_developed_indicators(), self.H_developed_indicators(), self.H_developed_indicators()])
    #     if res > 1:
    #         return 1
    #     else:
    #         return 0
        
    # def members_of_developed_households(self):
    #     ans = (int(self.H_is_developed()))*(int(self.size))
    #     return round(ans,2)
    
    # ################

    # #EDUCATION
    # ###############

    


    
    # def no_of_E_indicators(self):
    #     scores = [self.LE_score, self.DRO_score]
    #     ans = 0
    #     for score in scores:
    #         if score is not None:
    #             ans += 1
    #     return ans
    
    # def E_developed_indicators(self):
    #     scores = [self.LE_score, self.DRO_score]
    #     ans = 0
    #     for score in scores:
    #         if score is not None:
    #             ans += score
    #     return ans
    
    
    # def E_calculate_weightage(self):
    #     if self.no_of_E_indicators():
    #         return 0.2 * (1 / self.no_of_E_indicators())
    #     else:
    #         return 0
    
    # def E_DS(self):
    #     weightage = self.E_calculate_weightage()
    #     return weightage * self.E_developed_indicators()
    
    # def E_is_developed(self):
    #     if self.E_DS() > 0.033 :
    #         return 1
    #     else:
    #         return 0 
        
    

    # def E_is_multidimensionally_developed(self):
    #     res = sum([self.E_developed_indicators(), self.E_developed_indicators(), self.E_developed_indicators(), self.E_developed_indicators(), self.E_developed_indicators()])
    #     if res > 1:
    #         return 1
    #     else:
    #         return 0
        
    # def members_of_developed_households(self):
    #     return (int(self.E_is_developed()))*(int(self.size))

    # ##########

    # #SOL
    # ########
    


    
    # def no_of_S_indicators(self):
    #     scores = [self.IC_score, self.OW_score, self.SANI_score, self.FUEL_score, self.DRWA_score, self.ELECTR_score, self.ASS_score]
    #     ans = 0
    #     for score in scores:
    #         if score is not None:
    #             ans += 1
    #     return ans
    
    # def S_developed_indicators(self):
    #     scores = [self.IC_score, self.OW_score, self.SANI_score, self.FUEL_score, self.DRWA_score, self.ELECTR_score, self.ASS_score]
    #     ans = 0
    #     for score in scores:
    #         if score is not None:
    #             ans += score
    #     return ans
    
    
    # def S_calculate_weightage(self):
    #     if self.no_of_S_indicators():
    #         return 0.2 * (1 / self.no_of_S_indicators())
    #     else:
    #         return 0
    
    # def S_DS(self):
    #     weightage = self.S_calculate_weightage()
    #     return weightage * self.S_developed_indicators()
    
    # def S_is_developed(self):
    #     if self.S_DS() > 0.033 :
    #         return 1
    #     else:
    #         return 0 
        
    

    # def S_is_multidimensionally_developed(self):
    #     res = sum([self.S_developed_indicators(), self.S_developed_indicators(), self.S_developed_indicators(), self.S_developed_indicators(), self.S_developed_indicators()])
    #     if res > 1:
    #         return 1
    #     else:
    #         return 0
        
    # def members_of_developed_households(self):
    #     return (int(self.S_is_developed()))*(int(self.size))
    
    # ##########

    # #CULTURE
    # ##########
    


    
    # def no_of_C_indicators(self):
    #     scores = [self.LAN_score, self.ARTS_score]
    #     ans = 0
    #     for score in scores:
    #         if score is not None:
    #             ans += 1
    #     return ans
    
    # def C_developed_indicators(self):
    #     scores = [self.LAN_score, self.ARTS_score]
    #     ans = 0
    #     for score in scores:
    #         if score is not None:
    #             ans += score
    #     return ans
    
    
    # def C_calculate_weightage(self):
    #     if self.no_of_C_indicators():
    #         return 0.2 * (1 / self.no_of_C_indicators())
    #     else:
    #         return 0
    
    # def C_DS(self):
    #     weightage = self.C_calculate_weightage()
    #     return weightage * self.C_developed_indicators()
    
    # def C_is_developed(self):
    #     if self.C_DS() > 0.033 :
    #         return 1
    #     else:
    #         return 0 
        
    

    # def C_is_multidimensionally_developed(self):
    #     res = sum([self.C_developed_indicators(), self.C_developed_indicators(), self.C_developed_indicators(), self.C_developed_indicators(), self.C_developed_indicators()])
    #     if res > 1:
    #         return 1
    #     else:
    #         return 0
        
    # def members_of_developed_households(self):
    #     return (int(self.C_is_developed()))*(int(self.size))
    
    # ###########

    # #GOVERNANCE
    # ###########
    


    
    # def no_of_G_indicators(self):
    #     scores = [self.EV_score, self.MEET_score]
    #     ans = 0
    #     for score in scores:
    #         if score is not None:
    #             ans += 1
    #     return ans
    
    # def G_developed_indicators(self):
    #     scores = [self.EV_score, self.MEET_score]
    #     ans = 0
    #     for score in scores:
    #         if score is not None:
    #             ans += score
    #     return ans
    
    
    # def G_calculate_weightage(self):
    #     if self.no_of_G_indicators():
    #         return 0.2 * (1 / self.no_of_G_indicators())
    #     else:
    #         return 0
    
    # def G_DS(self):
    #     weightage = self.G_calculate_weightage()
    #     return weightage * self.G_developed_indicators()
    
    # def G_is_developed(self):
    #     if self.G_DS() > 0.033 :
    #         return 1
    #     else:
    #         return 0 
        
    

    # def G_is_multidimensionally_developed(self):
    #     res = sum([self.G_developed_indicators(), self.G_developed_indicators(), self.G_developed_indicators(), self.G_developed_indicators(), self.G_developed_indicators()])
    #     if res > 1:
    #         return 1
    #     else:
    #         return 0
        
    # def members_of_developed_households(self):
    #     return (int(self.G_is_developed()))*(int(self.size))
    
    ##############


