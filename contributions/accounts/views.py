from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'contributions/home.html')


def register(request):
    form = UserCreationForm()
    return render(request, 'contributions/register.html', {'form': form})
