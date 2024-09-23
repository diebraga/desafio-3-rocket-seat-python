import sys
import os

# Ajouter le chemin du répertoire racine (là où se trouve app.py) dans sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importer l'application Flask et l'objet db depuis app.py
from app import app, db

# Supprimer toutes les tables dans la base de données
with app.app_context():
    db.drop_all()
    print("Toutes les tables ont été supprimées.")