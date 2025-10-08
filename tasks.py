from invoke import task

@task
def mig(c):
    c.run("python manage.py makemigrations")

@task
def upg(c):
    c.run("python manage.py migrate")

@task
def admin(c):
    c.run("python manage.py createsuperuser")

@task
def apps(c):
    c.run("python manage.py startapp apps")




@task
def load(c):
    c.run(
        "python manage.py loaddata user.json settings.json faq.json certificate.json lead.json articles.json project.json product.json"
    )


@task
def dump(c):
    c.run("python manage.py dumpdata auth.user > user.json")
