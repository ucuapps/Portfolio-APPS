# Generated by Django 2.0.8 on 2019-04-03 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='current_study_year',
            field=models.IntegerField(blank=True, choices=[(1, 'First year'), (2, 'Second year'), (3, 'Third year'), (4, 'Fourth year')], null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='cv_hard_skills',
            field=models.ManyToManyField(blank=True, related_name='cv_hard_skills', to='student.Skill'),
        ),
        migrations.AddField(
            model_name='student',
            name='cv_programming_languages',
            field=models.ManyToManyField(blank=True, related_name='cv_programming_languages', to='student.Skill'),
        ),
        migrations.AddField(
            model_name='student',
            name='cv_projects',
            field=models.ManyToManyField(blank=True, related_name='cv_projects', to='student.Project'),
        ),
        migrations.AddField(
            model_name='student',
            name='cv_soft_skills',
            field=models.ManyToManyField(blank=True, related_name='cv_soft_skills', to='student.Skill'),
        ),
        migrations.AddField(
            model_name='student',
            name='cv_style',
            field=models.ManyToManyField(blank=True, related_name='cv_style', to='student.CvStyle'),
        ),
        migrations.AddField(
            model_name='student',
            name='cv_summary',
            field=models.TextField(blank=True, help_text='Enter not more than 280 symbols', max_length=280, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='cv_volunteering',
            field=models.ManyToManyField(blank=True, related_name='cv_volunteering', to='student.VolunteerExperience'),
        ),
        migrations.AddField(
            model_name='student',
            name='cv_working',
            field=models.ManyToManyField(blank=True, related_name='cv_working', to='student.WorkingExperience'),
        ),
        migrations.AddField(
            model_name='student',
            name='hard_skills',
            field=models.ManyToManyField(blank=True, related_name='hard_skills', to='student.Skill'),
        ),
        migrations.AddField(
            model_name='student',
            name='programming_languages',
            field=models.ManyToManyField(blank=True, related_name='programming_languages', to='student.Skill'),
        ),
        migrations.AddField(
            model_name='student',
            name='soft_skills',
            field=models.ManyToManyField(blank=True, related_name='soft_skills', to='student.Skill'),
        ),
        migrations.AddField(
            model_name='student',
            name='study_programme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.StudyProgramme'),
        ),
        migrations.AddField(
            model_name='student',
            name='summary',
            field=models.TextField(blank=True, help_text='Enter here 1-5 sentences about you. EX: Honors student with record of academic and extracurricular success. Extensive leadership experience, particularly within a higher education setting.Adept at working across departments, with faculty, administrators', null=True),
        ),
    ]
