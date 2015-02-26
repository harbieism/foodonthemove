from django.shortcuts import render, redirect
from foodonthemove.models import Account
from django.core.urlresolvers import reverse
from foodonthemove.serializers import AccountSerializer
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from rest_framework.renderers import JSONRenderer
from django.utils import timezone
import json
from django.core.context_processors import csrf


def index(request):
    if not request.user.is_authenticated():
        return redirect('/food/user_login')
    account_list = Account.objects.all()
    context = {'account_list': account_list}
    return render(request, 'foodonthemove/index.html', context)

def get_account(username):
    try:
        return Account.objects.get(username=username)
    except Account.DoesNotExist:
        return None


def user_login(request):
    if request.method == 'GET':
        return render(request, 'foodonthemove/user_login.html')
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = {"Error": "disabled_account"}
                error_json = json.dumps(error)
                return HttpResponse(error_json, content_type="application/json")
        else:
            error = {"Error": "invalid_login"}
            error_json = json.dumps(error)
            return HttpResponse(error_json, content_type="application/json")




def list_ticket(request):
    account_list = Account.objects.filter(is_admin=False)
    serialized = AccountSerializer(account_list, many=True)
    json_account = JSONRenderer().render(serialized.data)
    print "Yes"
    print json_account
    return HttpResponse(json_account, 'application/json')

def register(request):
    if request.method == "POST":
        try:
            email = request.POST.get("emailValue")
            username = request.POST.get("username")
            phone_number = request.POST.get("phoneNumber")
            userType = request.POST.get("userType")
            if int(userType) == 0:
                username = str(email)
            elif int(userType) == 1:
                username = str(phone_number)

            if (request.POST.get("contactEmail") == "on"):
                contact_email = True
            else:
                contact_email = False

            if (request.POST.get("contactCall") == "on"):
                contact_call = True
            else:
                contact_call = False

            if (request.POST.get("contactText") == "on"):
                contact_text = True
            else:
                contact_text = False

            first_name = request.POST.get("inputFirstname")
            last_name = request.POST.get("inputLastname")

            zip_code = request.POST.get("zipCode")

            is_paying = request.POST.get('inputPayment')
            if is_paying == '0':
                is_paying = False
            else:
                is_paying = True

            payment_amount = request.POST.get('inputAmount')
            meals = request.POST.get('inputMeals')
            password = request.POST.get('passwordValue')
            password_confirm = request.POST.get('passwordConfirmValue')
            account = get_account(username)
            if password == password_confirm:
                if account is None:
                    if is_paying:
                        account = Account.objects.create_user(
                            username=username, email=email, phone_number=phone_number,
                            contact_email=contact_email, contact_call=contact_call,
                            contact_text=contact_text, first_name=first_name,
                            last_name=last_name, zip_code=zip_code,
                            is_paying=is_paying, payment_amount=payment_amount,
                            password=password
                        )
                    else:
                        account = Account.objects.create_user(
                            username=username, email=email, phone_number=phone_number,
                            contact_email=contact_email, contact_call=contact_call,
                            contact_text=contact_text, first_name=first_name,
                            last_name=last_name, zip_code=zip_code,
                            is_paying=is_paying,
                            password=password
                        )

            return HttpResponseRedirect(reverse('register'))
        except:
            return HttpResponseRedirect(reverse('register'))


    elif request.method == "GET":
        return render(request, 'foodonthemove/register.html')
