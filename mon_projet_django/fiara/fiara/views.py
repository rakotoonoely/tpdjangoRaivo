from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PersonneForm,VoitureForm
from .models import Personne, Voiture


def personnehtml(request):
    context = {
        "form" : PersonneForm()
    }
    return render(request, "personne.html",context)

def personnes(request):
    if request.method == "GET":
        context = {
            "title":"personnes",
            "form" :PersonneForm(),
            "personnes" : Personne.objects.all()
        }
        return render(request,"personnes.html",context)
    elif request.method == "POST":
        data = PersonneForm(request.POST)
        id_form = request.POST.get("id_Utilisateur")
        if data.is_valid():
            nom_form = data.cleaned_data["nom"]
            prenom_form = data.cleaned_data["prenom"]
            age_form = data.cleaned_data["age"]
            genre_form = data.cleaned_data["genre"]
            if id_form == "":
                personne = Personne.objects.create(nom=nom_form,prenom=prenom_form,age=age_form,genre=genre_form)
                personne.save()
            else:
                personne = Personne.objects.filter(id=int(id_form)).first()
                personne.nom=nom_form
                personne.prenom = prenom_form
                personne.age=age_form
                personne.genre=genre_form
                personne.save()

            return redirect("personnes")
        return HttpResponse("Ajout échoué")

def personnes_supprimer(request, idUtilisateur):
    Personne.objects.filter(id=idUtilisateur).first().delete()
    return redirect("personnes")
def personnes_modifier(request, idUtilisateur):
    personne = Personne.objects.filter(id=idUtilisateur).first()
    context = {
        "title": "personnes",
        "idUtilisateur": personne.id,
        "form": PersonneForm(initial={'nom': personne.nom, 'prenom': personne.prenom,'age':personne.age,'genre':personne.genre}),
        "personnes": Personne.objects.all()
    }
    return render(request, "personnes.html", context)
    return redirect("personnes")



def voitureHtml(request):
    if request.method == "GET":
        context = {
            "form" : VoitureForm()
    }
        return render(request, "voiture.html", context)
    elif request.method == "POST":
        data = VoitureForm(request.POST)
        if data.is_valid():
            immatriculation_form = data.cleaned_data["immatriculation"]
            marque_form = data.cleaned_data["marque"]
            proprietaire_form = data.cleaned_data["proprietaire"]
            voiture = Voiture.objects.create(immatriculation=immatriculation_form, marque=marque_form,
                                             proprietaire=proprietaire_form)
            voiture.save()
            return HttpResponse("Ajout réussi")
        return HttpResponse ("Ajout échoué")


