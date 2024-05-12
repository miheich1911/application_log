from django import forms
from django.forms import TextInput
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from task.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
       model = Task
       fields = ['category', 'text', 'place', 'complete']
       widgets = {
           "place": TextInput(attrs={"class": "text"}),
       }
       labels = {
           "category": "Категория",
           "text": "Описание заявки",
           "place": "Место, где нужно произвести работу",
           'complete': "Статус заявки"

       }


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['complete']
        widgets = {
            "place": TextInput(attrs={"class": "text"}),
        }
        labels = {
            'complete': "Статус заявки"
        }