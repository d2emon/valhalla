from app import manager, db


from .models import User


@manager.command
def createsuperuser():
    """
    Create superuser
    """
    email = input("Email: ")
    username = input("Username: ")
    password = input("Password: ")
    superuser = User(
        email=email,
        username=username,
        password=password,
        is_admin=True,
    )
    db.session.add(superuser)
    db.session.commit()
