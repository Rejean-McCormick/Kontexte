# 07 — Feuille de route v1.1 : raffiner Orgo avec les scénarios d'Ekole

## Stratégie de migration

**Ne pas réécrire les 202 Kristals. Ne pas créer de MissionRuntime Ekole. Ne pas ajouter un second cycle de Task/Case.** Développer des **packs de situations**, leurs projections pédagogiques et les adaptateurs nécessaires aux contrats de Work/Orchestration d'Orgo.

Un dépôt `Ekole-Missions` est facultatif comme **bibliothèque de contenu**, mais il ne détient aucune machine d'exécution. Les nouvelles capacités génériques d'orchestration sont implémentées et qualifiées **dans Orgo**, car elles serviront à d'autres domaines.

## Répartition des changements

| Dépôt | Changements proposés | Ne doit pas faire |
| --- | --- | --- |
| **Orgo** | admission des scénarios éducationnels synthétiques; règles génériques de livraison d'indices; dépendances/jointures; solo/groupe; délais/replis; audit/idempotence | créer des notes scolaires, connaître les détails d'un diagnostic, publier des photos sans autorité |
| **Orgo_Worlds** | configurations/release de mondes, fixtures synthétiques, contexte de scénario | posséder Workflow/Case/Task/Signal ou bases opérationnelles d'Orgo |
| **Ekole** | correspondances curriculaires, preuves, MiniLab, rendu HTML/CSS/i18n, enseignant, exports non sensibles | implémenter des transitions de mission concurrentes à Orgo |
| **Pack de scénarios** | RoleFrame, MissionFrame, problèmes, indices, contenus, transpositions, tests | stocker l'état réel d'exécution ou inventer ses propres APIs Work |
| **Service médias gouverné** | coffre privé, consentements, révocation, filtrage tags | considérer `Task COMPLETED` comme permission de publier |

## Parcours de livraison

### Phase 0 — Audit des contrats, sécurité et mappings

- Identifier le chemin de Signal et les actions Orgo utilisables **aujourd'hui**, distinguer contrats codés et cibles documentées; établir les interfaces à enrichir.
- Établir correspondances candidates des apprentissages du pilote au catalogue Ekole et au PFEQ, puis revue pédagogique.
- Définir un scénario synthétique par versions et IDs stables, sans UUID runtime dans la source.
- Conditions de sortie : contrat Orgo signé, protection mineurs décidée, aucun transfert de PII dans les fixtures.

### Phase 1 — Pilotage SOLO dans Orgo

- Construire une mission pour un participant avec étapes, informations distribuées dans le temps, aide sur erreur, demande de matériel et clôture.
- Injecter/planifier dans Orgo avec l'outil de scénario existant si les opérations le permettent; ajouter à Orgo les actions génériques nécessaires après revue.
- Ekole affiche la vue déterminée par Orgo et réalise les exercices MiniLab; un calcul erroné ouvre la branche d'aide et non une note automatique.
- Conditions de sortie : pas de transition concurrente, pas de fuite de corrigé, reprise/idempotence et variation de RoleSkin neutre/sorcière.

### Phase 2 — Mission COOPÉRATIVE avec fragments A+B

- Répartir les informations entre deux élèves (ou plus), gérer autorisations, jointure, messages, disponibilité d'un partenaire et solution de secours.
- Orgo orchestre l'équipe de quatre, les tâches distinctes et la synchronisation.
- Conditions de sortie : join A+B déclenchée une fois; aucune récompense doublée sur reprise; absence partenaire gérée équitablement.

### Phase 3 — Suivi pédagogique Ekole

- Relier les constats et productions à un journal append-only pédagogique, distinct de la preuve de Work.
- Construire la `curriculum array` par élève, version de référentiel, période, preuve, soutien, jugement enseignant.
- Conditions de sortie : rapport reproductible couvert / pratiqué / maîtrisé / validé; refus de conversion automatique `Task COMPLETED`→`mastered`.

### Phase 4 — Klownkoins et publication gouvernée

- Comptes de monnaie fictive, transactions testables et contrôles de calcul; aucun effet financier réel.
- Publication des **œuvres** plutôt que portraits, consentement granulaire et retrait effectif.
- Conditions de sortie : cohérence ledger; refus/absence de consentement bloquent binaire et métadonnées publiques.

### Phase 5 — Qualification comme banc d'essai d'Orgo

- Réexécuter les mêmes patterns : solo, duo, équipe, absent, retard, contradiction, résolution, nouvelle quête.
- Tester un exemple **non scolaire** utilisant exactement les mêmes primitives (p. ex. coordination d'un atelier interne) sans code pédagogique spécial dans le moteur Orgo.
- Conditions de sortie : amélioration mesurée du noyau Orgo et non fonctionnalité isolée liée à un scénario d'enfant.

## Vérifications minimales

1. Même problème, plusieurs apparences; nombres et critères identiques.
2. Le niveau d'assistance ne devient pas visible à un autre élève.
3. Le fragment secret n'arrive pas avant son garde de livraison, ni chez un autre membre du World.
4. Replay de Signal ne crée pas deux Tasks, deux paiements ou deux débloquages.
5. Simulation ne peut pas provoquer d'email/achats/publication externe sans autorisation explicite.
6. Erreur/réponse correctes passent par le vérificateur Ekole; Orgo décide seulement la prochaine transition de travail.
7. La promotion d'une WorldRelease n'altère pas une mission déjà épinglée à une release antérieure.
8. Le journal scolaire et le rapport se reconstruisent même si la mission Orgo a été clôturée.
9. Le refus ou retrait d'autorisation de publication supprime l'accès au média/tag public.
10. Les pages Ekole de cours continuent de fonctionner si le mode Missions est désactivé.

## Compatibilité et rollback

Les nouvelles fonctionnalités doivent être désactivables indépendamment : scénarios de mission dans la projection Ekole, intégration Orgo, suivi pédagogique et publication média. **Si Orgo est indisponible, ne pas relancer secrètement un moteur parallèle dans Ekole** : afficher une indisponibilité claire, conserver la consultation conventionnelle des cours et proposer le mode papier/enseignant. Garder des preuves et des événements dans leurs propriétaires respectifs. Toute publication ou mutation opérationnelle doit rester conforme aux autorisations et aux procédures d'export de chacun.

## Vérifications des dépôts

- **Orgo :** utiliser sa procédure `docs/Technical-Reference/LOCAL_VALIDATION.md` et la suite de tests du Work/Orchestration/Scenario Injector, à qualifier dans l'environnement réel.
- **Orgo_Worlds :** appliquer les validations de `docs/Technical-Reference/Worlds/13_TEST_AND_ACCEPTANCE_PLAN.md` et les commandes `validate-all/plan` du world-scenario, sans `inject --apply` sur instance non isolée.
- **Ekole :** conserver la baseline du snapshot (`tools/ekole.py verify`, `valider_parcours.py`, `valider_mini_labs.py`, tests). Ne pas considérer l'exécution des commandes comme une certification pédagogique.

Aucune modification de code ni de bases de données n'a été effectuée par cette documentation.
