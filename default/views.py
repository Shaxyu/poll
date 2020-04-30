from django.shortcuts import render
from .models import poll

# Create your views here.
def poll_list(req):
    polls = poll.objects.all()
    return render(req, 'poll_list.html', {'poll_list':polls})

