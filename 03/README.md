# Router and blueprints
## 1. Router
```python
@app.route("/")
def index():
    return "hello world"
```
### 1.1 Query Routing Information
- Command-line method
```bash
export FLASK_APP=helloworld_production
flask routes
```
```bash
Endpoint  Methods  Rule
--------  -------  -----------------------
index     GET      /
static    GET      /static/
```
- Get it in the program
    - The url_map attribute in the application holds the route mapping information for the entire Flask application, and we can get the routing information by reading this attribute
   ```python
   print(app.url_map)
   ```
    - If we want to traverse the routing information in our program, we can do it as follows
   ```python
   for rule in app.url_map.iter_rules():
       print('name={} path={}'.format(rule.endpoint, rule.rule))
   ```
**Requirement**

Return all routing information within the application in json via /

**Realization**

```python
@app.route('/')
def route_map():
    """Main view, return all view URLs"""
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})
```
### 1.2 Specify the request method
In Flask, define routes whose default request method is:
- GET
- OPTIONS(included) -> Simplified version of a GET request to ask for server interface information
    - For example, the type of request allowed by the interface, the allowed request source domain name
    - CORS cross-domain: django-cors -> The options request is intercepted and processed in the middleware.
    - www.lemonmall.site -> api/lemonmall.site/users/1
        - Return response -> allow-origin 'www.lemonmall.site'
        - GET api.lemonmall.site/users/1
- HEAD (included) -> Simplified version of GET request
    - Returns only the response header when a GET request is processed, not the response body

The `methods` parameter allows us to specify our own request method for an interface.

Customized POST PUT DELETE PATCH

405 Method Not Allowed
```python
@app.route("/route1", methods=["POST"])
def view_func_1():
    return "hello world 1"

@app.route("/route2", methods=["GET", "POST"])
def view_func_2():
    return "hello world 2"
```

## 2. Blueprint
### 2.1 Requirement
In a Flask application project, if there are too many business views, is it possible to maintain the business units divided in a certain way, and separate the views, static files, template files, etc. used by each unit?

For example, from the business point of view, the entire application can be divided into user module unit, product module unit, order module unit, how to develop these different units, and ultimately integrated into a project application?

### 2.2 Blueprint
In Flask, the Blueprint is used to organize the management in modules.

A Blueprint can actually be understood as a container object that stores a set of view methods with the following characteristics:

- An application can have multiple Blueprint.
- A Blueprint can be registered to any unused URL such as “/user”, “/goods”.
- Blueprint can have their own templates, static files, or other common methods, and are not required to implement the application's views and functions.
- Blueprint should be registered when an application is initialized.

But a Blueprint is not a complete application, it can not run independently of the application, but must be registered to an application.

### 2.3 Usage
Using a blueprint can be broken down into three steps:
1. Create a blueprint object
```python
user_bp=Blueprint('user',__name__)
```
2. Operate on this blueprint object, register routes, specify static folders, register template filters
```python
@user_bp.route('/')
def user_profile():
    return 'user_profile'
```
3. Register this blueprint object with the application object
```python
app.register_blueprint(user_bp)
```

**Single file blueprints**
- Can create blueprint objects and define views in a single file.

**Catalog (package) blueprints**
- For a blueprint that is intended to contain multiple files, it is common to place the creation of the blueprint object in the Python package's `__init__.py` file.

```bash
--------- project # Project Catalog
  |------ main.py # Startup file
  |------ user  # User blueprint
  |  |--- __init__.py  # Create blueprint objects here
  |  |--- passport.py  
  |  |--- profile.py
  |  |--- ...
  |
  |------ goods # Commodity Blueprint
  |  |--- __init__.py
  |  |--- ...
  |...
```

### 2.4 Extended Usage
#### 2.4.1 Specify the url prefix of the blueprint
Use the url_prefix parameter when registering the blueprint in the application to specify
  ```python
   app.register_blueprint(user_bp, url_prefix='/user')
   app.register_blueprint(goods_bp, url_prefix='/goods')
   ```
#### 2.4.2 Blueprint internal static files
Unlike application objects, blueprint objects do not register static directory routes by default when they are created. We need to specify the static_folder parameter at creation time.

The following example sets the static_admin directory in the directory where the blueprint is located to the static directory.
  ```python
   admin = Blueprint("admin",__name__,static_folder='static_admin')
   app.register_blueprint(admin,url_prefix='/admin')
   ```
Static files in the `static_admin` directory can now be accessed using `/admin/static_admin/<filename>`.

The access path can also be changed with `static_url_path`.
  ```python
   admin = Blueprint("admin",__name__,static_folder='static_admin',static_url_path='/lib')
   app.register_blueprint(admin,url_prefix='/admin')
   ```
#### 2.4.3 Blueprint Internal Template Catalog
The default template directory for blueprint objects is the system's template directory, which can be set using the template_folder keyword parameter when creating a blueprint object.
  ```python
   admin = Blueprint('admin',__name__,template_folder='my_templates')
  ```
