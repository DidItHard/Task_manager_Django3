# Generated by Django 4.0.6 on 2022-07-30 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='importance',
        ),
        migrations.AddField(
            model_name='todo',
            name='creator',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='todo',
            name='important',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default='< no title >', max_length=200),
        ),
        migrations.AlterField(
            model_name='todo',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='decription',
            field=models.TextField(blank=True),
        ),
    ]
