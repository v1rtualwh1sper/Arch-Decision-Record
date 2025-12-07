# ADR - Architecture Decision Records

Les ADRs sont un outil léger et efficace pour documenter les décisions d’architecture logicielle. Ils permettent decapturer les raisons, alternatives, et conséquences des choix architecturaux, facilitant ainsi la maintenance et l’évolution des systèmes logiciels.
Ce dossier contient les ADR du projet. 
Chaque ADR est un fichier Markdown autonome.

## Template attendu

Chaque ADR doit contenir les sections suivantes :

```
#<Numero>.<Titre de la decision>
##Statut
Accepte / Rejete / Obsolete / En discussion
##Contexte
...
##Decision
...
##Alternatives envisagees
...
##Consequences
...
```

## Installation des outils locaux (hook)

Pour installer le hook local :

```bash
cp .git/hooks/pre-commit.example .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Commits atomiques & tags

Exemples pratiques pour un ADR individuel :

```bash
# créer une branche dédiée
git checkout -b adr/2-authn-oidc

# ajouter uniquement le fichier ADR (commit atomique)
git add doc/adr/2-authentification-oidc-oauth2-jwt.md
git commit -m "ADR: #2 Authentification OIDC/OAuth2 + JWT"

# push et PR
git push -u origin adr/2-authn-oidc

# Après revue et merge vers main, tagger une version ADR
git checkout main
git pull origin main
git tag -a v1.0-adr-final -m "ADR v1.0 - decisions initiales (DB, AuthZ, Sagas, Broker)"
git push origin --tags
```



## Génération automatique du sommaire des ADR

Pour faciliter la consultation des ADR, nous avons mis en place un script Python qui génère automatiquement un fichier `SUMMARY.md` dans le dossier `doc/`. 

### Fonctionnement

- Parcours tous les fichiers `.md` du dossier `doc/adr/`
- Extrait pour chaque ADR :
  - Numéro et titre
  - Statut (accepté, rejeté, en discussion)
  - Un extrait du contexte (premier paragraphe)
- Génère un tableau Markdown récapitulatif avec liens vers les fichiers ADR

### Utilisation

Depuis la racine du projet, exécuter :

```bash
python3 scripts/generate_adr_summary.py
```
