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
