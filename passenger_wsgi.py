import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

module_name = "wsgi"
module_path = os.path.join(os.path.dirname(__file__), "app", "wsgi.py")
spec = importlib.util.spec_from_file_location(module_name, module_path)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load WSGI module from {module_path}")
wsgi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wsgi)
application = wsgi.application
