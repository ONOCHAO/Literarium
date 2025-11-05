from django.shortcuts import render
from .models import Poem

def poem_list(request):
    poems = Poem.objects.all()
    return render(request, 'poems/poem_list.html', {'poems': poems})
from django.shortcuts import render

# Create your views here.
