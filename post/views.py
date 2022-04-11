from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
# def home(request):
#     context={
#     }
#     return render(request,'post/home.html',context)


class HomeListView(ListView):
    model = Post
    template_name='post/home.html'
    context_object_name='posts'
    

