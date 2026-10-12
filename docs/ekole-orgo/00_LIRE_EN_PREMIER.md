# Ekole — Upgrade : missions interdisciplinaires orchestrées avec Orgo

**Spécification fonctionnelle et technique v1.1 — 11 octobre 2026**  
**Statut : proposition de conception prête pour revue; non installée, non homologuée, non certifiée.**  
**Base examinée :** `znapshot_Ekole_10112210.zip` ; contexte d'interopérabilité : `znapshot_Orgo_10112135.zip`, `znapshot_Orgo_Worlds_10112135.zip`; concept de rôles : `Orgo_Ekole_Cadres_de_roles_v01.zip`.

## Décision en une phrase

**Orgo orchestre seul les missions individuelles ou collectives. L'enfant vit des missions transdisciplinaires et coopératives; le programme québécois devient un référentiel versionné d'apprentissages et de preuves, plutôt qu'une séparation obligatoire des activités par matière.** Les cours actuels restent accessibles comme bibliothèque et outil de rattrapage, pas comme horaire contraignant pour le moteur de missions.

## À lire dans l'ordre

1. `01_ETAT_DES_LIEUX_ET_INVARIANTS.md` — ce qui existe réellement dans le snapshot.
2. `02_ARCHITECTURE_CIBLE.md` — **Orgo comme seul orchestrateur**; autorité Ekole sur connaissances et preuves.
3. `03_FRAME_UNIVERSEL_ROLES_ET_MISSIONS.md` — modèle de rôle, trame narrative, interactions et adaptation.
4. `04_REFERENTIEL_PREUVES_ET_RAPPORTS.md` — « array » curriculaire, maîtrise, validation, relevés enseignant/ministère.
5. `05_PILOTE_FETE_SORCIERE.md` — mission intégrée complète, étapes, coopération et calculs.
6. `06_MEDIAS_IDENTITE_CONFIDENTIALITE.md` — photos, tags, refus, publication, consentement et sécurité.
7. `07_MIGRATION_ROADMAP_ET_TESTS.md` — hooks concrets, livraisons incrémentales, tests et non-régressions.
8. `08_DECISIONS_OUVERTES_ET_RISQUES.md` — choix non résolus, hypothèses et arbitrages.
9. `09_ADR_ORGO_GRAND_ORCHESTRATEUR.md` — décision d’architecture, mission solo, simulation, propriété des données et tests de transfert.
10. `annexes/` — exemples JSON et schémas **proposés** (pas les contrats déjà actifs).

## Ce que contient le pack

- Documents Markdown conçus pour être copiés sous `docs/UPGRADE_MISSIONS_INTERDISCIPLINAIRES_V1/` à la racine d'Ekole.
- Contrats JSON Schema et exemples **autonomes**, sans installation ni écriture dans les fichiers existants.
- Aucun contenu HTML généré, aucune image, aucune donnée réelle d'enfant ni migration effective de base de données.

## Glossaire qui évite les confusions

- **Kristal source** : connaissance et contrat de cours; autorité sur les notions et critères déjà décrits.
- **Rôle pédagogique / `RoleFrame`** : identité, langage, actions possibles, présentation; **jamais** un rôle RBAC.
- **Mission / `MissionFrame`** : situation-problème qui traverse plusieurs disciplines et produit un résultat concret.
- **Instance de mission** : exécution datée avec participants et tâches attribuées; ne fait pas partie du fichier de définition.
- **Preuve** : artefact ou observation vérifiable; une consultation n'est pas une preuve de maîtrise.
- **Curriculum map** : liens qualifiés des objectifs Ekole avec sources officielles versionnées.
- **Vue curriculaire (« array »)** : projection calculée à partir des événements pédagogiques, non banque de vérité mutable.
- **Étape pédagogique Ekole** : 1 à 4 par année, **distincte** des trois étapes officielles de bulletin.
- **WorldRelease** : origine/version de la configuration Orgo_Worlds; pas copie des tâches.

## Résultat attendu d'un pilote

Un élève de 3e année, qui choisit « Sorcière », fabrique un chapeau d'origami, compose une invitation bilingue, rencontre un camarade indiqué par l'enseignant/Orgo, contribue à sa tâche, coordonne quatre personnes, paye en Klownkoins et effectue les comptes avec l'enseignant. Ekole enregistre **ce qui a été travaillé et ce qui a réellement été démontré** dans chaque discipline sans assigner une maîtrise automatique. Les productions photographiées restent privées par défaut; seules les vues autorisées sont publiées.

**La mission a une fin réelle et motivante, tout en conservant les frontières techniques et pédagogiques.**

**Note de compatibilité :** le pack garde ses fichiers de cadres JSON v1 comme source de contenu; il n'autorise pas un second moteur de transitions côté Ekole. Le compilateur doit traduire les intentions de scénario vers Orgo sous contrat. Les routes/API de ce compilateur restent à concevoir et à qualifier.
