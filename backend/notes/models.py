from typing import Iterable, Optional
from django.db import models

# Create your models here.
class Note(models.Model) :
    created = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    
    @property
    def formatted_created(self):
        return self.created.strftime("%d-%m-%Y")
    
    # def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
    #     self.created = self.created.strftime("%d-%m-%Y %H:%M:%S")
    #     return super().save(force_insert, force_update, using, update_fields)