# 08 — Décisions ouvertes, risques et revue de gouvernance

## Choix à trancher avant écriture de code

| Décision | Proposition de départ | Validation requise |
| --- | --- | --- |
| Autorité des référentiels officiels | registre séparé, liens candidats jusqu'à revue humaine | spécialiste PFEQ / titulaire des contenus |
| Identification des élèves | service local sécurisé + pseudonymes exportables | établissement et responsable de protection des données |
| Orgo facultatif ou requis | **requis pour une mission orchestrée**, solo ou collective ; Ekole garde son portail de cours sans Orgo | architecture et capacité de l'école |
| Granularité Orgo Task | mandat social significatif, pas un clic | équipe Orgo Work |
| Niveau et adaptations | fonctions de soutien choisies au cas par cas et discrètes | enseignants + accessibilité + utilisateurs concernés |
| Consignes bilingues | source unique de données + phrases traduites revues; aucune génération libre live | équipe linguistique (SemantiK quand qualifié) |
| Calculs de taxes | simulation paramétrable non assimilée aux taux légaux | enseignant et concepteurs d'exercices |
| Preuves/maîtrise | événements séparés + revue enseignante; aucune maîtrise automatique par simple participation | gouvernance pédagogique |
| Publication d'œuvres | privé par défaut, consentement et autorisation explicites par portée | conseil scolaire/établissement + juridique |
| Conservation des médias | pas de « permanence » irrévocable; politique de retrait/restauration | responsable données + archives |
| Rapport institutionnel | agrégé et fondé sur mappings approuvés, non automatique | direction / autorités compétentes |
| Licence des HTML/images | vérifier sources, licences, droits d'œuvres et textes | responsable contenu et juriste selon besoins |

## Risques pédagogiques à surveiller

- **Habillage superficiel** : le rôle change les noms, sans que l'enfant doive décider ou agir; imposer production et interaction véritable.
- **Dépendance à un partenaire** : élève exclu si pair absent / non disponible; mode de secours indispensable.
- **Évaluation gonflée** : une activité riche prétend certifier math, français, anglais, arts et CCQ sans critère pour chaque discipline; test de preuve unitaire.
- **Jeu qui écrase l'apprentissage** : spectacle ou monnaie devient l'objectif principal; le bilan doit faire expliciter les stratégies apprises.
- **Comparaison de niveaux** : adaptation rendue visible par badges; ne pas montrer les parcours de soutien au groupe.
- **Tâches physiques mal calibrées** : déplacement/installation de chaises n'est pas automatiquement une compétence d'éducation physique; encadrement/sécurité requis.
- **Confusion scolaire officielle** : les 202 cours candidats ne représentent pas une homologation québécoise; maintenir versions et statut des mappings.

## Risques techniques et mesures de contrôle

- Double propriété de `Task` Orgo : **interdit**; créer des liens de mission plutôt qu'un second cycle de Task.
- Perte de contexte avec promotion d'une release : épingler la release au démarrage.
- Export Élève trop large : refuser toute copie de `kristals/` ou données de suivi; rester sur liste blanche stricte.
- Faux offline multiutilisateur : définir modes exploration et classe séparés.
- Mélange de confidentialité : politiques serveur fail-closed, tags filtrés, audit du retrait.
- Génération d'HTML incontrôlée : composants whitelist, sanitation, CSP, i18n et tests automatisés.
- Résultat non déterministe : chiffres et verdicts calculés depuis contrats/verificateurs, jamais depuis phrases générées.
- API/version changée : adaptateurs isolés et tests de contrat, ne pas écrire directement dans la DB d'Orgo.

## Hypothèses explicitement non vérifiées

- Aucune solution existante d'identité scolaire/registre des notes n'a été démontrée dans le snapshot étudié.
- Les interfaces décrites ici (`EvidenceLog` pédagogique, `CurriculumMap`, publicateur média et adaptateurs de contenus) sont des **propositions**, pas des services présents. Le runtime canonique de mission est celui d’**Orgo**, et les extensions nécessaires doivent être qualifiées dans son noyau.
- Ni les liens officiels cours↔ministère, ni les traductions anglaises, ni les règles fiscales pédagogiques ne sont approuvés par un organisme extérieur.
- La documentation fournie n'autorise aucune conclusion sur les droits de diffusion des photographies des enfants; politique de l'établissement indispensable.

## Définition de « upgrade réussi »

1. L'élève peut vivre une quête avec plusieurs apprentissages sans changer manuellement de matière.
2. Le même rôle peut être joué selon différents soutiens, sans exposition de ces différences.
3. La mission déclenche des interactions de qualité, des preuves individuelles et des quêtes cohérentes.
4. Un enseignant peut expliquer **exactement** pour chaque preuve : activité, compétence visée, source et version de référence, auteur/relecteur, degré d'autonomie, statut.
5. Les rapports distinguent honnêtement activités pratiquées, compétences maîtrisées et celles dont la correspondance officielle reste à valider.
6. Les données des mineurs demeurent protégées, y compris après révocation du partage.
7. Les vues par matières et cours existantes continuent de fonctionner.
