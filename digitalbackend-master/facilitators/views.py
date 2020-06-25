from django.shortcuts import render
from .models import Trainer
# Create your views here.
def home(request):
    if request.method=='POST':
        tname=request.POST.get('tname','')
        temail=request.POST.get('temail','')
        texp1=request.POST.get('texp1','')
        texp2=request.POST.get('texp2','')
        tphone=request.POST.get('tphone','')
        turl=request.POST.get('turl','')
        #tprofile=request.POST.get('tprofile','')
        q_s=request.POST.get('q/s','')
        tprofile=request.FILES['tprofile']
        trainer = Trainer(tname=tname,q_s=q_s,temail=temail,tphone=tphone,texp1=texp1,texp2=texp2,turl=turl,tprofile=tprofile)
        trainer.save()
    return render(request,'facilitators/home.html')