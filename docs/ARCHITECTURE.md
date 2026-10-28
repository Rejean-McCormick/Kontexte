# Kontexte : architecture canonique


## Principe

Une situation pédagogique ou professionnelle est constituée d'acteurs, de problèmes construits (simulation) ou réels, d'informations, de tâches, de relations, d'artefacts et de critères de succès. **La situation n'est pas propriétaire de sa propre machine à états.**

```
Orgo_Work + Orchestration (source canonique des Cases / Tasks / Signals / Workflows)
       │ autorisations / événements / tâches / transitions
       ├── World + release figée (Orgo_Worlds)
       │
       ▼
Kontexte (dépôt de définitions, modèles, rendu statique, adaptateurs)
       ├── Rôle = thème CSS + vocabulaire + perspective + choix de tâches
       ├── Mission = fiction + activités + ressources + fragments + associations
       ├── Projection autorisée HTML/CSS (+ traductions relues)
       ├── Klownkoins = calculs fictifs et vérifiables
       └── Contrats et preuves d'exercices (hors états Orgo)
       │
       ▼
Ekole / Kristals / MiniLab / PFEQ (connaissances, pratique, validation pédagogique)
```

### Limites de ce dépôt

- **Orgo** détient état opérationnel et transitions ; aucune classe Kontexte ne joue de rôle de moteur de workflow.
- Les projections sont générées hors ligne à partir des données, sans moteur de texte improvisé en temps réel. Les indices sont masqués par défaut.
- Pour distribuer de vrais fragments en fonction d'un événement, Orgo doit d'abord fournir l'autorisation par un canal serveur sécurisé. Ce raccordement n'est **pas encore opérationnel** ; voir [ORGO.md](ORGO.md).
- **Ekole** et un service d'évaluation scolaire habilité détiennent les validations individuelles, pas Orgo. Le stockage SQLite de Kontexte est uniquement un **exemple de développement avec des identités fictives**.
- Orgo_Worlds peut versionner un pack dans une World release, mais il ne détient pas les Cases/Tasks.
- Aucune note ministérielle, homologation ou conformité au PFEQ n'est prétendue.

## Contrôle par couche

| Domaine | Source canonique | Sur Kontexte |
|---|---|---|
| identité, affectation, mission en cours | Orgo + fournisseur d'identité | références, aucune autorisation de sécurité créée par un rôle |
| séquence, signal, état, gestion d'imprévu | Orgo | plan d'intention + fixture initiale |
| connaissances et objectifs | Ekole/Kristals | liens internes candidats avec 202 IDs |
| maîtrise et bulletin | enseignant / service autorisé | preuves factices, export d'illustration |
| rendu visualisé | Kontexte / Ekole | HTML/CSS contrôlé, sans scripts d'exécution |
| images privées et consentements | service média scolaire sécurisé | politique de publication restrictive, aucun hébergement |

## Pourquoi hors ligne ?

Le calcul des projections et la préparation du scénario sont localisables. L'orchestration collaborative réelle demande Orgo joignable sur le réseau local de l'école. Les identités et médias doivent être hébergés dans un périmètre dédié, conformément aux exigences applicables.
