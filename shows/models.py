from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):

        # errors dictionnary
        errors = {}
        
        # checking title
        if len(postData['show_title']) == 0:
            errors['show_title_emp'] = "Title can not be empty"
        elif len(postData['show_title']) > 0 and len(postData['show_title']) < 2:
            errors['show_title_len'] = "Title should be less at least 2 characters long"
        elif len(postData['show_title']) > 0 and len(postData['show_title']) > 255:
            errors['show_title_len2'] = "Title should be less than 255 characters long"    
            
        # checking network    
        if len(postData['show_network']) == 0:
            errors['show_network_emp'] = "Network can not be empty"
        elif len(postData['show_network']) < 3:
            errors['show_network_len'] = "Network should be less at least 3 characters long"    
        
        # checking date    
        if len(postData['show_date']) == 0:
            errors['show_date_emp'] = "Release date can not be empty"      
        else:
            # The strptime() method creates a datetime object from the given string.            
            release_date = datetime.strptime(postData['show_date'], "%Y-%m-%d")
            today_date = datetime.today()

            yesterday = today_date - timedelta(days=1)
                
            if release_date >= yesterday:
                errors['show_date_emp'] = "Release date must be less than today's date"          
       
        #checking description       
        if postData['show_description'] != '' and len(postData['show_description']) < 10:
            errors['show_description_emp'] = "Description should be less at least 10 characters long"   
            
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255, unique=True)
    network = models.CharField(max_length=255)
    release_date = models.DateField()    
    description = models.TextField(default="No description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"Show: (ID: {self.id}) -> {self.title} = {self.description} by {self.network}"
    
