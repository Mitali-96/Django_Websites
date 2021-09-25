from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Notes
from .forms import NoteCreationForm,NoteUpdateForm,AccountSettingsForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,'notes/index.html')

def register(request):
    form=UserCreationForm()
    if(request.method=='POST'):
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('notes:login')
    context={
        'form':form,
    }
    return render(request,'notes/register.html',context)
#def login(request):
    #return render(request,'notes/login.html')
@login_required
def home_page(request):
    notes=Notes.objects.all()
    form=NoteCreationForm()
    if(request.method=="POST"):
        form=NoteCreationForm(request.POST)
        if(form.is_valid()):
            note_obj=form.save(commit=False)
            note_obj.author=request.user
            note_obj.save()

            return redirect('notes:home_page')
    context={
        'notes':notes,
        'form':form,
    }
    return render(request,"notes/home.html",context)

@login_required
def settings(request):

    user=request.user
    form = AccountSettingsForm(instance=user)
    if (request.method == "POST"):
        user.username=request.POST['username']
        user.first_name=request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        messages.success(request,"Account Updated Succesfully")
        return  redirect('notes:settings')
    context = {
        'user': user,
        'form': form,
    }
    return render(request,'notes/settings.html',context)

def loggedout(request):
    return render(request,'notes/loggedout.html')

@login_required
def update(request,id):
    note_to_update=Notes.objects.get(id=id)
    form = NoteUpdateForm(instance=note_to_update)

    if (request.method == 'POST'):
        form = NoteUpdateForm(request.POST)

        if (form.is_valid()):
             note_to_update.title= form.cleaned_data['title']
             note_to_update.description=form.cleaned_data['description']

             note_to_update.save()
             return redirect('notes:home_page')
    context = {
        'note': note_to_update,
        'form':form
    }
    return render(request,'notes/update.html',context)

@login_required
def delete(request,id):
    note_to_delete=Notes.objects.get(id=id)
    note_to_delete.delete()
    return redirect('notes:home_page')

