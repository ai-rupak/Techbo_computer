from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Category)
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','section','status')
    list_filter =['section']
    list_editable = [ 'status', 'section']
    search_fields = ['title'] 

@admin.register(Client)
class  ClientAdmin(admin.ModelAdmin):
    list_display=('name','date')