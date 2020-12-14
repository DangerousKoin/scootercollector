from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Scooter
from .forms import ServiceForm

class ScooterCreate(CreateView):
  model = Scooter
  fields = ['model', 'make', 'description', 'year']

class ScooterUpdate(UpdateView):
  model = Scooter
  fields = ['make', 'description', 'year']

class ScooterDelete(DeleteView):
  model = Scooter
  success_url = '/scooters/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def scooters_index(request):
  scooters = Scooter.objects.all()
  return render(request, 'scooters/index.html', { 'scooters': scooters })

def scooters_detail(request, scooter_id):
  scooter = Scooter.objects.get(id=scooter_id)
  # Instantiate ServiceForm to be rendered in the template
  service_form = ServiceForm()
  return render(request, 'scooters/detail.html', {
    # Pass the scooter and service_form as context
    'scooter': scooter, 'service_form': service_form,
  })

def add_service(request, scooter_id):
	# create the ModelForm using the data in request.POST
  form = ServiceForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the scooter_id assigned
    new_service = form.save(commit=False)
    new_service.scooter_id = scooter_id
    new_service.save()
  return redirect('detail', scooter_id=scooter_id)