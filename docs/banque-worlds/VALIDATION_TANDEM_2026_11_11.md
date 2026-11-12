# Banque étendue et liaison Tandem — qualification du 11 novembre 2026

**Statut : simulation hors ligne uniquement; contenu éditorial candidat.**

- Les **11 missions B5 historiques** restent un inventaire explicite et figé dans `kontexte.qc3_b5.B5_HISTORICAL_MISSIONS`. Les six ajouts se trouvent dans `data/missions/` mais ne changent pas les statistiques de l'audit B5. Le contrôle échoue si une mission historique disparaît.
- Le Studio présente l'inventaire étendu de **17 missions**. L'audit B5 ne revendique jamais 17 missions historiques.
- Les six missions nouvelles conservent leur texte `safety.fr-CA` et comportent maintenant `real_spending: false`, `real_taxes: false`, `publication_default: private`. Cela autorise seulement la **génération de la prévisualisation synthétique, sans indices privés** via `ekole-tandem-preview`. Aucun élève ni World réel n'est activé.
- Les dix missions historiques autres que `fete-sorciere` n'ont pas ce bloc de garanties structurées; **elles restent non exportables** vers ce format fermé. Ne pas leur attribuer de garanties automatiquement.
- Les **52 étapes des six nouvelles missions** ont toujours `curriculum_ids: []`. Toute mise en correspondance doit rester candidate jusqu'à une revue pédagogique; aucune maîtrise n'est inférée.
- `Kontexte/src/kontexte/orgo.py` produit une fixture Orgo à **une Case et une tâche de révision**, pas le graphe opérationnel des étapes. Il n'existe aucune exécution automatique de mission dans ces correctifs.

## Tests

```powershell
cd C:\mycode\Ekole\Kontexte
$env:PYTHONPATH = 'src'
python -m unittest discover -s tests -p 'test_*.py' -q
python -m kontexte validate
```

Pour les vérifications croisées, exécuter `C:\mycode\Ekole\ekole\tools\verifier_ecosysteme_tandem.py` avec Python 3 et Node.js. Cette commande ne crée aucun état Orgo, Konnaxion ou Ékole.
