from django.db import models
from taggit.managers import TaggableManager
from teachers.models import Teacher

class Caterogytest(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    class Meta:
        db_table = "blog_category_test"

    def __str__(self):
        return self.name


# Create your models here.
class BlogTest(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    description = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Caterogytest, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "blog_test"