from django.db import models

# Create your models here.

"""Teams Model"""
class Teams(models.Model):
    """creating a model to store the details for the teams sections
    - Full name
    - profile photo
    - position
    - description
    [these will be filled in by the admin for now or we can create a page for that]
    """

    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    profile_photo = models.ImageField(upload_to='profiles')