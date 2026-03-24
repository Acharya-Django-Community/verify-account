from django.contrib import admin
from .models import Post
from .models import Feedback
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','created_by', 'updated_at')
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'question', 'created_at', 'answered_by', 'is_active')
# Register your models here.
