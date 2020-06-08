# Generated by Django 3.0.7 on 2020-06-05 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='case',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='answer',
        ),
        migrations.CreateModel(
            name='UserPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_attempts', models.IntegerField(default=0)),
                ('correct_answers', models.IntegerField(default=0)),
                ('complete', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.UserAnswer')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('num_questions', models.IntegerField(default=0)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.Case')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(related_name='questions', to='viewer.Quiz'),
        ),
    ]