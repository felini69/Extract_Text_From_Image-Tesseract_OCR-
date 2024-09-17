from django import forms
from .models import UploadedImage

# class ImageUploadForm(forms.ModelForm):
#     class Meta:
#         model = UploadedImage
#         fields = ['image']



class ImageUploadForm(forms.Form):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)
