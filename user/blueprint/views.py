from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user


from app import db
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
        )

        db.session.add(user)
        db.session.commit()
        flash('Регистрация успешно завершена! Теперь вы можете войти.')

        return redirect(url_for('auth.login'))
    return render_template(
        'auth/register.html',
        form=form,
        title='Регистрация',
    )


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
            form.password.data
        ):
            login_user(user)
            return redirect(url_for('home.start'))
        else:
            flash('Неправильный email или пароль')
    return render_template('auth/login.html', form=form, title='Вход')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('Вы покинули систему.')

    return redirect(url_for('auth.login'))
