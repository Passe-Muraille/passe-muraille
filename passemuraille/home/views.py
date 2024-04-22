from django.shortcuts import render, redirect
from .models import Enquete, Indice_chiffres, Indice_autre,Indice_chiffres_trouves, Indice_autre_trouves
from django.http import Http404
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
	return render(request, 'home/home.html')

def introduction_enquete(request, id_enquete):
	error = False
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
				
			user = authenticate(username=username, password=password)  # We check wither the data are correct
			if user:  # If the object returned is not None
				messages.success(request, "Vous êtes connecté")
				login(request, user)  # We log the user in
				return redirect('centrale_enquete', id_enquete)
				
			else:
				messages.error(request, 'Identifiant ou mot de passe incorrect')
				return redirect('introduction_enquete', id_enquete)
	else:
		form = LoginForm()
	enquete = Enquete.objects.get(id=id_enquete)
	return render(request, 'home/introduction_enquete.html', {'enquete':enquete, 'form':form})

@login_required
def centrale_enquete(request, id_enquete):
	enquete = Enquete.objects.get(id=id_enquete)
	questions_sans_point = enquete.questions.split('?')
	questions = []
	for question in questions_sans_point:
		if question != " " and question !="":
			questions.append(question + "?")
	indices_chiffres = Indice_chiffres.objects.filter(enquete=enquete)
	indices_autre = Indice_autre.objects.filter(enquete=enquete)
	indices_chiffres_trouves = Indice_chiffres_trouves.objects.filter(equipe=request.user)
	indices_autre_trouves = Indice_autre_trouves.objects.filter(equipe=request.user)
	#on verra si on veut les trier
	"""indices = []
	for indice in indices_chiffres:
		indices.append((indice.nom, indice.id))
	for indice in indices_autre:
		indices.append((indice.nom, indice.id))"""
	event = Event.objects.first()  # Retrieve the first Event object
	if event:
		time_remaining = event.event_date - timezone.now()  # Calculate time remaining
		hours = time_remaining.seconds // 3600
		minutes = (time_remaining.seconds % 3600) // 60
		seconds = time_remaining.seconds % 60
		data = {
			'name': event.name,
			'hours': hours,
			'minutes': minutes,
			'seconds': seconds
		}
	else:
		data = {
			'name': "No Event",
			'hours': 0,
			'minutes': 0,
			'seconds': 0
		}
	return render(request, 'home/centrale_enquete.html', {'enquete':enquete, 'indices_chiffres':indices_chiffres, "indices_autre":indices_autre, "indices_chiffres_trouves":indices_chiffres_trouves, "indices_autre_trouves":indices_autre_trouves, 'data':data, 'questions':questions})

@login_required
def indice_enigme_chiffres(request, id_indice_chiffres):
	indice_chiffres = Indice_chiffres.objects.get(id=id_indice_chiffres)
	return render(request, 'home/indice_enigme_chiffres.html', {'indice_chiffres':indice_chiffres})

@login_required
def indice_enigme_autre(request, id_indice_autre):
	indice_autre = Indice_autre.objects.get(id=id_indice_autre)
	return render(request, 'home/indice_enigme_autre.html', {'indice_autre':indice_autre})

@login_required
def indice_chiffres_ouverte(request, id_indice_chiffres):
	indices_chiffres_trouves = Indice_chiffres_trouves.objects.filter(equipe=request.user)
	deja_trouve = False
	for indice in indices_chiffres_trouves:
		if indice.indice.id == id_indice_chiffres:
			deja_trouve = True
	if not deja_trouve:
		newIndice = Indice_chiffres_trouves()
		newIndice.equipe = request.user
		newIndice.indice = Indice_chiffres.objects.get(id=id_indice_chiffres)
		newIndice.date_decouverte = datetime.now()
		newIndice.save()
	return render(request, 'home/indice_chiffres_ouverte.html', {'id_indice_chiffres':id_indice_chiffres})

@login_required
def indice_autre_ouverte(request, id_indice_autre):
	indices_autre_trouves = Indice_autre_trouves.objects.filter(equipe=request.user)
	deja_trouve = False
	for indice in indices_autre_trouves:
		if indice.indice.id == id_indice_autre:
			deja_trouve = True
	if not deja_trouve:
		newIndice = Indice_autre_trouves()
		newIndice.equipe = request.user
		newIndice.indice = Indice_autre.objects.get(id=id_indice_autre)
		newIndice.date_decouverte = datetime.now()
		newIndice.save()
	return render(request, 'home/indice_autre_ouverte.html', {'id_indice_autre':id_indice_autre})

from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Event  # Import the Event model from your app

def countdown_timer(request):
    event = Event.objects.first()  # Retrieve the first Event object
    if event:
        time_remaining = event.event_date - timezone.now()  # Calculate time remaining
        hours = time_remaining.seconds // 3600
        minutes = (time_remaining.seconds % 3600) // 60
        seconds = time_remaining.seconds % 60
        data = {
            'name': event.name,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
    else:
        data = {
            'name': "No Event",
            'hours': 0,
            'minutes': 0,
            'seconds': 0
        }
    return render(request, 'home/myapp.html', {'data': data})