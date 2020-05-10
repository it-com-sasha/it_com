from django.shortcuts import render
from django.views.generic.base import View

from .models import Page

class PagesHomeView(View):
    def get(self, request):
        pages = Page.objects.filter(show_on_home=True)
        return render(request, 'pages/pages_home.html', {'pages_list': pages})
        





