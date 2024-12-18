# Introduction to Flask
## 1. Flask
Flask was born in 2010, is Armin ronacher (human name) in Python language based on the Werkzeug toolkit written lightweight web development framework.

Flask itself is equivalent to a kernel , almost all other features have to use extensions ( mail extension Flask-Mail, user authentication Flask-Login, database Flask-SQLAlchemy), all need to use third-party extensions to achieve . For example, we can use Flask extensions to add ORM, form validation tools, file uploads, authentication, etc. Flask does not have a default database to use, we can choose MySQL, we can also use NoSQL.

Its WSGI toolkit using Werkzeug (routing module), the template engine uses Jinja2. These two are also the core of the Flask framework.

## 2. Framework Comparison
### 2.1 Lightness of the framework
Heavyweight framework: to facilitate the development of business programs, provides a wealth of tools, components, such as Django

Lightweight framework: only provide the core functions of the Web framework, free, flexible, highly customizable, such as Flask, Tornado

### 2.2 Comparison with Django
django provides:

- django-admin to quickly create a project works directory

- manage.py to manage project works

- orm model (database abstraction layer)

- admin backend to manage the site

- Caching mechanism

- File storage system

- user authentication system

All of these, flask do not have, need to extend the package to provide.

## 3. Common Expansion Packs
List of extensions: http://flask.pocoo.org/extensions/
- Flask-SQLalchemy: manipulating databases;
- Flask-script: inserting scripts;
- Flask-migrate: managing migrated databases;
- Flask-Session: session storage method specification;
- Flask-WTF: forms;
- Flask-Mail: mail;
- Flask-Bable: provide internationalization and localization support, translation;
- Flask-Login: authenticate user status;
- Flask-OpenID: authentication;
- Flask-RESTful: tools for developing REST APIs;
- Flask-Bootstrap: integration of front-end Twitter Bootstrap framework;
- Flask-Moment: localized date and time;
- Flask-Admin: a simple and extensible framework for managing interfaces


