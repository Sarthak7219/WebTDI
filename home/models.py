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
    
    def total_members_across_onedimensionally_developed_households(self):
        ans = []  # Initialize ans list outside of the loop
        households = self.household.all()   # Fetch all households using your ORM (e.g., Django's ORM)

        for i in range(5):
            total_members = 0  # Reset total_members for each dimension
            for household in households:
                members_of_onedimensionally_developed_households = household.is_developed()[i] * household.size
                total_members += members_of_onedimensionally_developed_households  # Update the total members for this dimension
            ans.append(total_members)  # Append the total_members for this dimension to the ans list

        return ans


    def get_tribal_indicator_members(self):
        households = self.household.all() 
        CD_members = 0
        IM_members = 0
        MC_members = 0
        CM_members = 0
        FS_members = 0
        LE_members = 0
        DRO_members = 0
        IC_members   =0
        OW_members   =0
        SANI_members =0
        FUEL_members =0
        DRWA_members =0
        ELECTR_members=0
        ASS_members  =0
        LAN_members  =0
        ARTS_members =0
        EV_members   =0
        MEET_members =0

        for i in households:
            CD_members += i.CD_score * i.size
            IM_members += i.IM_score * i.size
            MC_members += i.MC_score * i.size
            CM_members += i.CM_score * i.size
            FS_members += i.FS_score * i.size
            LE_members += i.LE_score * i.size
            DRO_members += i.DRO_score * i.size
            IC_members   += i.IC_score * i.size
            OW_members    += i.OW_score * i.size
            SANI_members   += i.SANI_score * i.size
            FUEL_members   += i.FUEL_score * i.size
            DRWA_members   += i.DRWA_score * i.size
            ELECTR_members += i.ELECTR_score * i.size
            ASS_members   += i.ASS_score * i.size
            LAN_members   += i.LAN_score * i.size
            ARTS_members   += i.ARTS_score * i.size
            EV_members   += i.EV_score * i.size
            MEET_members += i.MEET_score * i.size
            
        sum=[CD_members,IM_members,MC_members,CM_members,FS_members,LE_members,DRO_members,IC_members,OW_members ,SANI_members  ,FUEL_members  ,DRWA_members  ,ELECTR_members,ASS_members  , LAN_members  ,ARTS_members ,EV_members,MEET_members]
            
        ans = []
        total_members = self.get_total_tribals()
        for i in sum:
            indicator_score = (i/total_members)
            ans.append(round(indicator_score,2))
        return ans


    def tribal_dimensional_incidence(self, tribe_id):
        cnt = 0
        tribe_households = self.household.filter(tribe_id=tribe_id)  # Filter households by tribe_id
        ans = []

        for household in tribe_households:
            household_incidence = household.household_dimensional_incidence()  # Assuming this returns the incidence for the household
            cnt += household_incidence
            ans.append(cnt)

        return ans
    def tribal_incidence(self, tribe_id):
        ans = 0
        tribe_households = self.household.filter(tribe_id=tribe_id)  # Filter households by tribe_id
        for household in tribe_households:
            household_tribal_incidence = household.household_tribal_incidence()  # Assuming this returns the incidence for the household
            ans += household_tribal_incidence
        return ans
    
    def tribal_dimensional_intensity(self):
        ans = []
        households = self.household.all()

        for i in range(0,5):
            cnt = 0  # Reset cnt for each dimension
            for household in households:
                household_intensity = household.household_dimensional_intensity()[i]
                cnt += household_intensity
            ans.append(round(cnt, 3))

        return ans
    def tribal_intensity(self):
        
        households = self.household.all()
        cnt = 0  # Reset cnt for each dimension
        for household in households:
                household_tribal_intensity = household.household_tribal_intensity()[i]
                cnt += household_tribal_intensity
        return cnt
    
    def tribal_dimensional_index(self):
        ans = []
        for i in range(0,5):
            tribal_dimensional_incidence = self.tribal_dimensional_incidence()[i]
            tribal_dimensional_intensity=self.tribal_dimensional_intensity()[i]    
            tribal_dimensional_index=tribal_dimensional_incidence*tribal_dimensional_intensity
            ans.append(round(tribal_dimensional_index, 3))
        return ans
    
    def tribal_index(self):
        triball_incidence = self.triball_incidence()[i]
        tribal_intensity=self.tribal_intensity()[i]    
        tribal_index=triball_incidence*tribal_intensity
        return tribal_index
    
    def total_members_multi_dimensionally_developed_households(self):
        households = self.household.all()
        cnt = 0  # Reset cnt for each dimension
        for household in households:
                if household.is_multidimensionally_developed:
                    multi_dim_dev_mem+=household.size
                cnt += multi_dim_dev_mem
        return cnt

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
            if self.D_DS()[i] < 0.066 :
                cnt = 0
            else:
                cnt = 1
            ans.append(cnt)
        return ans
    
    def tribal_development_score(self):
        ans=0
        for i in range(0,5):
            ans=ans+self.D_DS()[i]
        return ans

    def is_multidimensionally_developed(self):    ##--> TO be Updated!!!!
        ans = []
        res = self.tribal_development_score()
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

    def household_dimensional_incidence(self):
        total_tribals = self.tribeID.get_total_tribals()
        
        incidence = []

        for i in range(0, 5):
            members_in_developed_households = self.members_of_developed_households()[i]  # Call the method as a function

            if total_tribals > 0:
                incidence_value = members_in_developed_households / total_tribals
            else:
                incidence_value = 0.0  # Handle the case where there are no households to avoid division by zero
            incidence.append(round(incidence_value, 2))
        return incidence
    def household_tribal_incidence(self):
        total_tribals = self.tribeID.get_total_tribals()
        if self.is_multidimensionally_developed():
           members_in_developed_households = self.size  # Call the method as a function

        if total_tribals > 0:
                incidence_value = members_in_developed_households / total_tribals
        else:
                incidence_value = 0.0  # Handle the case where there are no households to avoid division by zero
        
        return incidence_value
    


    def household_dimensional_intensity(self):
        intensity = []
        
        # Calculate the total members across one-dimensionally developed households once before the loop

        for i in range(0, 5):
            total_members_across_onedimensionally_developed_households = self.tribeID.total_members_across_onedimensionally_developed_households()[i]
            members_in_developed_households = self.members_of_developed_households()[i]  # Call the method as a function
            score = self.D_DS()[i]
            
            if total_members_across_onedimensionally_developed_households > 0:
                ans = (score * members_in_developed_households * 5) / total_members_across_onedimensionally_developed_households
            else:
                ans = 0.0  # Handle the case where total_members_across_onedimensionally_developed_households is zero

            intensity.append(round(ans, 3))

        return intensity
    
    def household_tribal_intensity(self):
        
        # Calculate the total members across one-dimensionally developed households once before the loop
            total_members_multi_dimensionally_developed_households = self.tribeID.total_members_multi_dimensionally_developed_households()
            if self.is_multidimensionally_developed:
              members_in_developed_households = self.size  # Call the method as a function
            score = self.tribal_development_score
            
            if total_members_multi_dimensionally_developed_households > 0:
                ans = (score * members_in_developed_households * 5) / total_members_multi_dimensionally_developed_households
            else:
                ans = 0.0  # Handle the case where total_members_across_onedimensionally_developed_households is zero\
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


