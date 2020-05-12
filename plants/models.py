from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Plant(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "Plant"

    def __str__(self):
        return self.name

class GroupWisePlant(models.Model):
    objects = None
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "GroupWisePlant"

class CastingPlan(models.Model):
    objects = None
    CP_ID = models.CharField(max_length=100, null=True)
    CP_PlanningNumber = models.CharField(max_length=100, null=True)
    CP_PlanningDate = models.CharField(max_length=100, null=True)
    CP_CastingPlanNo= models.CharField(max_length=100, null=True)
    CP_CustomerName = models.CharField(max_length=100, null=True)
    CP_GradeGroup = models.CharField(max_length=100, null=True)
    CP_NoOfHeat = models.CharField(max_length=100, null=True)
    CP_BilletRemarks = models.CharField(max_length=100, null=True)
    CP_RequiredQty = models.CharField(max_length=100, null=True)
    CP_Status = models.CharField(max_length=100, null=True)
    CP_CastingPlanLineNo = models.CharField(max_length=100, null=True)
    CP_DemandUID = models.CharField(max_length=100, null=True)
    CP_GRADE = models.CharField(max_length=100, null=True)
    CP_ItemNumber = models.CharField(max_length=100, null=True)
    CP_ItemName = models.CharField(max_length=100, null=True)
    CP_DemandSize = models.CharField(max_length=100, null=True)
    CP_DemandSizeCode = models.CharField(max_length=100, null=True)
    CP_DemandLength = models.CharField(max_length=100, null=True)
    CP_DemandLengthCode = models.CharField(max_length=100, null=True)
    CP_WTMTR = models.CharField(max_length=100, null=True)
    CP_WTPCS = models.CharField(max_length=100, null=True)
    CP_DemandPCS = models.CharField(max_length=100, null=True)
    CP_CalculativeQty = models.CharField(max_length=100, null=True)
    CP_DemandQty = models.CharField(max_length=100, null=True)
    CP_Shape = models.CharField(max_length=100, null=True)
    CP_CREATED_DATE = models.CharField(max_length=100, null=True)
    CP_AXDT = models.CharField(max_length=100, null=True)
    CP_DeleteStatus = models.CharField(max_length=100, null=True)
    CP_Deleteby = models.CharField(max_length=100, null=True)
    CP_Deletedate = models.CharField(max_length=100, null=True)
    reference1 = models.CharField(max_length=100, null=True)
    reference2 = models.CharField(max_length=100, null=True)
    reference3 = models.CharField(max_length=100, null=True)
    reference4 = models.CharField(max_length=100, null=True)
    reference5 = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "CastingPlan"

    def __str__(self):
        return self.CP_ID

class SBDHeatDetail(models.Model):
    Seqno = models.IntegerField(null=True, unique=True)
    PlanningId = models.ForeignKey('CastingPlan', null=True, on_delete=models.CASCADE)
    HEATNO = models.CharField(max_length=100, null=True)
    C= models.FloatField(null=True)
    Si = models.FloatField(null=True)
    Mn = models.FloatField(null=True)
    P = models.FloatField(null=True)
    S = models.FloatField(null=True)
    Cr = models.FloatField(null=True)
    Mo = models.FloatField(null=True)
    Ni = models.FloatField(null=True)
    Al = models.FloatField(null=True)
    Co = models.FloatField(null=True)
    Cu = models.FloatField(null=True)
    Nb = models.FloatField(null=True)
    Ti = models.FloatField(null=True)
    V = models.FloatField(null=True)
    W = models.FloatField(null=True)
    Pb = models.FloatField(null=True)
    Sn = models.FloatField(null=True)
    As = models.FloatField(null=True)
    Ca = models.FloatField(null=True)
    Sb = models.FloatField(null=True)
    Ta = models.FloatField(null=True)
    B = models.FloatField(null=True)
    N2 = models.FloatField(null=True)
    O2 = models.FloatField(null=True)
    Fe = models.FloatField(null=True)
    H2 = models.FloatField(null=True)
    CrEq = models.FloatField(null=True)
    NiEq = models.FloatField(null=True)
    NbTa = models.FloatField(null=True)
    FF = models.FloatField(null=True)
    DF = models.FloatField(null=True)
    Temp = models.FloatField(null=True)
    INSERT_DATE = models.DateTimeField(default=timezone.now)
    UPDATE_DATE = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "SBDHeatDetail"

    def __str__(self):
        return self.Seqno