from django.shortcuts import render
from .forms import GetSomeForm
import requests,json
from .openexchange import opexurl,appid

def getsome(request):
    if request.method == 'POST':
        form = GetSomeForm(request.POST)
        if form.is_valid():
            r = requests.get(opexurl+appid)
            rubrate = json.loads(r.text)['rates']['RUB']
            rub = '{0:.2f}'.format(form.cleaned_data['amount'] * rubrate)+' руб.'

            return render(request,'getsomecurrency/getsome.html',{'form':form,'amount':rub,'rubrate':str(rubrate)+' руб.'})
    else:
        form = GetSomeForm()

    return render(request,'getsomecurrency/getsome.html',{'form':form,'rubrate':'-'})
