from django import forms
from django.contrib import admin
from starter.models import Starter

class StarterForm(forms.ModelForm):
	class Meta:
		model = Starter

class StarterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Starter, StarterAdmin)
