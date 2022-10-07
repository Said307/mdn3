
 
from django.core.exceptions import ValidationError
from django import forms



def namecheck(value):
       
        if len(value) > 10:
            raise forms.ValidationError("Name Should be 10 digit")


class ContactForm(forms.Form):
    name =  forms.CharField(max_length=50,validators=[namecheck])
    telephone = forms.CharField()
    message =  forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    #image = forms.FileField()

    
   

    def clean_name(self):

        name=self.cleaned_data['name']

        return 'cleaned'+name

    def clean_telephone(self):

        number=self.cleaned_data['telephone']
        return '0044' + number

    def clean(self):
        cleaned_data = super().clean()
        
        name =cleaned_data['name']
        message= cleaned_data['message']
    
        if name in message:
            #raise ValidationError('Message cannot contain your name')
            self.add_error('name','big mistake in name')
            self.add_error('message','big mistake in message')
    
   
 
 

    
