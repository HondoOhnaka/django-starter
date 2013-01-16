from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from starter.models import Starter
from starter.forms import StarterForm

from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView

class MyFormView(CreateView):
    template_name = 'starter_form.html'
    form_class = StarterForm
    success_url = '/list-page/'

    def form_valid(self, form):
        return super(MyFormView, self).form_valid(form)

class MyUpdateView(UpdateView):
	template_name='starter_form.html'
	model = Starter
	success_url = '/list-page/'

class MyListView(ListView):
	model = Starter
	template_name = 'starter_list.html'

class MyDetailView(DetailView):
	model = Starter
	template_name = 'starter_detail.html'

