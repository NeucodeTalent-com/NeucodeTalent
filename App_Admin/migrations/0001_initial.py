# Generated by Django 5.0.9 on 2024-12-30 10:52

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProject',
            fields=[
                ('cp_id', models.AutoField(db_column='ClientID', primary_key=True, serialize=False)),
                ('client_name', models.CharField(db_column='ClientName', max_length=100)),
                ('project_name', models.CharField(db_column='ProjectName', max_length=100)),
                ('assessment_type', models.CharField(blank=True, db_column='AssessmentType', max_length=50, null=True)),
                ('start_date', models.DateField(db_column='ProjectStartDate')),
                ('end_date', models.DateField(db_column='ProjectEndDate')),
            ],
            options={
                'db_table': 'client_project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CliPr',
            fields=[
                ('cp_id', models.IntegerField(db_column='ClientID', primary_key=True, serialize=False)),
                ('client_name', models.CharField(db_column='ClientName', max_length=255)),
                ('project_name', models.CharField(db_column='ProjectName', max_length=255)),
                ('seeker_id', models.IntegerField(db_column='SeekerID')),
                ('seeker_name', models.CharField(db_column='SeekerName', max_length=255)),
                ('seeker_email', models.EmailField(db_column='SeekerEmail', max_length=254)),
                ('provider_id', models.IntegerField(db_column='ProviderID')),
                ('provider_name', models.CharField(db_column='ProviderName', max_length=255)),
                ('provider_email', models.EmailField(db_column='ProviderEmail', max_length=254)),
                ('relationship', models.CharField(db_column='Relationship', max_length=255)),
                ('status', models.CharField(db_column='Status', max_length=50)),
            ],
            options={
                'db_table': 'client_project_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FullRatingDataView',
            fields=[
                ('cp_id', models.IntegerField(db_column='ClientID', primary_key=True, serialize=False)),
                ('client_name', models.CharField(db_column='ClientName', max_length=255)),
                ('project_name', models.CharField(db_column='ProjectName', max_length=255)),
                ('seeker_name', models.CharField(db_column='SeekerName', max_length=255)),
                ('seeker_email', models.EmailField(db_column='SeekerEmail', max_length=254)),
                ('provider_email', models.EmailField(db_column='ProviderEmail', max_length=254)),
                ('relationship', models.CharField(db_column='Relationship', max_length=255)),
                ('question_text', models.TextField(db_column='QuestionText')),
                ('competency', models.CharField(db_column='Competency', max_length=255)),
                ('feedback_value', models.FloatField(db_column='FeedbackValue')),
            ],
            options={
                'db_table': 'full_rating_data_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainClient',
            fields=[
                ('clientid', models.AutoField(db_column='ClientID', primary_key=True, serialize=False)),
                ('clientname', models.CharField(db_column='ClientName', max_length=255)),
                ('projectname', models.CharField(db_column='ProjectName', max_length=255)),
                ('superusername', models.CharField(db_column='SuperUserName', max_length=255)),
                ('superuseremail', models.CharField(db_column='SuperUserEmail', max_length=255)),
                ('assessmenttype', models.CharField(blank=True, db_column='AssessmentType', max_length=50, null=True)),
                ('projectstartdate', models.DateField(db_column='ProjectStartDate')),
                ('projectenddate', models.DateField(db_column='ProjectEndDate')),
                ('status', models.CharField(db_column='Status', max_length=50)),
            ],
            options={
                'db_table': 'main_client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainQuestion',
            fields=[
                ('questionid', models.AutoField(db_column='QuestionID', primary_key=True, serialize=False)),
                ('clientname', models.CharField(db_column='ClientName', max_length=255)),
                ('projectname', models.CharField(db_column='ProjectName', max_length=255)),
                ('questiontext', models.CharField(db_column='QuestionText', max_length=255)),
                ('questiontype', models.CharField(db_column='QuestionType', max_length=50)),
                ('competency', models.CharField(db_column='Competency', max_length=50)),
                ('status', models.CharField(db_column='Status', max_length=50)),
            ],
            options={
                'db_table': 'main_question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainUser',
            fields=[
                ('userid', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('clientname', models.CharField(db_column='ClientName', max_length=255)),
                ('projectname', models.CharField(db_column='ProjectName', max_length=255)),
                ('seekername', models.CharField(db_column='SeekerName', max_length=255)),
                ('seekeremail', models.CharField(db_column='SeekerEmail', max_length=255)),
                ('providername', models.CharField(db_column='ProviderName', max_length=255)),
                ('provideremail', models.CharField(db_column='ProviderEmail', max_length=255)),
                ('relationship', models.CharField(db_column='Relationship', max_length=50)),
                ('status', models.CharField(db_column='Status', max_length=50)),
            ],
            options={
                'db_table': 'main_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OpenQuestionView',
            fields=[
                ('cp_id', models.IntegerField(db_column='ClientID', primary_key=True, serialize=False)),
                ('client_name', models.CharField(db_column='ClientName', max_length=255)),
                ('project_name', models.CharField(db_column='ProjectName', max_length=255)),
                ('seeker_name', models.CharField(db_column='SeekerName', max_length=255)),
                ('seeker_email', models.EmailField(db_column='SeekerEmail', max_length=254)),
                ('provider_email', models.EmailField(db_column='ProviderEmail', max_length=254)),
                ('relationship', models.CharField(db_column='Relationship', max_length=255)),
                ('question_text', models.TextField(db_column='QuestionText')),
                ('feedback_text', models.TextField(db_column='FeedbackText')),
            ],
            options={
                'db_table': 'open_question_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OptimumMinimumCriteriaView',
            fields=[
                ('cp_id', models.IntegerField(db_column='ClientID', primary_key=True, serialize=False)),
                ('seeker_id', models.IntegerField(db_column='SeekerID')),
                ('seeker_name', models.CharField(db_column='SeekerName', max_length=255)),
                ('seeker_email', models.EmailField(db_column='SeekerEmail', max_length=254)),
                ('optimum_criteria', models.CharField(db_column='Optimum_Criteria', max_length=255)),
                ('minimum_criteria', models.CharField(db_column='Minimum_Criteria', max_length=255)),
            ],
            options={
                'db_table': 'optimum_minimum_criteria_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('provider_id', models.AutoField(db_column='ProviderID', primary_key=True, serialize=False)),
                ('provider_first_name', models.CharField(db_column='FirstName', max_length=100)),
                ('provider_last_name', models.CharField(blank=True, db_column='LastName', max_length=100, null=True)),
                ('provider_email', models.CharField(db_column='Email', max_length=255)),
            ],
            options={
                'db_table': 'provider',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.IntegerField(db_column='QuestionID', primary_key=True, serialize=False)),
                ('question_text', models.CharField(blank=True, db_column='QuestionText', max_length=500, null=True)),
                ('question_type', models.CharField(blank=True, db_column='QuestionType', max_length=50, null=True)),
                ('competency', models.CharField(blank=True, db_column='Competency', max_length=100, null=True)),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelationshipView',
            fields=[
                ('seeker_id', models.IntegerField(db_column='SeekerID', primary_key=True, serialize=False)),
                ('provider_id', models.IntegerField(db_column='ProviderID')),
                ('cp', models.IntegerField(db_column='ClientID')),
                ('relationship', models.CharField(db_column='Relationship', max_length=50)),
            ],
            options={
                'db_table': 'relationship_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('seeker_id', models.AutoField(db_column='SeekerID', primary_key=True, serialize=False)),
                ('seeker_first_name', models.CharField(db_column='FirstName', max_length=100)),
                ('seeker_last_name', models.CharField(blank=True, db_column='LastName', max_length=100, null=True)),
                ('seeker_email', models.CharField(db_column='Email', max_length=255)),
            ],
            options={
                'db_table': 'seeker',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UniqueSeekerProviderView',
            fields=[
                ('cp_id', models.IntegerField(db_column='ClientID', primary_key=True, serialize=False)),
                ('provider_id', models.IntegerField(db_column='ProviderID')),
                ('seeker_id', models.IntegerField(db_column='SeekerID')),
                ('relationship', models.CharField(db_column='Relationship', max_length=255)),
            ],
            options={
                'db_table': 'unique_seeker_provider_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserDateView',
            fields=[
                ('cp_id', models.IntegerField(db_column='ClientID', primary_key=True, serialize=False)),
                ('client_name', models.CharField(db_column='ClientName', max_length=255)),
                ('project_name', models.CharField(db_column='ProjectName', max_length=255)),
                ('project_start_date', models.DateField(db_column='ProjectStartDate')),
                ('project_end_date', models.DateField(db_column='ProjectEndDate')),
            ],
            options={
                'db_table': 'user_date_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserProviderView',
            fields=[
                ('cp_id', models.IntegerField(db_column='ClientID', primary_key=True, serialize=False)),
                ('provider_id', models.IntegerField(db_column='ProviderID')),
                ('seeker_id', models.IntegerField(db_column='SeekerID')),
                ('provider_name', models.CharField(db_column='ProviderName', max_length=255)),
                ('provider_email', models.EmailField(db_column='ProviderEmail', max_length=254)),
                ('relationship', models.CharField(db_column='Relationship', max_length=255)),
                ('status', models.CharField(db_column='Status', max_length=50)),
            ],
            options={
                'db_table': 'user_provider_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserSeekerView',
            fields=[
                ('cp_id', models.IntegerField(db_column='ClientID', primary_key=True, serialize=False)),
                ('provider_id', models.IntegerField(db_column='ProviderID')),
                ('seeker_id', models.IntegerField(db_column='SeekerID')),
                ('seeker_name', models.CharField(db_column='SeekerName', max_length=255)),
                ('seeker_email', models.EmailField(db_column='SeekerEmail', max_length=254)),
                ('relationship', models.CharField(db_column='Relationship', max_length=255)),
                ('status', models.CharField(db_column='Status', max_length=50)),
                ('user_id', models.IntegerField(db_column='UserID')),
            ],
            options={
                'db_table': 'user_seeker_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FeedbackUI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp', models.IntegerField(db_column='ClientID')),
                ('seeker_id', models.IntegerField(db_column='SeekerID')),
                ('provider_id', models.IntegerField(db_column='ProviderID')),
                ('question_id', models.IntegerField(db_column='QuestionID')),
                ('feedback_value', models.CharField(blank=True, db_column='FeedbackValue', max_length=5, null=True)),
                ('feedback_text', models.CharField(blank=True, db_column='FeedbackText', max_length=1000, null=True)),
                ('feedback_status', models.CharField(blank=True, db_column='FeedbackStatus', max_length=10, null=True)),
            ],
            options={
                'db_table': 'feedback_ui',
            },
        ),
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('cp', models.OneToOneField(db_column='ClientID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='App_Admin.clientproject')),
                ('super_user_first_name', models.CharField(db_column='SuperUserFirstName', max_length=100)),
                ('super_user_last_name', models.CharField(blank=True, db_column='SuperUserLastName', max_length=100, null=True)),
                ('super_user_email', models.CharField(db_column='SuperUserEmail', max_length=255)),
            ],
            options={
                'db_table': 'client_superuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProviderURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(db_column='ClientName', max_length=255)),
                ('project_name', models.CharField(db_column='ProjectName', max_length=255)),
                ('provider_id', models.IntegerField(db_column='ProviderID')),
                ('provider_name', models.CharField(db_column='ProviderName', max_length=255)),
                ('provider_email', models.EmailField(db_column='ProviderEmail', max_length=254)),
                ('provi_url', models.URLField(db_column='ProviderURL')),
                ('unique_id', models.UUIDField(db_column='UniqueID', default=uuid.uuid4, editable=False, unique=True)),
                ('cp', models.ForeignKey(db_column='ClientID', on_delete=django.db.models.deletion.CASCADE, to='App_Admin.clientproject')),
            ],
            options={
                'db_table': 'provider_url',
            },
        ),
        migrations.CreateModel(
            name='SuperUserURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(db_column='ClientName', max_length=255)),
                ('project_name', models.CharField(db_column='ProjectName', max_length=255)),
                ('superuser_name', models.CharField(db_column='SuperUserName', max_length=255)),
                ('superuser_email', models.EmailField(db_column='SuperUserEmail', max_length=254)),
                ('super_url', models.URLField(db_column='SuperUserURL')),
                ('unique_id', models.UUIDField(db_column='UniqueID', default=uuid.uuid4, editable=False, unique=True)),
                ('cp', models.ForeignKey(db_column='ClientID', on_delete=django.db.models.deletion.CASCADE, to='App_Admin.clientproject')),
            ],
            options={
                'db_table': 'superuser_url',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('cp', models.OneToOneField(db_column='ClientID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='App_Admin.clientproject')),
                ('feedback_value', models.IntegerField(blank=True, db_column='FeedbackValue', null=True)),
                ('feedback_text', models.CharField(blank=True, db_column='FeedbackText', max_length=1000, null=True)),
                ('feedback_status', models.CharField(blank=True, db_column='FeedbackStatus', max_length=10, null=True)),
                ('provider_id', models.ForeignKey(db_column='ProviderID', on_delete=django.db.models.deletion.DO_NOTHING, to='App_Admin.provider')),
                ('question_id', models.ForeignKey(db_column='QuestionID', on_delete=django.db.models.deletion.DO_NOTHING, to='App_Admin.question')),
                ('seeker_id', models.ForeignKey(db_column='SeekerID', on_delete=django.db.models.deletion.DO_NOTHING, to='App_Admin.seeker')),
            ],
            options={
                'db_table': 'feedback',
                'unique_together': {('cp', 'seeker_id', 'provider_id', 'question_id')},
            },
        ),
    ]
