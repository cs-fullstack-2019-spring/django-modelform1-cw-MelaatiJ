from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewBlogPost


# Create your views here.

# view that created a new blog and saves it into the data base
def index(request):
    newBlog = NewBlogPost()
    if request.method == "POST":
        print("Blog post received")
        newBlog = NewBlogPost(request.POST)
        if newBlog.is_valid():
            newBlog.save()
        else:
            print("error")

    return render(request, "blogPostApp/index.html", {"blogPostForm": newBlog})
