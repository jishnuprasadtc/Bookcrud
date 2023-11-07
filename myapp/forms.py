from django import forms
from myapp.models import Books


class BookForms(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))


class BookModelForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control border border-primary"}),
            "author":forms.TextInput(attrs={"class":"form-control border border-primary"}),
            "price":forms.NumberInput(attrs={"class":"form-control border border-primary"})

        }
