from django.db import models
import decimal
from decimal import Decimal,InvalidOperation
from import_export import resources, fields
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
    
    def total_households_across_onedindicator_developed_households(self):
        ans = []  # Initialize ans list outside of the loop
        households = self.household.all()   # Fetch all households using your ORM (e.g., Django's ORM)

        for i in range(5):
            total_members = 0  # Reset total_members for each dimension
            for household in households:
                members_of_onedimensionally_developed_households = household.is_developed()[i] * household.size
                total_members += members_of_onedimensionally_developed_households  # Update the total members for this dimension
            ans.append(total_members)  # Append the total_members for this dimension to the ans list

        return ans

    

    
    # def get_censored_tribal_indicator_score(self):
    #     households = self.household.all() 
        
    #     # Use a dictionary to store indicator scores
    #     indicator_scores = {
    #         'CD': 0, 'IM': 0, 'MC': 0, 'CM': 0, 'FS': 0,
    #         'LE': 0, 'DRO': 0, 'IC': 0, 'OW': 0, 'SANI': 0,
    #         'FUEL': 0, 'DRWA': 0, 'ELECTR': 0, 'ASS': 0,
    #         'LAN': 0, 'ARTS': 0, 'EV': 0, 'MEET': 0
    #     }

    #     for household in households:
    #         tribal_household_index = household.household_tribal_index()

    #         if tribal_household_index >= 0.03:
    #             # Accumulate scores only if the index is greater than or equal to 0.03
    #             for indicator in indicator_scores:
    #                 score_attr = f"{indicator}_score"
                    
    #                 # Check if the household has the score attribute and it is not None
    #                 if hasattr(household, score_attr) and getattr(household, score_attr) is not None:
    #                     indicator_scores[indicator] += getattr(household, score_attr) * household.size

    #     # Calculate total members
    #     total_members = self.get_total_tribals()

    #     # Calculate indicator scores as a proportion of total members
    #     indicator_contributions = []
    #     for indicator, score in indicator_scores.items():
    #         indicator_score = (score / total_members) if total_members != 0 else 0
    #         indicator_contributions.append(round(indicator_score, 2))

    #     return indicator_contributions

    def dimensional_contribution_to_index(self):
        tribe_household=self.household.all()
        get_total_tribals=self.get_total_tribals()
        ans=[]
        for i in range(0,5):
          total_members_of_developed_households=0
          for household in tribe_household:
            total_members_of_developed_households+=household.members_of_developed_households()[i]
          ans.append(total_members_of_developed_households)
        dimensional_contribution_to_index=[]
        for i in ans:
            output=i/get_total_tribals
            dimensional_contribution_to_index.append(output)
        return dimensional_contribution_to_index

        

    def tribal_dimensional_incidence(self):
        ans = []
        households = self.household.all()

        for i in range(0,5):
            cnt = 0  # Reset cnt for each dimension
            for household in households:
                household_incidence = household.household_dimensional_incidence()[i]
                cnt += household_incidence
            ans.append(round(cnt, 3))

        return ans
    
    def tribal_incidence(self):
        ans = 0
        tribe_households = self.household.all() # Filter households by tribe_id
        for household in tribe_households:
            household_tribal_incidence = household.household_tribal_incidence()  # Assuming this returns the incidence for the household
            ans += household_tribal_incidence
        return round(ans,2)
    
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
                household_tribal_intensity = household.household_tribal_intensity()
                cnt += household_tribal_intensity
        return cnt
    
    def tribal_dimensional_index(self):
        ans = []
        incidence_values = self.tribal_dimensional_incidence()
        intensity_values = self.tribal_dimensional_intensity()

        for i in range(5):
            tribal_dimensional_incidence = incidence_values[i]
            tribal_dimensional_intensity = intensity_values[i]
            tribal_dimensional_index = tribal_dimensional_incidence * tribal_dimensional_intensity
            ans.append(round(tribal_dimensional_index, 3))

        return ans

    
    def tribal_index(self):
        tribal_incidence = self.tribal_incidence()
        tribal_intensity=self.tribal_intensity()  
        tribal_index=tribal_incidence*tribal_intensity
        return tribal_index
    
    def total_members_multi_dimensionally_developed_households(self):
        households = self.household.all()
        
        cnt = 0  # Reset cnt for each dimension
        for household in households:
                multi_dim_dev_mem = 0
                if household.is_multidimensionally_developed():
                    multi_dim_dev_mem=household.size
                cnt += multi_dim_dev_mem
        return cnt
    
    def indicators_score(self):
        households = self.household.all()
        total = []  # Initialize the total as an empty list

        # Assuming that the test_indicators for all households have the same structure (lists of lists)
        if households:
            # Initialize total as a copy of the first household's test_indicators
            total = [list(indicators) for indicators in households[0].test_indicators()]

            # Iterate through the rest of the households and add their test_indicators
            for household in households[1:]:
                indicators = household.test_indicators()
                for i in range(len(indicators)):
                    for j in range(len(indicators[i])):
                        total[i][j] += indicators[i][j]

          # This line prints the total to the console for debugging purposes

        return total


    def dimensional_score(self):
        households = self.household.all()
        ans = []  # Initialize an array to store dimensional scores
        for i in range(5):
            output=0
            for household in households:
                D_ds = household.D_DS()[i]
                if D_ds:
                 output += D_ds
            ans.append(output)
        return ans

    def indicator_contributions_to_dimension(self):
        dimensional_scores = self.dimensional_score()
        indicator_scores = self.indicators_score()  # Assuming this returns a list of lists of scores

        contributions = []  # Initialize an empty list to store contributions

        for i in range(len(indicator_scores)):
            if dimensional_scores[i] != 0:
                indicator_contribution = [] 
                for j in range(len(indicator_scores[i])):
                    contribution = round((indicator_scores[i][j] / dimensional_scores[i]) * 100,2)
                    indicator_contribution.append(contribution)
                contributions.append(indicator_contribution)

        return contributions


    def dimension_contribution_to_tdi(self):
        households = self.household.all()
        dimension_contribution_to_tdi=[]
        total_tribal_development_score =0
        total_D_DS=[]
        for i in range(0,5):
            count=0
            for household in households:
                D_DS=household.D_DS()[i]
                count+=D_DS
            total_D_DS.append(count)
        for household in households:
                tribal_development_score=household.tribal_development_score()
                total_tribal_development_score+=tribal_development_score
        for i in total_D_DS:
            if total_tribal_development_score !=0:
             dimension_contribution_to_tdi.append(round((i/total_tribal_development_score)*100,2))
        return dimension_contribution_to_tdi

        
    def get_censored_tribal_indicator_score(self):
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
            tribal_household_index=i.household_tribal_index()
            if tribal_household_index>=0.03:
                CD_members += i.CD_score * i.size if i.CD_score is not None else 0
                IM_members += i.IM_score * i.size if i.IM_score is not None else 0
                MC_members += i.MC_score * i.size if i.MC_score is not None else 0
                CM_members += i.CM_score * i.size if i.CM_score is not None else 0
                FS_members += i.FS_score * i.size if i.FS_score is not None else 0
                LE_members += i.LE_score * i.size if i.LE_score is not None else 0
                DRO_members += i.DRO_score * i.size if i.DRO_score is not None else 0
                IC_members   += i.IC_score * i.size if i.IC_score is not None else 0
                OW_members    += i.OW_score * i.size if i.OW_score is not None else 0
                SANI_members   += i.SANI_score * i.size if i.SANI_score is not None else 0
                FUEL_members   += i.FUEL_score * i.size if i.FUEL_score is not None else 0
                DRWA_members   += i.DRWA_score * i.size if i.DRWA_score is not None else 0
                ELECTR_members += i.ELECTR_score * i.size if i.ELECTR_score is not None else 0
                ASS_members   += i.ASS_score * i.size if i.ASS_score is not None else 0
                LAN_members   += i.LAN_score * i.size if i.LAN_score is not None else 0
                ARTS_members   += i.ARTS_score * i.size if i.ARTS_score is not None else 0
                EV_members   += i.EV_score * i.size if i.EV_score is not None else 0
                MEET_members += i.MEET_score * i.size if i.MEET_score is not None else 0
            else:
                CD_members += 0
                IM_members += 0
                MC_members += 0
                CM_members += 0
                FS_members += 0
                LE_members += 0
                DRO_members += 0
                IC_members   +=0
                OW_members   +=0
                SANI_members +=0
                FUEL_members +=0
                DRWA_members +=0
                ELECTR_members+=0
                ASS_members  +=0
                LAN_members  +=0
                ARTS_members +=0
                EV_members   +=0
                MEET_members +=0
        sum=[CD_members,IM_members,MC_members,CM_members,FS_members,LE_members,DRO_members,IC_members,OW_members ,SANI_members  ,FUEL_members  ,DRWA_members  ,ELECTR_members,ASS_members  , LAN_members  ,ARTS_members ,EV_members,MEET_members]
        
        ans = []
        total_members = self.get_total_tribals()
        for i in sum:
            indicator_score = (i/total_members)
            ans.append(round(indicator_score,2))
        print(ans)
        return ans

        


class Household(models.Model):
    tribeID = models.ForeignKey(Tribe, on_delete=models.CASCADE, related_name="household", null=True, blank=True)
    tribe_name = models.CharField(max_length=20, null=True, blank=True)
    size = models.IntegerField(null= True, blank=True)
    # decimal_field = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank=True)
    # HEALTH
    CD_score = models.IntegerField(null = True, blank=True)
    IM_score = models.IntegerField(null = True, blank=True)
    MC_score = models.IntegerField(null=True, blank=True)

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
                else:
                    continue
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
                else:
                    continue
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

    def test_indicators(self):

        scores_H = [self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score]
        scores_E = [self.LE_score, self.DRO_score]
        scores_S = [self.IC_score, self.OW_score, self.SANI_score, self.FUEL_score, self.DRWA_score, self.ELECTR_score, self.ASS_score]
        scores_C =[self.LAN_score, self.ARTS_score]
        scores_G = [self.EV_score, self.MEET_score]
        weightage=self.calculate_weightage()
        scores = [scores_H, scores_E, scores_S, scores_C, scores_G]
        ans=[]

        for i in scores:
            index = scores.index(i)
            dimension_indicators_array = []
            for j in i:

                if j is None:
                    continue

                else:

                    output=j*weightage[index]
                    dimension_indicators_array.append(output)
            ans.append(dimension_indicators_array)
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

    def is_multidimensionally_developed(self):
       
        res = self.tribal_development_score()
        if res > 0.33:
            ans = 1
        else:
            ans =0
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
        is_multidimensionally_developed=self.is_multidimensionally_developed()
        
        prod = (is_multidimensionally_developed)*(self.size)
        ans = prod/total_tribals
        return round(ans,2)

    


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
            members_in_developed_households=0
            if self.is_multidimensionally_developed():
              members_in_developed_households = self.size  # Call the method as a function
            score = self.tribal_development_score()
            
            if total_members_multi_dimensionally_developed_households > 0:
                ans = (score * members_in_developed_households ) / total_members_multi_dimensionally_developed_households
            else:
                ans = 0.0  # Handle the case where total_members_across_onedimensionally_developed_households is zero\
            return round(ans,2)

    def household_tribal_index(self):
        household_tribal_intensity=self.household_tribal_intensity()
        print('incedence and intensity')
        print(household_tribal_intensity)

        household_tribal_incidence=self.household_tribal_incidence()
        print(household_tribal_incidence)
        return round((household_tribal_intensity*household_tribal_incidence)*100,2)


      

    
    def developed_indicators_members(self):
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
                    cnt += score*self.size
            ans.append(cnt)
        return ans

    

      
