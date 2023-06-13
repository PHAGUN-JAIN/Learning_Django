from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.
@csrf_exempt
def books(request):
    if request.method == "GET":
        books = Book.objects.all().values()
        return JsonResponse({"books": list(books)})
