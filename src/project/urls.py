from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import path, include
from django.shortcuts import render

from apps.index.views import view_index

def view_css(request: HttpRequest) -> HttpResponse:
    return render(request, "style.css", content_type="text/css")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.index.urls")),
    path('css/', view_css, name="css"),
]