import glob
import os
import importlib

def init_plugins(app):
    modules = sorted(glob.glob(os.path.dirname(__file__) + "/*"))
    for module in modules:
        module_name = os.path.basename(module)
        if os.path.isdir(module) and module_name:
            module = '.' + module_name
            module = importlib.import_module(module, package='fero.plugins')
            module.load(app)
            app.logger.info("Loaded plugins: %s", module_name)