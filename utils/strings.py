import difflib
import string

def sanitize(raw_string):
    """Returns a searchable version of string."""
    chars_to_strip = string.punctuation + string.whitespace
    return strip_chars(chars_to_strip, raw_string).lower()

def strip_chars(chars_to_strip, raw_string):
    """Remove all occurrences of any characters in chars_to_strip from raw_string."""
    return ''.join(ch for ch in raw_string if ch not in set(chars_to_strip))

def string_match_length(str1, str2, isjunk=None):
    """Length of the list intersection of str1 and str2, starting at index 0 and going until a mismatch."""
    seq_matcher = difflib.SequenceMatcher(isjunk=isjunk, a=str1, b=str2)
    return seq_matcher.find_longest_match(0, len(str1), 0, len(str2)).size
