from django.http import HttpResponse


def personne (request, nom):
    return HttpResponse(f"Hello World {nom}")