# Generated by Django 4.0.1 on 2022-01-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('service', models.CharField(choices=[('web design', 'WEB DESIGN'), ('branding', 'BRANDING'), ('web aps', 'WEB APS'), ('graphic', 'GRAPHIC'), ('support', 'SUPPORT')], default='web design', max_length=20)),
                ('message', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]