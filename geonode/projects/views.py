from django.shortcuts import get_object_or_404, render, redirect,\
    render_to_response
from django.utils import timezone

from models import Project
from forms import ProjectForm

# queries
order = Project.objects.all()
# .order_by('published_date')


def list_projects(request):

    projects = order

    if len(projects) == 0:
        code = 'NULL'
        return render(
            request,
            'projects/projects.html',
            {'projects': projects, 'code': code, })
    else:
        return render(
            request,
            'projects/projects.html',
            {'projects': projects})

    return render_to_response(
        "projects/projects.html",
        {"json": project_json})


def list_complete_projects(request):
    projects = order.filter(status='CP')
    if len(projects) == 0:
        code = 'NULL_COMPLETE'
        return render(
            request,
            'projects/projects.html',
            {'projects': projects, 'code': code, })
    else:
        return render(
            request,
            'projects/projects.html',
            {'projects': projects})


def list_ongoing_projects(request):
    projects = order.filter(status='ON')
    if len(projects) == 0:
        code = 'NULL_ONGOING'
        return render(
            request,
            'projects/projects.html',
            {'projects': projects, 'code': code, })
    else:
        return render(
            request,
            'projects/projects.html',
            {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(
        request,
        'projects/project.html',
        {'project': project})


def new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            # DO STH ELSE
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})


def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            # DO STH MORE
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_edit.html', {'form': form})
