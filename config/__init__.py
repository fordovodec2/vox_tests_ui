import os
import dotenv
dotenv.load_dotenv()

env = os.getenv('ENV', 'stand')

if env == 'prod':
    from .prod import *
elif env == 'preprod':
    from .preprod import *
else:
    from .stand import *
