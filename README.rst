s1crets
=======

s1crets is a thin Python wrapper to read secrets from cloud resources.
Currently supported are:
 * `AWS Secrets Manager <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html>`_
 * `AWS Systems Manager's Parameter Store <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html>`_

Wherever supported, it can be used to read/update non-encrypted values as well.

Installing
----------

Install and update using `pip`_:

.. code-block:: text

    pip install -U s1crets

A Simple Example
----------------

.. code-block:: python

    # Using AWS Parameter Store
    import s1crets.providers.aws
    ps = s1crets.providers.aws.ParameterStore()
    ps.get('/prod/databases/mysql/bigdb/root')
    ps.get_by_path('/prod/databases/mysql')
    ps.path_exists('/prod/databases/mysql')
    ps.update('/prod/databases/mysql/bigdb/root', 'S3cr3Tp4Ssw0Rd!^')

    # AWS Secrets Manager
    sm = s1crets.providers.aws.SecretsManager()
    sm.get('prod/databases/mysql/bigdb/root')
    sm.path_exists('prod/databases/mysql')
    sm.update('prod/databases/mysql/bigdb/root', 'S3cr3Tp4Ssw0Rd!^')


.. code-block:: text

    $ s1crets get secrets/json_test
    {'level1': {'level2': 3}}
    $ s1crets get secrets/json_test level1
    {'level2': 3}
    $ s1crets get secrets/json_test level1 level2
    3
