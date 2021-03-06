# flask-guide
Step-by-step tutorial for building a simple Flask application using Python; optimized for use in a CS class.


## What We'll Do
By following along with this project and our lesson(s), you'll walk away with a skeleton for a fully functional Flask web-app. You'll have several roles for users, a db with several tables, and basic authentication. This is meant to serve as a template; however, the basic framework will allow you to create apps of any kind/focus.

## Instructions
Follow the instructions below to set up your development environment for completing this project.

### Before we meet
1. Clone this repo:

   ```Shell
   $ git clone https://github.com/robertjdominguez/flask-guide
   ```

2. Install required libraries

   ```Shell   
   $ cd flask-guide && pip install -r requirements.txt
   ```

3. Install [Atom](https://atom.io/) and install these Atom packages via the following commands...these will make our development process much smoother:

    ```Shell
    $ apm install atom-beautify
    $ apm install atom-bootstrap4
    $ apm install atom-jinja2
    $ apm install autocomplete-python
    $ apm install install busy-signal
    $ apm install flask-snippets
    $ apm install emmet
    $ apm install python-indent
    $ apm install python-autopep8
    $ apm install todo-show
    ```

    NB: a dependency for the python-autopep8 package will be the `autopep8` library for Python...install it by running
      `$ pip install autopep8`

    Also, in order for the python-autopep8 package to run correctly, you'll need to go to the package's settings and check the "Format On Save" box. After this, every time you save a Python file, the package will parse it and format your code to the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.

4. Install [ngrok](https://ngrok.com/download) -- we'll use this later to tunnel a web-server and test on mobile.

5. Check out the TODO.md file. We'll use this as a task list to help us stay organized and move at the right pace.
