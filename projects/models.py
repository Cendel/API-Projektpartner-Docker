from django.db import models
from users.models import User
import shutil
import os


class Project(models.Model):
    projectStatus = models.BooleanField(default=False)
    adminAdvice = models.BooleanField(default=False)
    projectTitle = models.CharField(max_length=255, blank=False)
    projectPlace = models.CharField(max_length=255, blank=False)
    estimatedImplementationDate = models.DateTimeField(blank=False)
    slogan = models.CharField(max_length=50, blank=False)
    about = models.TextField(blank=False)
    goal = models.TextField(blank=False)
    support = models.TextField(blank=False)
    shortDesc = models.CharField(max_length=200, blank=False)
    longDesc = models.TextField(blank=False)
    projectImage = models.ImageField(upload_to='project_images/')
    createdBy = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    createdByName = models.CharField(max_length=255, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    followerList = models.ManyToManyField(User, related_name='followed_projects', blank=True)
    participantCount = models.PositiveIntegerField(default=0)
    projectValue = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=False)
    totalShares = models.PositiveIntegerField(default=0, blank=False)
    shareValue = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=False)
    maxSharesPerPerson = models.PositiveIntegerField(default=0, blank=False)
    sharesTaken = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.projectTitle} by {self.createdByName} has {self.participantCount} participant(s)."

    def save(self, *args, **kwargs):
        if self.createdBy:
            self.createdByName = self.createdBy.name
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        media_path = os.path.join('media', 'project_attachments_files', self.projectTitle)
        if os.path.exists(media_path):
            shutil.rmtree(media_path)

        storage, path = self.projectImage.storage, self.projectImage.path
        super().delete(*args, **kwargs)
        storage.delete(path)
