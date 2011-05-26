"""
Basic Module for using GPTwoSample
==================================

Provides basic ``twosample`` class, which should be superclass for all implementations of gptwosample

"""
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)

from gptwosample.twosample.twosample_base import *