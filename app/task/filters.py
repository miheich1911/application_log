from django import forms
from .models import Category
from django_filters import FilterSet, DateFilter, ModelChoiceFilter, ChoiceFilter
from .resourses import STATUS


class TaskFilter(FilterSet):
    time_in = DateFilter(
        label='Созданные после',
        lookup_expr='gt',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form'})
    )
    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        lookup_expr='exact',
        label='Категория',
        empty_label='любая'
    )

    complete = ChoiceFilter(
        choices=STATUS,
        label='Статус',
        empty_label='любой'
        )



