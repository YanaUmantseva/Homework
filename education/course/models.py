from django.db import models



class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    topics = models.ManyToManyField(Topic, related_name='courses')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='authors')

    def __str__(self):
        return self.name
