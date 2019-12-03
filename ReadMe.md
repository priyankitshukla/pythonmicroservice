

1. Run command pip install -r requirement.txt

2. Create a package to make project modular or we can create startup project by create a file name as main.py in base project only.1

3. Import Flask using below import
```python
        from flask import Flask
```
4. Initialize app
```python
            app = Flask(__name__)
```
5. Create a route for the url.
```python
        @app.route('/')
            def index():
            return  'This is home page'
```
6. Add app.run() to run the application , user Debug=True for hot deployment otherwise we need to restart the server each time.

7. use below command to run the base app-
```
           cd employeedetail
           python main.py
```
8. Access application on port 5000

Ref- full [main.py](https://github.com/priyankitshukla/pythonmicroservice/blob/master/employeedetail/main.py)


## ############################## Introduce HTML templates ####################


Step 1- Now add another import with flask render_templates

            from flask import Flask, render_template


Step 2- change return statement with

            return  render_template('index.html')

Step 3- Create a folder name with templates make sure name matches

            now create a file name index.html

            <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>HCL Technologies</title>
                </head>
                <body>
                    <h2> Welcome to HCL</h2>
                </body>
                </html>