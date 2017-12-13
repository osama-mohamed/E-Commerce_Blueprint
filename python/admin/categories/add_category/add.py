

from flask import render_template, request
from wtforms import Form, StringField, validators
from python.admin.login.login_check import *
from python.database.flask_database import *

add_category_admin = Blueprint('add_category_admin', __name__)

# admin add new category validator form

class CategoryForm(Form):
    category = StringField('Category', [validators.InputRequired(), validators.length(min=1, max=100)])


# admin add new category page

@add_category_admin.route('/admin/add_category', methods=['post', 'get'])
@is_admin_logged_in
def add_category():
    cur = mysql.connection.cursor()

    # view messages
    cur.execute("SELECT * FROM contact_us WHERE status = %s ORDER BY id DESC LIMIT 6;", ["not_seen"])
    messages = cur.fetchall()

    # show messages number
    cur.execute("SELECT COUNT(id) FROM contact_us WHERE status = %s ", ['not_seen'])
    count_message = cur.fetchone()
    count_messages = count_message['COUNT(id)']

    # show new orders number
    cur.execute("SELECT COUNT(status) FROM buy_orders WHERE status = %s", ['Pending'])
    count_order = cur.fetchone()
    count_orders_where_pending = count_order['COUNT(status)']

    # show new orders
    cur.execute("SELECT COUNT(status), user_name FROM buy_orders WHERE status = %s GROUP BY user_name ASC LIMIT 12", ['Pending'])
    count_orders_by_user = cur.fetchall()

    cur.close()
    form = CategoryForm(request.form)
    if request.method == 'POST' and form.validate():
        category = form.category.data.lower()
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM categories WHERE category = BINARY %s", [category])
        if result > 0:
            cur.close()
            flash('This Category Already Exists', 'warning')
            return redirect(url_for('dashboard.admin_dashboard'))
        if category == ' ':
            cur.close()
            flash('You Should Type A Word!', 'warning')
            return redirect(url_for('add_category'))
        if result == 0:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO categories (category) VALUES(%s);", ([category]))
            mysql.connection.commit()
            cur.close()
            flash('You Have Added New Category successfully!', 'success')
            return redirect(url_for('dashboard,admin_dashboard'))
    return render_template('admin_add_category.html', form=form, admin_name=session['admin_username'], admin_image=session['admin_image'], permission=session['permission'], messages=messages, count_messages=count_messages, count_orders_where_pending=count_orders_where_pending, count_orders_by_user=count_orders_by_user)