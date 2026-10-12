# Kontexte — Profil Québec / 3e année du primaire (v0.3)

**Périmètre** : couche d'adaptation du catalogue **culturellement neutre** de Kontexte v0.2, pour une classe francophone de 3e année du primaire québécois (deuxième cycle).

## Héritage : NE PAS écraser les trames neutres

```
data/trames/catalogue-neutral-v0.2.json       ← trame neutre inchangée, SHA-256 b475de9ede6880…
      + locales/qc/fr-CA/grade3/        ← surcouche québécoise référençant les ID parents
      + objectifs-candidats.json         ← enseignements visés, Kristals Ekole associés (pas codes MEQ)
      + parcours-36-semaines.json        ← plan d'instanciation par étapes internes Ekole
      + Orgo (dépôt existant)            ← seul orchestrateur des cas, tâches, indices, signaux
      + Ekole (dépôt existant)           ← preuves pédagogiques et correspondances officielles
```

La couche québécoise contient **60 adaptations**, **83 objectifs pédagogiques internes**, **32 trames pilotes planifiées et 34 micro-situations complémentaires, dans un parcours indicatif de 36 semaines**, et **15 exercices chiffrés vérifiables**. La banque des 28 trames restantes sert aux reprises, enrichissements et remplacements. Les deux niveaux de données restent séparés : `base_trame_id` référence l'identité du problème, l'overlay précise les objets et les apprentissages.

**Important sur « entièrement »** : la couche est complète **au niveau de l'inventaire des 60 trames et des objets de conception**. Elle n'est **pas** un programme scolaire officiellement homologué, pas 36 semaines de séquences clés en main, et elle ne démontre pas que les apprentissages ont été enseignés ou maîtrisés. Les correspondances exactes et la couverture de toutes les prescriptions de 3e année doivent encore faire l'objet de la revue décrite dans `reports/audit-couverture.json` et `locales/qc/fr-CA/grade3/seances-a-completer.json`.

## Dossiers

| Fichier | Contenu |
| --- | --- |
| `data/trames/catalogue-neutral-v0.2.json` | Source neutre de référence, copie binaire intacte |
| `locales/qc/fr-CA/grade3/profil-localisation.json` | Québec, langue, mesures, culture, sécurité |
| `locales/qc/fr-CA/grade3/overlays-60.json` | 60 localisations distinctes et leurs objectifs |
| `locales/qc/fr-CA/grade3/objectifs-candidats.json` | Index d'objectifs internes et IDs Ekole existants |
| `locales/qc/fr-CA/grade3/programmes-exigences.json` | Contenus repérés dans les sources officielles, surtout CCQ 3e |
| `locales/qc/fr-CA/grade3/parcours-36-semaines.json` | Proposition de planification, 4 étapes Ekole |
| `locales/qc/fr-CA/grade3/seances-a-completer.json` | Registre transparent des objectifs non planifiés par les trames pilotes |
| `locales/qc/fr-CA/grade3/exercices-deterministes.json` | Problèmes de maths, opérations exactes et corrigés |
| `examples/fete-sorciere-instance.json` | Exemple de déclinaison du même problème neutre sous l'habillage sorcière |
| `examples/preuve-pseudonyme.json` | Trace candidate non validée, sans donnée réelle |
| `reports/audit-couverture.json` | Couverture DOCUMENTAIRE, aucun score d'élève |
| `schemas/overlay-qc3.schema.json` | Contrat d'adaptation |
| `scripts/verifier.py` | Vérification hors ligne de l'héritage, liens et calculs |
| `index.html` | Index interactif hors ligne, sans réseau ni suivi utilisateur |

## Principes pédagogiques

1. **Interdisciplinarité réelle** : une trame peut mobiliser plusieurs disciplines au fil d'actions concrètes.
2. **Même rôle, parcours adaptable** : les aides ou la difficulté ne doivent pas révéler un handicap ou une classification personnelle.
3. **Informations distribuées** : Kontexte décrit les fragments; **Orgo** décide l'assignation, la libération et les transitions, en solo ou en groupe.
4. **Couvert ≠ maîtrisé ≠ validé** : l'instance collecte une preuve; Ekole et le personnel compétent déterminent le statut.
5. **Respect culturel** : Québec ne signifie pas une seule façon de célébrer, parler, vivre ou connaître le territoire.
6. **Politique médias restrictive** : un refus bloque l'export des fichiers et des tags identifiants; un simple floutage visuel ne suffit pas.
7. **CCQ protégé** : les thèmes obligatoires, y compris la prévention des agressions sexuelles, ne sont pas confiés à une simulation non encadrée.
8. **Calcul de taxes** : pourcentages / véritables taxes = enrichissement facultatif et scénarios guidés, pas acquisition ministérielle automatiquement attribuée à la 3e année.

## Vérifier

```bash
python3 scripts/verifier.py
```

## Guide d'intégration

Le compilateur Kontexte doit charger le scénario neutre immuable, vérifier son empreinte, puis fusionner les propriétés **autorisées** de l'overlay (`titre_qc`, contexte, objets, variantes, liens pédagogiques). Les déclencheurs restent des **intentions** jusqu'à leur matérialisation par Orgo. En production, ne jamais exposer un bloc d'indices destiné à un autre élève via HTML statique accessible. Les corrections ne doivent jamais se retrouver dans l'export public Élève.

Voir `docs/INTEGRATION.md`, `docs/SOURCES.md` et `docs/VALIDATION_PEDAGOGIQUE.md`.

## Deux fichiers supplémentaires après enrichissement

- `locales/qc/fr-CA/grade3/micro-situations-34.json` : activités ciblées pour les 34 objectifs internes absents des 32 trames du tronc annuel.
- `examples/corrige-enseignant-ne-pas-exporter.json` : 60 réponses ou pistes de vérification **strictement réservées au personnel habilité**, jamais à l’export Élève.

Les deux indices de chaque scénario sont maintenant des **données concrètes distinctes**; Orgo doit décider quand et à qui les dévoiler.
