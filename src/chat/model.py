from django.db import models
from userbiography.model import UserBio

'''
Relationship: Linked to UserBio through a foriegn,
so each message is associated with a specific user

Relevant Sources: https://docs.djangoproject.com/en/5.0/topics/db/models/#automatic-primary-key-fields
'''
class Messages(models.Model):
    user = models.ForeignKey(UserBio, on_delete=models.CASCADE) # Foreign key to UserBio, to link each unique user
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Message from {self.user.user_name} at {self.time}"