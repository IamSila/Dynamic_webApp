from django.db import models

# Create your models here.

"""Teams Model"""
class Team(models.Model):
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

    def __str__(self):
        """returns the full_name of the object as the name of that object"""
        return f"{self.full_name} ----> {self.position}"



"""analytics model"""
class Analytic(models.Model):
    """creating the fields in the db for the analytics table
    - clients
    - projects
    - Hours of support
    - workers
    """
    clients = models.IntegerField()
    projects = models.IntegerField()
    Hours_of_support = models.IntegerField()
    workers = models.IntegerField()

    def __str__(self):
        """names assigned to the object of this class"""
        return "siteAnalytics"