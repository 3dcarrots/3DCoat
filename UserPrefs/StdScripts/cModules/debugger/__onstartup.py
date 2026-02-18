import os
os.environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"

import debugpy
import cPy.cCore

print(os.path.realpath.__code__.co_filename)
debugpy_endpoint = debugpy.listen(("localhost", cPy.cCore.cExtension.DebugPort()), in_process_debug_adapter = True)


