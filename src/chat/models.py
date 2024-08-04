from django.db import models
from userbiography.model import UserAccount

# Create your models here.
'''
Relationship: Linked to UserAccount through a foriegn,
so each chat message is associated with a UserAccount

@Note: Foreign key to UserAccount

@Relevant Sources: https://docs.djangoproject.com/en/5.0/topics/db/models/#automatic-primary-key-fields
'''
class Chats(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE) # Foreign key to UserAccount, to link each unique user
    message = models.TextField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Message from {self.user.user_name} at {self.time}"