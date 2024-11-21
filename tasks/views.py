from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from django.contrib.admin.views.decorators import staff_member_required


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        Task.objects.create(user=request.user, title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description', '')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/edit_task.html', {'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})

# Restrict view to only admin users
@login_required
@user_passes_test(lambda u: u.is_superuser)  # Allow only superusers
def admin_dashboard(request):
    users = User.objects.all()  # Get all users
    return render(request, 'tasks/admin_dashboard.html', {'users': users})

@login_required
@user_passes_test(lambda u: u.is_superuser)  # Allow only superusers
def send_invitation(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Send an invitation email
        subject = 'You are invited to join the Task Manager'
        message = 'Please click the link below to register On Task Manager:\nhttp://127.0.0.1:8000/'
        from_email = settings.EMAIL_HOST_USER

        try:
            send_mail(subject, message, from_email, [email])
            messages.success(request, f"Invitation sent to {email}!")
        except Exception as e:
            messages.error(request, f"Error sending email: {str(e)}")
        
        return redirect('admin_dashboard')
    
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Explicitly set the backend before calling login
            user.backend = 'django.contrib.auth.backends.ModelBackend'

            login(request, user)  # Log the user in after successful signup
            return redirect('task_list')  # Redirect to task list or home page
        else:
            return render(request, 'registration/signup.html', {'form': form})  # Pass the form with errors
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def custom_logout_view(request):
    return render(request, 'registration/logout_confirm.html')
    

def logout_view(request):
    auth_logout(request)
    return redirect('login') 

@staff_member_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, f"User {user.username} has been deleted.")
    return redirect('admin_dashboard')