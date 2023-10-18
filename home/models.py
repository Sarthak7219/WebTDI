from django.db import models
from django.db.models import Sum


# Create your models here.
class Tribe_Image(models.Model):
    image=models.ImageField(upload_to='images')
    location=models.CharField(max_length=50)
    date=models.DateField()


class Tribe(models.Model):
    name = models.CharField(max_length=50)
    image = models.ForeignKey(Tribe_Image, on_delete=models.CASCADE, related_name='tribe_image', null=True, blank=True)
    incidence = models.FloatField(null=True, blank=True)
    intensity = models.FloatField(null=True, blank=True)
    tdi = models.FloatField(null=True, blank=True)

    def get_total_tribals(self):
        total_tribals = self.household.aggregate(total_tribals=Sum('size'))['total_tribals']
        return total_tribals or 0

    def total_members_across_onedimensionally_developed_households(self):
        ans = [0] * 5
        households = self.household.all()

        for household in households:
            is_developed = household.is_developed()
            for i in range(5):
                ans[i] += is_developed[i] * household.size

        return ans

    def total_households_across_onedindicator_developed_households(self):
        ans = [0] * 5
        households = self.household.all()

        for household in households:
            is_developed = household.is_developed()
            for i in range(5):
                ans[i] += is_developed[i]

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
        tribe_households = self.household.all()
        total_tribals = self.get_total_tribals()
        
        ans = [0] * 5  # Initialize the ans list with zeros
        
        for household in tribe_households:
            members_of_developed_households = household.members_of_developed_households()
            for i in range(5):
                ans[i] += members_of_developed_households[i]
        
        dimensional_contribution_to_index = [i / total_tribals for i in ans if total_tribals != 0]
        
        return dimensional_contribution_to_index

        

    def tribal_dimensional_incidence(self):
        ans = [0] * 5  # Initialize the ans list with zeros
        households = self.household.all()

        for i in range(5):
            for household in households:
                ans[i] += household.household_dimensional_incidence()[i]

        ans = [round(val, 3) for val in ans]

        return ans
    
    def tribal_incidence(self):
        ans = 0
        tribe_households = self.household.all()

        for household in tribe_households:
            household_tribal_incidence = household.household_tribal_incidence()
            ans += household_tribal_incidence

        return int(round(ans * 100, 2))

    def tribal_dimensional_intensity(self):
        ans = [0] * 5  # Initialize the ans list with zeros
        households = self.household.all()

        for i in range(5):
            for household in households:
                ans[i] += household.household_dimensional_intensity()[i]

        ans = [round(val, 3) for val in ans]

        return ans
    

    def tribal_intensity(self):
        households = self.household.all()
        cnt = 0  # Initialize cnt
        for household in households:
            household_tribal_intensity = household.household_tribal_intensity()
            cnt += household_tribal_intensity
        return int(round(cnt * 100, 2))

    def tribal_dimensional_index(self):
        incidence_values = self.tribal_dimensional_incidence()
        intensity_values = self.tribal_dimensional_intensity()

        ans = [round(incidence_values[i] * intensity_values[i], 3) for i in range(5)]

        return ans

    def tribal_index(self):
        tribal_incidence = self.tribal_incidence()/100
        tribal_intensity = self.tribal_intensity()/100
        tribal_index = tribal_incidence * tribal_intensity
        return round(tribal_index,2)

    def total_members_multi_dimensionally_developed_households(self):
        # Get all households of the tribe
        households = self.household.all()

        total_members = 0

        for household in households:
            if household.is_multidimensionally_developed():
                total_members += household.size

        return total_members

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
        ans = [0] * 5  # Initialize an array to store dimensional scores

        for i in range(5):
            for household in households:
                D_ds = household.D_DS()[i]
                if D_ds:
                    ans[i] += D_ds

        return ans

    def indicator_contributions_to_dimension(self):
        dimensional_scores = self.dimensional_score()
        indicator_scores = self.indicators_score()  # Assuming this returns a list of lists of scores

        contributions = []  # Initialize an empty list to store contributions

        for i in range(len(indicator_scores)):
            if dimensional_scores[i] != 0:
                indicator_contribution = [
                    round((score / dimensional_scores[i]) * 100, 2) for score in indicator_scores[i]
                ]
                contributions.append(indicator_contribution)

        return contributions


    def dimension_contribution_to_tdi(self):
        households = self.household.all()
        dimension_contribution_to_tdi = []
        total_D_DS = [0] * 5  # Initialize total_D_DS list with zeros
        total_tribal_development_score = 0

        for i in range(5):
            for household in households:
                D_DS = household.D_DS()[i]
                total_D_DS[i] += D_DS

        for household in households:
            tribal_development_score = household.tribal_development_score()
            total_tribal_development_score += tribal_development_score

        if total_tribal_development_score != 0:
            dimension_contribution_to_tdi = [round((i / total_tribal_development_score) * 100, 2) for i in total_D_DS]

        return dimension_contribution_to_tdi

        
    def get_censored_tribal_indicator_score(self):
        households = self.household.all()
        indicators = [
            'CD_score', 'IM_score', 'MC_score', 'CM_score', 'FS_score', 'LE_score',
            'DRO_score', 'IC_score', 'OW_score', 'SANI_score', 'FUEL_score', 'DRWA_score',
            'ELECTR_score', 'ASS_score', 'LAN_score', 'ARTS_score', 'EV_score', 'MEET_score'
        ]

        indicator_members = [0] * len(indicators)

        for household in households:
            tribal_household_index = household.household_tribal_index()
            for idx, indicator in enumerate(indicators):
                indicator_value = getattr(household, indicator, None)
                if tribal_household_index >= 0.03 and indicator_value is not None:
                    indicator_members[idx] += indicator_value * household.size

        total_members = self.get_total_tribals()
        indicator_scores = [round(member / total_members, 2) for member in indicator_members]

        return indicator_scores

        


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
        scores_C = [self.LAN_score, self.ARTS_score]
        scores_G = [self.EV_score, self.MEET_score]

        scores = [scores_H, scores_E, scores_S, scores_C, scores_G]

        ans = [sum(1 for score in sublist if score is not None) for sublist in scores]
        
        return ans

    
    def developed_indicators(self):
        scores_H = [self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score]
        scores_E = [self.LE_score, self.DRO_score]
        scores_S = [self.IC_score, self.OW_score, self.SANI_score, self.FUEL_score, self.DRWA_score, self.ELECTR_score, self.ASS_score]
        scores_C = [self.LAN_score, self.ARTS_score]
        scores_G = [self.EV_score, self.MEET_score]

        scores = [scores_H, scores_E, scores_S, scores_C, scores_G]

        ans = [sum(score for score in sublist if score is not None) for sublist in scores]

        return ans


    def calculate_weightage(self):
        no_of_indicators = self.no_of_indicators()
        
        ans = [round(0.2 * (1 / no) if no else 0, 2) for no in no_of_indicators]

        return ans


    def test_indicators(self):
        scores_H = [self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score]
        scores_E = [self.LE_score, self.DRO_score]
        scores_S = [self.IC_score, self.OW_score, self.SANI_score, self.FUEL_score, self.DRWA_score, self.ELECTR_score, self.ASS_score]
        scores_C = [self.LAN_score, self.ARTS_score]
        scores_G = [self.EV_score, self.MEET_score]

        weightage = self.calculate_weightage()
        scores = [scores_H, scores_E, scores_S, scores_C, scores_G]
        ans = []

        for i in scores:
            dimension_indicators_array = []
            for j, w in zip(i, weightage):
                if j is not None:
                    dimension_indicators_array.append(round(j * w, 2))
            ans.append(dimension_indicators_array)

        return ans


               
                
    
        
    
    
    
    def D_DS(self):
        weightage = self.calculate_weightage()
        developed_indicators = self.developed_indicators()
        ans = [round(w * d, 2) for w, d in zip(weightage, developed_indicators)]
        return ans

    def is_developed(self):
        D_DS = self.D_DS()
        ans = [1 if d_ds >= 0.066 else 0 for d_ds in D_DS]
        return ans

    
    def tribal_development_score(self):
        return round(sum(self.D_DS()), 2)

    def is_multidimensionally_developed(self):
        return 1 if self.tribal_development_score() > 0.33 else 0


    def members_of_developed_households(self):
        is_dev = self.is_developed()
        return [round(is_dev[i] * self.size, 2) for i in range(5)]


    def household_dimensional_incidence(self):
        total_tribals = self.tribeID.get_total_tribals()
        
        incidence = []
        
        members_of_developed_households = self.members_of_developed_households()  # Calculate once

        for i in range(5):
            if total_tribals > 0:
                incidence_value = members_of_developed_households[i] / total_tribals
            else:
                incidence_value = 0.0  # Handle the case where there are no households to avoid division by zero
            incidence.append(round(incidence_value, 2))
        return incidence

    
    def household_tribal_incidence(self):
        total_tribals = self.tribeID.get_total_tribals()
        is_multidimensionally_developed = self.is_multidimensionally_developed()
        
        if total_tribals > 0:
            ans = round((is_multidimensionally_developed * self.size) / total_tribals, 2)
        else:
            ans = 0.0  # Handle the case where there are no tribals to avoid division by zero
        return ans


    


    def household_dimensional_intensity(self):
        intensity = []

        # Calculate the shared values once before the loop
        total_members_across_onedimensionally_developed_households = self.tribeID.total_members_across_onedimensionally_developed_households()
        members_in_developed_households = self.members_of_developed_households()
        D_DS_values = self.D_DS()

        for i in range(0, 5):
            total_members = total_members_across_onedimensionally_developed_households[i]
            members_in_households = members_in_developed_households[i]
            score = D_DS_values[i]

            if total_members > 0:
                ans = round((score * members_in_households * 5) / total_members, 3)
            else:
                ans = 0.0  # Handle the case where total_members is zero

            intensity.append(ans)

        return intensity

    
    def household_tribal_intensity(self):
        # Calculate the shared values once before the loop
        total_members_multi_dimensionally_developed_households = self.tribeID.total_members_multi_dimensionally_developed_households()
        members_in_developed_households = self.size if self.is_multidimensionally_developed() else 0
        score = self.tribal_development_score()

        if total_members_multi_dimensionally_developed_households > 0:
            ans = round((score * members_in_developed_households) / total_members_multi_dimensionally_developed_households, 2)
        else:
            ans = 0.0  # Handle the case where total_members_multi_dimensionally_developed_households is zero

        return ans


    def household_tribal_index(self):
        household_tribal_intensity=self.household_tribal_intensity()

        household_tribal_incidence=self.household_tribal_incidence()
        return round((household_tribal_intensity*household_tribal_incidence)*100,2)


      

    
    def developed_indicators_members(self):
        scores_H = [self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score]
        scores_E = [self.LE_score, self.DRO_score]
        scores_S = [self.IC_score, self.OW_score, self.SANI_score, self.FUEL_score, self.DRWA_score, self.ELECTR_score, self.ASS_score]
        scores_C = [self.LAN_score, self.ARTS_score]
        scores_G = [self.EV_score, self.MEET_score]

        scores = [scores_H, scores_E, scores_S, scores_C, scores_G]
        total_sum = 0

        for indicator_group in scores:
            total_sum += sum([score for score in indicator_group if score is not None])

        return round(total_sum * self.size, 2)


    

      
