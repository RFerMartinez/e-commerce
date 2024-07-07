from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQILTE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce',
        'USER': 'postgres',
        'PASSWORD': 'FerBD42276',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}