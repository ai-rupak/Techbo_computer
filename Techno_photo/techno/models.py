from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

# class Category(models.Model):
#     name= models.CharField(max_length=200)

#     def __str__(self):
#         return self.name
    
class Post(models.Model):
    STATUS=(
        ('0','Draft'),
        ('1','Publish'),
    )

    SECTION = (
        ('Main_post','Main_post'),
        ('Recent','Recent'),
        ('Popular','Popular'),
        ('Gallary','Gallary'),
        ('Editors_Pick','Editors_Pick'),
        
    )

    featured_image = models.ImageField(upload_to='Images')
    title = models.CharField(max_length=200)
    content = RichTextField()
    # category = models.ForeignKey(Category,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)
    status = models.CharField(choices=STATUS,max_length=100)
    section =models.CharField(choices =SECTION,max_length=200)

    def __str__(self):
        return self.title
    
class Client(models.Model):
    name = models.CharField(max_length=50)
    mobile_no = models.IntegerField(max_length=12)
    event_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add = False)
    address = models.CharField(max_length=300)
    message = models.CharField(max_length=400)

    def __str__(self):
        return self.name

