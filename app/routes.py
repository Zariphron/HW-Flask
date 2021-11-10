from app import myapp_obj
from app.forms import TopCities
from flask import render_template, flash, redirect

@myapp_obj.route("/")
def home():
    user = {'name': 'Kevin'}
    form = TopCities()
    if form.validate_on_submit():
        flash(f'City submitted: {form.City.city_name}')
        return redirect('/')
    return render_template('home.html', user=user, form=form)

