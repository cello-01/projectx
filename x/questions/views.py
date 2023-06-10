from django.shortcuts import render
from .models import Question

# Create your views here.


def question(request):
    
      return render(request, 'questions/question.html')

def questions(request):
      
      return render(request, 'questions/questions.html', {'ques':Question.objects.all()})


def check_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_answer = request.POST.get('answer')

        question = Question.objects.get(id=question_id)

        if question.correct_answer == selected_answer:
            # تم اختيار الإجابة الصحيحة
            # يمكنك إعطاء رسالة نجاح أو توجيه المستخدم إلى السؤال التالي
            messages.success(request, 'إجابة صحيحة!')
            return redirect('questions')  # هنا يمكنك تحديد العرض الذي تريد توجيه المستخدم إليه بعد الإجابة على السؤال
        else:
            # تم اختيار إجابة خاطئة
            # يمكنك إعطاء رسالة خطأ أو توجيه المستخدم إلى السؤال التالي
            messages.error(request, 'إجابة خاطئة، حاول مرة أخرى!')
            return redirect('questions')  # هنا يمكنك تحديد العرض الذي تريد توجيه المستخدم إليه بعد الإجابة على السؤال