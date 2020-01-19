from .models import Textbook

from django import forms

class AddTextbookForm(forms.ModelForm):
    class Meta:
        model = Textbook
        fields = ('title', 'author', 'edition', 'link')
        widgets = {
            'title':forms.TextInput(attrs={
                    'class':'form-control blue-box title-input',
                    'placeholder':'Title'}
            ),
            'author':forms.TextInput(attrs={
                    'class':'form-control blue-box author-input',
                    'placeholder':'Author'}
            ),
            'edition':forms.NumberInput(attrs={
                    'class':'form-control blue-box edition-input',
                    'placeholder':'0'}
            ),
            'link':forms.TextInput(attrs={
                    'class':'form-control blue-box link-input',
                    'placeholder':'URL'}
            ),
        }