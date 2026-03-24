from django.shortcuts import render ,redirect
from .models import Post
from .forms import PostForm
from .models import Feedback
from .forms import FeedbackForm

def home(request):
    return render(request,'home.html')

def post(request):
    posts = Post.objects.filter(is_active=True)
    return render(request, 'post.html', {'posts': posts})
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = PostForm()

    return render(request, 'post_list.html', {'form': form})

def feedback_list(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')

    else:
        form = FeedbackForm()
    context = {
        'form':form,
        'feedback':Feedback.objects.filter(is_active=True).order_by('-created_at')
     }
    return render(request,'feedback_list.html',context)





# Create your views here.