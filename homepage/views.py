import subprocess
from django.shortcuts import render
from homepage.forms import CowForm
from homepage.models import Cow

def index(request):
    if request.method == "POST": 
        form = CowForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data.get("text")
            Cow.objects.create(text=text)
            cowjoke = subprocess.run(f'cowsay', input=text.encode("utf-8"), capture_output=True, shell=True)
            form = CowForm()
            return render(request, 'index.html', {'form':form, 'subprocess': cowjoke.stdout.decode()})
    form = CowForm()
    return render(request, 'index.html', {'form':form})

# def placeholder
def history(request):
    cows = Cow.objects.all().order_by('-id')[:10]
    return render(request, 'history.html', {"cowsays": cows})
    
