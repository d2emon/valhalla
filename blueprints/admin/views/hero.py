from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required


from app import db
from .. import admin
from ..forms import HeroForm
from story.models import Hero


def check_admin():
    """
    Prevent non-admin from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


@admin.route('/heroes', methods=['GET', 'POST'])
@login_required
def list_heroes():
    """
    List all heroes
    """
    check_admin()

    heroes = Hero.query.all()

    return render_template(
        'admin/heroes.html',
        heroes=heroes,
        title="Истории"
    )


@admin.route('/heroes/<int:id>/edit', methods=['GET', 'POST'])
@admin.route('/heroes/add', methods=['GET', 'POST'])
@login_required
def edit_hero(id=None):
    """
    Add/Edit a hero
    """
    check_admin()

    if id is not None:
        hero = Hero.query.get_or_404()
    else:
        hero = Hero()

    form = HeroForm(obj=hero)
    if form.validate_on_submit():
        hero.name = form.name.data
        hero.description = form.description.data
        db.session.add(hero)
        db.session.commit()
        try:
            db.session.add(hero)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            flash(hero.errors)
            flash('Error: department name already exists.')
        return redirect(url_for('admin.list_heroes'))

    if hero.id:
        title = "Править Историю"
    else:
        title = "Новая История"

    return render_template(
        'admin/hero.html',
        hero=hero,
        form=form,
        title=title,
    )


@admin.route('/heroes/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_hero(id):
    """
    Delete a hero from database
    """
    check_admin()

    hero = Hero.query.get_or_404(id)
    db.session.delete(hero)
    db.session.commit()
    flash('You have successfully deleted the department.')

    return redirect(url_for('admin.list_heroes'))
