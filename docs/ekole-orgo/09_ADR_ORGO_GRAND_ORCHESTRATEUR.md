# ADR-009 — Orgo est le grand orchestrateur; Ekole est un banc d'essai pédagogique

**Statut : décision d'architecture adoptée pour cette proposition, non implémentée**  
**Date : 11 octobre 2026**  
**Remplace** dans le document précédent toute proposition d'un `MissionRuntime` Ekole propriétaire de transitions, d'une orchestration « réservée au multiélève » ou d'un pont Orgo seulement optionnel pour les missions actives.

## 1. Thèse

> Une seule machine, Orgo, distribue la bonne information à la bonne personne au bon moment et pilote les états de travail. Ekole fournit des situations-problèmes scolaires construites et simulées, les connaissances et les preuves d'apprentissage.

Une mission pédagogique est un **cas d'utilisation du moteur Orgo existant**, solo ou collectif. On ne crée ni second moteur de workflow dans Ekole ni autre source canonique de `Case`, `Task`, `Signal` ou d'affectation. Les scènes scolaires servent à tester et raffiner la machine sur des cas nombreux, sûrs, répétables et mesurables, puis à transférer les améliorations à d'autres usages d'Orgo.

## 2. Frontières d'autorité à respecter

| Objet | Propriétaire canonique | Règle |
|---|---|---|
| Mission en exécution, personnes assignées, état et transitions opérationnels | **Orgo**, via Work + Orchestration | Réutiliser `Case`, `Task`, `Signal`, version de Workflow et processus durables ; éviter un Task par microclic |
| Rejets, notifications, délais, escalades, distribution des informations | **Orgo** | Les gardes doivent être déterministes/auditables ; aucun indice sensible livré à une personne non autorisée |
| Configuration du World et provenance des releases | **Orgo_Worlds** | Control-plane uniquement ; ne détient jamais Work/Case/Task ; release épinglée |
| Savoirs, objectifs, MiniLab, critères et relevé scolaire | **Ekole / Kristals**, service pédagogique habilité pour données d'élèves | Référentiel versionné, preuves distinctes des statuts opérationnels |
| Définitions des situations, rôles pédagogiques, contenus et thèmes | **Pack de contenu de missions** (`Ekole-Missions` possible) | Données/présentations compilables, **pas** de moteur de workflow concurrent |
| Présentations HTML/CSS multilingues | **Ekole / compilateur de présentation** | Affiche la vue autorisée de l'état Orgo, sans décider à sa place de la progression |
| Médias identifiants et consentement de publication | **Service de publication autorisé** | Privé par défaut; consentement résolu avant toute exposition publique |

Le fait qu'Orgo conserve des preuves d'exécution n'en fait pas le juge de la maîtrise scolaire. `Task COMPLETED` signifie que l'acte a été déclaré/contrôlé selon son contrat, pas que la compétence PFEQ est acquise.

## 3. Deux types de situations, un seul moteur

**Situation réelle :** une demande arrive de l'extérieur et Orgo l'organise jusqu'à son aboutissement.  
**Situation éducative :** le concepteur crée intentionnellement une pénurie, une mission, une contradiction, un indice à recevoir, une réparation ou un budget fictif. Ces événements synthétiques entrent dans Orgo par des contrats d'entrée normaux, marqués comme simulation. 

**Ne pas simuler Orgo lui-même** : on simule les contraintes du monde et les problèmes soumis à Orgo. Un Workflow n'a pas besoin de savoir si le problème « manque un contenant » provient d'un vrai stock ou d'une fiche de jeu ; la provenance, les autorisations et les effets externes doivent toutefois empêcher qu'une simulation déclenche une vraie dépense, un message externe ou une publication involontaire.

## 4. Une mission solo n'est pas un cas spécial

Exemple de sorcière seule :

1. Un événement de mission crée/active le travail opérationnel Orgo.
2. Orgo donne à l'élève le mandat « préparer 8 lanternes », avec seulement les données nécessaires.
3. L'élève interagit avec une projection Ekole; MiniLab vérifie des calculs, et renvoie un constat/référence de résultat.
4. Orgo choisit le prochain état selon la **transition d'exécution** (tentative, aide demandée, réponse remise, matériau obtenu). Il ne déduit pas la maîtrise scolaire d'un simple clic.
5. Quand le calcul est incorrect, le scénario ouvre une branche d'indice ou de manipulation; quand la tâche est finie, il ouvre la suite de l'aventure.
6. Ekole associe les preuves aux éléments du programme, avec les critères de validation appropriés.

Une mission à quatre personnes utilise les mêmes primitives, mais avec des affectations distinctes, des jointures d'informations, des livraisons et des synchronisations entre Tasks.

## 5. Distribution ciblée d'information

Chaque fragment a une référence stable et un contrat : `owner`, `audience`, `release_condition`, `visibility`, `expires_at?`, `curricular_intent` (dans Ekole), `simulation_provenance`, `content_ref`. Orgo contrôle **à qui et quand** le fragment peut être livré; Ekole réalise **comment** il est présenté (HTML, version fr-CA/en révisée, audio, pictogrammes, aide). On évite de copier dans des événements publics des consignes privées ou des données d'élèves.

Règle-clé : **la tension est construite, mais le traitement est réel**. La personne reçoit un problème de la bonne hauteur; un indice ne part que lorsque le contrat de progression le prévoit; une absence de partenaire doit avoir un repli sûr. L'élève peut changer de `RoleSkin` sans changer les conclusions mathématiques ou les autorisations informatiques.

## 6. Interactions transversales à éprouver dans le pilote

```text
Conception du problème → pack versionné
  → World/release et scénario synthétique
  → Signal accepté (Orgo)
  → Case (contexte durable lorsque nécessaire) + Task(s)
  → WorkflowVersion épinglée / garde / affectation
  → InfoFragment autorisé → rendu Ekole par thème de rôle
  → action de l'élève → événement / pièce / résultat contrôlé
  → Orgo : suite, attente, indice, collaboration, nouvelle quête
  → Ekole : preuve d'apprentissage + revue + matrice québécoise
```

Pour le prototype, l'injecteur de scénario d'Orgo peut servir à `validate/plan/apply` des **fixtures synthétiques**, sans prétendre que les futures règles de jointure pédagogique sont déjà implémentées. Les règles/ports manquants seront ajoutés à Orgo par extension du moteur existant et soumis à ses tests, pas dupliqués côté Ekole.

## 7. Séparation entre contenu éducatif, orchestration et évaluations

- Le **RoleFrame** et le **MissionFrame** sont des sources de scénario; leurs transitions sont compilées/mappées vers le langage de Workflow/Process d'Orgo, pas exécutées en parallèle.
- L'**adaptation privée** peut déterminer la quantité de soutien ou le prochain fragment disponible; Orgo reçoit des droits/capacités d'interaction minimales, jamais une étiquette médicale publique.
- Le **correcteur** reste déterministe ou soumis à revue humaine. Orgo consomme l'état de réalisation pour choisir la prochaine action, pas pour attribuer une note officielle.
- **Klownkoins** : registre pédagogique virtuel dont les mouvements sont déclenchés par les états contrôlés d'Orgo, avec interdiction de conversion en argent réel ou d'effets financiers réels.
- **Consentement** : une autorisation de publication reste de compétence du service média; une Task terminée ne peut pas la remplacer.

## 8. Tests qui prouvent une amélioration d'Orgo

| Test | Mesure observable |
|---|---|
| Mission solo avec erreur puis indice | bonne transition, aucun dévoilement prématuré |
| Mission solo avec parcours enrichi | même rôle visible; variantes privées distinctes |
| Échange A+B entre deux élèves | jointure autorisée, un seul déblocage |
| Absence/retard/refus d'un partenaire | repli sans blocage ni culpabilisation |
| Équipe de quatre + dépendances | aucun déclenchement de spectacle avant les sorties requises |
| Répétition d'un Signal et reconnexion | idempotence; pas de double quête ou paiement |
| Relance avec ancienne WorldRelease | déroulé reproductible et contexte historique respecté |
| Exécution du même pattern hors école | les primitives Orgo sont réutilisées sans logique scolaire codée au cœur |
| Refus de diffusion d'une photo | absence de binaire, vignette et métadonnées publiques |

## 9. Ce qui existe déjà et ce qui reste à concevoir

**Documenté dans le snapshot Orgo :** Work owner sur Case/Task, Signal, orchestration/versioning, évaluateur pur, processus durables, opérations/outbox, scénario synthétique et injecteur. **Documenté dans Orgo_Worlds :** séparation des Worlds et releases, sans propriétaire de Work. 

**Non démontré comme implémenté pour Ekole :** distribution conditionnelle de fragments pédagogiques, compiler MissionFrame → Workflow Orgo, pilotage complet de scénarios élèves, identité scolaire appropriée, suivi certifiant des compétences et publication média consentie. Ces travaux sont des **intégrations et enrichissements d'Orgo/Ekole**, pas la création d'un second orchestrateur.

## 10. Conséquence pour les dépôts

- **Orgo :** propriétaire des éventuelles améliorations **génériques** d'orchestration (jointure de fragments, garde conditionnelle, repli, simulations robustes).
- **Orgo_Worlds :** mondes, contextes de releases et pack de fixtures, selon ses contrats.
- **Ekole :** savoirs, présentations, MiniLab, curriculum et preuves pédagogiques.
- **Ekole-Missions (facultatif) :** un dépôt **de contenu et de compilation de scénarios** peut être pratique. Il n'héberge ni Task/Case/Signal ni runtime concurrent. Ce n'est pas une nouvelle plateforme.

**Décision finale : Orgo orchestre. Ekole enseigne et atteste. Les scénarios provoquent des événements que la même machine sait traiter.**
