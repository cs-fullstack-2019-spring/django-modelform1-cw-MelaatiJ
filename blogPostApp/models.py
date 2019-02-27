from django.db import models
from django.utils import timezone


# Create your models here.

# * Create a BlogPost model with the following fields:
#     ```
# title
# text
# created_date (should be populated with current dat/time when record created)
# published_date (should be populated when record created and if updated)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=4000)
    created_date = models.DateTimeField(default=timezone.now)
