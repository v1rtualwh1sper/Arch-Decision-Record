#1. Choix de la base de donnees

##Statut
Accepte

##Contexte
Le systeme doit gerer un grand nombre de transactions (emprunts, reservations) avec une forte coherence des donnees. Les donnees doivent etre persistantes et accessibles rapidement.

##Decision
Utiliser PostgreSQL comme base de donnees relationnelle.

##Alternatives envisagees
- MongoDB : Rejete car moins adapte pour les transactions complexes.
- MySQL : Rejete car moins performant pour les requetes complexes.

##Consequences
- Positives : Coherence transactionnelle, requetes complexes possibles.
- Negatives : Configuration plus complexe qu’une base NoSQL.
