# Tandem P1 — Kontexte → aperçu enseignant Ekole, sous autorité Orgo

**Statut : export local de conception, non opérationnel. Aucun compte enfant, aucune API Orgo.**

Kontexte est le propriétaire des **définitions de situations**, jamais des états `Case`/`Task`/`Signal`.
La commande `ekole-tandem-preview` convertit une mission `synthetic: true` en
`ekole.tandem-teacher-preview/1.0`, le format **déjà installé** dans Ekole P1.

```powershell
$env:PYTHONPATH = 'src'
python -m kontexte ekole-tandem-preview fete-sorciere `
  --tenant-id 11111111-1111-4111-8111-111111111111 `
  --world-id 22222222-2222-4222-8222-222222222222 `
  --world-release-id 33333333-3333-4333-8333-333333333333 `
  --workflow-ref fete-sorciere-v1 --out preview-ekole.synthetic.json
```

Les trois UUID ci-dessus sont des **valeurs fictives de contrat**, **pas les UUID
réels de FakePlant**, et ne prouvent aucun droit d'accès ni l'existence d'une release.
Dans Ekole déjà corrigé :
`py -3 launcher.py --contenu none --tandem-preview CHEMIN_DU_JSON --verifier`.

Garanties P1 : liste fermée des champs; rôle comme **référence pédagogique** et non
permission; aucune identité, nom, note, média, indice privé ni paiement exporté.
`ready` / `waiting` sont des **états indicatifs du plan** selon les dépendances,
**jamais** un état validé par Orgo ou une autorisation de libérer de l'information.
L'aperçu est à destination de l'enseignant sur un hôte local uniquement.

L'orchestrateur Orgo seul devra ensuite vérifier l'identité de l'enseignant,
le tenant/World/release, compiler et publier une version de Workflow vérifiée,
affecter les élèves et distribuer les fragments selon des gardes authentifiées.
**Aucune commande de ce dépôt n'appelle `apply`** dans l'injecteur Orgo.
Une tâche Orgo terminée ne constitue jamais une preuve de compétence maîtrisée.
