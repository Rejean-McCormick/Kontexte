# Conception de la surcouche (Kontexte → Orgo → Ekole)

## Règle d'héritage

- `base_trame_id` pointe vers la trame neutre, sans la copier dans l'adaptateur.
- Les empreintes du catalogue et de chaque trame verrouillent l'héritage; une migration doit être revue si le catalogue change.
- Les propriétés québécoises sont **seulement** : contexte, objets, labels, langue, matériel, actions d'apprentissage, aides, liens d'objectifs, sécurité.
- Une variation culturelle peut remplacer le décor et les pratiques, mais ne peut supprimer arbitrairement l'interdépendance et le problème central.

## Protocole de chargement (proposé, non déployé)

1. Charger `catalogue/trames-neutral-v0.2.json`.
2. Charger `profil-localisation.json` et `overlays-60.json`, vérifier les SHA-256 avec `scripts/verifier.py`.
3. Sélectionner `base_trame_id`, appliquer les propriétés de présentation locale et rendre les contenus accessibles en fr-CA.
4. Récupérer du catalogue Ekole les objectifs et leurs versions, sans que Kontexte émette une note officielle.
5. Créer **dans Orgo** l'instance opérationnelle : participants, signaux, tâches, information détenue, disponibilité, échéances. Orgo est l'autorité des états.
6. Transmettre à Ekole les observations et copies de production autorisées, en séparant couvert, observé, maîtrisé et validé.
7. Le stockage des travaux d'enfants et des médias doit passer par un service école sécurisé; ce dépôt ne contient aucun compte ni service de photos.

## Interface suggérée

- `resolve(base_id, locale_id, grade, version) -> design_projection`
- `to_orgo_intent(projection, participants_opaque) -> proposal_for_orgo` : pas de transition automatique dans Kontexte
- `from_orgo_observation(orgo_event) -> candidate_learning_evidence` : Ekole valide ou rejette
- `render_html(context, audience) -> html` : jamais les secrets d'un autre participant ni les corrigés enseignant
- `media.exportable(asset_id, publication_scope)` : *deny by default*, revue de consentement distincte

## Déploiement

- `Kontexte` est un dépôt de scénarios et de rendus; aucune duplication du runtime d'Orgo.
- `Orgo` est l'orchestrateur unique, indépendamment du nombre de participants.
- `Ekole` est le référentiel pédagogique et doit conserver ses journaux même si Kontexte est désinstallé.
- L'export élève d'Ekole reste en liste blanche; **jamais** d'export de JSON source contenant des indices privés ou des corrections.

## Étapes de livraison

**A** : revue des 60 overlays et des 32 pilotes par enseignants, adaptation culturelle locale et accessibilité.

**B** : implémenter l'import des intentions dans les contrats existants d'Orgo, sans nouvelle machine d'états dans Kontexte.

**C** : intégrer observations et validation dans Ekole, protections multiélèves et tests d'isolement.

**D** : exécuter les essais locaux de classe, vérifier que les activités ciblent les compétences annoncées.
