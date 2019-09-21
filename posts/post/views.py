from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from .models import Post,Author
from .forms import PostModelForm
# Create your views here.


def posts_list(request):
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    messages.info(request, 'Here are all the blog posts')
    return render(request, "details/posts_list.html", context)


def posts_detail(request,slug):
    unique_post = get_object_or_404(Post, slug=slug)
    context = {'post': unique_post}
    messages.info(request, 'This is the specific detail view')
    return render(request, "details/posts_detail.html", context)


def posts_create(request):
    author, created = Author.objects.get_or_create(user=request.user,email=request.user.email,cellphone_num = 9849989501)
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        messages.info(request, 'Successfully created a new blog post')
        return redirect('/posts/')
    context = {
        'form': form
    }
    return render(request, "details/posts_create.html", context)


def posts_update(request,slug):
    unique_post = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, request.FILES or None, instance = unique_post)
    if form.is_valid():

        form.save()
        messages.info(request, 'Successfully updated')
        return redirect('/posts/')
    context = {'form': form}
    return render(request, "details/posts_create.html", context)


def posts_delete(request,slug):
    unique_post = get_object_or_404(Post, slug=slug)
    unique_post.delete()
    messages.info(request, 'Successfully deleted')
    return redirect('/posts/')







