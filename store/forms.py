from django import forms
from .models import Product


class ProductCreate(forms.ModelForm):
    name = forms.CharField()
    title = forms.CharField()
    class Meta:
        model = Product
        fields = "__all__"
    # def clean_name(self,*args,**kwargs):
    #     name = self.cleaned_data.get('name')
    #     if len(name) < 5:
    #         raise forms.ValidationError("name should be atleast 5 character")
    #     else:
    #         return name
    # def clean_address(self,*args,**kwargs):
    #     address = self.cleaned_data.get('address')
    #     if len(address) < 5:
    #         raise forms.ValidationError("address should be atleast 5 character")
    #     else:
    #         return address



