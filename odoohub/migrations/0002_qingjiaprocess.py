# Generated by Django 3.1.7 on 2021-02-24 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewflow', '0008_jsonfield_and_artifact'),
        ('odoohub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QingJiaProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.process')),
                ('text', models.CharField(max_length=150)),
                ('days', models.CharField(max_length=150)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
