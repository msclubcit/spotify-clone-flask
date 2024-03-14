## Task 2 - Your first contribution
* Description - Displaying static html and css with bootstrap using Flask
* Duration -  `1 day`
* Difficulty -  `Easy level`
* Imporatnce - Building block of web development 
* What to do?
    - [x] You have to create a html templates using bootstrap to whoever pages are assigned to.
    - [x] Route the given url to the static web page.

* Requirements
    * HTML, CSS (Bootstrap 5)
    * Python / Flask (basics)
* Learning materials
    * Documentation
        * [Flask official documentation](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)
        * [Bootstrap 5 Official documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
    * Youtube videos 
        *  [Flask in one hour by Free Code Camp](https://www.youtube.com/watch?v=Z1RJmh_OqeA)
        * [Learn bootstrap in 15 minutes](https://www.youtube.com/watch?v=eow125xV5-c)


* Assignee
    | Contributor  | Static page | URL |
    | --- | ---|---|
    | @Rithvikbng  | `base.html`  |(parent template)|
    | @Nikhil Kumar  | `home.html` |`/`|
    | @Harshitham1204  | `about.html` |`/about`|
    | @Prithvirajn  | `contact.html`  |`/contact`|
    | @DILIP-SHEESH  | `disclaimer.html`  |`/disclaimer`|


## Details of pages

> [Please read Bootstrap 5 Official documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

*  `base.html`
    * This template is the main layout of the html templates.
    * path: `templates/base.html`
    * contents
        * Basic bootstrap (https://getbootstrap.com/docs/5.3/getting-started/introduction/)
        * bootstrap navbar (https://getbootstrap.com/docs/5.3/components/navbar/)
        * bootstrap footer (https://getbootstrap.com/docs/5.3/examples/footers/) (refer "view-source")
        * flask Template inheritance:  ` extends, block ` tags (https://flask.palletsprojects.com/en/2.3.x/patterns/templateinheritance/)
    * By using all these, create a basic parent template.
    * No flask code needed (except jinja template code)

    * Example of base.html
    ```html
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Example </title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <!-- add navbar -->
        {% block content %}

        {% endblock content %}
        <!-- add footer -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>

    ```
    * Exammple of other child pages
    ```html
    {% extends 'base.html' %}

    {% block content %}
    <!-- page content -->
    {% endblock content %}
    ```

* `home.html`
    * Create a standard home page for this project.
    * Refer these examples from bootstrap (https://getbootstrap.com/docs/5.3/examples/)
    * Must include `Hero section`, `Features`, etc
    * Creativity level depends on you. 

* `about.html`
    * Include contents like Small description about this project, contributor information, features etc.

* `contact.html`
    * Add a form including `name`, `email` and `message`

* `disclaimer.html`
    * Add some laws and regulations 
    * There are lots of free disclaimer generator use those.



### Installation

`pip install flask`

### How to bind url to a page

```python

from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
```

To run the code

`flask run --debug`
