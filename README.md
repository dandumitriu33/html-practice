# Mozilla Developer Network - HTML practice repository

This is just an educational/practice repository for html with a terrible looking site made in Flask.

The MDN tutorial can be found here: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML

## Installation

**Note**: Installation process may be different depending on operating system.  

If you want to see this project you can follow these steps:
1. Install Python 3 - https://www.python.org/  
Please look up how to install it on your operating system
2. Install Pip for Python 3 - https://pip.pypa.io/en/stable/installing/  
Pip is needed to install Flask and Virtualenv
3. Clone the repository on your local machine

        git clone https://github.com/dandumitriu33/html-practice.git  
4. In the project directory, run the following:

        pip install virtualenv
        virtualenv venv
        source venv/bin/activate
        pip install -U Flask  
        
    On Ubuntu you can now run 
    
        pip install -r requirements.txt
        
5. Run the server by typing  

        python3 app.py
6. On your browser, go to http://127.0.0.1:5000

Some more info on installing the components:  
- Installing virtualenv - https://virtualenv.pypa.io/en/latest/installation/
- Installing Flask - https://pypi.org/project/Flask/
- Using pip freeze and installing from requirements.txt - https://pip.pypa.io/en/stable/reference/pip_freeze/
