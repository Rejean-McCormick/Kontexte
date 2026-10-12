# ADR-001 — Orgo est l'unique orchestrateur

**Acceptée, conception Kontexte v0.1.0.**

Contexte : les scénarios pédagogiques doivent produire du travail solo et collectif, distribuer des fragments d'information, gérer leurs dépendances et parfois engendrer des quêtes. Ces mécaniques se transposent aux organisations et doivent renforcer Orgo, sans créer une seconde machine à états dans Ekole.

Décision : Kontexte décrit, projette et adapte les expériences; Orgo conserve tout état opérationnel, notamment `Case`, `Task`, `Signal`, `WorkflowVersion`. Ekole conserve les connaissances et les preuves pédagogiques. Les propositions `joins`, dépendances et indices sont compilables **en intention**, mais leur exécution conditionnelle doit être confiée à Orgo une fois les primitives manquantes développées.

Conséquences : un snapshot de démonstration ne déclenche qu'une Task de préparation. Tant que l'exécution complète n'est pas qualifiée, ne pas annoncer de missions coopératives opérationnelles auprès d'une classe.

Référence : `docs/ekole-orgo/09_ADR_ORGO_GRAND_ORCHESTRATEUR.md`, archivée.
