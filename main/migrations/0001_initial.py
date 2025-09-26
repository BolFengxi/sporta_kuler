

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(help_text='Price of the product in IDR')),
                ('description', models.TextField()),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('category', models.CharField(choices=[('BALL', 'Ball'), ('BOOT', 'Football Boots'), ('KIT', 'Kits & Jerseys'), ('EQUI', 'Equipment'), ('ACCS', 'Accessories'), ('OTHR', 'Other Football Items')], default='OTHR', max_length=20)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
    ]
