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

Initialize s1crets
^^^^^^^^^^^^^^^^^^


import s1crets.providers.aws


s1crets module
==============

.. automodule:: s1crets
    :members:

s1crets cache
=============

.. automodule:: s1crets.cache
    :members:
