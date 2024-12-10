from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

class MyLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True  # Redirect authenticated users to a specified page

    def get_success_url(self):
        return reverse_lazy('tasks')  # Redirect to 'tasks' view after successful login

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')  # Display error message
        return self.render_to_response(self.get_context_data(form=form))


class MyLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have logged out successfully.")
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):  # Renaming from SignUpView to RegisterView
    form_class = UserCreationForm
    template_name = 'users/register.html'  # Use 'register.html' for the signup form
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()  # Save the new user
        login(self.request, user)  # Log the user in immediately after signup
        messages.success(self.request, "Your account has been created successfully!")
        return response
