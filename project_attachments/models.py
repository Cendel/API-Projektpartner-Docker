from django.db import models
from projects.models import Project
import os


def upload_to_path(instance, filename):
    project_name = Project.objects.get(id=instance.project.id).projectTitle
    return f'project_attachments_files/{project_name}/{filename}'


class Attachment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to=upload_to_path, null=True, blank=True)
    file_name = models.CharField(max_length=200, null=True, blank=True)
    file_extension = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.file:
            self.file_name = os.path.splitext(self.file.name)[0]
            self.file_extension = os.path.splitext(self.file.name)[1]
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.file:
            storage, path = self.file.storage, self.file.path
            storage.delete(path)
        super().delete(*args, **kwargs)
