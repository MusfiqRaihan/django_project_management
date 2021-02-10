from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from project_admin.forms import AddDevelopersForm, AddDevelopmentToolsForm, AddDevelopmentMethodForm, AddPaymentTypeForm
from project_admin.models import Development_Member, Development_Tool, development_methodology, Payment_type


def add_developers(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            try:
                developers = Development_Member.objects.all().order_by('-created_on')
                form = AddDevelopersForm(request.POST or None)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.save()
                    messages.success(request, "Add Successfully")
                    return redirect('add-developers')

                context = {
                    "username": user,
                    "form": form,
                    "developers": developers,
                }
                return render(request, 'admin/profile/addition/all_developers.html', context)

            except:
                raise Http404

        else:
            return Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def delete_developers(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            try:
                developers = Development_Member.objects.get(id=pid)
                developers.delete()
                return redirect('add-developers')
            
            except:
                raise Http404

        else:
            return Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def add_development_tools(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            try:
                tools = Development_Tool.objects.all().order_by('-created_on')
                form = AddDevelopmentToolsForm(request.POST or None)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.save()
                    messages.success(request, "Add Successfully")
                    return redirect('add-development-tools')

                context = {
                    "username": user,
                    "form": form,
                    "tools": tools,
                }
                return render(request, 'admin/profile/addition/all_development_tools.html', context)

            except:
                raise Http404

        else:
            return Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def delete_development_tools(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            try:
                teams = Development_Tool.objects.get(id=pid)
                teams.delete()
                return redirect('add-development-tools')

            except:
                raise Http404

        else:
            return Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')


def add_development_method(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            try:
                methods = development_methodology.objects.all().order_by('-created_on')
                form = AddDevelopmentMethodForm(request.POST or None)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.save()
                    messages.success(request, "Add Successfully")
                    return redirect('add-development-method')

                context = {
                    "username": user,
                    "form": form,
                    "methods": methods,
                }
                return render(request, 'admin/profile/addition/development_methodoly.html', context)

            except:
                raise Http404

        else:
            return Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')



def delete_development_method(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            try:
                methods = development_methodology.objects.get(id=pid)
                methods.delete()
                return redirect('add-development-method')

            except:
                raise Http404

        else:
            return Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')




def add_payment_types(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            try:
                payment = Payment_type.objects.all().order_by('-created_on')
                form = AddPaymentTypeForm(request.POST or None)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.save()
                    messages.success(request, "Add Successfully")
                    return redirect('add-payment-types')

                context = {
                    "username": user,
                    "form": form,
                    "payment": payment,
                }
                return render(request, 'admin/profile/addition/payment_types.html', context)

            except:
                raise Http404

        else:
            return Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')



def delete_payment_types(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            try:
                payment = Payment_type.objects.get(id=pid)
                payment.delete()
                return redirect('add-payment-types')

            except:
                raise Http404

        else:
            return Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('user-login')
