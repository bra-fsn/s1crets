Welcome to s1crets's documentation!
===================================

s1crets is a thin Python wrapper to read secrets from cloud resources.
Currently supported are:
 * `AWS Secrets Manager <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html>`_
 * `AWS Systems Manager's Parameter Store <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html>`_

Wherever supported, it can be used to read/update non-encrypted values as well.

Installation
------------
You can install it with `pip install s1crets`.

User's guide
------------

.. toctree::
   :maxdepth: 4

   cli
   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
