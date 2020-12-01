from .forms import CommentForm
from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponseRedirect
# Create your views here.


def blog_index(request):
    # -created_on is descending. largest value first
    posts = Post.objects.all().order_by('-created_on')
    context = {'posts': posts}
    return render(request, 'blogs/blog_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(  # filtered by the 'category' item sent by the POST request form
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blogs/blog_category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()  # ginawa natin sa forms.py #making an instance of this class
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():  # is_valid is a django library method
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form':form,
    }
    return render(request, 'blogs/blog_detail.html', context)
