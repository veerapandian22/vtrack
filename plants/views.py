import csv, io
from django.shortcuts import render
from plants.models import CastingPlan
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

def upload_excel(request):
    if request.method == 'POST':
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            CastingPlan.objects.create(CP_ID=row['CP_ID'],
                                       CP_PlanningNumber=row['CP_PlanningNumber'],
                                       CP_PlanningDate=row['CP_PlanningDate'],
                                       CP_CastingPlanNo=row['CP_CastingPlanNo'],
                                       CP_CustomerName=row['CP_CustomerName'],
                                       CP_GradeGroup=row['CP_GradeGroup'],
                                       CP_NoOfHeat=row['CP_NoOfHeat'],
                                       CP_BilletRemarks=row['CP_BilletRemarks'],
                                       CP_RequiredQty=row['CP_RequiredQty'],
                                       CP_Status=row['CP_Status'],
                                       CP_CastingPlanLineNo=row['CP_CastingPlanLineNo'],
                                       CP_DemandUID=row['CP_DemandUID'],
                                       CP_GRADE=row['CP_GRADE'],
                                       CP_ItemNumber=row['CP_ItemNumber'],
                                       CP_ItemName=row['CP_ItemName'],
                                       CP_DemandSize=row['CP_DemandSize'],
                                       CP_DemandSizeCode=row['CP_DemandSizeCode'],
                                       CP_DemandLength=row['CP_DemandLength'],
                                       CP_DemandLengthCode=row['CP_DemandLengthCode'],
                                       CP_WTMTR=row['CP_WTMTR'],
                                       CP_WTPCS=row['CP_WTPCS'],
                                       CP_DemandPCS=row['CP_DemandPCS'],
                                       CP_CalculativeQty=row['CP_CalculativeQty'],
                                       CP_DemandQty=row['CP_DemandQty'],
                                       CP_Shape=row['CP_Shape'],
                                       CP_CREATED_DATE=row['CP_CREATED_DATE'],
                                       CP_AXDT=row['CP_AXDT'],
                                       CP_DeleteStatus=row['CP_DeleteStatus'],
                                       CP_Deleteby=row['CP_Deleteby'],
                                       CP_Deletedate=row['CP_Deletedate'])
        return render(request, 'plants/upload_excel.html')
    else:
        return render(request, 'plants/upload_excel.html')


def casting_plan(request):
    CastingPlans = CastingPlan.objects.all()
    return render(request, 'plants/casting_plan.html', {"CastingPlans": CastingPlans})


