# Request and Response
## 1. Processing requests
**Requirement**

When we need to read the data carried by a client request in view writing, how can we get the data out correctly?

The data carried by the request may appear in different places in the HTTP message, and different methods need to be used to get the parameters.

### 1.1 URL path parameters (dynamic routing)
For example, there is a request to access the interface address /users/123, where 123 is actually a specific request parameter indicating that information about user 123 is requested. At this point how do we extract the 123 data from the url?

Unlike Django, which writes regular expressions directly when defining routes, Flask uses a converter syntax:
```python
@app.route('/users/<user_id>')
def user_info(user_id):
    print(type(user_id))
    return 'hello user {}'.format(user_id)
```
The <> here is a converter, which defaults to a string type, i.e., it matches the data at this location in string format and passes it into the view with string as the datatype type and `user_id` as the parameter name.

**Flask also provides other types of converters**
```bash
DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
}
```
Matching the above example to data in integers can be used as follows:
```python
@app.route('/users/<int:user_id>')
def user_info(user_id):
    print(type(user_id))
    return 'hello user {}'.format(user_id)


@app.route('/users/<int(min=1):user_id>')
def user_info(user_id):
    print(type(user_id))
    return 'hello user {}'.format(user_id)
```
**Customized converters**

If we encounter the need to match the cell phone number data extracted from /sms_codes/18512345678, Flask's built-in converter will not be able to meet the demand, this time we need to customize the converter.

**Definition method(Customizing the converter is done in 3 main steps)**
1. Create a converter class that holds the regular expression when matched
 ```python
from werkzeug.routing import BaseConverter

class MobileConverter(BaseConverter):
    """
    Mobile phone
    """
    regex = r'1[3-9]\d{9}'
```
- Note that the name regex is fixed

2. Inform Flask apps about customized converters
  ```python
  app = Flask(__name__)
  
  # Add the custom converter to the converter dictionary and specify that the converter is used with the name: mobile
  app.url_map.converters['mobile'] = MobileConverter
  ```

3. Define the use of converters where they are used
  ```python
  @app.route('/sms_codes/<mobile:mob_num>')
  def send_sms_code(mob_num):
      return 'send sms code to {}'.format(mob_num)
  ```
### 1.2 Other parameters
If we want to get the parameters passed elsewhere, we can read them through the **request** object provided by Flask.

The parameters in different locations are stored in different properties of the request.

Properties	| Description      | Types  
---|------------------|-----|
data	| Logging the requested data and converting it to a string	 | *   
form	|Logging form data in requests|	MultiDict
args	|Query parameters in logging requests|	MultiDict
cookies	|Logging cookie information in requests|	Dict
headers	|Record the headers in the request|	EnvironHeaders
method	|Log the HTTP method used for the request	|GET/POST
url	|Record the URL address of the request|	string
files	|Logging of files requested for upload	|*

To get the parameter channel_id in request/articles?channel_id=1, we can use it as follows:
```python
from flask import request

@app.route('/articles')
def get_articles():
    channel_id = request.args.get('channel_id')
    return 'you wanna get articles of channel {}'.format(channel_id)
```

**Upload a picture**

Client uploads an image to the server and saves it to the server
```python
from flask import request

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['pic']
    # with open('./demo.png', 'wb') as new_file:
    #     new_file.write(f.read())
    f.save('./demo.png')
    return 'ok'
```

## 2. Processing Response
**Requirement**

How to return different response messages in different scenarios?

### 2.1 Return to Templates

Use the `render_template` method to render the template and return.

For example, create a new template index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
My template
<br/>{{ my_str }}
<br/>{{ my_int }}
</body>
</html>
```

Back-end view
```python
from flask import render_template

@app.route('/')
def index():
    mstr = 'Hello alex'
    mint = 10
    return render_template('index.html', my_str=mstr, my_int=mint)
```
### 2.2 Redirect
```python
from flask import redirect

@app.route('/demo2')
def demo2():
    return redirect('https://www.google.com')
```

### 2.3 Return Json
```python
from flask import jsonify

@app.route('/demo3')
def demo3():
    json_dict = {
        "user_id": 10,
        "user_name": "alex"
    }
    return jsonify(json_dict)
```
- return jsonify
    - Convert to json format
    - Set the response header Content-Type:application/json
### 2.4 Customizing status codes and response headers
#### 2.4.1 Tuple way

A tuple may be returned, such a tuple must be of the form **(response, status, headers)** and contain at least one element. The status value overrides the status code, and headers can be a list or dictionary as an additional message header value.
  ```python
  @app.route('/demo4')
  def demo4():
      # return 'Status code is 666', 666
      # return 'Status code is 666', 666, [('Name', 'Python')]
      return 'Status code is 666', 666, {'Name': 'Python'}
  ```
#### 2.4.2 make_response way
  ```python
  @app.route('/demo5')
  def demo5():
      resp = make_response('make response test')
      resp.headers["Name"] = "Python"
      resp.status = "404 not found"
      return resp
  ```

## 3. Cookie vs Session
### 3.1 Cookie
**Set**
```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/cookie')
def set_cookie():
    resp = make_response('set cookie ok')
    resp.set_cookie('username', 'alex')
    return resp
```
Set the expiration date
```python
@app.route('/cookie')
def set_cookie():
    response = make_response('hello world')
    response.set_cookie('username', 'alex', max_age=3600)
    return response
```
**Read**
```python
from flask import request

@app.route('/get_cookie')
def get_cookie():
    resp = request.cookies.get('username')
    return resp
```
**Delete**
```python
from flask import request

@app.route('/delete_cookie')
def delete_cookie():
    response = make_response('hello world')
    response.delete_cookie('username')
    return response
```

### 3.2 Session
SECRET_KEY needs to be set first.
```python
class DefaultConfig(object):
    SECRET_KEY = 'fih9fh9eh9gh2'

app.config.from_object(DefaultConfig)

# Or set up directly
app.secret_key='xihwidfw9efw'
```
**Set**
```python
from flask import session

@app.route('/set_session')
def set_session():
    session['username'] = 'alex'
    return 'set session ok'
```
**Read**
```python
@app.route('/get_session')
def get_session():
    username = session.get('username')
    return 'get session username {}'.format(username)
```