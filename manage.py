@manager.commmand
def deploy():
    from flask.ext.migrate import upgrade
    from app.models import Role,User
    upgrade()
    Role.insert_roles()
    User.add_self_follows()