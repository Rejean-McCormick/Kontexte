# Revue pédagogique — lot 2

Le catalogue des 202 Kristals est **interne et expérimental**, pas un équivalent certifié du Programme de formation de l'école québécoise.

La banque possède maintenant **55 correspondances candidates vérifiées techniquement**, entre 7 missions et des Kristals existants. Elles ne changent pas `steps[].curriculum_ids`, donc Ékole ne reçoit aucune nouvelle preuve d'apprentissage automatiquement.

- Consulter `integrations/ekole/REVUE_PEDAGOGIQUE_55_CANDIDATS.csv` pour décider, étape par étape, si la proposition convient; fournir un critère observable par discipline.
- Le registre JSON contient le hash SHA-256 de la consigne et la version de mission; toute retouche à une consigne invalide le registre jusqu'à régénération et nouvelle revue.
- L'approbation future doit être versionnée et liée à un enseignant habilité; elle ne doit pas être inférée d'un test automatique.
- Les 10 missions historiques sans `safety.real_spending:false`, `safety.real_taxes:false`, `safety.publication_default:private` sont dans `integrations/ekole/securite-missions-historiques-a-revoir.json`. Leur aperçu Tandem reste bloqué. Réviser séparément la sécurité de chacune avant de changer les propriétés.

Vérification : `python -m kontexte.curriculum_candidates --json` avec `PYTHONPATH=src`.
