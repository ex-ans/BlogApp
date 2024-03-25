from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from myBlogApp.models import BlogPost
from django.db.models import Max
from django.contrib import messages

# Create your views here.


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Sucessfull")
            # return HttpResponse("Welcome you are logged in")
            return redirect('/home')
        else:
            return render(request , 'signin.html')
    return render(request , 'signin.html')



def signup(request):
     if request.method == 'POST':
         username = request.POST.get('username')
         email = request.POST.get('email')
         password  = request.POST.get('password')
         cpassword  = request.POST.get('cpassword')
         print(username , password)
         if password == cpassword:
             user = User.objects.create_user(username , email , password)
             user.save()
             messages.success(request, "User Signedup successfully Please Log in.")
             print("user add succesfully")
             return redirect('/signin')
         else:
             print("Password did'nt matched")
         
     return render(request, 'signup.html')




def index(request):
    return render(request , 'index.html')



def home(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    blogs = BlogPost.objects.order_by('date')
    return render(request , 'home.html', {'blogs': blogs})




def createblog(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    blog_id = 1 if BlogPost.objects.count()==0 else BlogPost.objects.aggregate(max = Max('blog_id'))["max"]+1
    if request.method == 'POST':
        author = User.objects.get(username=request.user)
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = request.POST.get('date')
        blog = BlogPost(blog_id=blog_id, title= title, author= author , content=content, date=date)
        blog.save()
        messages.success(request, "Blog created successfully.")
        print("Your Blog Saved Sucessfully in DataBase!")
        return redirect('/home')
    return render(request , 'createblog.html' , locals())


def uploadedblog(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    else:
        blogs = BlogPost.objects.filter(author=request.user)
        return render(request,"uploadedblog.html" , {'blogs' : blogs})

    



def logoutuser(request):
    logout(request)
    return redirect('/signin')

def readmore(request , blog_id):
    readmore = BlogPost.objects.get(blog_id = blog_id)
    print(readmore)
    return render(request, 'readmore.html', {'readmore': readmore})


def delete(request , blog_id):
    blog = BlogPost.objects.get(blog_id = blog_id)
    blog.delete() 
    messages.success(request, "Your Blog has been deleted.")
    return redirect('/uploadedblog')
    

def edit(request , blog_id):
    edit = BlogPost.objects.get(blog_id = blog_id)
    print(edit)
    return render(request, 'edit.html', {'edit': edit})

def updated(request , blog_id):
        title = request.POST.get("title")
        content = request.POST.get("content")
        date = request.POST.get("date")
        update = BlogPost.objects.get(blog_id=blog_id)
        update.title = title
        update.content = content
        update.date = date
        update.save()
        messages.success(request, "Your Blog has been updated.")
        return redirect('/uploadedblog')


def search(request):
    if request.method == "GET":
        search_query = request.GET.get("search")
        if search_query:
            alldata = BlogPost.objects.filter(title__contains=search_query) 
            print(alldata)
            return render(request, 'search.html', {'alldata': alldata})
        else:
            return render(request, 'search.html', {})
    return render(request , 'search.html')