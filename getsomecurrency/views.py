from django.views import View
from django.shortcuts import render
from .forms import GetSomeForm
import requests,json
from .openexchange import opexurl,appid
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


"""
FBV и CBV варианты getsome
"""
# def getsome(request):
#     if request.method == 'POST':
#         form = GetSomeForm(request.POST)
#         if form.is_valid():
#             r = requests.get(opexurl+appid)
#             rubrate = json.loads(r.text)['rates']['RUB']
#             rub = '{0:.2f}'.format(form.cleaned_data['amount'] * rubrate)+' руб.'
#
#             return render(request,'getsomecurrency/getsome.html',{'form':form,'amount':rub,'rubrate':str(rubrate)+' руб.'})
#     else:
#         form = GetSomeForm()
#
#     return render(request,'getsomecurrency/getsome.html',{'form':form,'rubrate':'-'})



class GetSome(View):
    def post(self,request):
        form = GetSomeForm(request.POST)
        if form.is_valid():
            r = requests.get(opexurl+appid)
            rubrate = json.loads(r.text)['rates']['RUB']
            #rub = '{0:.2f}'.format(form.cleaned_data['amount'] * rubrate)+' руб.'
            amount_usd = form.cleaned_data['amount']
            amount_rub = amount_usd*rubrate
            rub ='{0:.2f}'.format(amount_rub) +' руб.'
            return render(request,'getsomecurrency/getsome.html',{'form':form,'amount':rub,'rubrate':str(rubrate)+' руб.'})
        else:
            form = GetSomeForm()
            return render(request,'getsomecurrency/getsome.html',{'form':form,'rubrate':'-'})


    def get(self,request):
        form = GetSomeForm()
        return render(request,'getsomecurrency/getsome.html',{'form':form,'rubrate':'-'})

"""
API REST принимаем json {'usd': amount} и отдаём {'rub': amount}
"""
# @csrf_exempt
# def jsontalk(request):
#     jsontalk.csrf_exempt = True
#     if request.method == 'POST':
#         in_msg_dict = json.loads(request)
#         r = requests.get(opexurl+appid)
#         rubrate = json.loads(r.text)['rates']['RUB']
#         amount = in_msg_dict['usd'] * rubrate
#         answer ={'rub':amount}
#
#         return json.dumps(answer)
#     else:
#         in_msg_dict = json.loads(request)
#         r = requests.get(opexurl+appid)
#         rubrate = json.loads(r.text)['rates']['RUB']
#         amount = in_msg_dict['usd'] * rubrate
#         answer ={'rub':amount}
#         return json.dumps(answer)
#         #return render(request,'getsomecurrency/getsome.html',{'form':form,'rubrate':'-'})


class JsonTalk(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(JsonTalk, self).dispatch(*args, **kwargs)

    def post(self,request):

        in_msg_dict = json.loads(request.body)
        r = requests.get(opexurl+appid)
        rubrate = json.loads(r.text)['rates']['RUB']
        amount = in_msg_dict['usd'] * rubrate
        answer ={'rub':amount}
        return HttpResponse(json.dumps(answer))
