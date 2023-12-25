from django.shortcuts import render
from . import models

# Create your views here.

def list_patients(request):
    all_patients = models.Patient.objects.all()
    ctx = {'patients': all_patients}
    # print(ctx)

    # return render(request, 'office/list.html',content = ctx)
    return render(request, 'office/list.html',ctx)