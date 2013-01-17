from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse, reverse_lazy

from django.views.generic import TemplateView

def main_page(TemplateView):
	template_name="main_page.html"
