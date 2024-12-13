from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser  # Assuming a custom user model


class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_notifications')
    verb = models.CharField(max_length=255)  # Description of the action (e.g., "liked your post")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Generic relation to any model (e.g., Post, Comment)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'Notification for {self.recipient} by {self.actor}: {self.verb}'
