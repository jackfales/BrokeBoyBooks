from .models import Textbook

from django import forms

class AddTextbookForm(forms.ModelForm):
    class Meta:
        model = Textbook
        fields = ('title', 'author', 'edition', 'link')
        widgets = {
            'title':forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Title'}
            ),
            'author':forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Author'}
            ),
            'edition':forms.NumberInput(attrs={
                    'class':'form-control',
                    'placeholder':'0'}
            ),
            'link':forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'URL'}
            ),
        }