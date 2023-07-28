from django.db import models

class Feedback(models.Model):
    name = models.charField(max_length=100)
    email = models.EmailField(max_length)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} = {self.email}"
    
