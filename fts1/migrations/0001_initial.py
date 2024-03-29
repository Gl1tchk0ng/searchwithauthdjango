# Generated by Django 5.0.2 on 2024-02-08 14:25

import django.contrib.postgres.search
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('input_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='fts1.input')),
            ],
        ),
    ]
