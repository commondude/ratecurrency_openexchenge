from django.test import TestCase,SimpleTestCase,RequestFactory
from getsomecurrency.views import  JsonTalk
import json
from django.http import HttpRequest
from django.test import Client
from django.urls import reverse
# import urllib3



# Create your tests here.
# class ApiRestRateCurTests(SimpleTestCase):
#
#     def test_api_rest_return_json(self):
#         client = Client()
#         data = {'usd': 100.20}
#         data_json= json.dumps(data)
#         answer_raw = client.post(reverse('json'),{'body':data_json})
#         print(answer_raw)
#         answer_json = json.loads(str(answer_raw))
#         print(type(answer['rub'])==type(data['usd']))
#         self.assertJSONEqual(type(answer['rub']),type(data['usd']))
