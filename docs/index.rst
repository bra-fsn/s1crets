Welcome to s1crets's documentation!
===================================

s1crets is a thin Python wrapper to read secrets from cloud resources.
Currently supported are:
 * `AWS Secrets Manager <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html>`_
 * `AWS Systems Manager's Parameter Store <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html>`_


Installation
------------
You can install it with `pip install s1crets`.

Command Line Usage
------------------
Upon successful installation, you should have the `s1crets` command line utility:

.. program-output:: s1crets --help

Getting a secret
~~~~~~~~~~~~~~~~
You can get a secret's decyphered value with a simple command like this::

  $ s1crets get --provider aws.sm secrets/test
  test



.. automodule:: s1crets
    :members:

.. automodule:: s1crets.cache
    :members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
