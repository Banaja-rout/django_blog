from django.shortcuts import render,  redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.models import Session
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Blog
from .forms import *





def home(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(user=request.user)
        return render(request, 'home.html', {'blogs': blogs})
    else:
        return render(request, 'home.html')
    #posts = Blog.objects.all()
    #return render(request, 'home.html', {'posts': posts})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    session_key = request.session.session_key

 
    if not request.session.get('viewed_post_{}'.format(pk)):
        
        blog.views += 1
        blog.save()
        request.session['viewed_post_{}'.format(pk)] = True

    return render(request, 'blog_detail.html', {'blog': blog})


@login_required
def like_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        if request.user in blog.likes.all():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)  # Redirect to the home page after successfully creating a post
    else:
        form = BlogForm()
    return render(request, 'create.html', {'form': form})



@login_required
def edit_blog(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogPostUpdateForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=blog.pk)  # Assuming you have a URL named 'blog_list' for listing blogs
    else:
        form = BlogPostUpdateForm(instance=blog)
    return render(request, 'update.html', {'form': form})

@login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'delete.html', {'blog': blog})  # Redirect to the home page



def signup_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:

            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('home')
            

    return render (request,'registration.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
            
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html') 


def user_logout(request):
    logout(request)
    return redirect('home') 
