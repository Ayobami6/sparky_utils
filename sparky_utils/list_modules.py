import pkgutil
import importlib


def list_modules():
    """List all modules in the current package."""
    package_name = __name__.rsplit(".", 1)[0]
    package = importlib.import_module(package_name)

    module_list = []
    if hasattr(package, "__path__"):
        for module_info in pkgutil.iter_modules(package.__path__):
            module_list.append(module_info.name)

    return module_list
