from django.db import models

# Create your models here.

# <---- نموذج لحفظ الاسئلة في قاعدة البيانات--->
class Question(models.Model):
    question = models.TextField(max_length=1500, default='نص السؤال ')
    option_1 = models.CharField(max_length=100, default='الاخيار الاول ')
    option_2 = models.CharField(max_length=100, default='الاخيار الثاني ')
    option_3 = models.CharField(max_length=100, default='الاخيار الثالث ')
    option_4 = models.CharField(max_length=100, default='الاخيار الرابع ')
    correct_answer = models.CharField(max_length=100 , default='الاجابة الصحيحة ')
    # date_time = models.DateTimeField()