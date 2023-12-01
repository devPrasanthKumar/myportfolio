from django import forms


class SendMailForm(forms.Form):

    sender_name = forms.CharField(
        max_length=200, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    sender_email = forms.EmailField(
        max_length=200, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    subject = forms.CharField(
        max_length=400, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
