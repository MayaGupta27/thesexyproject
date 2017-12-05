from numpy import genfromtxt
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GenesExtended.sqlite'
app.config['SECRET_KEY'] = "random string"

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

db = SQLAlchemy(app)

class genes(db.Model):
    __tablename__ = 'genes'
    __table_args__ = {'sqlite_autoincrement': True}
    name = db.Column(db.String(100), primary_key=True)
    rsNum = db.Column(db.String(50))
    goodAllele = db.Column(db.String(200))
    riskAllele = db.Column(db.String(1000))

def __init__(self, name, rsNum, goodAllele, riskAllele):
    self.name = name
    self.rsNum = rsNum
    self.goodAllele = goodAllele
    self.riskAllele = riskAllele

@app.route('/')
def show_all():
    return render_template('show_all.html', genes=genes.query.all())

@app.route('/new', methods=['GET', 'POST'])
def new():

    if request.method == 'POST':
        if not request.form['name'] or not request.form['rsNum'] or not request.form['goodAllele']:
            flash('Please enter all the fields', 'error')
        else:
            gene = genes(name = request.form['name'], rsNum = request.form['rsNum'],
                              goodAllele = request.form['goodAllele'], riskAllele = request.form['riskAllele'])
            db.session.add(gene)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
