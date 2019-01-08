from django.shortcuts import render
from django.shortcuts import redirect

from billing.models import Deposit
from billing.models import Call


def index(request):
    # add html template here
    template = ''
    return render(request, template)


def customers(request):
    template = ''
    # here we will display list of customers taken from DB
    return render(request, template)


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
    template = ''
    # here we should take deposits from db and show them in a HTML file
    deposits = Deposit.objects.all()
    context = {'deposits': deposits}
    return render(request, template, context)


def add_call_page(request:
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
    template = ''
    # here we should take calls from db and show them in a HTML file
    calls = Call.objects.all()
    context = {'calls': calls}
    return render(request, template, context)