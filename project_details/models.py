from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from project_admin.models import development_methodology, Development_Tool


class ProjectDetail(models.Model):
    profile_name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100, unique=True)
    company_phone = PhoneNumberField(null=False, blank=False, unique=True)
    company_address = models.TextField(max_length=200)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    completion_date = models.DateField(auto_now=False, auto_now_add=False)
    project_summary = models.TextField(max_length=1000)
    project_goal = models.TextField(max_length=1000)
    project_impact = models.TextField(max_length=1000)
    project_requirement = models.TextField(max_length=1000)
    development_methodology = models.ForeignKey(development_methodology, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title



class ProjectDevelopmentTool(models.Model):
    profile_name = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    fronted = models.CharField(max_length=100)
    backend = models.CharField(max_length=100)
    database = models.CharField(max_length=100)
    server_side = models.CharField(max_length=100)
    repository = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.project_name.title



class ProjectTeamMember(models.Model):
    profile_name = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    member_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.project_name.title



class ProjectFeaturePayment(models.Model):
    profile_name = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    feature = models.JSONField(default=None)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.project_name.title



class ProjectMonthlyPayment(models.Model):
    profile_name = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    monthly = models.JSONField(default=None)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.project_name.title




class ProjectServiceCharge(models.Model):
    profile_name = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    service = models.FloatField()
    total = models.FloatField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.project_name.title




class ClientProfile(models.Model):
    client_name = models.CharField(max_length=100)
    profile_name = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, unique=True, blank=True)
    password = models.CharField(max_length=100)
    client_phone = PhoneNumberField(blank=True, unique=True, max_length=14)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.client_name


class ToDoList(models.Model):
    project_name = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user.username


class Timeline_User(models.Model):
    project_name = models.CharField(max_length=50)
    profile_name = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, auto_now=False, auto_now_add=False, null=True)
    completion_date = models.DateField(blank=True, auto_now=False, auto_now_add=False, null=True)
    update_completion_date = models.DateField(blank=True, auto_now=False, auto_now_add=False, null=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.project_name


def save_timeline_by_user_update(sender, instance, created, **kwargs):
    if created:
        Timeline_User.objects.create(
            project_name=instance.title,
            profile_name=instance.profile_name,
            start_date=instance.start_date,
            completion_date=instance.completion_date,
        )
    else:
        time = Timeline_User.objects.get(project_name=instance.title, profile_name=instance.profile_name)
        com = time.completion_date
        Timeline_User.objects.create(
            project_name=instance.title,
            profile_name=instance.profile_name,
            start_date=instance.start_date,
            completion_date=com,
            update_completion_date=instance.completion_date,
        )


post_save.connect(save_timeline_by_user_update, sender=ProjectDetail)



class ProjectPaymentDone(models.Model):
    project_name = models.CharField(max_length=50)
    profile_name = models.CharField(max_length=50)
    budget = models.FloatField(blank=True, null=True)
    previous_payment = models.FloatField(blank=True, null=True, default=0.0)
    due = models.FloatField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.project_name


def save_payment_done_update(sender, instance, created, **kwargs):
    if created:
        ProjectPaymentDone.objects.create(
            project_name=instance.project_name.title,
            profile_name=instance.profile_name,
            budget=instance.total,
        )
    else:
        pass


post_save.connect(save_payment_done_update, sender=ProjectServiceCharge)
