from django.db import models

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
    
    

class Household(models.Model):

    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE, related_name="household", null=True, blank=True)
    size = models.IntegerField(null= True, blank=True)

    CD_score = models.BooleanField(null=True, blank=True)
    IM_score = models.BooleanField(null=True, blank=True)
    MC_score = models.BooleanField(null=True, blank=True)
    CM_score = models.BooleanField(null=True, blank=True)
    FS_score = models.BooleanField(null=True, blank=True)

    no_of_H_indicators = models.IntegerField(null=True, blank=True) 
    def H_developed_indicators(self):
        # Calculate the sum of Boolean fields
        return sum([self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score])
    
    def H_calculate_weightage(self):
        if self.no_of_indicators:
            return 0.2 * (1 / self.no_of_indicators)
        else:
            return 0
    


    def H_is_multidimensionally_developed(self):
        res = sum([self.health.is_developed, self.education.is_developed(), self.sol.is_developed(), self.culture.is_developed(), self.governance.is_developed()])
        if res > 1:
            return 1
        else:
            return 0
        
    def H_DS(self):
        weightage = self.calculate_weightage()
        return weightage * self.developed_indicators()
    
    def H_is_developed(self):
        if self.H_DS > 0.033 :
            return 1
        else:
            return 0 



class Health(models.Model):
    CD_score = models.BooleanField(null=True, blank=True)
    IM_score = models.BooleanField(null=True, blank=True)
    MC_score = models.BooleanField(null=True, blank=True)
    CM_score = models.BooleanField(null=True, blank=True)
    FS_score = models.BooleanField(null=True, blank=True)
    # HH_id = models.IntegerField(null=True, blank=True)
    no_of_H_indicators = models.IntegerField(null=True, blank=True) 
    HH = models.ForeignKey(Household, on_delete=models.CASCADE, related_name="health", null=True, blank=True)


    def developed_indicators(self):
        # Calculate the sum of Boolean fields
        return sum([self.CD_score, self.IM_score, self.MC_score, self.CM_score, self.FS_score])
    
    def calculate_weightage(self):
        if self.no_of_indicators:
            return 0.2 * (1 / self.no_of_indicators)
        else:
            return 0

    # @property
    def H_DS(self):
        weightage = self.calculate_weightage()
        return weightage * self.developed_indicators()
        
    

    def is_developed(self):
        if self.H_DS > 0.033 :
            return 1
        else:
            return 0 
        
    def members_of_developed_households(self):
        return (int(self.is_developed()))*(int(self.HH.size))


class Education(models.Model):
    no_of_indicators = models.IntegerField(null=True, blank=True)
    HH = models.ForeignKey(Household, on_delete=models.CASCADE, related_name="education", null=True, blank=True)
    LE_score = models.BooleanField(null=True, blank=True)
    DRO_score = models.BooleanField(null=True, blank=True)

    def calculate_weightage(self):
        if self.no_of_indicators:
            return 0.2 * (1 / self.no_of_indicators)
        else:
            return 0

    def developed_indicators(self):
        # Calculate the sum of Boolean fields
        return sum([self.LE_score, self.DRO_score])

    # @property
    def E_DS(self):
        weightage = self.calculate_weightage()
        return weightage * self.developed_indicators()
    
    def is_developed(self):
        if self.E_DS > 0.033 :
            return 1
        else:
            return 0
        
    def members_of_developed_households(self):
        return (int(self.is_developed()))*(int(self.HH.size))



class SOL(models.Model):
    no_of_indicators = models.IntegerField(null=True, blank=True)
    HH = models.ForeignKey(Household, on_delete=models.CASCADE, related_name="sol", null=True, blank=True)
    IC_score = models.BooleanField(null=True, blank=True)
    OW_score = models.BooleanField(null=True, blank=True)
    SANI_score = models.BooleanField(null=True, blank=True)
    FUEL_score = models.BooleanField(null=True, blank=True)
    DRWA_score = models.BooleanField(null=True, blank=True)
    ELECTR_score = models.BooleanField(null=True, blank=True)
    ASS_score = models.BooleanField(null=True, blank=True)

    def calculate_weightage(self):
        if self.no_of_indicators:
            return 0.2 * (1 / self.no_of_indicators)
        else:
            return 0

    def developed_indicators(self):
        # Calculate the sum of Boolean fields
        return sum([self.IC_score, self.OW_score, self.SANI_score, self.FUEL_score, self.DRWA_score, self.ELECTR_score])

    # @property
    def S_DS(self):
        weightage = self.calculate_weightage()
        return weightage * self.developed_indicators()
    
    def is_developed(self):
        if self.S_DS > 0.033 :
            return 1
        else:
            return 0
        
    def members_of_developed_households(self):
        return (int(self.is_developed()))*(int(self.HH.size))



class Culture(models.Model):
    no_of_indicators = models.IntegerField(null=True, blank=True)
    HH = models.ForeignKey(Household, on_delete=models.CASCADE, related_name="culture", null=True, blank=True)
    LAN_score = models.BooleanField(null=True, blank=True)
    ARTS_score = models.BooleanField(null=True, blank=True)

    def calculate_weightage(self):
        if self.no_of_indicators:
            return 0.2 * (1 / self.no_of_indicators)
        else:
            return 0

    def developed_indicators(self):
        # Calculate the sum of Boolean fields
        return sum([self.LAN_score, self.ARTS_score])

    # @property
    def C_DS(self):
        weightage = self.calculate_weightage()
        return weightage * self.developed_indicators()
    
    def is_developed(self):
        if self.C_DS > 0.033 :
            return 1
        else:
            return 0
        
    def members_of_developed_households(self):
        return (int(self.is_developed()))*(int(self.HH.size))


class Governance(models.Model):
    no_of_indicators = models.IntegerField(null=True, blank=True)
    HH = models.ForeignKey(Household, on_delete=models.CASCADE, related_name="governance", null=True, blank=True)
    EV_score = models.BooleanField(null=True, blank=True)
    MEET_score = models.BooleanField(null=True, blank=True)

    def calculate_weightage(self):
        if self.no_of_indicators:
            return 0.2 * (1 / self.no_of_indicators)
        else:
            return 0

    def developed_indicators(self):
        # Calculate the sum of Boolean fields
        return sum([self.EV_score, self.MEET_score])

    # @property
    def G_DS(self):
        weightage = self.calculate_weightage()
        return weightage * self.developed_indicators()
    
    def is_developed(self):
        if self.G_DS > 0.033 :
            return 1
        else:
            return 0

    def members_of_developed_households(self):
        return (int(self.is_developed()))*(int(self.HH.size))