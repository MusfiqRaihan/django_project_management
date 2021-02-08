import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from project_admin.models import development_methodology, Development_Tool, Development_Member, Payment_type
from .models import ToDoList, ProjectDetail, ProjectDevelopmentTool, ProjectTeamMember, ProjectFeaturePayment, \
    ProjectServiceCharge, ClientProfile, Timeline_User, ProjectPaymentDone, ProjectMonthlyPayment
from .forms import CreateProjectDetailForm


def add_project_details(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name__in=['admin', 'staff']).exists():
            user = get_object_or_404(User, id=request.user.id)
            software_method = development_methodology.objects.all()
            form = CreateProjectDetailForm(request.POST or None)
            if request.method == "POST":
                form = CreateProjectDetailForm(request.POST or None)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.profile_name = user
                    instance.save()
                    return redirect('/add_project/development/tools/add/' + str(instance.id))
                return render(request, 'add_project/add_project_details.html', {"form": form})

            else:
                context = {
                    "username": user,
                    "method": software_method,
                    "form": form,
                }
                return render(request, 'add_project/add_project_details.html', context)

        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')



def add_development_tools(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name__in=['admin', 'staff']).exists():
            user = get_object_or_404(User, id=request.user.id)
            project = ProjectDetail.objects.get(id=pid)
            fronted_development_tool = Development_Tool.objects.filter(development_method='Frontend Framework')
            backend_development_tool = Development_Tool.objects.filter(development_method='Backend Framework')
            database_development_tool = Development_Tool.objects.filter(development_method='Database')
            server_development_tool = Development_Tool.objects.filter(development_method='Server-Side')
            repository_development_tool = Development_Tool.objects.filter(development_method='Repository')

            context = {
                "front": fronted_development_tool,
                "back": backend_development_tool,
                "data": database_development_tool,
                "server": server_development_tool,
                "repo": repository_development_tool,
                "username": user,
            }

            if request.method == "POST":
                front = request.POST['fronted']
                back = request.POST['backend']
                database = request.POST['database']
                server = request.POST['server_side']
                repository = request.POST['repository']

                project_development_tool = ProjectDevelopmentTool.objects.create(
                    profile_name=user,
                    project_name=project,
                    fronted=front,
                    backend=back,
                    database=database,
                    server_side=server,
                    repository=repository,
                )
                project_development_tool.save()
                return redirect('/add_project/role/management/' + str(project.id))

            return render(request, 'add_project/project_development_tools.html', context)

        else:
            raise Http404


    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')




def project_role(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name__in=['admin', 'staff']).exists():
            user = get_object_or_404(User, id=request.user.id)
            project = ProjectDetail.objects.get(id=pid)
            get_designation = Development_Member.objects.all()

            get_teams = ProjectTeamMember.objects.filter(project_name=project)

            context = {
                'designation': get_designation,
                'get_teams': get_teams,
                'add_project': project,
                'username': user,
            }

            if request.method == "POST":
                get_designation = request.POST['designation']
                get_name = request.POST['programmer_name']

                teams = ProjectTeamMember.objects.create(
                    profile_name=user,
                    project_name=project,
                    designation=get_designation,
                    member_name=get_name,
                )
                teams.save()
                return redirect('/add_project/role/management/' + str(project.id))

            return render(request, 'add_project/role_management.html', context)

        else:
            raise Http404



    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')




def get_designation_id(request, name):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name__in=['admin', 'staff']).exists():
            get_name = Development_Member.objects.get(position=name)
            key = get_name.position
            value = get_name.name
            json_object = {
                key: value
            }
            return JsonResponse(json_object)
        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')



def delete_project_team(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name__in=['admin', 'staff']).exists():
            team = ProjectTeamMember.objects.get(id=pid)
            project = team.project_name
            team.delete()
            return redirect('/add_project/role/management/' + str(project.id))

        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')



def get_payment(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name__in=['admin', 'staff']).exists():
            user = get_object_or_404(User, id=request.user.id)
            project = ProjectDetail.objects.get(id=pid)
            payment_type = Payment_type.objects.all()
            teams = Development_Member.objects.all()

            context = {
                'type': payment_type,
                'username': user,
                'teams': teams,
                'add_project': project,
            }

            return render(request, 'add_project/project_payment.html', context)
        else:
            raise Http404


    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')




def get_feature_payment(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name__in=['admin', 'staff']).exists():
            user = get_object_or_404(User, id=request.user.id)
            payment_type = Payment_type.objects.all()
            project = ProjectDetail.objects.get(id=pid)

            context = {
                'username': user,
                'type': payment_type,
                'add_project': project,
            }
            if request.method == "POST" and request.is_ajax():
                payment = request.POST
                print(payment['values'])

                features = ProjectFeaturePayment.objects.create(
                    profile_name=user,
                    project_name=project,
                    feature=json.loads(payment['values']),
                )
                features.save()

            return render(request, 'add_project/project_feature_payment.html', context)
        else:
            raise Http404


    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')





def get_monthly_payment(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name__in=['admin', 'staff']).exists():
            user = get_object_or_404(User, id=request.user.id)
            payment_type = Payment_type.objects.all()
            project = ProjectDetail.objects.get(id=pid)
            get_designations = ProjectTeamMember.objects.filter(profile_name=user,
                                                                project_name=project)

            context = {
                'username': user,
                'type': payment_type,
                'add_project': project,
                'teams': get_designations,
            }

            if request.method == "POST" and request.is_ajax():
                payment = request.POST

                get_monthly = ProjectMonthlyPayment.objects.create(
                    profile_name=user,
                    project_name=project,
                    monthly=json.loads(payment['values']),
                )
                get_monthly.save()

            return render(request, 'add_project/project_monthly_payment.html', context)
        else:
            raise Http404


    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')





def get_service_charge(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name__in=['admin', 'staff']).exists():
            user = get_object_or_404(User, id=request.user.id)
            project = ProjectDetail.objects.get(id=pid)

            context = {
                'username': user,
                'add_project': project,
            }
            if request.method == "POST":
                service = request.POST['service']

                services = ProjectServiceCharge.objects.create(
                    profile_name=user,
                    project_name=project,
                    service=service,
                )
                services.save()
                return redirect('/add_project/details/overview/' + str(project.id))

            return render(request, 'add_project/project_service_charge.html', context)
        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')



def delete_project(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            project = ProjectDetail.objects.get(id=pid, profile_name=user)
            project.delete()
            project_detail = ProjectDetail.objects.filter(profile_name=user.id).order_by('-created_on')
            context = {
                "add_project": project_detail,
            }
            return render(request, 'admin/profile/index.html', context)

        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')




def project_details_overview(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name='admin').exists():
            try:
                user = get_object_or_404(User, id=request.user.id)
                project = ProjectDetail.objects.get(id=pid, profile_name=user)
                project_dev = ProjectDevelopmentTool.objects.get(project_name=pid)
                project_team = ProjectTeamMember.objects.filter(project_name=pid)
                service = ProjectServiceCharge.objects.get(project_name=pid)
                features_payment = ProjectFeaturePayment.objects.filter(project_name=pid)

                context = {
                    'username': user,
                    'add_project': project,
                    'project_dev': project_dev,
                    'project_team': project_team,
                    'service': service,
                    'features': features_payment,
                }

                return render(request, 'project_details/project_details.html', context)


            except:
                raise Http404

        elif user.groups.filter(name='staff').exists():
            try:
                user = get_object_or_404(User, id=request.user.id)

                project = ProjectDetail.objects.get(id=pid, profile_name=user)

                project_dev = ProjectDevelopmentTool.objects.get(project_name=pid)
                project_team = ProjectTeamMember.objects.filter(project_name=pid)
                service = ProjectServiceCharge.objects.get(project_name=pid)
                features_payment = ProjectFeaturePayment.objects.filter(project_name=pid)

                context = {
                    'username': user,
                    'add_project': project,
                    'project_dev': project_dev,
                    'project_team': project_team,
                    'service': service,
                    'features': features_payment,
                }

                return render(request, 'project_details/project_details.html', context)

            except:
                raise Http404

        else:
            raise Http404



    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')


# do from here



def project_team_details(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        if user.groups.filter(name__in=['admin', 'staff']).exists():
            try:
                user = get_object_or_404(User, id=request.user.id)
                project = ProjectDetail.objects.get(id=pid, profile_name=user)

                context = {
                    "username": user,
                    "add_project": project,
                    "teams": ProjectTeamMember.objects.filter(project_name=project, profile_name=user).order_by(
                        '-created_on'),
                }
                return render(request, 'project_details/team.html', context)

            except:
                raise Http404

        else:
            raise Http404

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')




def project_todo_list(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        project = ProjectDetail.objects.get(id=pid)

        if request.method == "POST":
            get_todolist = request.POST['todolist']

            todolist = ToDoList.objects.create(
                project_name=project,
                user=user,
                todo=get_todolist
            )
            todolist.save()
            context = {
                "username": user,
                "add_project": project,
                "id": pid,
                "todolist": ToDoList.objects.filter(project_name=project, user=user).order_by('-created_on'),
            }
            return render(request, 'staff/project_details/todo.html', context)

        else:
            context = {
                "username": user,
                "add_project": project,
                "id": pid,
                "todolist": ToDoList.objects.filter(project_name=project, user=user).order_by('-created_on'),
            }
            return render(request, 'staff/project_details/todo.html', context)

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')


def delete_todo_list(request, pid):
    if request.user.is_authenticated:
        todo = get_object_or_404(ToDoList, id=pid)
        project = todo.project_name
        todo.delete()
        return redirect('/add_project/todo/lists/' + str(project.id))

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')


def project_timeline(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        project = ProjectDetail.objects.get(id=pid)
        timeline = Timeline_User.objects.filter(project_name=project, profile_name=user)

        context = {
            "username": user,
            "add_project": project,
            "timeline": timeline,
        }
        return render(request, 'staff/project_details/timeline.html', context)

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')


def project_feedback(request, pid):
    if request.user.is_authenticated:
        return render(request, 'staff/project_details/feedback.html')

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')


def project_payments(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        project = ProjectDetail.objects.get(id=pid)
        get_pay_info = ProjectPaymentDone.objects.get(project_name=project,
                                                      profile_name=user)

        if request.method == "POST":
            get_new_payment = request.POST['new_payment']
            payment_done = ProjectPaymentDone.objects.get(project_name=project,
                                                          profile_name=user,
                                                          id=get_pay_info.id)

            payment_done.previous_payment += float(get_new_payment)
            payment_done.due = float(payment_done.budget) - float(payment_done.previous_payment)
            payment_done.save()


            context = {
                "username": user,
                "add_project": project,
                "payment": ProjectPaymentDone.objects.get(project_name=project,
                                                          profile_name=user)
            }
            return render(request, 'staff/project_details/payment.html', context)

        else:
            context = {
                "username": user,
                "add_project": project,
                "payment": ProjectPaymentDone.objects.get(project_name=project.title,
                                                          profile_name=user.username)
            }
            return render(request, 'staff/project_details/payment.html', context)

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')


def project_client_details(request, pid):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        project = ProjectDetail.objects.get(id=pid)

        if request.method == "POST":
            get_name = request.POST['name']
            get_phone = request.POST['phone']
            get_email = request.POST['email']
            get_password = request.POST['password']

            clients = ClientProfile.objects.create(
                project_name=project,
                profile_name=user,
                email=get_email,
                password=get_password,
                client_name=get_name,
                client_phone=get_phone,
            )
            clients.save()
            context = {
                "username": user,
                "add_project": project,
                "clients": ClientProfile.objects.filter(project_name=project, profile_name=user).order_by(
                    '-created_on'),
            }
            return render(request, 'staff/project_details/client.html', context)

        else:
            context = {
                "username": user,
                "add_project": project,
                "clients": ClientProfile.objects.filter(project_name=project, profile_name=user).order_by(
                    '-created_on'),
            }
            return render(request, 'staff/project_details/client.html', context)

    else:
        messages.add_message(request, messages.WARNING, 'Need to be login!')
        return redirect('/')