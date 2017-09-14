from django.contrib.auth.models import User as AuthUser
    projects = Project.objects.filter(author=user,  is_main_branch=True)
        "img": user.avatar,
    projects = Project.objects.filter(author=user,  is_main_branch=True)
    return p_list
    projects = Star.objects.filter(user=user,  project__is_main_branch=True)
    return p_list
            "img": f.follower.avatar,
            "img": f.followed.email.avatar,
    stars_to_me = Star.objects.filter(project__author=user, project__is_main_branch=True)
    forks_by_me = Fork.objects.filter(forked_project__author=user, forked_project__is_main_branch=True)
    forks_to_me = Fork.objects.filter(original_project__author=user, original_project__is_main_branch=True)
        project = Project.objects.filter(name__iexact=projectname, is_main_branch=True).first()
            if f.previous_file is not None and f.previous_file.name != f.name:
                current_files.pop(f.previous_file.name)
            "author_img": c.project.author.avatar,
        file_set.append([f.previous_file, f])
        i = 0
            if i == 0 or i == 1:
            i = i+1
        "author_img": project.author.avatar,


def addProject(username, project_name, branch_name, project_descr, commit_msg, files):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    project = Project.objects.create(name=project_name, branch=branch_name, author=user, description=project_descr, is_main_branch=True)
    commit = Commit.objects.create(project=project, message=commit_msg)

    for f in files:
        File.objects.create(commit=commit, name=f.name, size=f.size, code=f.read())


def editFile(username, projectname, branchname, oldfilename, filename, code, commit_message):
    user = User.objects.filter(username__iexact=username).first()

    if user is None:
        raise Http404("User does not exist")

    project = Project.objects.filter(name__iexact=projectname, branch__iexact=branchname).first()

    if project is None:
        raise Http404("Project does not exist")

    old_file = File.objects.filter(commit__project=project, name=oldfilename).order_by('-commit__time').first()

    commit = Commit.objects.create(project=project, message=commit_message)
    File.objects.create(commit=commit, name=filename, size=len(code), code=code, previous_file=old_file)


def editProfile(old_username, username, name, email, avatar, password):

    user = User.objects.filter(username__iexact=old_username).first()
    authuser = AuthUser.objects.filter(username__iexact=old_username).first()

    if user is None or authuser is None:
        raise Http404("User does not exist")

    if username:
        user.username = username
    if name:
        user.name = name
    if email:
        user.email = email
    if avatar:
        user.avatar = avatar

    if password:
        authuser.set_password(password)
    if username:
        authuser.username = username

    user.save()
    authuser.save()