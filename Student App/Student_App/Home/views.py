from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        frm=StudentRegistration(request.POST)
        if frm.is_valid():
            nm=frm.cleaned_data['name']
            rol=frm.cleaned_data['roll']
            cls=frm.cleaned_data['Class']
            ag=frm.cleaned_data['Age']
            Ciy=frm.cleaned_data['City']
            reg=User(name=nm,roll=rol,Class=cls,Age=ag,City=Ciy)
            reg.save()
            
            frm=StudentRegistration()
    else:
        frm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/ADD.html',{'form':frm,'stu':stud})

def delete_data(request, id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/update.html',{'form':fm})

