import time

from django.shortcuts import render, redirect
from django.contrib import messages

from allauth.account.decorators import login_required

from django_rq import job

from .models import Secret

# https://github.com/rq/django-rq#job-decorator
@job
@login_required
def generate_bg():
    time.sleep(2) # Simulate expensive operation.
    Secret.objects.create()

@login_required
def index(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'keygen/index.html', context)

@login_required
def generate(request):
    if request.GET.get('bg'):
        generate_bg.delay()
        messages.success(request, 'Generating new key in background. Refresh page after two seconds to see generated key.')
    else:
        Secret.objects.create()
        messages.success(request, 'Generated new key.')
    return redirect('home')

@login_required
def delete(request):
    Secret.objects.all().delete()
    messages.success(request, 'Deleted all keys.')
    return redirect('home')
