from django.shortcuts import render ,redirect
from .models import Create_resume
from .forms import Create_resumeForm
# Create your views here.
def index(request):
   resume = Create_resume.objects.all()
   return render(request , 'createresume/home.html' , {'title' : 'Главная страница' , 'resumes' : resume})

def about(request):
   return render(request , 'createresume/about.html')

def resume(request): 
   error = ''
   if request.method == 'POST':
      form = Create_resumeForm(request.POST , request.FILES)
      if form.is_valid():
         form.save()
         img_obj = form.instance
         return redirect('home')
      else:
         error = 'Форма была неверной'
         
   form = Create_resumeForm()
   context = {
      'form' : form ,
      'error': error,
   }
   return render(request , 'createresume/resume.html' , context)
