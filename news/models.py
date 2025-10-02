from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from teachers.models import Teacher
from taggit.managers import TaggableManager
from utils.models import CleanableFileModel

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'
        db_table = "categories"
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-list')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(CleanableFileModel):
    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
    )
    
    title = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True, db_index=True, help_text="Jika tidak diisi, akan otomatis terisi dengan judul")
    content = RichTextUploadingField()
    author = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='blog_posts')
    category = models.ManyToManyField(Category, related_name='posts', help_text="Pada PC, Tekan Ctrl untuk memilih lebih dari satu kategori")
    tags = TaggableManager()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    featured_image = models.ImageField(upload_to='blog_images/', default='no-image.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'posts'
        db_table = "posts"
        indexes = [
            models.Index(fields=['slug', 'created_at', 'author']),
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    file_field_names = ['featured_image']

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.slug])
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', db_index=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_index=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'comments'
        db_table = "comments"
        indexes = [
            models.Index(fields=['post', 'created_at', 'author']),
        ]

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'