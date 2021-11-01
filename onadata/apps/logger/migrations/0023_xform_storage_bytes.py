# Generated by Django 2.2.14 on 2021-10-29 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logger', '0022_create_xform_submission_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='xform',
            name='storage_bytes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='xformsubmissioncounter',
            name='xform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='xformcounter', to='logger.XForm'),
        ),
    ]
