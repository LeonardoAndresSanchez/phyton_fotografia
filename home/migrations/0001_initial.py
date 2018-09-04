# Generated by Django 2.0.7 on 2018-07-19 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camara', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fotografo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(max_length=100)),
                ('camara', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Camara')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modeloc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_camara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_fotografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='fotografo',
            name='tipof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Tipo_fotografia'),
        ),
        migrations.AddField(
            model_name='camara',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Modelo'),
        ),
        migrations.AddField(
            model_name='camara',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Tipo_camara'),
        ),
    ]