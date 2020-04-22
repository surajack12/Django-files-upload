from django import forms

class ProfileImageForms(forms.Form):
    image = form.forms.FileField(label="Select a file")
    
    
)