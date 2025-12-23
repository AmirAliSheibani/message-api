from django.db import models

# Create your models here.
class Message(models.Model):
    sender_choices = [
        ("user", "User"),
        ("system", "System"),
    ]

    sender = models.CharField(max_length=10, choices=sender_choices) #from
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.text[:20]}"
