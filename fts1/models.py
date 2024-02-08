from django.db import models
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.utils import timezone

class Input(models.Model):
    input_id = models.AutoField(primary_key=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.text = self.text.lower()
        super().save(*args, **kwargs)
        self.text = self.text.split('\n\n')

class Paragraph(models.Model):
    document = models.ForeignKey(Input, on_delete=models.CASCADE, related_name='paragraphs')
    paragraph_id = models.AutoField(primary_key=True)
    search_vector = SearchVectorField(null=True)
    
    def save(self, *args, **kwargs):
        self.refresh_search_vector()
        super().save(*args, **kwargs)

    def refresh_search_vector(self):
        # Update search_vector field based on the text
        vector = SearchVector('text', weight='A')
        self.search_vector = vector
