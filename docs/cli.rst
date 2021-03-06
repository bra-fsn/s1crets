Command Line Usage
==================
Upon successful installation, you should have the `s1crets` command line utility:

.. program-output:: s1crets --help

Getting a secret
----------------
You can get a secret's deciphered value with a simple command like this::

  $ s1crets get --provider aws.sm secrets/test
  secret_value

You can use a different provider (for example AWS Parameter Store)::

  $ s1crets get --provider aws.ps /secrets/test
  secret_value

JSON contents in secrets are supported. You can query into the document itself::

  $ s1crets get secrets/json_test
  {'level1': {'level2': 3}}
  $ s1crets get secrets/json_test level1
  {'level2': 3}
  $ s1crets get secrets/json_test level1 level2
  3


Listing all secrets below a path
--------------------------------
You can list all secrets under a path if the provider supports it (for eg. AWS PS)::

  $ s1crets get-by-path --provider aws.ps /prod/databases/mysql
  /prod/databases/mysql/bigdatabase1/root S3cr3Tp4Ssw0Rd
  /prod/databases/mysql/bigdatabase1/user1 password
  /prod/databases/mysql/dolphin/root default


Checking whether a path exists or not
-------------------------------------
`exists` can be used to check whether a path exists or not. For providers, which
supports the notion of paths (like AWS PS), it will return true not just for exact
key matches, but for path prefixes as well::

  $ s1crets exists --provider aws.ps /prod/databases/mysql/dolphin && echo OK
  OK
  $ s1crets exists --provider aws.ps /prod/databases/mysql/nonexistent || echo NA
  NA

Updating secrets
----------------
You can update existing secrets (in this example with a JSON content)::

  $ s1crets update --provider aws.sm secrets/json_test '{"level1": {"level2": 6}}'
