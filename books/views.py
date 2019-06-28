# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.mail import send_mail
from django import forms
import datetime
from django.core import serializers

from .models import Publisher

# def search_form(request):
#     return render_to_response('search_form.html')

def search(request, model):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = model.objects.filter(title__icontains=q)
            return render_to_response('books/search_results.html',
                {'books': books, 'query': q})
    return render_to_response('books/search_form.html',
        {'errors': errors })

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
        	initial={'subject': 'I love your site!'}
        )
    return render_to_response('books/contact_form.html', {'form': form})

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('books/current_datetime.html', locals())

def hello(request):
    publisher = Publisher.objects.all()
    data = serializers.serialize("json", publisher)
    return HttpResponse(data, content_type='application/json')

def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('books/hours_ahead.html', locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
