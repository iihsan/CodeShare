from django import forms
from .models import Snip
from feed.models import Post
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
class snipForm(forms.ModelForm):
    helper = FormHelper()

    class Meta:
        model=Post
        widgets = {'author': forms.HiddenInput()}
        fields= ('title', 'description', 'code', 'lang', 'tags', 'author')
        # labels={'title':'Snippet Title','description':'New Snippet','code':'Secret Code','lang': 'Syntax Highlighting'}

class searchForm(forms.Form):
    helper = FormHelper()
    search = forms.CharField(max_length=100, widget= forms.TextInput
                           (attrs={'class':'is-small input is-info', 'placeholder':'Search Text Here'}))
    