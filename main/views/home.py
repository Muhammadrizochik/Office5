# from django.views.generic import TemplateView

from django.shortcuts import render

def home(request):
    return render(request, "index.html", context={})

# class Home(TemplateView):
#     template_name = "index.html"
