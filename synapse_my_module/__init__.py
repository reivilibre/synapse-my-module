from synapse_my_module.module import MyModule

__all__ = ["MyModule"]

# __version__ = "0.0.0"

from importlib_metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    pass
