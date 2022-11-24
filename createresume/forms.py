from django.forms import ModelForm , Textarea , TextInput
from .models import Create_resume 

class Create_resumeForm(ModelForm):
   class Meta:
      model = Create_resume 
      fields = ['name' , 'surname' , 'gender' , 'age' , 'email' , 'tell' , 'location' , 'descr' , 'descr_hardSkill' , 'photo']
      widgets = {
         'name': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Имя'}),
         'surname': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Фамилия'}),
         'gender': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Пол'}),
         'age': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Возраст'}),
         'email': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Почта'}),
         'tell': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Номер телефона'}),
         'location': TextInput(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'Местопроживание'}),
         'descr': Textarea(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'О себе'}),
         'descr_hardSkill': Textarea(attrs={'class' : 'form-control mb-3' , 'placeholder' : 'О hardSkill'}),
      }