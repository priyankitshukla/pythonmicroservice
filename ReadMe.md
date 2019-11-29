```python
Step 1- Check out project from git in to Pycharm.1

Step 2- run command pip install -r requirement.txt

Step 3- Create a package to make project moduler or we can create startup project by create a file name as main
        .py in base project only.1

Step 4- Import Flask using below import

        from flask import Flask

Step 5- Initialize app

            app = Flask(__name__)

Step 6- create a route for the url.

        @app.route('/')
            def index():
            return  'This is home page'

Step 7 - add app.run() to run the application , user Debug=True for hot deployment otherwise we need to restart the server each time.

Step 8 - use below command to run the base app-

           cd employeedetail
           python main.py

Step 9- Access application on port 5000

Ref- full main.py code

        from flask import Flask

app = Flask(__name__)


        @app.route('/')
            def index():
                return  'This is home page'


        if __name__=="__main__":
            app.run(debug=True)