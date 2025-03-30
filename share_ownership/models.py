from django.db import models
from rest_framework.exceptions import ValidationError

from users.models import User
from projects.models import Project


class ShareOwnership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    shares = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.name} owns {self.shares} shares in {self.project}"

    class Meta:
        # Bir user ve bir project için sadece bir kayıt olmalı
        unique_together = ['user', 'project']

    def clean(self):
        if self.shares < 1:
            raise ValidationError("Shares must be at least 1.")

    def save(self, *args, **kwargs):
        self.clean()
        if not self.pk:
            self.project.participantCount += 1
            self.project.sharesTaken += self.shares
            self.project.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.project.participantCount -= 1 if self.project.participantCount > 0 else 0
        self.project.sharesTaken -= self.shares if self.project.sharesTaken >= self.shares else 0
        self.project.save()
        super().delete(*args, **kwargs)

# There is no update functionality for ShareOwnership model at the moment.
# If an update functionality will be considered in the future, the following is the code for the update functionality:

# from django.db.models.signals import post_save, pre_delete

# @receiver(post_save, sender=ShareOwnership)
# def update_project_on_ownership_save(sender, instance, created, **kwargs):
#     if created:
#         instance.project.participantCount += 1
#         instance.project.sharesTaken += instance.shares
#         instance.project.save()
#
#
# @receiver(pre_delete, sender=ShareOwnership)
# def update_project_on_ownership_delete(sender, instance, **kwargs):
#     instance.project.participantCount -= 1
#     instance.project.sharesTaken -= instance.shares
#     instance.project.save()

