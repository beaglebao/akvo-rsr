# -*- coding: utf-8 -*-

"""Akvo RSR is covered by the GNU Affero General Public License.

See more details in the license.txt file located at the root folder of the
Akvo RSR module. For additional details on the GNU license please
see < http://www.gnu.org/licenses/agpl.html >.
"""

from datetime import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render

from ..forms import (PasswordForm, ProfileForm, UserOrganisationForm, UserAvatarForm,
                     SelectOrgForm, IatiExportForm)
from ..filters import remove_empty_querydict_items
from ...utils import pagination, filter_query_string
from ..models import (Country, Employment, Organisation, OrganisationCustomField, Project,
                      ProjectEditorValidation, ProjectEditorValidationSet)

import json


@login_required
def my_rsr(request):
    """
    Redirect to the 'My Details' page in MyRSR, if the user is logged in.

    :param request; A Django request.
    """
    return HttpResponseRedirect(reverse('my_details', args=[]))


@login_required
def my_details(request):
    """
    If the user is logged in, he/she can change his user details and password here. In addition,
    the user can request to join an organisation.

    :param request; A Django request.
    """
    if request.method == "POST" and 'avatar' in request.FILES:
        request.FILES['avatar'].name = request.FILES['avatar'].name.encode('ascii', 'ignore')
        avatar_form = UserAvatarForm(request.POST, request.FILES, instance=request.user)
        if avatar_form.is_valid():
            avatar_form.save()
        return HttpResponseRedirect(reverse('my_details'))

    profile_form = ProfileForm(
        initial={
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        }
    )
    organisation_form = UserOrganisationForm()
    avatar_form = UserAvatarForm()

    json_data = json.dumps({'user': request.user.employments_dict([])})

    organisation_count = Organisation.objects.all().count()
    country_count = Country.objects.all().count()

    change_password_form = PasswordForm(request.user)

    context = {
        'organisation_count': organisation_count,
        'country_count': country_count,
        'user_data': json_data,
        'profileform': profile_form,
        'organisationform': organisation_form,
        'avatarform': avatar_form,
        'change_password_form': change_password_form,
    }

    return render(request, 'myrsr/my_details.html', context)


@login_required
def my_updates(request):
    """
    If the user is logged in, he/she can view a list of own updates.

    :param request; A Django request.
    """
    updates = request.user.updates().select_related('project')

    q = request.GET.get('q')
    if q:
        q_list = q.split()
        for q_item in q_list:
            updates = updates.filter(title__icontains=q_item)
    qs = remove_empty_querydict_items(request.GET)
    page = request.GET.get('page')
    page, paginator, page_range = pagination(page, updates, 10)

    context = {
        'page': page,
        'paginator': paginator,
        'page_range': page_range,
        'q': filter_query_string(qs),
        'q_search': q,
    }
    return render(request, 'myrsr/my_updates.html', context)


@login_required
def my_projects(request):
    """
    If the user is logged in, he/she can view a list of projects linked to the user account.

    :param request; A Django request.
    """

    # Get user organisation information
    organisations = request.user.approved_employments().organisations()
    creator_organisations = organisations.filter(can_create_projects=True).\
        values_list('id', flat=True)

    # Get project list
    if request.user.is_superuser or request.user.is_admin:
        projects = Project.objects.all()
    else:
        projects = organisations.all_projects().distinct()

    # Custom filter on project id or (sub)title
    q = request.GET.get('q')
    if q:
        try:
            project_pk = int(q)
            projects = projects.filter(pk=project_pk)
        except Project.DoesNotExist:
            Project.objects.none()
        except ValueError:
            q_list = q.split()
            for q_item in q_list:
                projects = projects.filter(title__icontains=q_item) | \
                    projects.filter(subtitle__icontains=q_item)

    # Pagination
    qs = remove_empty_querydict_items(request.GET)
    page = request.GET.get('page')
    page, paginator, page_range = pagination(page, projects, 10)

    # Get related objects of page at once
    page.object_list = page.object_list.select_related('validations').\
        prefetch_related('publishingstatus')

    # Add custom fields in case user adds a new project
    new_project_custom_fields = OrganisationCustomField.objects.filter(
        organisation__in=organisations
    )

    context = {
        'organisations': organisations,
        'new_project_custom_fields': new_project_custom_fields,
        'page': page,
        'paginator': paginator,
        'page_range': page_range,
        'q': filter_query_string(qs),
        'q_search': q,
        'reportable_organisations': creator_organisations
    }
    return render(request, 'myrsr/my_projects.html', context)


@login_required
def project_editor_select(request):
    """
    Project editor without a project selected. Only accessible to Admins, Project editors and
    M&E Managers.

    :param request; A Django HTTP request and context
    """
    user = request.user
    me_managers = Group.objects.get(name='M&E Managers')
    admins = Group.objects.get(name='Admins')
    project_editors = Group.objects.get(name='Project Editors')

    if not (user.is_admin or user.is_superuser or user.in_group(me_managers) or
            user.in_group(admins) or user.in_group(project_editors)):
        raise PermissionDenied

    projects = Project.objects.all() if user.is_admin or user.is_superuser else user.my_projects()

    context = {
        'user': user,
        'projects': projects,
    }

    return render(request, 'myrsr/select_project.html', context)


@login_required
def project_editor(request, project_id):
    """
    If the user is logged in and has sufficient permissions (Admins, M&E Managers and Project
    Editors), he/she can edit the selected project.

    :param request; A Django request.
    :param project_id; The selected project's ID.
    """
    try:
        project = Project.objects.prefetch_related(
            'related_projects',
            'related_projects__project',
            'contacts',
            'partnerships',
            'partnerships__organisation',
            'results',
            'results__indicators',
            'results__indicators__periods',
            'conditions',
            'budget_items',
            'budget_items__label',
            'country_budget_items',
            'transactions',
            'transactions__provider_organisation',
            'transactions__receiver_organisation',
            'transactions__sectors',
            'planned_disbursements',
            'locations',
            'locations__country',
            'locations__administratives',
            'recipient_countries',
            'recipient_regions',
            'sectors',
            'policy_markers',
            'links',
            'documents',
            'keywords',
        ).select_related(
            'publishingstatus__status',
            'primary_location',
            'primary_location__country'
        ).get(pk=project_id)
    except Project.DoesNotExist:
        return Http404

    if not request.user.has_perm('rsr.change_project', project):
        raise PermissionDenied

    # Custom fields
    custom_fields_section_1 = project.custom_fields.filter(section=1).order_by('order', 'id')
    custom_fields_section_2 = project.custom_fields.filter(section=2).order_by('order', 'id')
    custom_fields_section_3 = project.custom_fields.filter(section=3).order_by('order', 'id')
    custom_fields_section_4 = project.custom_fields.filter(section=4).order_by('order', 'id')
    custom_fields_section_5 = project.custom_fields.filter(section=5).order_by('order', 'id')
    custom_fields_section_6 = project.custom_fields.filter(section=6).order_by('order', 'id')
    custom_fields_section_7 = project.custom_fields.filter(section=7).order_by('order', 'id')
    custom_fields_section_8 = project.custom_fields.filter(section=8).order_by('order', 'id')
    custom_fields_section_9 = project.custom_fields.filter(section=9).order_by('order', 'id')
    custom_fields_section_10 = project.custom_fields.filter(section=10).order_by('order', 'id')

    # Validations / progress bars
    validations = ProjectEditorValidation.objects.select_related('validation_set')
    validation_sets = ProjectEditorValidationSet.objects.all()
    project_validation_sets = project.validations.all()

    # Countries
    countries = Country.objects.all()


    context = {
        'id': project_id,
        'project': project,
        'projectmodel': Project,
        'validations': validations,
        'validation_sets': validation_sets,
        'project_validation_sets': project_validation_sets,
        'countries': countries,

        # Custom fields
        'custom_fields_section_1': custom_fields_section_1,
        'custom_fields_section_2': custom_fields_section_2,
        'custom_fields_section_3': custom_fields_section_3,
        'custom_fields_section_4': custom_fields_section_4,
        'custom_fields_section_5': custom_fields_section_5,
        'custom_fields_section_6': custom_fields_section_6,
        'custom_fields_section_7': custom_fields_section_7,
        'custom_fields_section_8': custom_fields_section_8,
        'custom_fields_section_9': custom_fields_section_9,
        'custom_fields_section_10': custom_fields_section_10,
    }

    return render(request, 'myrsr/project_editor/project_editor.html', context)


@login_required
def my_iati(request):
    """
    If the user is logged in and has sufficient permissions (Admins, M&E Managers and Project
    Editors), he/she can view and create IATI files.

    :param request; A Django request.
    """
    user = request.user

    if not user.has_perm('rsr.project_management'):
        raise PermissionDenied

    org = request.GET.get('org')
    selected_org, iati_exports, export_added, project_count = None, None, False, 0

    select_org_form = SelectOrgForm(user)
    iati_export_form = None

    if not org and not (user.is_superuser or user.is_admin) \
            and user.approved_organisations().count() == 1:
        selected_org = user.approved_organisations()[0]

    elif org:
        try:
            selected_org = Organisation.objects.get(pk=int(org))
        except Organisation.DoesNotExist:
            raise PermissionDenied
        if not (user.is_superuser or user.is_admin) \
                and not user.has_perm('rsr.change_organisation', selected_org):
            raise PermissionDenied

    if selected_org:
        iati_exports = selected_org.iati_exports.all().order_by('-last_modified_at')
        projects = selected_org.reporting_on_projects().public()
        project_count = projects.count()
        initial = {
            'is_public': True,
            'projects': [p.pk for p in projects]
        }
        iati_export_form = IatiExportForm(initial=initial, org=selected_org)

    if request.method == 'POST':
        iati_export_form = IatiExportForm(selected_org, request.POST)
        if iati_export_form.is_valid():
            iati_export_form.save(reporting_organisation=selected_org, user=user)
            export_added = True

    context = {
        'select_org_form': select_org_form,
        'iati_export_form': iati_export_form,
        'selected_org': selected_org,
        'exports': iati_exports,
        'export_added': export_added,
        'project_count': project_count
    }

    return render(request, 'myrsr/my_iati.html', context)


@login_required
def my_reports(request):
    """
    If the user is logged in, he/she can create reports based on a project or organisation.

    :param request; A Django request.
    """
    return render(request, 'myrsr/my_reports.html', {})


@login_required
def user_management(request):
    """
    Show the user management page. It is possible to manage employments on this page, e.g. approve
    an employment or change the group of a certain employment. Also allows users to invite other
    users.

    :param request; a Django request.
    """
    user = request.user

    if not user.has_perm('rsr.user_management'):
        raise PermissionDenied

    if user.is_admin or user.is_superuser:
        # Superusers or RSR Admins can manage and invite someone for any organisation
        employments = Employment.objects.select_related().\
            prefetch_related('country', 'group').order_by('-id')
        organisations = Organisation.objects.all()
        roles = Group.objects.filter(
            name__in=['Users', 'User Managers', 'Project Editors', 'M&E Managers', 'Admins']
        )
    else:
        # Others can only manage or invite users to their own organisation, or the
        # organisations that they content own
        connected_orgs = user.employers.approved().organisations().content_owned_organisations()
        connected_orgs_list = [
            org.pk for org in connected_orgs if user.has_perm('rsr.user_management', org)
        ]
        organisations = Organisation.objects.filter(pk__in=connected_orgs_list)
        employments = organisations.employments().exclude(user=user).select_related().\
            prefetch_related('country', 'group').order_by('-id')
        roles = Group.objects.filter(name__in=['Users', 'Project Editors'])

    q = request.GET.get('q')
    if q:
        q_list = q.split()
        for q_item in q_list:
            employments = employments.filter(user__username__icontains=q_item) | \
                employments.filter(user__first_name__icontains=q_item) | \
                employments.filter(user__last_name__icontains=q_item) | \
                employments.filter(organisation__name__icontains=q_item) | \
                employments.filter(organisation__long_name__icontains=q_item)

    qs = remove_empty_querydict_items(request.GET)
    page = request.GET.get('page')
    page, paginator, page_range = pagination(page, employments, 10)

    all_groups = [
        Group.objects.get(name='Users'),
        Group.objects.get(name='User Managers'),
        Group.objects.get(name='Project Editors'),
        Group.objects.get(name='M&E Managers'),
        Group.objects.get(name='Admins')
    ]

    employments_array = []
    for employment in page:
        employment_dict = model_to_dict(employment)
        employment_dict['other_groups'] = [
            model_to_dict(group, fields=['id', 'name']) for group in all_groups
        ]
        if employment.country:
            country_dict = model_to_dict(employment.country, fields=['id', 'iso_code', 'name'])
            employment_dict["country"] = country_dict
        if employment.group:
            group_dict = model_to_dict(employment.group, fields=['id', 'name'])
            employment_dict["group"] = group_dict
        if employment.organisation:
            organisation_dict = model_to_dict(employment.organisation, fields=[
                'id', 'name', 'long_name'
            ])
            employment_dict["organisation"] = organisation_dict
        if employment.user:
            user_dict = model_to_dict(employment.user, fields=[
                'id', 'first_name', 'last_name', 'email'
            ])
            employment_dict["user"] = user_dict
        employments_array.append(employment_dict)

    organisations_list = []
    for organisation in organisations:
        organisation_dict = {'id': organisation.id, 'name': organisation.name}
        organisations_list.append(organisation_dict)

    roles_list = []
    for role in roles:
        roles_dict = {'id': role.id, 'name': role.name}
        roles_list.append(roles_dict)

    context = {}
    if employments_array:
        context['employments'] = json.dumps(employments_array)
    context['organisations'] = json.dumps(organisations_list)
    context['roles'] = json.dumps(roles_list)
    context['page'] = page
    context['paginator'] = paginator
    context['page_range'] = page_range
    if q:
        context['q_search'] = q
    context['q'] = filter_query_string(qs)

    return render(request, 'myrsr/user_management.html', context)


@login_required
def results_data_select(request):
    """
    My results section without a project selected. Only accessible to M&E Managers, Admins and
    Project editors.

    :param request; A Django HTTP request and context
    """
    user = request.user
    me_managers = Group.objects.get(name='M&E Managers')
    admins = Group.objects.get(name='Admins')
    project_editors = Group.objects.get(name='Project Editors')

    if not (user.is_admin or user.is_superuser or user.in_group(me_managers) or
            user.in_group(admins) or user.in_group(project_editors)):
        raise PermissionDenied

    projects = Project.objects.all() if user.is_admin or user.is_superuser else user.my_projects()

    context = {
        'user': user,
        'projects': projects.filter(is_impact_project=True),
    }

    return render(request, 'myrsr/select_project.html', context)


@login_required
def results_data(request, project_id):
    """
    My results section. Only accessible to M&E Managers, Admins and Project editors.

    :param request; A Django HTTP request and context
    :param project_id; The ID of the project
    """
    project = get_object_or_404(Project, pk=project_id)
    user = request.user

    if not user.has_perm('rsr.change_project', project):
        raise PermissionDenied

    me_managers_group = Group.objects.get(name='M&E Managers')
    me_managers = project.publishing_orgs.employments().approved().filter(group=me_managers_group)

    context = {
        'project': project,
        'user': user,
        'me_managers': me_managers.exists(),
    }

    return render(request, 'myrsr/results_data.html', context)
