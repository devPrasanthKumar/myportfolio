from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.mail import send_mail

from portApp.forms import SendMailForm
# Create your views here.


class IndexView(TemplateView):
    template_name = "html/index.html"


class SendEmailView(FormView):
    template_name = "html/contact.html"
    form_class = SendMailForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        sender_name = form.cleaned_data["sender_name"]
        sender_email = form.cleaned_data["sender_email"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        admin_mail = "jackoffjerry52010@gmail.com"
        print(sender_email, sender_name, subject, message, admin_mail)

        message_from_admin = f" Hai {sender_name} ,\n\n\n I have recived your mail \n\n\n thanks for visiting my page \n\n\n have a good day :)"
        send_mail(subject, message, sender_email, [admin_mail])

        send_mail("Reply from Admin", message_from_admin,
                  admin_mail, [sender_email])

        return super().form_valid(form)
