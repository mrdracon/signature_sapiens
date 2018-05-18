import StringIO
from flask import render_template, redirect, send_file, make_response, Response
from app import app
from app.forms import SignatureForm

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return redirect('/signature')

@app.route('/signature', methods=['GET', 'POST'])
def signature():
    form = SignatureForm()
    if form.validate_on_submit():
#        flash('Generating Signature...')
        strIO = StringIO.StringIO()
        strIO.write(render_template('create_signature.html', first_name=form.first_name.data, last_name=form.last_name.data, position=form.position.data, email=form.email.data, mob=form.mob.data))
        strIO.seek(0)
        #res = make_response(strIO)
        #res
        return Response(strIO,
                mimetype='text/html',
                headers={"Content-Disposition":"attachment;filename=signature.htm"})
    return render_template('signature.html', form=form)
