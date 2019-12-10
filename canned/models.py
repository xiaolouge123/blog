from django.db import models

# Create your models here.
class CannedDialog(models.Model):
    canned_dialog_category = models.CharField(max_length=200)
    canned_dialog_duc = models.CharField(max_length=200)
    
    def __str__(self):
        return "Category: {} ; DUC: {}".format(self.canned_dialog_category, 
        self.canned_dialog_duc)