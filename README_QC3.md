# Kontexte — Extension Québec, 3e année

Ce dépôt est la version de Kontexte v0.1.0 enrichie d'une **surcouche documentaire Québec 3e**, non d'un runtime de mission supplémentaire.

- Catalogue neutre inchangé : `data/trames/catalogue-neutral-v0.2.json`
- Adaptations : `data/locales/qc/fr-CA/grade3/overlays-60.json`
- Objectifs internes : `data/locales/qc/fr-CA/grade3/objectifs-candidats.json`
- Parcours annuel : `data/locales/qc/fr-CA/grade3/parcours-36-semaines.json`
- Micro-situations : `data/locales/qc/fr-CA/grade3/micro-situations-34.json`
- Corrigés ENSEIGNANT non destinés à l'export : `teacher-only/qc3/`
- Documentation : `docs/locales/qc3/`

**Attention** : les objets du répertoire `teacher-only/` ne doivent pas être inclus dans un export public Élève. Un compilateur de missions destinées à l'élève doit reconstruire sa sortie depuis des valeurs autorisées par Orgo, pas exporter directement le JSON source des deux indices.

L'outil de vérification de la surcouche autonome est inclus dans l'archive distincte `Kontexte_QC_3e_v0.3.zip`. Le dépôt intégré n'est pas un système de suivi de maîtrise en production.
