from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return  render_template('index.html')

employee = {
        'id' : 'NAN',
        'organization' : 'HCL'
}

@app.route('/detail/<int:id>')
def employeedetail(id):
    employee.update({'id':id})
    return  employee

if __name__=="__main__":
    app.run(debug=True)