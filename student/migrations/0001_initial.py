# Generated by Django 2.0.8 on 2019-04-03 14:46

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
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Please fill the field with the certificate name Example: Data Science Summer School', max_length=60)),
                ('image', models.FileField(upload_to='%Y/%m/%d')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CvStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('css_file', models.FilePathField(default='bw_style.css', match='([a-zA-Z]+)\\.css', path='static/static/css/cv_styles')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=30)),
                ('period_start', models.DateField(blank=True, null=True)),
                ('period_end', models.DateField(blank=True, null=True)),
                ('description', models.TextField(max_length=130)),
                ('university', models.CharField(max_length=225, null=True)),
                ('field_of_study', models.CharField(blank=True, max_length=225, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Afrikaans', 'Afrikaans'), ('Arabic', 'Arabic'), ('Asturian', 'Asturian'), ('Azerbaijani', 'Azerbaijani'), ('Bulgarian', 'Bulgarian'), ('Belarusian', 'Belarusian'), ('Bengali', 'Bengali'), ('Breton', 'Breton'), ('Bosnian', 'Bosnian'), ('Catalan', 'Catalan'), ('Czech', 'Czech'), ('Welsh', 'Welsh'), ('Danish', 'Danish'), ('German', 'German'), ('Lower Sorbian', 'Lower Sorbian'), ('Greek', 'Greek'), ('English', 'English'), ('Australian English', 'Australian English'), ('British English', 'British English'), ('Esperanto', 'Esperanto'), ('Spanish', 'Spanish'), ('Argentinian Spanish', 'Argentinian Spanish'), ('Colombian Spanish', 'Colombian Spanish'), ('Mexican Spanish', 'Mexican Spanish'), ('Nicaraguan Spanish', 'Nicaraguan Spanish'), ('Venezuelan Spanish', 'Venezuelan Spanish'), ('Estonian', 'Estonian'), ('Basque', 'Basque'), ('Persian', 'Persian'), ('Finnish', 'Finnish'), ('French', 'French'), ('Frisian', 'Frisian'), ('Irish', 'Irish'), ('Scottish Gaelic', 'Scottish Gaelic'), ('Galician', 'Galician'), ('Hebrew', 'Hebrew'), ('Hindi', 'Hindi'), ('Croatian', 'Croatian'), ('Upper Sorbian', 'Upper Sorbian'), ('Hungarian', 'Hungarian'), ('Interlingua', 'Interlingua'), ('Indonesian', 'Indonesian'), ('Ido', 'Ido'), ('Icelandic', 'Icelandic'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Georgian', 'Georgian'), ('Kabyle', 'Kabyle'), ('Kazakh', 'Kazakh'), ('Khmer', 'Khmer'), ('Kannada', 'Kannada'), ('Korean', 'Korean'), ('Luxembourgish', 'Luxembourgish'), ('Lithuanian', 'Lithuanian'), ('Latvian', 'Latvian'), ('Macedonian', 'Macedonian'), ('Malayalam', 'Malayalam'), ('Mongolian', 'Mongolian'), ('Marathi', 'Marathi'), ('Burmese', 'Burmese'), ('Norwegian Bokmål', 'Norwegian Bokmål'), ('Nepali', 'Nepali'), ('Dutch', 'Dutch'), ('Norwegian Nynorsk', 'Norwegian Nynorsk'), ('Ossetic', 'Ossetic'), ('Punjabi', 'Punjabi'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Brazilian Portuguese', 'Brazilian Portuguese'), ('Romanian', 'Romanian'), ('Russian', 'Russian'), ('Slovak', 'Slovak'), ('Slovenian', 'Slovenian'), ('Albanian', 'Albanian'), ('Serbian', 'Serbian'), ('Serbian Latin', 'Serbian Latin'), ('Swedish', 'Swedish'), ('Swahili', 'Swahili'), ('Tamil', 'Tamil'), ('Telugu', 'Telugu'), ('Thai', 'Thai'), ('Turkish', 'Turkish'), ('Tatar', 'Tatar'), ('Udmurt', 'Udmurt'), ('Ukrainian', 'Ukrainian'), ('Urdu', 'Urdu'), ('Vietnamese', 'Vietnamese'), ('Simplified Chinese', 'Simplified Chinese'), ('Traditional Chinese', 'Traditional Chinese')], max_length=255)),
                ('level', models.CharField(choices=[('A1', 'Beginner'), ('A2', 'Elementary'), ('B1', 'Intermediate'), ('B2', 'Upper Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficient')], max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('plang_level', models.CharField(choices=[('1', 'Beginner'), ('2', 'Elementary'), ('3', 'Intermediate'), ('4', 'Upper Intermediate'), ('5', 'Advanced')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_field', models.CharField(default='', help_text='Word/words/abbreviation which describes your project. Example: ML, WEB, IOT, NLP, CV, AI, Design, Networks, BA, Visualization, Robotics, Data Mining, Software, Security, Analysis, Economics', max_length=20)),
                ('name', models.CharField(help_text='Project title. Example: Health Care project', max_length=60)),
                ('about', models.TextField()),
                ('collaborators', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_type', models.CharField(choices=[('hard', 'Hard skill'), ('soft', 'Soft skill'), ('programming', 'Programming languages')], max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudyProgramme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Event title. Example: ML Conference', max_length=60)),
                ('description', models.TextField(max_length=150)),
                ('link', models.URLField(blank=True, null=True)),
                ('organization', models.CharField(blank=True, max_length=225, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(default='', help_text='Example: Back-end dev', max_length=255)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('period_start', models.DateField(blank=True, null=True)),
                ('period_end', models.DateField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Fill the field with description of your responsibilities, gained experience', null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(blank=True, to='student.Skill'),
        ),
    ]