from django.db import migrations
from django_safemigrate import Safe


def update_build_queue(apps, schema):
    """Update project build queue to include the previously implied build-
    prefix."""
    Project = apps.get_model("projects", "Project")
    for project in Project.objects.all():
        if project.build_queue is not None:
            if not project.build_queue.startswith("build-"):
                project.build_queue = "build-{}".format(project.build_queue)
                project.save()


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("projects", "0015_add_project_allow_promos"),
    ]

    operations = [
        migrations.RunPython(update_build_queue),
    ]
