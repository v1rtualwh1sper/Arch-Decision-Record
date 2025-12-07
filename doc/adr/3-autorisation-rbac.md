#3. Autorisation RBAC

##Statut
Accepte

##Contexte
Le systeme comporte plusieurs types d’utilisateurs avec des privileges differents.

##Decision
Utiliser un controle d'acces base sur les roles (RBAC) stockes dans l’IdP. Les roles seront verifies via un middleware sur chaque service.

##Alternatives envisagees
- ACLs internes : Rejete.
- ABAC seul : Rejete.
- RBAC local dans le code : Rejete.

##Consequences
- Positives : Centralise, coherent, extensible.
- Negatives : Depend du bon parametrage IdP.

##Liens
- Depend de l’authentification OIDC (ADR #2).
