from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from hospital.models import *
from django.contrib import messages
from patient.forms import *
from django.db.models import Q
from lab.models import LabTest


# Create your views here.

@login_required
def index(request):
    patient = None
    if request.method == 'POST':
        gin = request.POST['gin']
        dob = request.POST['dob']
        try:
            print(dob)
            patient = Patient.objects.get(gin=gin, dob=dob)
        except 	Patient.DoesNotExist:
            messages.error(request, 'Please Check the Inputs !')
        except Exception:
            messages.error(request, 'Invalid Patient GIN Number !')  
    else:
        pass
    return render(request, 'doctor/index.html', {'patient': patient})


@login_required
def add_record(request, pid):
    patient = Patient.objects.get(pk=pid)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.doctor = Doctor.objects.get(user=request.user)
            obj.patient = patient
            obj.save()
            if request.POST.get('test', None):
                return redirect('doctor_add_test', rid=obj.id)
            else:
                return redirect('doctor_view_record', pid=pid)
    else:
        form = MedicalRecordForm()
    return render(request, 'doctor/add_record.html',{'form': form})

@login_required
def add_test(request, rid):
    record = MedicalRecord.objects.get(pk=rid)
    if request.method == 'POST':
        form = LabTestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.record = record
            obj.save()
            return redirect('doctor_view_record', pid=record.patient_id)
    else:
        form = LabTestForm()
    return render(request, 'doctor/add_test.html',{'form': form})


@login_required
def view_record(request, pid):
    records = MedicalRecord.objects.filter(patient_id=pid)
    return render(request, 'doctor/manage_record.html',{'records': records})

@login_required
def record_details(request, id):
    record = MedicalRecord.objects.get(pk=id)
    return render(request, 'doctor/record_details.html',{'record': record})

@login_required
def test_details(request, id, pid):
    try:
        test = LabTest.objects.get(record_id=id)
    except:
        test = None
        return HttpResponse(f"<script>window.alert('Not Found...!');window.location.href='/doctor/record/view/{pid}'</script>")
    return render(request, 'doctor/test_details.html',{'record': test})

@login_required
def delete_record(request, id):
    record = MedicalRecord.objects.get(pk=id)
    record.delete()
    return redirect('doctor_index')


@login_required
def edit_record(request, id):
    record = MedicalRecord.objects.get(pk=id)
    if request.method == 'POST':
        form = MedicalRecordForm(data=request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('doctor_record_details', id=id)
    else:
        form = MedicalRecordForm(instance=record)
    return render(request, 'doctor/edit_record.html',{'form': form})


@login_required
def send_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('doctor_send_feedback')
    else:
        form = FeedbackForm()
    return render(request, 'doctor/feeback.html', {'form': form})


@login_required
def message_view(request):
    msg = Chat.objects.filter(receiver=request.user)
    return render(request, 'doctor/chat_view.html', {'msg': msg})

@login_required
def replay_message(request, id):
    chat = Chat.objects.get(pk=id)
    if request.method == 'POST':
        replay = request.POST['replay']
        chat.replay = replay
        chat.save()
        return redirect('doctor_view_message')
    else:
        pass
    return render(request, 'doctor/chat_replay.html')