import os

if os.environ.get("FALCON_ENVIRONMENT") == "dev" :
    from .dev import *
elif os.environ.get("FALCON_ENVIRONMENT") == "prod" :
    from .prod import *
else:
    from .local import *

