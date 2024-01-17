from django.shortcuts import render
from .models import Topic


# Create your views here.
def index(request):
    return render(request, 'mainpage/index.html')


def topics(request):
    topics = Topic.objects
    context = {'topics': topics}
    return render(request, 'mainpage/topics.html', context)


def tamilisai(request):
    return render(request, 'mainpage/tamilisai.html')


def tamilisai_events(request):
    return render(request, 'mainpage/tamilisai_events.html')


def textbook(request):
    return render(request, 'mainpage/textbook.html')


def parai(request):
    return render(request, 'mainpage/parai.html')


def pg(request):
    return render(request, 'mainpage/pg.html')


def silambam(request):
    return render(request, 'mainpage/silambam.html')


def sg(request):
    return render(request, 'mainpage/sg.html')