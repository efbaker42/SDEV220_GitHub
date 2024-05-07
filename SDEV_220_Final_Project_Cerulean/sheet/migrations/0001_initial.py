# Generated by Django 5.0.5 on 2024-05-07 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength_score', models.SmallIntegerField()),
                ('dexterity_score', models.SmallIntegerField()),
                ('constitution_score', models.SmallIntegerField()),
                ('intelligence_score', models.SmallIntegerField()),
                ('wisdom_score', models.SmallIntegerField()),
                ('charisma_score', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player_Entry',
            fields=[
                ('character_name', models.TextField(primary_key=True, serialize=False)),
                ('level', models.SmallIntegerField()),
                ('armor_class', models.SmallIntegerField()),
                ('initiative', models.SmallIntegerField()),
                ('hit_points', models.SmallIntegerField()),
                ('conditions', models.TextField(blank=True, null=True)),
                ('inspiration', models.BooleanField()),
                ('inventory', models.TextField()),
                ('spells', models.TextField(blank=True, null=True)),
                ('speed', models.TextField()),
                ('defenses', models.TextField()),
                ('features', models.TextField()),
                ('traits', models.TextField()),
                ('proficiencies', models.TextField()),
                ('proficiency_value', models.SmallIntegerField()),
                ('languages', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('player_entry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='sheet.player_entry')),
                ('skill', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('base_score', models.SmallIntegerField()),
                ('prof', models.BooleanField()),
                ('abl', models.SmallIntegerField()),
                ('skill_score', models.SmallIntegerField()),
            ],
            bases=('sheet.player_entry',),
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('abilities_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='sheet.abilities')),
                ('skills_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sheet.skills')),
                ('last_saved', models.DateTimeField(blank=True, null=True)),
            ],
            bases=('sheet.skills', 'sheet.abilities'),
        ),
    ]
