from django import forms  
from eventapp.models import Participant, Inquiry, Newslettersubcriber

class ParticipantForm(forms.ModelForm):  
    class Meta:  
        model = Participant  
        fields = "__all__"  
class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = "__all__"
class NewslettersubcriberForm(forms.ModelForm):
    class Meta:
        model = Newslettersubcriber
        fields = "__all__"
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'E-Mail here'}),
        }


