from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from billing.models import Deposit
from billing.models import Call
from django.db.models import Sum


#def index(request):
    # add html template here
#    template = 'billing/post_list.html'
#    return render(request, template)

def users(request):
    template = 'billing/users.html'
    # here we will display list of customers taken from B
    users = User.objects.all()
    context = {'users': users}
    return render(request, template, context)



def customer_detail_page(request):
    pass

def add_deposit_page(request):
    # add html template here
    # example of a form can be found here: https://docs.google.com/document/d/1P46boyASjme1g1HP7RwuWr48-q_Wdumj3KWRcOXsGew/edit
    template = ''
    # here we will process form submissions
    # form data can be accessed like this: request.POST
    # data should be written to DB
    # after this, we should redirect to the list of deposits
    return redirect('/deposits/')

def deposits(request):
    # add html template here
    template = 'billing/deposits.html'
    # here we should take deposits from db and show them in a HTML file
    deposits = Deposit.objects.all()
    context = {'deposits': deposits}
    return render(request, template, context)


def add_call_page(request):
    # add html template here
    # example of a form can be found here: https://docs.google.com/document/d/1P46boyASjme1g1HP7RwuWr48-q_Wdumj3KWRcOXsGew/edit
    template = ''
    # here we will process form submissions
    # form data can be accessed like this: request.POST
    # data should be written to DB
    # after this, we should redirect to the list of calls
    return redirect('/calls/')


def calls(request):
    # add html template here
    template = 'billing/calls.html'
    # here we should take calls from db and show them in a HTML file
    calls = Call.objects.all()
    context = {'calls': calls}
    return render(request, template, context)


def deposits_calls(request):
    template = 'billing/deposits_calls.html'
    deposits = Deposit.objects.all()
    calls = Call.objects.all()
    users = User.objects.all()
    calls_dict = {}
    deposits_dict = {}
    sum_duration_dict = {}
    sum_deposits_dict = {}
    bal_dict = {}
    date = {}
    date_deposit = {}
    for user in users:
        sum_duration = Call.objects.filter(user = user).aggregate(Sum('duration'))['duration__sum']
        calls_dict[user] = Call.objects.filter(user = user)
        sum_deposits = Deposit.objects.filter(user = user).aggregate(Sum('seconds'))['seconds__sum']
        deposits_dict[user] = Deposit.objects.filter(user = user)
        balance = sum_deposits - sum_duration
        sum_duration_dict[user] = sum_duration
        sum_deposits_dict[user] = sum_deposits
        bal_dict[user] = balance
        date[user] = Call.created_at
        date_deposit[user] = Deposit.created_at

    context = {'sum_duration_dict': sum_duration_dict, 'sum_deposits_dict': sum_deposits_dict, 'bal_dict': bal_dict, 'calls_dict': calls_dict, 'deposits_dict': deposits_dict, 'date': date, 'date_deposit': date_deposit}

    result = render(request, template, context)
    return result

def add_call(request, pk):
    template = 'billing/add_call.html'
    user = User.objects.get(pk=pk)
    context = {'pk': pk, 'user':user}
    return render(request, template, context)

def add_deposit(request, pk):
    template = 'billing/add_deposit.html'
    user = User.objects.get(pk=pk)
    context = {'pk': pk, 'user':user}
    return render(request, template, context)

# This view can only be used for handling form submissions
def add_call_form(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        duration = request.POST.get('duration', 0)
        print(type(duration))
        dd = int(duration)
        if dd > 0:
            Call.objects.create(user=user, duration=dd)
        print(user, request.POST)
    return redirect('/')

def add_deposit_form(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        seconds = request.POST.get('seconds', 0)
        print(type(seconds))
        dd = int(seconds)
        if dd > 0:
            Call.objects.create(user=user, seconds=dd)
        print(user, request.POST)
    return redirect('/')

