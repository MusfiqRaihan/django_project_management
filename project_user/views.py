from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, Http404
from project_details.models import ProjectDetail
from project_user.forms import RegisterClient, RegisterStaff
from django.contrib.auth.models import Group


def user_login(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            return redirect('admin-index')
        elif user.groups.filter(name='staff').exists():
            return redirect('staff-index')
        elif user.groups.filter(name='client').exists():
            return redirect('client-index')

    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter(name='admin').exists():
                    return redirect('admin-index')
                elif user.groups.filter(name='staff').exists():
                    return redirect('staff-index')
                elif user.groups.filter(name='client').exists():
                    return redirect('client-index')


            messages.add_message(request, messages.ERROR, 'Username Or Password Mismatch!')
            return redirect('user-login')

        return render(request, 'login.html')


def admin_index(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            project_detail = ProjectDetail.objects.filter(profile_name=user.id).order_by('-created_on')
            context = {
                "username": user,
                "add_project": project_detail,
            }
            return render(request, 'admin/profile/index.html', context)
        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def staff_index(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='staff').exists():
            project_detail = ProjectDetail.objects.filter(profile_name=user.id).order_by('-created_on')
            context = {
                "username": user,
                "add_project": project_detail,
            }
            return render(request, 'staff/profile/index.html', context)
        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')




def client_index(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='client').exists():
            project_detail = ProjectDetail.objects.filter(profile_name=user.id).order_by('-created_on')
            context = {
                "username": user,
                "add_project": project_detail,
            }
            return render(request, 'client/profile/index.html', context)
        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')




def add_staff(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            user = get_object_or_404(User, id=request.user.id)
            form = RegisterStaff(request.POST or None)
            if form.is_valid():
                staff = form.save(commit=False)
                staff.save()
                group = Group.objects.get(name='staff')
                staff.groups.add(group)
                messages.success(request, "Registration Successfully Completed")
                return redirect('all-staff-list')
            else:
                return render(request, 'admin/profile/staff_register.html', {"form": form, "username": user})
        else:
            raise Http404
    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')



def all_staff_lists(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            get_staff = Group.objects.get(name="staff").user_set.all()
            context = {
                "staff": get_staff,
                "username": user,
            }
            return render(request, 'admin/profile/all_staff.html', context)
        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')



def all_client_lists(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            get_client = Group.objects.get(name="client").user_set.all()
            context = {
                "client": get_client,
                "username": user,
            }
            return render(request, 'admin/profile/all_clients.html', context)
        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')



def add_client(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='client').exists():
            form = RegisterClient(request.POST or None)
            if form.is_valid():
                staff = form.save(commit=False)
                staff.save()
                group = Group.objects.get(name='client')
                staff.groups.add(group)
                messages.success(request, "Registration Successfully Completed")
                return redirect('user-login')
            else:
                return render(request, 'add_client.html', {"form": form})
        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')




def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Successfully Logged Out!')
    return redirect('/')

