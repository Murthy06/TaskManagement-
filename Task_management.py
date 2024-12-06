Google Authentication Settings (settings.py)


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'your-google-client-id',
            'secret': 'your-google-client-secret',
            'key': ''
        }
    }
}

#task model

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


#task views

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "description"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "description"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")


#task urls

from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("add/", views.TaskCreateView.as_view(), name="task_add"),
    path("<int:pk>/edit/", views.TaskUpdateView.as_view(), name="task_edit"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task_delete"),
]


#Google OAuth Key Model (tasks/models.py)

class OAuthKey(models.Model):
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)

    def __str__(self):
        return self.client_id

#Admin Panel (tasks/admin.py)
from django.contrib import admin
from .models import Task, OAuthKey

admin.site.register(Task)
admin.site.register(OAuthKey)


#Send Invitation Email (tasks/utils.py)
from django.core.mail import send_mail

def send_invitation(email, link):
    subject = "You're Invited!"
    message = f"Click the link to join: {link}"
    send_mail(subject, message, 'admin@example.com', [email])

