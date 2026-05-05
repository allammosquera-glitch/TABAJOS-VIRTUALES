from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv('DATABASE_URL')
debug    = os.getenv('DEBUG')
env      = os.getenv('ENVIRONMENT')

print(f'Base de datos: {database}')
print(f'Modo debug:    {debug}')
print(f'Ambiente:      {env}')