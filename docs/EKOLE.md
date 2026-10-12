# Ekole : preuve et programme québécois

Le catalogue copié `data/catalogue/202_kristals.json` est celui de `znapshot_Ekole_10112210.zip` et annonce **202 Kristals / 2183 items**. Il est explicitement **expérimental**. `graphe_pedagogique.json` est aussi conservé avec son statut de décisions pédagogiques internes; ceci ne crée aucune équivalence automatiquement validée au PFEQ.

À chaque étape de mission, `curriculum_ids` référence des IDs de ce catalogue. La commande `curriculum` vérifie leur existence et exporte les rapprochements internes avec `official_pfeq_id=null`, jusqu'à revue d'un enseignant habilité sur le programme et la progression applicables.

## Distinguer les 5 faits observables

- `observed` : une observation a été consignée.
- `covered` : une notion a été abordée.
- `practiced` : une tentative ou un exercice a été réalisé.
- `mastered` : une maîtrise a été documentée avec validation humaine autorisée.
- `validated` : une validation critériée est attestée par un responsable habilité.

Le prototype local refuse `mastered`/`validated` sans identifiant du réviseur et `human_review`. Il ne certifie pas lui-même l'habilitation; cette vérification devra appartenir au futur service scolaire sécurisé. Le regroupement garde tous les statuts sans déduire qu'un `COMPLETED` Orgo signifie un `mastered` Ekole.

## Déploiement réel des traces

Il faudra un service séparé avec comptes et autorisations école, audit, exigences de consentement selon le contexte, rétention limitée, effacement et accès, chiffrement et gestion des preuves. Le SQLite livré n'est **pas** une solution de production pour données de mineurs. Il n'y a aucun partage automatique vers le ministère.

Un rapport institutionnel futur peut agréger la couverture et les preuves anonymisées selon autorisation; ni des identités individuelles ni des notes officielles ne sont inventées.
