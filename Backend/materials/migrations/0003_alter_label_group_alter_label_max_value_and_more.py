# Generated by Django 5.1.5 on 2025-02-21 18:22

import django.core.validators
import django.db.models.deletion
import materials.models
import materials.validation
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups_courses', '0002_group_edit_permissions_joinrequest'),
        ('materials', '0002_alter_material_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='groups_courses.group'),
        ),
        migrations.AlterField(
            model_name='label',
            name='max_value',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='label',
            name='min_value',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='material',
            name='file',
            field=models.FileField(default=None, null=True, upload_to=materials.models.material_file_path, validators=[materials.validation.validate_file_mime, django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'txt']), materials.validation.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='material',
            name='url',
            field=models.URLField(default=None, null=True, validators=[materials.validation.VideoURLValidator()]),
        ),
    ]
