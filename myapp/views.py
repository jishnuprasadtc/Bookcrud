from django.shortcuts import render,redirect
from myapp.forms import BookForms,BookModelForm
from django.views.generic import View
from myapp.models import Books

# Create your views here.

class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BookModelForm()
        return render(request,"book_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            # Books.objects.create(**form.cleaned_data)
            print("add")
            return render(request,"book_add.html",{"form":form})
        else:
            return render(request,"book_add.html",{"form":form})



class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()     # use model class name
        return render(request,"Booklist.html",{"data":qs})
    
    def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        qs=Books.objects.filter(name__icontains=name)
        return render(request,"Booklist.html",{"data":qs})


class BookDetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        return render(request,"book_detail.html",{"book":qs})
    

class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return redirect("book-all")
    

class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookModelForm(instance=obj)
        return render(request,"book_edit.html",{"form":form})
    


    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookModelForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            print("updated")
            return redirect("book-detail",pk=id)
        else:
            return render(request,"book_edit.html",{"form":form})


