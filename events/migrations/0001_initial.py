# Generated by Django 3.2.5 on 2021-11-11 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='event id')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description')),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
                ('no_of_attendant', models.PositiveIntegerField(verbose_name='number of attendant')),
                ('location', models.CharField(max_length=255, verbose_name='location')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='link')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('image', models.ImageField(upload_to='media/events/', verbose_name='image')),
                ('is_gallery', models.BooleanField(default=False, verbose_name='is gallery')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('attendant', models.ManyToManyField(related_name='attendants', to=settings.AUTH_USER_MODEL)),
                ('bit_school', models.ManyToManyField(to='accounts.BitsSchool')),
                ('contact', models.ManyToManyField(related_name='contacts', to=settings.AUTH_USER_MODEL)),
                ('create_by', models.ForeignKey(default='deleted', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EventGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='media/galleries/', verbose_name='images')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleries', to='events.event')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.ManyToManyField(to='events.Tag'),
        ),
    ]
