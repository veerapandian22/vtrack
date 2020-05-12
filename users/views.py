import csv, io
import pandas as pd
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from users.models import UserProfile
from django.contrib.auth.models import Group
from plants.models import Plant
from plants.models import GroupWisePlant

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    request.session['users_count'] = User.objects.all().count()
    request.session['online'] = User.objects.filter(is_login=1).count()
    return render(request, 'index.html', {'count': request.session['users_count'],
                                          'online': request.session['online']})

@login_required
def user_logout(request):
    now = timezone.now()

    User.objects.filter(id=request.user.id).update(is_login=False)

    profile = UserProfile.objects.filter(id=request.session['userprofile_id'])

    for prof in profile:
        UserProfile.objects.filter(id=request.session['userprofile_id']).update(duration=now-prof.login_time)

    UserProfile.objects.filter(id=request.session['userprofile_id']).update(logout_time=now)

    logout(request)
    return redirect('login')

def index(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('pwd'))
        if user:
            auth_login(request, user)
            User.objects.filter(id=request.user.id).update(is_login=True)
            request.session['users_count'] = User.objects.all().count()
            request.session['online'] = User.objects.filter(is_login=1).count()

            userprofile = UserProfile.objects.create(user_id=request.user.id,
                                                     login_time=timezone.now())
            request.session['userprofile_id'] = userprofile.id

            return render(request, 'index.html', {'count': request.session['users_count'],
                                                  'online': request.session['online']})
        else:
            return render(request, 'login.html', {'message': 'Credentials incorrect'})
    else:
        return render(request, 'index.html')

@login_required
def list_user(request: any):
    users = User.objects.exclude(id=request.user.id).select_related('role')
    return render(request, 'users/list_user.html', {"users": users})

def add_user(request):
    if request.method == 'POST':
        user = User.objects.create(password=make_password(request.POST.get("pwd")),
                                   is_superuser=0,
                                   username=request.POST.get("required"),
                                   first_name=request.POST.get("fname"),
                                   last_name=request.POST.get("lname"),
                                   email=request.POST.get("email"),
                                   is_staff=1,
                                   is_active=request.POST.get("user_status"),
                                   pwd=request.POST.get("pwd"),
                                   role_id=request.POST.get('group'))
        if user:
            return redirect('list_user')
        else:
            return render(request, 'users/add_user.html', {'message': 'Something went wrong'})
    else:
        groups = Group.objects.all()
        return render(request, 'users/add_user.html', {"groups": groups})

def view_user(request):
    user = User.objects.get(id=request.GET.get('id'))
    return render(request, 'users/view_user.html', {"user": user})

def edit_user(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST.get('user_id'))
        user.username = request.POST.get('username')
        user.email = request.POST.get('user_email')
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.password = make_password(request.POST.get('password'))
        user.pwd = request.POST.get('password')
        user.is_active = 1 if request.POST.get('user_status') == "1" else 0
        user.role_id = request.POST.get('group')
        user.save()
        users = User.objects.all()
        return render(request, 'users/list_user.html', {"users": users, 'message': 'Successfully user modified'})
    else:
        user = User.objects.get(id=request.GET.get('id'))
        groups = Group.objects.all()
        return render(request, 'users/edit_user.html', {"user": user, "groups": groups})

def bulk_import(request):
    if request.method == 'POST':
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            password = get_random_string(length=16)
            User.objects.create(password=make_password(password),
                                pwd=password,
                                is_superuser=row['is_superuser'],
                                username=row['username'],
                                first_name=row['first_name'],
                                last_name=row['last_name'],
                                email=row['email'],
                                is_staff=1,
                                is_active=row['is_active'])
        return render(request, 'users/bulk_import.html', {'message': 'Successfully CSV imported'})
    else:
        return render(request, 'users/bulk_import.html')

def export_users_as_csv(request):
    users = User.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users_list.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Email Address', 'First Name', 'Last Name',
                     'User Status', 'User Level', 'Date Joined', 'Last Login'])
    for user in users:
        is_active = 'Active' if user.is_active else 'In-Active'
        is_superuser = 'Super User' if user.is_superuser else 'User'

        writer.writerow([user.username, user.email, user.first_name, user.last_name,
                         is_active, is_superuser, user.date_joined, user.last_login])
    return response

def del_user(request):
    User.objects.filter(id=request.GET.get('id')).delete()
    users = User.objects.all()
    return render(request, 'users/list_user.html', {"users": users, 'message': 'Successfully user deleted'})

def bulk_template(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bulk_import.csv"'

    writer = csv.writer(response)
    writer.writerow(['username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser'])
    return response

def list_roles(request):
    groups = Group.objects.all()
    return render(request, 'users/list_roles.html', {"groups": groups})

def role(request):
    if request.method == 'POST':
        group = Group.objects.create(name=request.POST.get('role'), description=request.POST.get('desc'), is_active=1)
        group.save()
        for check in request.POST.getlist('checks[]'):
            group_plant = GroupWisePlant(is_active=1, group_id=group.id, plant_id=check)
            group_plant.save()
        return redirect("/list_roles/")
    else:
        plants = Plant.objects.all()
        return render(request, 'users/role.html', {"plants": plants})

def statics(request):
    profiles = UserProfile.objects.select_related('user')
    return render(request, 'users/statics.html', {"profiles": profiles})
