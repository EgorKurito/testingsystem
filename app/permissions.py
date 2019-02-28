from django.contrib.auth import models
from django.shortcuts import redirect


class AnonymousRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('admin:index')
        return super().dispatch(request, *args, **kwargs)


permissions_for_teachers_codenames = {
    'admin': [
        'add_logentry',
        'change_logentry',
        'view_logentry'
    ],
    'app': [
        'add_answer',
        'change_answer',
        'delete_answer',
        'view_answer',
        'add_question',
        'change_question',
        'delete_question',
        'view_question',
        'change_studentanswer',
        'view_studentanswer',
        'change_studenttest',
        'view_studenttest',
        'delete_studenttest',
        'add_test',
        'change_test',
        'delete_test',
        'view_test',
        'add_topic',
        'change_topic',
        'delete_topic',
        'view_topic',
        'add_topicquestion',
        'change_topicquestion',
        'delete_topicquestion',
        'view_topicquestion',
        'view_studenttestquestion',
        'change_studenttestquestion',
        'add_group',
        'change_group',
        'view_group',
        'delete_group'
    ]
}

teachers_group_name = 'Teachers'


def add_to_teachers_group(user):
    teachers_group, created = models.Group.objects.get_or_create(name=teachers_group_name)
    if created:
        permissions = []
        for app_group in permissions_for_teachers_codenames:
            permissions.extend(models.Permission.objects.filter(
                content_type__app_label=app_group,
                codename__in=permissions_for_teachers_codenames[app_group]
            ))
        teachers_group.permissions.set(permissions)
    user.groups.add(teachers_group)
