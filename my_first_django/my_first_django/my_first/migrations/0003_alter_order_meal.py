# Generated by Django 4.0.2 on 2022-02-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first', '0002_alter_order_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='meal',
            field=models.TextField(choices=[('Cheeseburger', 'Cheeseburger'), ('Hot dog', 'Hot dog'), ('Pizza', 'Pizza'), ('T-Bone', 'T-Bone'), ('French fries', 'French fries'), ('Salmon tartar', 'Salmon tartar')], max_length=20),
        ),
    ]