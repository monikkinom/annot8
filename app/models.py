from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)


class Code(models.Model):
    user = models.ForeignKey(User)
    code = models.TextField()
    title = models.CharField(max_length=200)
    choice = (
        ('cpp', 'C++'),
        ('python', 'Python'),
        ('php', 'PHP'),
        ('c', 'C'),
        ('java', 'Java'),
        ('javascript', 'Javascript'),
        ('csharp', 'C#'),
        ('python', 'Python'),
        ('ruby', 'Ruby'),
        ('swift', 'Swift'),
        ('objectivec', 'Objective-C'),
        ('css', 'CSS'),
        ('php', 'Unknown/Text'),
    )
    language = models.CharField(choices=choice,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Annot8s'

class Annotations(models.Model):
    code = models.ForeignKey(Code)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    start = models.IntegerField()
    end = models.IntegerField()
    cx = (
        ('marked','Green'),
        ('marked2','Red'),
        ('marked3','Yellow')
    )
    color = models.CharField(choices=cx,max_length=100)

    class Meta:
        verbose_name_plural = 'Annotations'