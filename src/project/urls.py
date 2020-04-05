from pathlib import Path
from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
here = Path(__file__).parent.resolve()

def view_index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

def background(r):
    index = here.parent.parent / "webb.png"
    with index.open("rb") as f:
        return HttpResponse(f.read(), content_type="image/png")
def viewstyle(r):
    index = here.parent.parent / "style.css"
    with index.open() as f:
        return HttpResponse(f.read(), content_type="text/css")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index, name="index"),
    path('css/', viewstyle),
    path('img/', background),
]