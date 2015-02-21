from django.shortcuts import renderm
from foodonthemove.models import Account
# Create your views here.
def index(request):
    account_list = Account.objects.all()