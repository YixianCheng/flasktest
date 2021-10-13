from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprint = Blueprint('owners',__name__,
                                template_folder='templates/owners')

@owners_blueprint.route('/add',methods=['GET','POST'])
def add():

    form = AddForm()
    if form.validate_on_submit():
        puppy_id = form.puppy_id.data
        name = form.name.data
        new_owner = Owner(name,puppy_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('addOwner.html',form=form)
