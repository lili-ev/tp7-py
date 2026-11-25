
from datetime import datetime


class ValidationMixin:
    def valider_titre(self):
        if not self.titre or not self.titre.strip():
            raise ValueError("Le titre est obligatoire")
        return True


class HistoriqueMixin:
    def __init__(self):
        self.historique = []

    def enregistrer_historique(self):
        self.historique.append(self.description)

    def afficher_historique(self):
        print("\nHistorique des descriptions :")
        for i, description in enumerate(self.historique, 1):
            print(f"{i}. {description}")


class JournalisationMixin:
    def journaliser(self, action):
        print(f"[Journal] {datetime.now()}: {action}")


class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):

    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.date_creation = datetime.now()

        self.valider_titre()
        HistoriqueMixin.__init__(self)

        self.journaliser(f"Création de la tâche : {self.titre}")

    def mettre_a_jour(self, description):
        self.enregistrer_historique()
        self.description = description
        self.journaliser(f"Modification de la tâche : {self.titre}")


# Exemple d'utilisation

tache = Tache("Projet Python", "Première description")

tache.mettre_a_jour("Deuxième description")

tache.afficher_historique()
