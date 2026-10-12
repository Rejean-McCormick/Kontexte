# 01 — État des lieux vérifié dans le snapshot Ekole

Cette section résume les fichiers effectivement présents dans l'archive du 11 octobre 2026. **La présence d'un fichier n'établit ni la qualité pédagogique ni la disponibilité d'un service multiutilisateur déployé.**

## Existant à préserver

| Emplacement existant | Ce que le snapshot contient | Conséquence pour l'upgrade |
| --- | --- | --- |
| `catalogue/202_kristals.json` | 202 descriptions de Kristals pédagogiques (catalogue `ekole.catalogue/0.1`) | Référencer les IDs stables `qc-pri-*`, ne pas dupliquer les contenus |
| `kristals/<id>/authoring/CONTRAT_PEDAGOGIQUE.json` | Objectif observable, preuve attendue, familles, modalités de revue; 202 structures annoncées, qualité variable | Garder le Kristal propriétaire du contrat pédagogique |
| `site/eleve/data/eleves/catalogue.json` | 202 cours, disciplines, années/étapes **suggérées**, statut `pedagogical_preview_unreviewed` | Navigation inchangée; la suggestion d'année n'est pas une vérité officielle |
| `site/data/organisation-parcours.json` | Configuration années/cycles/4 étapes pédagogiques, 3 bulletins distincts | Ne pas confondre « étape » de projet et bulletin officiel |
| `site/data/parcours-affectations.json` | Table par année/étape, **listes vides** et provenance éditoriale | Pas de placement automatique officiel du fait de la présence d'une mission |
| `site/eleve/data/kristals-experiences.json` | Expériences v11 proposées; progression « découvrir, essayer, expliquer, explorer » | Réutiliser les phases comme ressources pour missions, pas les écraser |
| `site/eleve/labo/data/catalogue.json` | MiniLab v14 (entraînements déterministes, candidats) | Réutiliser les calculateurs pour preuves élémentaires, sans déduire validation officielle |
| `site/eleve/data/activites-v14.json` | Raccordements d'activités; propositions non approuvées | Ne pas présenter ces liens comme correspondances officielles |
| `site/eleve/app.js` | Interface statique; commentaire explicite : « No account, tracking, assessment, or gradebook » | **Aucun suivi individuel réel actuellement**; besoin d'un service dédié sécurisé |
| `tools/compiler_experiences_v11.py` | Compilation d'expériences depuis `experience/SCENARIO_APPRENTISSAGE.json` | Ajouter une compilation de missions **parallèle**, non intrusive |
| `tools/synchroniser_ekole_apps.py` | Reconstruction des vues Élève et vérifications de catalogues/visuels/mondes | Nouveau compilateur à intégrer après tests et feature flag |
| `tools/export_ekole_eleve_v8.py` | Export Élève statique par **liste blanche** et contrôles de médias | Ne pas exporter un dossier de missions par simple copie globale; liste blanche explicite |
| `tools/serve_enseignant.py` | Serveur de prévisualisation local, session/CSRF, **pas authentification scolaire** | Ne pas y mettre des dossiers de vrais enfants avant création d'un service approprié |
| `docs/CONTRAT_COURS_PARCOURS.md` | Contrat cours ≠ parcours; quatre étapes pédagogiques non bulletin | Conserver compatibilité d'usage manuel cours/matière |
| `docs/07_SECURITE.md` | Portail statique sans comptes, notes ou données personnelles | Les preuves identifiantes restent hors de l'export statique |

## État réel du problème

Le catalogue et la navigation classent aujourd'hui les cours par matière, année et étape. Cela **ne rend pas obligatoire** ce classement pour l'expérience future. En revanche, on ne peut pas seulement coller une couche CSS sur le site et prétendre avoir une progression validée : les données d'élèves et les décisions d'évaluation n'existent pas encore dans le portail anonyme.

Des ID Ekole **présents dans le catalogue** peuvent être reliés à un pilote : `qc-pri-fr-021` (rédiger phrases et paragraphes; suggestion 3e), `qc-pri-als-006` (parler de situations familières; suggestion 3e), `qc-pri-ap-003` (composer dans l'espace; suggestion 2e), `qc-pri-ma-025` (longueurs, masses et capacités; suggestion 1re), `qc-pri-ma-017` (pourcentages/proportionnalité; suggestion 6e). **Ce sont des pistes locales, non des équivalences ministérielles validées.** Le calcul explicite d'un pourcentage de taxe en 3e année est donc un enrichissement accompagné, pas une maîtrise officielle présumée.

## Invariants non négociables

1. **Aucune mutation des Kristals sources** au seul motif qu'un élève choisit un rôle.
2. **Aucun score unique multi-matières** : chaque compétence réclame un critère, une preuve et un niveau d'autonomie.
3. **Aucune preuve d'apprentissage créée par présence ou participation seule**.
4. **Rôle pédagogique ≠ permission informatique**; ne jamais transformer « Sorcière » en rôle d'accès Orgo/Moodle.
5. **Données d'enfants isolées du site statique** et de l'export élève; refus de publication appliqué au service/au fichier livré, jamais seulement avec un voile CSS.
6. **Aucune IA distante nécessaire à l'exécution de base**; HTML/texte multilingue compilés et revus préalablement.
7. **Aucun corrigé secret dans un HTML public**; la pratique formative et l'évaluation sécurisée n'ont pas la même architecture.
8. **Le professeur conserve le jugement pédagogique** et approuve les événements physiques, dépenses et publication des travaux.
9. **Un parcours de mission hors rôle reste disponible**; personne n'est obligé de jouer un personnage.
10. **La compatibilité « cours classiques » reste entière** afin de ne pas couper l'apprentissage conventionnel.

## Frontière Orgo

`znapshot_Orgo_10112135.zip` documente un Work propriétaire des `Case`, `Task`, `Signal`, `Workflow`; un Scenario Injector synthétique `orgo.scenario.v1` n'est **pas** un moteur scolaire complet. `znapshot_Orgo_Worlds_10112135.zip` sépare `World`, `WorldRelease`, `WorldMembership` et provenance des workflows d'exécution. Toute connexion est donc **une extension à écrire et tester**, pas une capacité déjà installée dans Ekole.
