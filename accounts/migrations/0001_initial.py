from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='slug')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('BAC_id', models.CharField(max_length=255, verbose_name='BAC id')),
                ('is_verified', models.BooleanField(default=False, verbose_name='is verified')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('phone_number', models.CharField(max_length=14, verbose_name='phone number')),
                ('year_of_graduation', models.CharField(max_length=20, verbose_name='year of graduation')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='country')),
                ('certificate', models.FileField(upload_to='', verbose_name='certificate')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'alumni'), (2, 'excos'), (3, 'admin')], default=1, verbose_name='User Type')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BitsSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='bits school name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],

            options={
                'verbose_name_plural': 'Bits Schools',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to='', verbose_name='profile photo')),
                ('bio', models.CharField(blank=True, max_length=255, null=True, verbose_name='Bio')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('website_link', models.URLField(verbose_name='website link')),
                ('portfolio_link', models.URLField(verbose_name='portfolio link')),
                ('facebook_profile', models.URLField(verbose_name='facebook profile')),
                ('twitter_profile', models.URLField(verbose_name='twitter profile')),
                ('linkedin_profile', models.URLField(verbose_name='linkedIn profile')),
                ('skill_sets', models.CharField(blank=True, max_length=255, null=True, verbose_name='skill sets')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='bits_school',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bits_schools', to='accounts.bitsschool'),

        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
