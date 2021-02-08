from django.db import models













# class Announcement(models.Model):
#     client_name = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
#     project_name = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
#     announce = models.TextField(max_length=150)
#     created_on = models.DateField(auto_now=False, auto_now_add=True)
#
#     def __str__(self):
#         return self.client_name.client_name
#
#
# class Feedback(models.Model):
#     client_name = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
#     project_name = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
#     feedback = models.TextField(max_length=150)
#     created_on = models.DateField(auto_now=False, auto_now_add=True)
#
#     def __str__(self):
#         return self.client_name.client_name
#
#
# class Discussion_forum(models.Model):
#     client_name = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
#     project_name = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
#     discuss = models.TextField(max_length=150)
#     created_on = models.DateField(auto_now=False, auto_now_add=True)
#
#     def __str__(self):
#         return self.client_name.client_name
