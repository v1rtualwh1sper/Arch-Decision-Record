#5. Choix du broker d’evenements (Kafka)

##Statut
Accepte

##Contexte
Le systeme doit gerer des evenements fiables : reservations, rappels, notifications, operations de compensation.

##Decision
Utiliser Apache Kafka comme broker d’evenements pour garantir durabilite, replay, et haute disponibilite.

##Alternatives envisagees
- RabbitMQ : Rejete (moins adapte aux flux massifs).
- SQS : Rejete (dependance cloud specifique).

##Consequences
- Positives : Fiabilite, haute performance.
- Negatives : Complexite d’exploitation.

##Liens
- Necessaire pour les Sagas (ADR #4).
