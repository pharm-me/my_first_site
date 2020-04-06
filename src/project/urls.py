from pathlib import Path
from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
here = Path(__file__).parent.resolve()

def view_index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

def view_css(request: HttpRequest) -> HttpResponse:
    return render(request, "style.css", content_type="text/css")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index, name="index"),
    path('css/', view_css, name="css"),
]