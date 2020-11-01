# Generated by Django 3.1.2 on 2020-11-01 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer_id', models.IntegerField(unique=True)),
                ('kor_name', models.CharField(max_length=100)),
                ('eng_name', models.CharField(max_length=100)),
                ('kor_company_name', models.CharField(max_length=100)),
                ('eng_company_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('country_code', models.CharField(max_length=200, null=True)),
                ('country_name', models.CharField(max_length=200, null=True)),
                ('alcohol', models.CharField(max_length=20, null=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(null=True, upload_to='beer')),
                ('image_url', models.CharField(max_length=200, null=True)),
                ('rate', models.CharField(default='0.0', max_length=100)),
            ],
            options={
                'db_table': 'Beer',
            },
        ),
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('date', models.DateField(auto_now_add=True)),
                ('rate', models.IntegerField(null=True)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='api.beer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='api.user')),
            ],
            options={
                'db_table': 'Review',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='api.beer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='api.user')),
            ],
            options={
                'db_table': 'Like',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient', to='api.beer')),
            ],
            options={
                'db_table': 'Ingredient',
            },
        ),
    ]
