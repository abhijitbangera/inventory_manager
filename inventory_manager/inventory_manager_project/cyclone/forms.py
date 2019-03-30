from django import forms
from cyclone.models import arrays, employees

class arrays_form(forms.ModelForm):
	class Meta:
		model= arrays
		fields = '__all__'
		exclude = ['array_status']

class arrays_release_form(forms.ModelForm):
	class Meta:
		model= arrays
		fields = '__all__'
		exclude = ['employee_array', 'array_status']

