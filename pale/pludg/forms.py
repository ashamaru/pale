from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    business = forms.CharField(max_length=100)
    plz_city = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    sender = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)
