# Banque de Worlds pédagogiques Ékole × Orgo — proposition v0.1

**Statut : contenu éditorial synthétique pour revue, non déployé et non destiné à des dossiers réels d’élèves.**

## Objet

Appliquer la convention **un scénario = un World Orgo** (par groupe/classe lorsque l’isolation le demande), sans transformer chaque station ou chaque problème en World distinct. Un World contient une aventure et son contexte versionné; Orgo conserve les Cases, Tasks, Signals et la progression effective. Les stations, les indices et les dialogues sont des étapes et des fragments de mission, pas des micro-Worlds.

Ce paquet ne crée **aucun World**, **aucune Case**, **aucune Task**, **aucun compte enfant** et ne modifie aucun dépôt source. Les fichiers JSON ne sont **pas** des fichiers `orgo.scenario.v1` injectables directement dans Orgo; ce sont des définitions `kontexte.mission/1` compatibles avec son schéma source.

## Ce qui existait avant cet apport

Le catalogue référence, sans les recopier, les **11 missions déjà présentes** sous `Kontexte/data/missions/` : Fête de la sorcière, boulangerie, chantier-maquette, conseil-village, expédition, atelier-mécanique, jardin-fermier, laboratoire, salon-coiffure, chaudron des mesures (solo) et spectacle-clown. Ces sources conservent leur autorité et leurs IDs. D’autres contenus actifs/candidats existent déjà dans Ékole Québec, Inkuisite, Akor et Kompose : on les relie par référence, on ne les clone pas.

## La vraie banque déjà existante : 60 + 60 + 34

Au-delà des 11 fichiers `kontexte.mission/1`, les sources comprennent **60 trames neutres**, **60 adaptations Québec/3e année**, **34 micro-situations** et un parcours pédagogique indicatif de **36 semaines**. Les nouvelles missions proposées ici sont des **développements** de trames déjà existantes; voir `INDEX_TRAMES_EXISTANTES.md`. Ces niveaux ne s’additionnent pas pour prétendre avoir 165 Worlds exécutables.

## Contenu ajouté

Six nouvelles missions **synthétiques** au format Kontexte : grand ménage chez mamie, randonnée à vélo, spectacle des histoires inventées, rallye des métiers, mystère de la bibliothèque, pique-nique des quatre saisons. Les missions utilisent les **rôles déjà catalogués** sous `Kontexte/data/roles`, des fragments avec libération `orgo_authorized`, des dépendances acycliques, des jointures et des modes d'adaptation réutilisés du schéma existant. Les `curriculum_ids` restent vides : les liens pédagogiques doivent être qualifiés par Ékole/CurriculumMap avant d’être annoncés comme validés.

## Chemin d’intégration sans doublon

1. **Édition :** déposer les scénarios retenus dans `Kontexte/data/missions/`, sous revue humaine et tests de référence; enrichir les scénarios existants au lieu de les remplacer.
2. **Préparation :** faire produire à Kompose un plan de rôle, d’accès, de dépendances et d’adaptations; l’attribution doit être validée par l’enseignant, non pilotée par un score brut.
3. **Pont :** Akor transporte les intentions et les projections approuvées, sans devenir détenteur de tâches ou de preuves scolaires.
4. **World :** Orgo_Worlds crée/référence un World privé (`world_key`) et une WorldRelease immuable; vérifier le membership réel et l’isolation entre classes. Cette étape reste à développer/qualifier pour les missions réelles.
5. **Exécution :** compiler/approuver un scénario opérationnel vers le **contrat distinct** `orgo.scenario.v1`, valider/planifier via `Orgo/tools/scenario-injector`, puis autoriser explicitement l’application par un acteur enseignant vérifié. Ne jamais importer directement le JSON Kontexte.
6. **Kidaxion :** future interface enfant *simplifiée de Konnaxion*, avec actions structurées (demander, expliquer, recevoir un indice, confirmer); aucun code Kidaxion retrouvé dans les sources examinées. Konnaxion assure les canaux si autorisés; Orgo décide quelles informations peuvent être révélées.
7. **Pédagogie :** Ékole rattache des **preuves individuelles** à des critères/version/objectif, indépendamment de `Task COMPLETED`. Le CurriculumReadModel est une **conception documentée**, pas encore un service complet vérifié.

## Granularité à préserver

- **Banque :** modèle pédagogique réutilisable, sans identités.
- **World :** aventure isolée, référence de scénario + release. Dans un établissement avec plusieurs classes, un World distinct par groupe peut être nécessaire pour éviter toute exposition croisée.
- **Case / mission run :** participation d'un groupe sur une période donnée, sous la WorldRelease épinglée.
- **Task :** action apportant un livrable ou une décision. Éviter une Task par clic/message.
- **Station / rencontre :** étape de mission, rôle narratif et fragments autorisés.
- **Preuve pédagogique :** trace validable par Ékole pour un élève; n'est pas une Task.

## Tests de contenu déjà exécutés

Les six JSON passent le schéma `Kontexte/schemas/mission.v1.schema.json`. Références des rôles, graphes de dépendances, IDs et jointures contrôlés par programme. Les six missions ont également passé une **prévisualisation de rôle locale Kompose** (`preview-kontexte --role`, simulation seulement). Aucun test HTTP Orgo, aucun déploiement, aucune intégration d'identité, aucun suivi d’enfant réel.

Voir `INDEX_TRAMES_EXISTANTES.md`, `AUDIT_ET_PRIORITES.md`, `PARCOURS_EXEMPLES.md`, `PISTES_SUPPLEMENTAIRES.md`, `catalogue.json`, `validation.json`.
