# 02 — Architecture cible v1.1 : Orgo comme moteur canonique

> **Révision importante :** cette version annule le schéma v1.0 où Ekole possédait un `MissionRuntime` et où Orgo n'était qu'un `SocialMissionAdapter` facultatif. Pour une **mission interactive orchestrée**, Orgo est le moteur dès le premier élève, y compris en solo.

## Schéma d'ensemble

```text
Kristals Ekole + références PFEQ            Packs versionnés (RoleFrame/MissionFrame)
       |                                                  |
       |                                     Scénarios, indices, tensions, i18n
       |                                                  |
       |                        mapping/compilation contrôlée vers contrats Orgo
       |                                                  |
       |                                      Orgo_Worlds : World/WorldRelease
       |                                                  |
       +-------------------  ORGO  -----------------------+
                             Signal
                       Work : Case / Task
                WorkflowVersion / Process / Routing
                Informations autorisées au bon moment
                         |            |
            vue Ekole HTML/CSS        constats/actions/proofs
                         |            |
                   Expérience élève   |
                              \       /
                          preuves scolaires
                                  |
                        registre pédagogique Ekole
                                  |
                     matrice québécoise et rapports
```

**Orgo_Worlds est une frontière de contexte et de versions, pas un deuxième runtime opérationnel.** Les deux archives distinguent explicitement leurs propriétés : Orgo possède Work/Case/Task/Signal et les workflows; Worlds possède World, release, membership et routage.

## Autorités

| Domaine | Source de vérité |
| --- | --- |
| État de mission, acteurs, mandats, dépendances, ordonnancement et distribution d'information | Orgo |
| Définition des tensions/problèmes et rôles narratifs | Pack de scénarios contrôlé |
| Monde, release, contexte de simulation | Orgo_Worlds |
| Matières, compétences, connaissances, réponses de MiniLab, qualification du curriculum | Ekole/Kristals |
| Preuves scolaires, maîtrise et validation | Ekole, dans un stockage pédagogique sécurisé |
| Photos/tags/consentement de publication | Service média gouverné, distinct des Tasks Orgo |

**Deux notions de preuve** coexistent sans se confondre : Orgo peut attester qu'une Task a été exécutée; Ekole peut attester qu'une compétence a été démontrée dans des conditions précisément décrites. L'une n'implique pas l'autre.

## Orgo ne distingue pas « solo » et « groupe » comme deux moteurs

- **Solo :** Orgo assigne et séquence les tâches d'un seul élève, gère tentatives, indices, matériel disponible, délais et branches; une Case durable est créée selon la pertinence du contexte, et on évite un Task par clic.
- **Coopératif :** exactement les mêmes primitives gèrent plusieurs participants, la répartition d'indices, les rencontres et les jointures.
- **Simulation :** les contraintes sont construites et signalées comme synthétiques. Le moteur Orgo utilisé est le vrai moteur de travail, avec les mêmes garanties de version et d'idempotence; les effets réels (paiement, envoi externe, publication) sont bloqués ou explicitement admis dans leur environnement.

## Le rôle comme couche CSS et comme lexique d'actions

Le thème `RoleSkin` personnalise les couleurs, personnages, vocabulaire, objets, HTML et parfois la mise en situation. Il n'attribue **aucun droit RBAC**. Les aides privées et le niveau ne sont ni affichés dans le thème public ni déduits d'un diagnostic. Les mêmes connaissances et critères de validation sont accessibles sous plusieurs habillages.

Le `MissionFrame` porte les objets, tensions, informations et dépendances; sa réalisation opérationnelle se fait **en Orgo**. Aucun ordonnanceur d'état supplémentaire dans Ekole.

## HTML et multilingue

La source sémantique et les valeurs validées alimentent un compilateur de présentation Ekole. Les propositions HTML d'IA passent par composants/slots approuvés, échappement, CSP, vérifications de contraste/accessibilité et revue des traductions. SemantiK peut être un outil pour réaliser des phrases sous ses contrats; il ne remplace pas le système de Workflows. Les secrets et corrigés ne figurent jamais dans les projections HTML servies à un élève non autorisé.

## Interface d'événements proposée (pas API implémentée)

| Événement conceptuel | Traitement canonique |
| --- | --- |
| `scenario_started` | Orgo accepte un Signal, référence scénario/World/release et ouvre Work approprié |
| `fragment_eligible` | Orgo décide de la disponibilité selon sa version de workflow et les droits d'accès |
| `artifact_submitted` | Référence d'artefact, réception et revue par service propriétaire; Orgo reçoit résultat minimal |
| `assistance_requested` | Orgo décide si indice, matériel, personne ou branche devient disponible |
| `task_completed` | Orgo progresse opérationnellement; Ekole n'en infère aucune maîtrise automatique |
| `learning_evidence_validated` | Ekole enregistre sa preuve; Orgo peut recevoir un événement/référence minimal pour continuer |
| `mission_closed` | Orgo clôture le contexte opérationnel; Ekole finalise séparément le bilan pédagogique |

Les noms ci-dessus sont des **événements de conception**, pas une promesse de routes API déjà présentes. Les intégrer aux canaux et contrats acceptés par Orgo après qualification.

## Le tableau de bord québécois

La matrice curriculaire reste une projection de preuves Ekole avec identifiants source, version, critère, contexte, soutien, statut et validation. Une même mission peut pointer vers plusieurs cours sans en réécrire les Kristals. Ne pas confondre 4 étapes internes Ekole avec les périodes institutionnelles de bulletin.

## Déploiement

Ekole peut continuer à fonctionner comme portail de cours **sans** Orgo lorsque les missions sont désactivées. En revanche, une **mission orchestrée** exige Orgo, qu'elle soit solo ou collective. Un export statique d'une démonstration sans état multiutilisateur est une prévisualisation, **pas** un second moteur d'exécution. Le déploiement local/hors ligne de l'ensemble Orgo+Ekole reste une cible à tester concrètement (identité, réseau, données, reprise).

Voir `09_ADR_ORGO_GRAND_ORCHESTRATEUR.md` pour l'argumentaire, la simulation et les tests de transférabilité.
