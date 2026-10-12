# Contrats Kontexte v1

- `data/roles/*.json`: `kontexte.role/1`, nom/intro localisés, thème validé sur liste blanche, grammaire de rôle (actions, objets, problèmes, partenaires).
- `data/missions/*.json`: `kontexte.mission/1`, fiction, 1-6 année suggérée, étapes, dépendances dans l'ordre topologique, infos fragmentées, jointures, trois niveaux d'aide non publics, liens Ekole.
- `integrations/orgo/*.scenario.json`: **format `orgo.scenario.v1` authentifié par l'injecteur officiel**; le scénario livré initialise seulement le Case et la Task de revue, pas l'exécution pédagogique.
- `integrations/orgo/*.blueprint.json`: intentions déclaratives de situations, non un Workflow Orgo exécutable.
- `integrations/ekole/*.curriculum-links.json`: rapprochements internes candidats; `official_pfeq_id:null` tant que revue officielle absente.
- `kontexte.evidence/1`: événements de pratique, observation ou revue pédagogique (démo locale).

## Livraison d'informations

`fragments[*].release = orgo_authorized`. Le rendu exige `trusted_authorization=True` avec IDs autorisés *issus d'un environnement serveur de confiance*. Jamais du navigateur, d'un paramètre URL, ni d'un nom de rôle. Les modes preview avec `--demo-fragments` sont réservés aux données entièrement fictives.

La jointure de fragments (`joins`) est une **intention** de scénario: elle doit être traduite en garde/condition générique Orgo, avec autorisations par destinataire, dédoublonnage, repli si partenaire absent. La présence d'une jointure dans le JSON ne déclenche rien toute seule.

## Difficulté inclusive

`accompagne`, `standard`, `approfondi` déterminent les aides et niveaux de défi, non l'identité publique. Pas d'inférence médicale, pas d'indication de trisomie ni de diagnostic en profil public. Toujours offrir des chemins de secours et alternatives accessibles. Pour la validation de compétence, enregistrer le soutien réellement reçu.

## Localisation

Chaque contenu canonique garde des valeurs `fr-CA`, et peut porter `en`. Si la version anglaise manque, un repli **visible dans la langue originale** intervient: ce n'est pas une traduction produite ou certifiée. Un export de langues devrait être revu par humains et soumis au futur contrat SemantiK qualifié.

## HTML

Rendu échappé via `html.escape`, CSS à thèmes autorisés, sans texte HTML arbitraire en contenu ni script externe. Tout enrichissement interactif réel requiert un composant approuvé par le noyau Ekole et un examen d'accessibilité et sécurité. Séparer rendu autorisé d'un simple modèle HTML généré par IA non fiable.
