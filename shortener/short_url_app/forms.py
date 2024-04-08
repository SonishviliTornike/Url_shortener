from django import forms

class TakeUrl(forms.Form):
    url_form = forms.CharField(max_length=140, label='Enter URL to shorten:')
