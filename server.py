from flask import Flask, render_template, send_file
from forms import UploadJD
import parsers as pr
from run import run

app = Flask("my app")
app.config['SECRET_KEY'] = 'ce3cbf5309689c6e3487c49e59a9addb'
app.add_url_rule('/resumes/<path:filename>', endpoint='resumes', view_func=app.send_static_file)

@app.route('/', methods=['GET','POST'])
def upload():
	form = UploadJD()
	results = {}
	if form.validate_on_submit():
		results = run(form.jd.data, pr.explore('corpus/tokenized/'))
	return render_template("jd.html", form=form, results=results)

@app.route('/download/<path:filename>')
def send(filename):
	return send_file(filename)

if __name__ == '__main__':
	app.run(debug=True)