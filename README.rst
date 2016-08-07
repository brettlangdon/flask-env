flask-env
=========

Easily set Flask settings from environment variables.

The reason for using :code:`flask-env` is to be able to follow the `12-factor app <http://12factor.net/>`_ suggestions for configuring your application.

With :code:`flask-env` you can define your default configuration options in code and very easily override via environment variables.


Installation
~~~~~~~~~~~~

.. code:: bash

   pip install flask_env


Usage
~~~~~

With :code:`flask-env` you will define your configuration as an object and load it into your Flask application via `app.config.from_object <http://flask.pocoo.org/docs/0.11/api/#flask.Config.from_object>`_ method.

To use in Python 2:

.. code:: python

   from flask import Flask
   from flask_env import MetaFlaskEnv


   class Configuration(object):
       __metaclass__ = MetaFlaskEnv

       DEBUG = False
       PORT = 5000


   app = Flask(__name__)
   app.config.from_object(Configuration)


To use in Python 3:

.. code:: python

   from flask import Flask
   from flask_env import MetaFlaskEnv


   class Configuration(metaclass=MetaFlaskEnv):
       DEBUG = False
       PORT = 5000


   app = Flask(__name__)
   app.config.from_object(Configuration)


Configuration
~~~~~~~~~~~~~

:code:`flask-env` offers two configuration options to determine how/which environment variables are loaded.

ENV_PREFIX
  Only consider environment variables that start with this prefix.
  The prefix will be removed from the environment variable name when setting in the configuration.
  (default: :code:`''`, example: :code:`ENV_PREFIX = 'MYAPP_'`)

AS_JSON
  Whether or not to try and parse each configuration value as JSON.
  This will ensure that when setting variables as integers/null/booleans that they properly get parsed in their applicable Python types.
  (default: :code:`True`, example: :code:`AS_JSON = False`)


Setting configuration values:

.. code:: python

   from flask_env import MetaFlaskEnv


   class Configuration(metaclass=MetaFlaskEnv):
       ENV_PREFIX = 'MYAPP_'
       AS_JSON = False
