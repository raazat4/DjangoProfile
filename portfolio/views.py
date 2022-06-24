from django.shortcuts import render, redirect
from portfolio.models import Contact
# Create your views here.
def index(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')   
      subject = request.POST.get('subject')   
      message = request.POST.get('message')
      contact = Contact(name=name, email=email, subject=subject, message=message)
      contact.save()
   return render(request, "index.html")
