from django.shortcuts import render
from foodonthemove.models import Account
from foodonthemove.serializers import AccountSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

def index(request):
    account_list = Account.objects.all()
    context = {'account_list': account_list}
    return render(request, 'foodonthemove/index.html', context)


def list_ticket(request):
    account_list = Account.objects.all()
    serialized = AccountSerializer(account_list, many=True)
    json_account = JSONRenderer().render(serialized.data)
    print "Yes"
    print json_account
    return HttpResponse(json_account, 'application/json')
