import warnings

try:
    from .timeseries import *
except ImportError as e:
    warnings.warn(e)
