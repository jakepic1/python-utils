import json
import decimal
import datetime

def extract_subdict(dictionary, keys):
    """Returns a subdict of dictionary that contains only the keys specified."""
    return {key: dictionary[key] for key in keys}

def flatten(matrix):
    """Returns a list from a 2d matrix (list of lists)."""
    return [item for sublist in matrix for item in sublist]

def find_index(match_function, iterable):
    """Returns the index of the first item in an iterable that matches the match_function, otherwise -1."""
    return next((i for (i, item) in enumerate(iterable) if match_function(item)), -1)

def find(match_function, iterable, default=None):
    """Returns the first item in an iterable that matches the match_function, otherwise default."""
    index = find_index(match_function, iterable)
    if index == -1:
        return default
    return iterable[index]

def categorize(func, iterable):
    """Returns a 2-item tuple:
    Items in iterable that match function func, and items in iterable that don't match func.
    """
    return filter(func, iterable), filter(lambda x: not func(x), iterable)

def json_dumps(arg, *args, **kwargs):
    """Used just like the regular json.dumps, but with a special encoder to handle non-serializable objects."""

    class Encoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                return float(o)
            elif isinstance(o, datetime.datetime):
                return str(o)
            return super(Encoder, self).default(o)

    kwargs.setdefault('indent', 4)
    kwargs.setdefault('sort_keys', True)
    kwargs.setdefault('cls', Encoder)
    return json.dumps(arg, *args, **kwargs)
