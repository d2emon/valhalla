from flask import render_template
# from flask_login import current_user, login_required


from . import home


@home.route('/')
def index():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Добро Пожаловать!")
