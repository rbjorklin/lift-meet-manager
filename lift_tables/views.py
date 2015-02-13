from django.shortcuts import render
from lift_tables.models import Competition, Lifter

def index(request):
    comp = Competition.objects.get()
    context = {'competition': comp}
    return render(request, 'lift_tables/index.html', context)

# Create your views here.
