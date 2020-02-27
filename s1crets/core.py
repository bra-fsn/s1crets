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


def get_provider(provider, **params):
    m = importlib.import_module(name='.{}'.format(provider),
                                package='s1crets.providers')
    return m.SecretProvider(**params)


def args_cache_key(*args, **kwargs):
    args = list(args)
    for k, v in kwargs.items():
        if isinstance(v, list):
            v = tuple(v)
        try:
            hash(v)
        except Exception:
            continue
        args.append((k, v))
    return tuple(args)


# list is unhashable, so we use only the positional args for the cache key.
# This means tags have to be specified as a kw arg.
# @cachetools.cached(cache={}, key=args_cache_key)
def get(provider='aws.sm', path=None):
    p = get_provider(provider)
    return p.get(path)


def get_by_path(provider='aws.sm', path=None):
    p = get_provider(provider)
    return p.get_by_path(path)
