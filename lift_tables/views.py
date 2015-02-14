from django.shortcuts import render
from lift_tables.models import Competition, Lifter

def index(request):
    competition = Competition.objects.get()
    result_set = competition.result_set
    context = {'competition': competition, 'result_set': result_set}
    return render(request, 'lift_tables/index.html', context)
