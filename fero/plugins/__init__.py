import glob
import os
import importlib

from flask import g

def init_plugins(app):
    app._loaded_plugins = []
    modules = sorted(glob.glob(os.path.dirname(__file__) + "/*"))
    for module in modules:
        module_name = os.path.basename(module)
        if os.path.isdir(module) and module_name:
            app._loaded_plugins.append(module_name)
            module = '.' + module_name
            module = importlib.import_module(module, package='fero.plugins')
            module.load(app)
    app.logger.info("Loaded plugins: %s", app._loaded_plugins)