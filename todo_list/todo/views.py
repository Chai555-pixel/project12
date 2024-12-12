# todo/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Task

# Home view
def home(request):
    return render(request, 'todo/home.html')  # Render the home template

# Task list view (class-based view)
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'  # The context variable for the task list
    template_name = 'todo/task_list.html'  # Template name (optional, defaults to 'todo_list/task_list.html')


# Task detail view
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'  # The context variable name in the template
    template_name = 'todo/task_detail.html'  # Optional, defaults to 'todo/task_detail.html'

# TaskCreate view to handle the creation of a new task
class TaskCreate(CreateView):
    model = Task  # The model for the view
    fields = ['title', 'description', 'completed']  # Fields to be shown in the form
    success_url = reverse_lazy('tasks')  # Where to redirect after a successful form submission

    # Customizing the form_valid method to associate the user with the task
    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the logged-in user
        messages.success(self.request, "The task was created successfully.")  # Flash message
        return super().form_valid(form)  # Proceed with form validation and save

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']  # Fields to display in the form
    success_url = reverse_lazy('tasks')  # Redirect to task list after successful update

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")  # Flash message on success
        return super().form_valid(form)
    
class TaskDelete(DeleteView):
    model = Task  # The model to delete (Task)
    context_object_name = 'task'  # Name of the object passed to the template
    success_url = reverse_lazy('tasks')  # Redirect to task list after deletion

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super().form_valid(form)