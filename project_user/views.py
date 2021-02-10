from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, Http404
from project_details.models import ProjectDetail
from project_user.forms import RegisterClientForm, RegisterStaffForm, EditStaffProfileForm, EditStaffPasswordForm, \
    ProfileInfoForm, EditClientProfileForm, EditClientPasswordForm
from django.contrib.auth.models import Group
from .models import Profile


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


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Successfully Logged Out!')
    return redirect('/')


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


# staff part start
def add_staff(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            user = get_object_or_404(User, id=request.user.id)
            form = RegisterStaffForm(request.POST or None)
            if form.is_valid():
                staff = form.save(commit=False)
                staff.save()
                group = Group.objects.get(name='staff')
                staff.groups.add(group)
                messages.success(request, "Registration Successfully Completed")
                return redirect('all-staff')
            else:
                return render(request, 'admin/profile/staff/add_staff.html', {"form": form, "username": user})
        else:
            raise Http404
    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def all_staffs(request):
    if request.user.is_authenticated:
        username = get_object_or_404(User, id=request.user.id)
        if username.groups.filter(name='admin').exists():
            get_user = Group.objects.get(name="staff").user_set.all()

            user_list = []
            for userid in get_user:
                get_staff = Profile.objects.get(user=userid)
                user_list.append(get_staff)

            context = {
                "staff": user_list,
                "username": username,
            }
            return render(request, 'admin/profile/staff/all_staff.html', context)
        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def edit_staff_profile(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            staff = get_object_or_404(User, id=pid)
            form = EditStaffProfileForm(request.POST or None, instance=staff)
            if form.is_valid():
                staff = form.save(commit=False)
                staff.save()
                messages.success(request, "Successfully Updated")
                return redirect('all-staff')
            else:
                return render(request, 'admin/profile/staff/edit_staff_profile.html', {"form": form, "username": user})
        else:
            raise Http404
    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def edit_staff_password(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            staff = get_object_or_404(User, id=pid)
            form = EditStaffPasswordForm(request.POST or None, instance=staff)
            if form.is_valid():
                staff = form.save(commit=False)
                staff.save()
                messages.success(request, "Successfully Updated")
                return redirect('all-staff')
            else:
                return render(request, 'admin/profile/staff/edit_staff_password.html', {"form": form, "username": user})
        else:
            raise Http404
    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def staff_additional_profile_info(request, pid):
    if request.user.is_authenticated:
        username = get_object_or_404(User, id=request.user.id)
        if username.groups.filter(name='admin').exists():
            get_profile = Profile.objects.get(id=pid)
            form = ProfileInfoForm(request.POST or None, instance=get_profile)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, "Successfully Updated")
                return redirect('all-staff')
            else:
                return render(request, 'admin/profile/add_additional_profile.html',
                              {"form": form, "username": username})
        else:
            return Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def delete_staff(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            staff = get_object_or_404(User, id=pid)
            staff.delete()
            return redirect('all-staff')

        else:
            raise Http404
    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


# client part start
def client_add(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            user = get_object_or_404(User, id=request.user.id)
            form = RegisterClientForm(request.POST or None)
            if form.is_valid():
                client = form.save(commit=False)
                client.save()
                group = Group.objects.get(name='client')
                client.groups.add(group)
                messages.success(request, "Registration Successfully Completed")
                return redirect('all-client')
            else:
                return render(request, 'admin/profile/client/add_client.html', {"form": form, "username": user})
        else:
            raise Http404
    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def all_clients(request):
    if request.user.is_authenticated:
        username = get_object_or_404(User, id=request.user.id)
        if username.groups.filter(name='admin').exists():
            get_user = Group.objects.get(name="client").user_set.all()

            user_list = []
            for userid in get_user:
                get_client = Profile.objects.get(user=userid)
                user_list.append(get_client)

            context = {
                "client": user_list,
                "username": username,
            }
            return render(request, 'admin/profile/client/all_clients.html', context)
        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def edit_client_profile(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            client = get_object_or_404(User, id=pid)
            form = EditClientProfileForm(request.POST or None, instance=client)
            if form.is_valid():
                client = form.save(commit=False)
                client.save()
                messages.success(request, "Successfully Updated")
                return redirect('all-client')
            else:
                return render(request, 'admin/profile/client/edit_client_profile.html',
                              {"form": form, "username": user})
        else:
            raise Http404
    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def edit_client_password(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            client = get_object_or_404(User, id=pid)
            form = EditClientPasswordForm(request.POST or None, instance=client)
            if form.is_valid():
                client = form.save(commit=False)
                client.save()
                messages.success(request, "Successfully Updated")
                return redirect('all-client')
            else:
                return render(request, 'admin/profile/client/edit_client_password.html',
                              {"form": form, "username": user})
        else:
            raise Http404
    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def client_additional_profile_info(request, pid):
    if request.user.is_authenticated:
        username = get_object_or_404(User, id=request.user.id)
        if username.groups.filter(name='admin').exists():
            get_profile = Profile.objects.get(id=pid)
            form = ProfileInfoForm(request.POST or None, instance=get_profile)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, "Successfully Updated")
                return redirect('all-client')
            else:
                return render(request, 'admin/profile/add_additional_profile.html',
                              {"form": form, "username": username})
        else:
            return Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def delete_client(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            client = get_object_or_404(User, id=pid)
            client.delete()
            return redirect('all-client')

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
