# Generated by Django 4.0.4 on 2022-05-05 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('phone_number', models.TextField()),
                ('email', models.EmailField(max_length=50)),
                ('previous_illness', models.TextField()),
                ('chronic_diseases', models.TextField()),
                ('addictions', models.TextField()),
                ('blood_type', models.CharField(max_length=5)),
                ('allergy', models.TextField()),
                ('current_meds', models.TextField()),
                ('previous_surgeries', models.TextField()),
                ('disabilities', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
