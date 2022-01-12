from django.shortcuts import render, redirect
from .models import Patient, ClinicalData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClinicalDataForm


class PatientListView(ListView):
    model = Patient


class PatientCreateView(CreateView):
    model = Patient
    fields = ('firstName', 'lastName', 'age')
    success_url = reverse_lazy('index')


class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')


def addData(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalsApp/clinicaldata_form.html', {'form': form, 'patient': patient})


def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            HeightAndWeight = eachEntry.componentValue.split('/')
            if len(HeightAndWeight) > 1:
                FeetToMeters = float(HeightAndWeight[0]) * 0.4536
                BMI = (float(HeightAndWeight[1]))/(FeetToMeters*FeetToMeters)
                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValue = BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request, 'ClinicalsApp/generateReport.html', {'data': responseData})
