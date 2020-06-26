# import json
# import requests
#
# from django.shortcuts import render
# from django.views import View
#
# from . import models
#
# from bs4 import BeautifulSoup
#
#
# class SearchListView(View):
#     queryset = models.SiteURL.objects.all()
#
#     def post(self, request):
#         data = json.loads(request.body)
#
#         req = requests.get(f'{models.SiteURL.URL}{data["query"]}')
#         html = req.text
#         soup = BeautifulSoup(html, 'html.parser')
#
#

