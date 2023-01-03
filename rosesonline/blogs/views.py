from django.shortcuts import render, get_object_or_404
from .models import Blogs
from django.core.paginator import Paginator

def get_client_if(request):
    x_forwared_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwared_for:
        ip = x_forwared_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def view(request, slug):
    blog = get_object_or_404(Blogs, slug=slug)
    ip = get_client_if(request)
    # print(request.META)
    print()
    return render(request, 'blogs/blog-view.html', context={'blog': blog})

def blogs(request, *args, **kwargs):
    blogs = Blogs.objects.values('title', 'sub_text','body', 'createdAt', 'image','image_link', 'author', 'slug').order_by('-id')
    paginator = Paginator(blogs, 25)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    return render(request, 'blogs/blogs-list.html', context={'page_obj': page_obj})