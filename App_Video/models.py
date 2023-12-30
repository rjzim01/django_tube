from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Video(models.Model):
    author = models.ForeignKey(
        User, related_name='post_author', on_delete=models.CASCADE)
    video_title = models.CharField(max_length=264, verbose_name='Put a Title')
    slug = models.SlugField(max_length=264, unique=True)
    video_description = models.TextField(verbose_name='Video description...')
    video_thumbnail = models.ImageField(
        upload_to='video_thumbnail',
        verbose_name='Image',
        null=True,
        default=None
    )

    video_file = models.FileField(
        upload_to='videos', verbose_name='Video File')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return self.video_title


class Comment(models.Model):
    video = models.ForeignKey(
        Video, related_name='video_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='user_comment', on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date',]

    def __str__(self):
        return self.comment
