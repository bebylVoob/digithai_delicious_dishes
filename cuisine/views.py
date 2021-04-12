from django import forms
from django.shortcuts import render

from cuisine.models import Cuisine, Dishes


def cuisine_views(request):
    # Just for blank query.
    parameter_now = ''
    cuisine = request.GET.get('cuisine', None)
    cuisine_list = Cuisine.objects.values_list('type_name', flat=True).order_by('type_name').distinct()
    cuisine_dict = {}
    if cuisine:
        cuisine_dict = Dishes.objects.select_related('cuisine').filter(cuisine__type_name=cuisine)
        parameter_now += '?cuisine=' + cuisine
        return render(
            request,
            'cuisine.html',
            {
                'cuisine': cuisine,
                'cuisine_list': cuisine_list,
                'cuisine_dict': cuisine_dict
            }
        )
    return render(
        request,
        'cuisine.html',
        {
            'cuisine': cuisine,
            'cuisine_list': cuisine_list,
            'cuisine_dict': cuisine_dict
        }
    )
