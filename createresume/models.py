from django.db import models

# Create your models here.

class Profile(models.Model):
   login = models.CharField('Login' , max_length=255)
   password = models.CharField('password' , max_length=255)
   
   def __str__(self) -> str:
      return self.login
   
   class Meta:
      verbose_name = 'Профиль'
      verbose_name_plural = 'Профили'
   
class Create_resume(models.Model):
   name = models.CharField('Имя' , max_length=255)
   surname = models.CharField('Фамилия' , max_length=255)
   gender = models.CharField('Пол' , max_length=255)
   age = models.CharField('Возраст' , max_length=255)
   email = models.EmailField('Почта' , max_length=255)
   tell = models.CharField('Номер Телефона' , max_length=255)
   location = models.CharField('Местоположение' , max_length=255)
   descr = models.TextField('Описание о себе' , max_length=255)
   descr_hardSkill = models.TextField('Описание HardSkill' , max_length=255)
   photo = models.ImageField(upload_to='images')
   
   def __str__(self) -> str:
      return self.name