# Audit consolidé — ce qui est déjà là et ce qu’il faut raccorder

## Autorités existantes (source examinée)

| Responsable | Élément retrouvé | État vérifié dans l’archive | Ne pas créer en double |
|---|---|---|---|
| Kontexte | `data/missions/*.json`, `schemas/mission.v1.schema.json`, `data/roles/*.json`, pilote fête, 202 cours référencés indirectement | 11 missions dont 1 solo; 38 cadres de rôles; **60 trames neutres, 60 overlays QC3, 34 micro-situations et 36 semaines proposées**; modèles de fragments/jointures | Banque de missions et définition des rôles |
| Ékole | `tandem/projection.py`, enseignant preview, parcours de rôles, `activite_locale.py` | Démo P1 locale sans connexion runtime; exercice local possible via Inkuisite | Portail élève/enseignant, compétence scolaire |
| Ékole Québec | 202 contenus candidats + paquets locaux, non homologués | Corpus existant | Refaire les cours |
| Inkuisite | stock `attempts`, évaluation d’exercice, journal | Tentatives locales sans identité scolaire qualifiée | Nouveau correcteur de base |
| Kompose | validation et prévisualisation synthétique, règles d’affectation documentées | Pas de solveur de production ni admission réelle | Moteur d’attribution parallèle dans Ékole |
| Akor | intention, projection, contrats de pont | Revue synthétique / non déployée pour enfants | Nouvel orchestrateur |
| Orgo | Case, Task, Signal, Workflow, scénario `orgo.scenario.v1`, injector | Moteur opérationnel existant; admission pédagogique non terminée | Un second moteur de tâches |
| Orgo_Worlds | World, WorldRelease, WorldMembership; pack/injection séparés | Frontière de versionnement et de navigation; pas de World scolaire déployé confirmé | Stocker les Tasks dans Worlds |
| Konnaxion | identités, échanges et collaboration | Produit existant mais pas de Kidaxion détecté dans la recherche des sources | Réinventer messages et identités |
| Kidaxion | Nom et intention apportés dans la conversation | Interface simplifiée **à réaliser**, pas un service source confirmé | Un backend social distinct |

## Quatre écarts qu’il faut corriger avant la classe

**A. Admission et lancement.** Un enseignant authentifié doit approuver la mission, les rôles, les accès, la WorldRelease et la session. Les fixtures de démonstration P1/P2 ne prouvent pas cette admission.

**B. Distribution sécurisée de l’information.** Les fragments des rôles doivent être libérés par les autorisations Orgo, après contrôle des participants; un bouton enfant ne peut pas se donner un rôle ni révéler un corrigé.

**C. Journal des apprentissages.** Tracer `learner_ref` pseudonyme, `mission_run_id`, `step_id`, `objective_ref`, `artifact_ref`, `support`, `result`, `validator`, `date`, `version`; ne jamais convertir une tâche Orgo achevée en compétence acquise automatiquement.

**D. Recommandation pédagogique.** Proposer des tâches parce qu’il manque des **preuves variées et récentes**, en tenant compte du soutien et du contexte. L’enseignant tranche; les enfants ne voient ni classements ni difficultés privées des autres.

## Règle de recommandation proposée (non implémentée)

Classer chaque objectif d’un enfant par : non rencontré / rencontré / pratiqué / démontré / validé / transféré. Afficher le nombre d'occasions distinctes, de tentatives et de réussites observables, les dates, les contextes, les aides. Proposer en premier une mission contenant des tâches différentes liées à un objectif **peu documenté**, puis une tâche de transfert si une compétence est déjà démontrée dans un contexte. Ne jamais baser l'affectation sur le seul nombre de tâches ou un classement social.

## Correspondances à revoir

- Les 11 missions ne sont pas toutes également détaillées : la fête à 11 étapes, les autres souvent des squelettes à 3 étapes et une mission solo. Les détailler progressivement.
- La « fête de la sorcière » possède plusieurs représentations : mission Kontexte à 11 étapes, aperçu enseignant/fixture Ékole synthétique à 4 tâches, intention de revue Orgo à 11 intentions. **Ne pas traiter les 4 tâches comme l’exécution de la mission complète.** Harmoniser références et versions avant d’en faire un produit.
- Orgo_Worlds conserve seulement l’enveloppe World/WorldRelease; le pont vers Orgo doit passer par l'interface autorisée, sans SQL transversal.
- Une réunion/rencontre avec une personne nouvellement arrivée doit rester respectueuse, volontaire ou fictive; éviter que l’enfant lui demande des informations personnelles sur sa migration.

## Ordre d’exécution recommandé

1. Approuver le modèle d’édition Kontexte et réviser le pilote *Fête de la sorcière* **sans changement d’ID**.
2. Création/membership du World privé, WorldRelease épinglée et référence de scénario.
3. Un parcours solo de mission Orgo réel et sécurisé, sans social/indices entre enfants.
4. Puis la version coopérative : stations, fragments, aides et absences; interface Kidaxion simple, modérée.
5. Enfin : preuve Ékole et tableau de couverture par élève, filtres d’objectifs, recommandations explicables.

## Prudence sur la notion de World

« Un scénario = un World » est une bonne **convention de présentation** pour ton projet, pas une nouvelle définition du modèle de données Orgo_Worlds. Le World reste une frontière opérationnelle d’accès et d’isolation. Une nouvelle classe ne doit pas voir les membres ni les artefacts d’une autre classe même si elle utilise le même scénario source; il faut donc choisir une clé World tenant compte du périmètre privé d’exécution, et non seulement du titre de l’aventure.
