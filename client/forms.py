from django import forms  
from .models import Document 



class UploadForm(forms.Form):    
    file = forms.FileField() # for creating file input  

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', ) 
        
           

  