from django.shortcuts import render
from django.views.generic.base import View

from .models import Page

class PagesView(View):
    def get(self, request):
        pages = Page.objects.all()
        return render(request, 'pages/pages_list.html', {'pages_list': pages})
        





