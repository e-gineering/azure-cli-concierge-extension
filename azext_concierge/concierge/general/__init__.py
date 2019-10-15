import pkg_resources
from ._help import load_create_help

pkg_resources.declare_namespace(__name__)

load_create_help()
