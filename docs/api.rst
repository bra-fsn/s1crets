API usage
=========

s1crets tries to provide the same(-ish) interface for all secret providers.
Some implementation details and the feature sets are of course different though.

Caching
-------

By default all accesses are cached into memory with a cache of 1000 entries and
TTL of 15 minutes.
If you want to customize that, you have two options:

Caching into the memory
~~~~~~~~~~~~~~~~~~~~~~~

You can set the cache parameters by submitting the `cache_args`::

  import s1crets.providers.aws
  ps = s1crets.providers.aws.ParameterStore(cache_args={'cache_size': 10, 'cache_ttl': 60})


Caching onto disk
~~~~~~~~~~~~~~~~~

Instead of keeping the cache in memory, you can persists that to disk with the `diskcache` module::

  ps = s1crets.providers.aws.ParameterStore(cache_args={'cache_on_disk':True, 'key_cache_dir': '/data/key_cache', 'path_cache_dir': '/data/path_cache'})

BEWARE that this stores sensitive information unencrypted, you have to take care against malicious access to those files!
Using diskcache can solve cache persistency (for eg. between script executions) or sharing the cache between multiple
instances.


AWS
---

Assuming a role
~~~~~~~~~~~~~~~

Doing operations in either store, you have to have the relevant permissions, both for the
service and corresponding encryption (KMS) keys.
If your current role doesn't have those, you can switch temporarily to another role by assuming it.

An example for doing that::

  import s1crets.providers.aws
  ROLEARN = f'arn:aws:iam::{TARGET_ACCOUNT}:role/my-assume-role'
  ps = s1crets.providers.aws.ParameterStore(sts_args={'RoleArn': ROLEARN, 'RoleSessionName': 'myscript'})


Systems Manager Parameter Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`AWS Systems Manager Parameter Store <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html>`_
(PS from now on) provides access to a path-like structured, `/` separated key-value store.
You can access your parameters on the `AWS SSM PS console <https://console.aws.amazon.com/systems-manager/parameters>`_.


Initializing the module
^^^^^^^^^^^^^^^^^^^^^^^

You can create a Parameter Store object this way::

  import s1crets.providers.aws
  ps = s1crets.providers.aws.ParameterStore()

Getting a secret
^^^^^^^^^^^^^^^^

To get a secret::

  ps.get('/prod/databases/mysql/bigdb/root')

This will return a `KeyError` Exception if the key doesn't exist.
If the value is JSON-decodeable, you'll receive a dictionary.

Listing all secrets below a path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PS supports the notion of paths, so you can get all secrets below one::

  ps.get_by_path('/prod/databases/mysql')

This will return a dictionary with the PS keys and their values.


Checking whether a path exists or not
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can check whether a path (and in PS case it means the path or a key) exists::

  ps.path_exists('/prod/databases/mysql')

Returns a boolean.

Updating secrets
^^^^^^^^^^^^^^^^

It's possible to update values as well. This will use the same `KeyId` as the
original value::

  ps.update('/prod/databases/mysql/bigdb/root', 'S3cr3Tp4Ssw0Rd!^')


Secrets Manager
~~~~~~~~~~~~~~~

`AWS Secrets Manager <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html>`_
(SM from now on) provides access to a key-value encrypted store.
You can access your secrets on the `AWS SM console <https://console.aws.amazon.com/secretsmanager/home>`_.

SM can store arbitrary values (even binary), but if you use the console, they will mostly be JSONs.
s1crets automatically tries to parse JSON, so you'll get a parsed result.


Initializing the module
^^^^^^^^^^^^^^^^^^^^^^^

You can create a Secrets Manager object this way::

  import s1crets.providers.aws
  sm = s1crets.providers.aws.SecretsManager()

Getting a secret
^^^^^^^^^^^^^^^^

To get a secret::

  sm.get('prod/databases/mysql/bigdb/root')

This will return a `KeyError` Exception if the key doesn't exist.
If the value is JSON-decodeable, you'll receive a dictionary.


Checking whether a key exists or not
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can check whether a key exists::

  sm.path_exists('prod/databases/mysql')

Returns a boolean.

Note that SM doesn't support the notion of path, so you can only check for exact key names.

Updating secrets
^^^^^^^^^^^^^^^^

It's possible to update values as well. This will use the same encryption key as the
original value::

  sm.update('prod/databases/mysql/bigdb/root', 'S3cr3Tp4Ssw0Rd!^')



s1crets module
==============

.. automodule:: s1crets
    :members:
