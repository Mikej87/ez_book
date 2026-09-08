from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_dish_dishes_dish_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='dishes',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='items',
        ),
    ]
