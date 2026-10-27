# B5 — Kontexte Québec, 3e année : rôles, scénarios et boulangerie

Cette mise à jour est **isolée de l'application Ekole**. Elle ne modifie ni Kristal, ni Spek, ni kompose, ni Orgo, et ne met aucune mission en production. C'est un paquet de conception, de contrôle des liens et de démonstration autonome.

## Nouveaux outils en ligne de commande

À la racine Kontexte (Python 3.10+; aucune dépendance externe) :

```bash
PYTHONPATH=src python -m kontexte qc3-audit-b5 --out sorties/b5-audit
PYTHONPATH=src python -m kontexte qc3-pilot-b5 --out sorties/b5-pilote
PYTHONPATH=src python -m unittest discover -s tests -v
```

Sous Windows : `set PYTHONPATH=src` dans `cmd`, ou `$env:PYTHONPATH = 'src'` dans PowerShell, avant `python -m kontexte ...`. Un lanceur dédié `LANCER_B5.bat` est fourni.

Les sorties sont **ajoutées**, jamais écrites sur le catalogue neutre.

## 1. Inventaire traçable

`qc3-audit-b5` :
- Valide l'intégrité du catalogue neutre et **chaque** empreinte SHA-256 parent, l'unicité des 60 overlays, les rôles, les objectifs candidats et le calendrier.
- Produit `audit-b5.json`, `index-scenarios-b5.csv` (60 scénarios), `index-objectifs-b5.csv` (83 objectifs), `index-roles-b5.csv` (38 rôles), `calendrier-b5.csv` (36 semaines).
- Identifie **32 scénarios principaux**, **28 scénarios de banque**, **49 objectifs candidats mobilisés dans les 32**, **34 objectifs supplémentaires représentés par 34 micro-situations proposées**.
- Vérifie que les micro-situations CCQ sensibles identifiées conservent le statut d'enseignement encadré, non converti en jeu obligatoire.

**Important** : ce sont des objectifs **internes candidats**, pas une liste officielle exhaustive de la 3e année du Québec. Ils ne prouvent ni la réalisation des séances, ni un acquis, ni une conformité ministérielle.

## 2. Pilote de boulangerie — deux audiences

`qc3-pilot-b5` crée deux **répertoires distincts** :

- `student-preview/boulangerie.json` et `.html` : histoire et défi enfant **non publiés**. Variante solo de **3 plateaux de 4**, conçue ici comme adaptation de démonstration. Elle ne contient pas le corrigé ni les indices privés.
- `teacher-only/boulangerie-plan.json` et `boulangerie-enseignant.html` : 3 rôles, objectifs liés au catalogue interne, déroulement suggéré, différenciation, **exercice source 6 × 4 = 24**, indices à distribuer uniquement par Orgo autorisé, corrigé réservé et précautions.

### Les sources ont deux formulations, conservées sans modification

- `data/missions/boulangerie.json` : mission historique squelette, **12 pains**, liens principalement à `qc-pri-ma-006` (addition), non raccordée à la surcouche 3e complète.
- `data/locales/qc/fr-CA/grade3/overlays-60.json` + `exercices-deterministes.json` : `commande-de-pains`, **6 plateaux × 4 pains = 24**; objectif candidat multiplication lié à `qc-pri-ma-008`, semaine **10**, étape interne **2**.

La variante solo simplifiée **3 × 4** est explicitement une adaptation **B5** : elle ne réécrit aucune des deux sources et n'est pas le véritable scénario collaboratif.

### Statuts et exigences

- **Aucune publication** d'office dans Ekole; un enseignant doit relire et approuver avant diffusion réelle.
- Les **rôles sont des perspectives narratives**, jamais des permissions d'accès au système.
- Le scénario peut proposer des informations distribuées, mais **Kontexte ne les révèle pas** aux participants et ne déclenche pas les étapes. **Orgo demeure l'unique orchestrateur opérationnel** (ADR-001 du dépôt Kontexte).
- Une tâche terminée ou une réponse calculée ne suffit pas à attester la maîtrise.
- Contenu culturel et contextuel à relire avec des enseignants pertinents, y compris les variantes accessibles.

## 3. Contrat de consolidation proposé (non imposé)

Les fichiers JSON produits utilisent `kontexte.b5-audit/1`, `kontexte.b5-preview-eleve/1` et `kontexte.b5-plan-enseignant/1` : **formats provisoires de B5**. La consolidation décidera d'un adaptateur partagé pour :

- `scenario_id` / `overlay_id` et empreintes sources ;
- `role_id` et identité de perspective (sans permissions) ;
- `qc3.*` objectifs candidats et `qc-pri-*` Kristals candidats ;
- `audience` student_preview / teacher_only ; `statut` brouillon / revue / publication ;
- disponibilité des ressources pédagogiques, consentement et modes d'adaptation ;
- limites de coordination Orgo et éventuels contrats kompose à arbitrer dans **B6**.

Aucune route HTTP n'est ajoutée à Kontexte : un export d'aperçu n'est pas une API Élève sécurisée. Ne jamais servir publiquement `teacher-only/`, `sorties/` entières ou les exports de Studio avec fragments.

## 4. Régression

Le dépôt de départ 0.4 comptait **49 tests qui passaient**. Cette branche ajoute **10 tests** et conserve les 49 existants. Les tests couvrent intégrité, références, calendrier, corrigé non exporté, séparation physique des fichiers, chiffrement par empreinte du catalogue, lecture CSV et règles CCQ. Voir `TESTS.md` du paquet B5.
