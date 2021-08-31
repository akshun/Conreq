# Generated by Django 3.2.6 on 2021-08-31 03:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0004_envvar_screenshot'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EnvVar',
            new_name='EnvironmentVariable',
        ),
        migrations.AlterModelOptions(
            name='environmentvariable',
            options={},
        ),
        migrations.RenameField(
            model_name='apppackage',
            old_name='notice_message',
            new_name='banner',
        ),
        migrations.CreateModel(
            name='NoticeMessage',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('mark_read', models.BooleanField(default=False)),
                ('app_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_store.apppackage')),
            ],
        ),
    ]
