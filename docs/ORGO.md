# Orgo : intégration vérifiée et travaux nécessaires

Snapshot utilisé : `znapshot_Orgo_10112135.zip`, `znapshot_Orgo_Worlds_10112135.zip` (fournis dans la conversation). Les fichiers de ces dépôts ne sont **pas vendus ni incorporés dans ce dépôt**.

## Ce qui marche aujourd'hui

1. `kontexte orgo-fixture fete-sorciere --out sortie.scenario.json`
2. Depuis le dépôt Orgo fourni : `node tools/scenario-injector/cli.mjs validate /chemin/sortie.scenario.json`
3. `node tools/scenario-injector/cli.mjs plan /chemin/sortie.scenario.json`
4. **Seulement dans un environnement Orgo de test** : `inject ... --apply` selon README Orgo et avec autorisation préalable.

La fixture produit un `Case` et une Task **de préparation**. Elle ne prépublie ni les fragments d'information, ni les missions enfantines, ni les photographies. Aucune API externe n'est appelée à la génération.

Le `OrgoAPI` de `src/kontexte/orgo_http.py` fournit en code des lectures des Tasks/Cases et un changement d'état explicite, avec révision, authentification bearer serveur et clé d'idempotence. Il n'est pas exposé au navigateur et refuse les hôtes distants par défaut.

## Ce qui manque pour « grand orchestrateur » en classe

- Réception de `MissionFrame` comme une **publication de WorkflowVersion ou Process** après compilation et revue; graphe de dépendances dynamique non compilé ici.
- Ciblage sûr d'un fragment à une personne selon une décision prise et autorisée par Orgo (à qui / quand / pour quelle version); jeton de capability signé / identité scolaire résolue / expiration.
- Jointure A+B après communication réelle d'informations, preuve du partage, idempotence et repli si partenaire absent.
- Sélecteur d'aide pédagogique sans exposition des paramètres médicaux ni duplication d'algorithme de progression.
- Webhooks d'accomplissement vers un service Ekole de preuves signé et auditable; un `Task COMPLETED` n'est pas une preuve de maîtrise.
- Mécanismes génériques de compensation, retard, annulation et retour pour missions solo ou collectives.
- Vérification d'accès à la session/salle, identité de l'élève, permissions du professeur; intégration à Orgo_Worlds pour les releases.

**Ces fonctions doivent être développées dans Orgo comme primitives générales, pas copiées comme un moteur de quêtes Kontexte.** Il serait trompeur de déclarer la plateforme prête pour une classe multiutilisateur avant leur réalisation.

## Sûreté simulation

`synthetic: true` et `epistemic_status: synthetic_demo_fixture` sont systématiques. Ne pas connecter les simulations à des envois de messages externes, paiements, déplacements autonomes d'enfants, partage public, publication d'images ni déclencheurs organisationnels réels.

## API Orgo observée

Le snapshot contient notamment `/api/v3/tasks`, `/api/v3/cases`, `/api/v3/signals`, `/api/v3/workflows` et le patch `tasks/:id/status` avec `revision`. Les contrats diffèrent selon les versions; revalider lors de chaque mise à niveau.
