# Generated by Django 3.0.4 on 2020-04-15 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0019_auto_20200406_1609'),
        ('classification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classifications', to='classification.Category')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Paper')),
                ('sub_category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classifications', to='classification.Subcategory')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classifications', to='classification.Token')),
            ],
        ),
    ]
