from django.db import models
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.indexes import GinIndex
import re

class Paragraph(models.Model):
    text = models.TextField()
    tokenized_text = models.TextField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.tokenized_text = self.tokenize_and_lowercase(self.text)
        super(Paragraph, self).save(*args, **kwargs)

    def tokenize_and_lowercase(self, text):
        # Tokenize words and convert them to lowercase
        words = re.findall(r'\w+', text, re.UNICODE)
        return ' '.join(word.lower() for word in words)

    def search(self, query):
        # Creating a word-to-paragraph index for efficient searching
        vector = SearchVector('tokenized_text')
        query = SearchQuery(query)
        rank = SearchRank(vector, query)
        return self.filter(tokenized_text__search=query).annotate(rank=rank)