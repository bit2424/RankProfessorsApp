from django.test import TestCase

# Create your tests here.
from polls.models import Choice, Question
from django.utils import timezone
q = Question(question_text = "LOL?" , pub_date = timezone.now())
q.save() 
q2  = Question.objects.create(question_text="¿Cuál es el mejor curso de platzi?" , pub_date=timezone.now()) 
