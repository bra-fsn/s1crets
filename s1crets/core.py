from __future__ import absolute_import
import importlib


class DictQuery(dict):
    def get(self, keys, default=None):
        val = None

        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [v.get(key, default) if v else None for v in val]
                else:
                    try:
                        val = val.get(key, default)
                    except AttributeError:
                        return default
            else:
                val = dict.get(self, key, default)

            if val == default:
                break
        return val


def _get_provider(provider, **params):
    m = importlib.import_module(name='.{}'.format(provider),
                                package='s1crets.providers')
    return m.SecretProvider(**params)


def get(provider='aws.sm', path=None, keypath=None):
    """Get a secret from the given `provider`

    Args:
        provider (str): Secret provider, currently supported:
            aws.sm: AWS Secrets Manager
            aws.ps: AWS Parameter Store
        path (str): The path for the given secret
        keypath (list): the key path for looking into a JSON secret

    Returns:
        secret: The returned secret, can be string, bytes or in case of JSON,
                a dictionary
    """
    p = _get_provider(provider)
    return p.get(path, keypath=keypath)


def path_exists(provider='aws.sm', path=None, keypath=None):
    p = _get_provider(provider)
    return p.path_exists(path, keypath=keypath)


def get_by_path(provider='aws.sm', path=None):
    p = _get_provider(provider)
    return p.get_by_path(path)


def update(provider='aws.sm', path=None, value=None):
    p = _get_provider(provider)
    return p.update(path, value)
