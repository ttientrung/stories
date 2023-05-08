from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateStories(request, stories, results):
    page = request.GET.get('page')
    paginator = Paginator(stories, results)

    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        stories = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        stories = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    righIndex = (int(page) + 3)
    if righIndex > paginator.num_pages:
        righIndex = paginator.num_pages + 1
    
    custom_range = range(leftIndex, righIndex)

    return stories, custom_range