#2. Authentification OIDC/OAuth2 et tokens JWT

##Statut
Accepte

##Contexte
Le systeme doit authentifier des utilisateurs publics et internes. Besoins : SSO, gestion centralisee, tokens courts, securite forte.

##Decision
Utiliser OpenID Connect et OAuth2 avec un Identity Provider (ex : Keycloak). Utiliser des JWT courts pour l'acces et des refresh tokens securises.

##Alternatives envisagees
- JWT auto-geres sans IdP : Rejete.
- Sessions stateful : Rejete.
- API Keys : Rejete.

##Consequences
- Positives : Standardise, securise, scalable.
- Negatives : Dependence a un IdP.

##Liens
- Voir ADR #3 pour l'autorisation RBAC.
