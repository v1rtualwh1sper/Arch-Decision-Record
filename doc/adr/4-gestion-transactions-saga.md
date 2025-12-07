#4. Gestion des transactions distribuees (Sagas)

##Statut
Accepte

##Contexte
Le systeme gere des operations multi-services : emprunts, reservations, notifications. Les operations doivent etre coherentes sans lock global.

##Decision
Utiliser le pattern Saga (orchestration) afin de gerer les echecs et compensations.

##Alternatives envisagees
- 2PC : Rejete (couplage fort, non scalable).
- Eventual Consistency non structuree : Rejete (complexite et risques).

##Consequences
- Positives : Haute scalabilite, resilience.
- Negatives : Complexite additionnelle dans les workflows.

##Liens
- Repose sur le broker d'evenements (ADR #5).
