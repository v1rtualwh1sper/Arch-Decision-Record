# Sommaire des ADR

_Généré le 2025-12-07 22:51:36Z_

Ce fichier liste les ADR disponibles dans `doc/adr/`.

| # | Titre | Statut | Fichier | Contexte (extrait) |
|---:|---|---|---|---|
| 1 | Choix de la base de donnees | Accepte | [1-base-de-donnees.md](./1-base-de-donnees.md) | Le systeme doit gerer un grand nombre de transactions (emprunts, reservations) avec une forte coherence des donnees. Les donnees doivent… |
| 2 | Authentification OIDC/OAuth2 et tokens JWT | Accepte | [2-authentification-oidc-oauth2-jwt.md](./2-authentification-oidc-oauth2-jwt.md) | Le systeme doit authentifier des utilisateurs publics et internes. Besoins : SSO, gestion centralisee, tokens courts, securite forte. |
| 3 | Autorisation RBAC | Accepte | [3-autorisation-rbac.md](./3-autorisation-rbac.md) | Le systeme comporte plusieurs types d’utilisateurs avec des privileges differents. |
| 4 | Gestion des transactions distribuees (Sagas) | Accepte | [4-gestion-transactions-saga.md](./4-gestion-transactions-saga.md) | Le systeme gere des operations multi-services : emprunts, reservations, notifications. Les operations doivent etre coherentes sans lock… |
| 5 | Choix du broker d’evenements (Kafka) | Accepte | [5-broker-evenements-kafka.md](./5-broker-evenements-kafka.md) | Le systeme doit gerer des evenements fiables : reservations, rappels, notifications, operations de compensation. |
