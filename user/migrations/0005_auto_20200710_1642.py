# Generated by Django 3.0.1 on 2020-07-10 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200710_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.AutoField(primary_key=True, serialize=False)),
                ('board_name', models.CharField(max_length=255)),
                ('is_state_board', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Corrections',
            fields=[
                ('correction_id', models.AutoField(primary_key=True, serialize=False)),
                ('marks_received', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('submissions_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Submissions')),
            ],
        ),
        migrations.AlterField(
            model_name='classenrollment',
            name='enrollment_status',
            field=models.CharField(blank=True, choices=[('enrolled', 'enrolled'), ('not_enrolled', 'not_enrolled')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='SubmissionResources',
            fields=[
                ('submissions_resource_id', models.AutoField(primary_key=True, serialize=False)),
                ('resource_type', models.CharField(blank=True, choices=[], max_length=100, null=True)),
                ('resource_link', models.URLField(max_length=500)),
                ('caption', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('submission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Submissions')),
            ],
        ),
        migrations.CreateModel(
            name='School_Board_Bridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.IntegerField()),
                ('board_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('school_id', 'board_id')},
            },
        ),
        migrations.CreateModel(
            name='HomeworkResources',
            fields=[
                ('homework_resource_id', models.AutoField(primary_key=True, serialize=False)),
                ('resource_type', models.CharField(blank=True, choices=[], max_length=200, null=True)),
                ('file_field', models.FileField(upload_to='files_images/homeworkresources/%Y/%m/%d/')),
                ('homework_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Homework')),
            ],
        ),
        migrations.CreateModel(
            name='CorrectionsResources',
            fields=[
                ('correction_resource_id', models.AutoField(primary_key=True, serialize=False)),
                ('resource_type', models.CharField(blank=True, choices=[], max_length=200, null=True)),
                ('resource_link', models.URLField(max_length=500)),
                ('caption', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('correction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Corrections')),
            ],
        ),
    ]
