from django.shortcuts import render
from allauth.account.decorators import login_required
from user.models import UserModel

# Create your views here.
@login_required
def index(request):
    html = "<html><body>you are logged in, welcome!</body></html>"
    return render(request, 'user/index.html')