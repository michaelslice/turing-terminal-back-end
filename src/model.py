from django.db import models
from userbiography.model import UserBio

'''


'''
class Messages(models.Model):
    user = models.ForeignKey(UserBio, on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Message from {self.user.user_name} at {self.time}"