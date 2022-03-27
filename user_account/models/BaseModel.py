from django.db import models


class BaseModel(models.Model):
    '''
    Base model containing timestamps for object
    creation and modification
    '''
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
