from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import *
from django.db.models import Q
from .utils import paginateStories
from .forms import FormContact


def index(request):
    stories = Story.objects.order_by('-public_day')
    most_viewed = Story.objects.order_by('viewed')[0:5]
    category = Category.objects.all()
    young_children = Category.objects.get(name='Young Children').story_set.all().order_by('-public_day')
    older_children = Category.objects.get(name='Older Children').story_set.all().order_by('-public_day')
    newest = stories[0]
    list_4_stories = stories[1:5]
    list_6 = stories[0:6]
    videos = Story.objects.filter(url__startswith='https://youtu.be/')
    context = {'category': category,'stories': stories, 'newest': newest, 'list_4_stories': list_4_stories, 'young_children': young_children, 'older_children': older_children, 'most_viewed': most_viewed, 'list_6': list_6, 'videos': videos}

    return render(request, 'stories/index.html', context)

def contact_us(request):
    # Cách 1
    # if request.POST.get('btnSend'):
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')

    #     print(name)
    #     print(email)
    #     print(subject)
    #     print(message)
        
    #     contact = Contact(name=name, email=email, subject=subject, message=message)
    #     contact.save()
    
    form = FormContact()
    if request.POST.get('btnSend'):
        form = FormContact(request.POST, Contact)
        if form.is_valid():
            request.POST._mutable = True
            post = form.save(commit=False)
            post.name = form.cleaned_data['name']
            post.email = form.cleaned_data['email']
            post.subject = form.cleaned_data['subject']
            post.message = form.cleaned_data['message']
            post.save()

    stories = Story.objects.order_by('-public_day')
    most_viewed = Story.objects.order_by('viewed')[0:5]
    category = Category.objects.all()
    list_6 = stories[0:6]
    context = {'category': category, 'most_viewed': most_viewed, 'list_6': list_6, 'form': form,}
    return render(request, 'stories/contact_us.html', context)

def story(request, pk):
    stories = Story.objects.order_by('-public_day')
    most_viewed = Story.objects.order_by('viewed')[0:5]
    category = Category.objects.all()
    list_6 = stories[0:6]
    story = Story.objects.get(pk=pk)
    context = {'story': story, 'category': category, 'most_viewed': most_viewed, 'list_6': list_6}
    return render(request, 'stories/story.html', context)

def older_children(request):
    older_children = Category.objects.get(name='Older Children').story_set.all().order_by('-public_day')
    stories = Story.objects.order_by('-public_day')
    most_viewed = Story.objects.order_by('viewed')[0:5]
    category = Category.objects.all()
    list_6 = stories[0:6]
    context = {'older_children': older_children, 'category': category, 'most_viewed': most_viewed, 'list_6': list_6}
    return render(request, 'stories/older_children.html', context)

def young_children(request):
    young_children = Category.objects.get(name='Young Children').story_set.all().order_by('-public_day')
    stories = Story.objects.order_by('-public_day')
    most_viewed = Story.objects.order_by('viewed')[0:5]
    category = Category.objects.all()
    list_6 = stories[0:6]
    context = {'young_children': young_children, 'category': category, 'most_viewed': most_viewed, 'list_6': list_6}
    return render(request, 'stories/young_children.html', context)

def search_result(request):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query').strip()

    search_result = Story.objects.distinct().filter(
        Q(category__name__icontains=search_query)|
        Q(name__icontains=search_query)|
        Q(author__icontains=search_query)|
        Q(summary__icontains=search_query)|
        Q(content__icontains=search_query)
    ).order_by('-public_day')

    search_result, custom_range = paginateStories(request, search_result, 4)
    stories = Story.objects.order_by('-public_day')
    most_viewed = Story.objects.order_by('viewed')[0:5]
    category = Category.objects.all()
    list_6 = stories[0:6]

    context = {"search_result": search_result, "search_query": search_query, 'category': category, 'most_viewed': most_viewed, 'list_6': list_6, 'custom_range': custom_range}
    return render(request, 'stories/search_result.html', context)

def category(request, pk):
    stories_filter = Story.objects.filter(category=pk).order_by('-public_day')
    stories_filter, custom_range = paginateStories(request, stories_filter, 4)
    stories = Story.objects.order_by('-public_day')
    most_viewed = Story.objects.order_by('viewed')[0:5]
    cate = Category.objects.get(pk=pk)
    category = Category.objects.all()
    list_6 = stories[0:6]
    context = {'stories_filter':stories_filter, 'stories':stories, 'category': category, 'most_viewed': most_viewed, 'list_6': list_6, 'cate': cate, 'custom_range': custom_range,}
    return render(request, 'stories/category.html', context)




def master(request):
    return render(request, 'stories/_Master.html')
# Create your views here.
