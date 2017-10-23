from django import forms

#from .models import Categoria

class ContactForm(forms.Form):
	nombre = forms.CharField()
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea())


'''class AddCategory(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)
'''
