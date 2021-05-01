from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .forms import ParticipantForm, InquiryForm, NewslettersubcriberForm


# Create your views here.

def homepage(request):
    if request.method == "POST":
        form = NewslettersubcriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NewslettersubcriberForm()
    return render(request, 'eventapp/index.html',{'form':form})

def register(request ):   #participant_id

    # participant = get_object_or_404(Participant, id=participant_id, )

    sent = False

    if request.method == "POST":  
        form = ParticipantForm(request.POST)  
        if form.is_valid():
            cd = form.cleaned_data  
            form.save() 
            subject = f"{cd['name']} Event Registration" 
            message = f"Thank you for registering for the Tec event at UCU. You mmay attend pyhsically or virtually using this link"
            send_mail(subject, message, 'masozeravictor@gmail.com',[cd['email']])
            
            sent = True 

            return redirect('/')  
            
    else:  
        form = ParticipantForm()  
    return render(request,'eventapp/register.html',{'form':form})  

def show(request):  
    participants = Participant.objects.all()  
    return render(request,"eventapp/show.html",{'students':students})  

def contact(request):
    if request == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InquiryForm()
    return render(request, "eventapp/contact.html",{'form':form})

# def subscribe(request):
#     if request == "POST":
#         form = NewslettersubcriberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('')
#     else:
#         form = NewslettersubcriberForm()
#     return render(request, "eventapp/index.html",{'form':form})