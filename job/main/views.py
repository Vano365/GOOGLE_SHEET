from tabnanny import verbose
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
	login_url = '/login/'
	template_name = "main/index.html"

	def get(self, request, *args, **kwargs):
		
		context = {
		}

		return render(request, self.template_name, context=context)
