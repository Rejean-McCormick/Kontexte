# 04 — Le référentiel québécois comme « array » de couverture et de maîtrise

## Décision principale

**La grille scolaire n'est plus le plan d'exécution des activités; elle devient le référentiel de preuve des apprentissages.** Une même action peut porter plusieurs liens curriculaires, mais les liens ont des statuts et des critères spécifiques. Un cursus n'est pas réputé complété parce qu'une mission est terminée.

## Deux registres et une projection

1. **CurriculumRegistry** *(design, versionné)* : énoncés vérifiés et localisables du PFEQ / Progressions des apprentissages / Cadres d'évaluation, références de publication, période d'application, matière, cycle/niveau, compétences et provenance; décrire la source officielle avec précision ou laisser `official_ref=null`.
2. **CurriculumMap** *(gouvernance)* : correspondance `mission_step -> objective_id Ekole -> official_ref`, statut `candidate|reviewed|approved|rejected`, raison, auteur/relecteur, date et version de texte. Aucun rapprochement lexical automatique n'est une preuve d'équivalence.
3. **CurriculumReadModel** *(array de lecture par élève)* : agrégation des événements d'activité et de validation, recalculable et adaptée à la période. Elle affiche, **pour chaque cours et élément du référentiel**, ce qui fut exposé, pratiqué, maîtrisé, validé et transféré.

```text
          Mission: invitation bilingue + origami + paiement
              |                     |                |
          EvidenceLog ---------- CurriculumMap ---- Kristal de cours
              |                                        |
       CurriculumReadModel <------------------- Registry versionné
              |
          Rapport enseignant / relevé de groupe / rapport agrégé institutionnel
```

## États séparés (éviter le booléen « appris »)

| Champ | Condition minimale | Autorité |
| --- | --- | --- |
| `encountered` | l'élève a eu accès à une activité pertinente, avec contexte et date | télémétrie minimale ou confirmation humaine; **pas une réussite** |
| `practiced` | tentative/action réellement faite; tâche identifiée | moteur / observation qualifiée |
| `demonstrated` | production ou réponse répondant à un critère observable | correcteur exact ou personne |
| `mastery_level` | argumenté par plusieurs preuves ou une évaluation conforme aux règles; conditions et degré d'autonomie connus | enseignant/règles institutionnelles validées |
| `validation_status` | `unreviewed`, `automatic_practice_only`, `teacher_reviewed`, `institutionally_approved`, `withdrawn` | autorité identifiée; la validation technique n'est pas ministérielle |
| `transfer` | mobilisation du même apprentissage dans une situation substantiellement nouvelle | comparaison de preuves, revue selon règle |

La compétence a **un historique d'états et d'évidences**, pas un booléen permanent. Une maîtrise peut être reconfirmée, révisée ou invalidée; l'historique est auditable sans garder indéfiniment des données nominatives.

## Forme de l'« array » de synthèse (exemple fictif)

```json
{
  "learner_ref": "pseudonyme-classe-042",
  "school_year": "2026-2027",
  "period": {"kind": "ekole_pedagogical_step", "index": 2},
  "curriculum_snapshot": "curriculum-qc-2026-candidat",
  "items": [
    {
      "ekole_course_id": "qc-pri-fr-021",
      "official_ref": null,
      "mapping_status": "candidate",
      "encountered": true,
      "practiced": true,
      "demonstrated": true,
      "mastery_level": "not_determined",
      "validation_status": "teacher_reviewed",
      "evidence_refs": ["evidence-invitation-001"]
    },
    {
      "ekole_course_id": "qc-pri-ma-008",
      "official_ref": null,
      "mapping_status": "candidate",
      "encountered": true,
      "practiced": true,
      "demonstrated": false,
      "mastery_level": "not_determined",
      "validation_status": "automatic_practice_only",
      "evidence_refs": ["evidence-budget-001"]
    }
  ]
}
```

**Attention :** `official_ref` à `null` interdit tout rapport affirmant la conformité ou la couverture d'une compétence ministérielle précise. La correspondance à un des 202 cours Ekole ne suffit pas : les statuts de ces cours sont expérimentaux.

## Une preuve avec plusieurs correspondances, mais sans extrapolation

L'invitation bilingue peut donner :
- une trace de **français écrit** si l'on évalue effectivement la structure, les informations, l'orthographe et le destinataire;
- une trace d'**anglais** seulement si un critère observable adéquat a été évalué (la simple présence d'une traduction copiée ne démontre pas l'autonomie en anglais);
- une trace de **coopération** si l'aide apportée à la personne destinataire est observée selon des critères distincts;
- aucune preuve automatique d'arts plastiques si elle n'a pas composé elle-même l'affiche.

En situation aménagée, conserver le champ `support` descriptif et confidentiel; ne pas en déduire « non maîtrisé » ou « maîtrisé » mécaniquement. L'indépendance de l'élève peut varier selon la compétence évaluée, et non selon son rôle public.

## Journal d'événements : architecture et audit

- événements append-only, `event_id`, horodatage, `learner_ref`, `mission_run_id`, `step_id`, `artifact_ref`, `criteria_ref`, `context`, `result`, `support`, `assessment_mode`, `validator_ref`, `source_versions`, `privacy_scope`;
- dédoublonnage par `idempotency_key` et empreinte des valeurs d'entrée;
- correction par événement `evidence_corrected` qui pointe sur l'original, pas écrasement silencieux;
- un évaluateur de réponses déterministes ne devient pas, par simple renvoi `true`, un jugement officiel;
- conserver des références vers artefacts sous contrôle d'accès, plutôt que copier leur texte/leurs photos dans le log;
- règles d'archivage, accès/export/suppression et rétention définies par l'établissement avant collecte réelle.

## Trois vues, trois niveaux d'accès

### Vue élève
Progression personnelle intelligible (« j'ai découvert », « j'ai essayé », « je peux expliquer »), sans étiquette clinique ou classement humiliant, sans prétendre représenter un bulletin officiel.

### Vue enseignant
Relevé **par année scolaire, cycle, cours, compétence, période et mission**; filtre `non vu / pratiqué / preuve disponible / à revoir / validé`, outil pour retrouver critère, contexte, aide fournie, version des textes et évaluateur. L'enseignant peut corriger avec justification, exporter un relevé contrôlé, voir les trous de couverture du référentiel.

### Vue direction/ministère (si autorisé)
Rapports agrégés : taux de couverture par **référentiel/version**, unités non couvertes, occurrences des modes d'apprentissage, validité des correspondances, distribution de preuves et limites d'échantillon. Pas de transmission automatique de photos ou identifiants d'enfants, pas de hiérarchie publique d'enfants, ni prétention à un « certificat du ministère ». Transmission externe seulement avec base légale, accords et validations institutionnelles appropriés.

## Périodes à ne pas confondre

Ekole a **4 étapes pédagogiques locales**; la documentation du snapshot distingue **3 étapes officielles de bulletin**. Stocker les deux référentiels comme dimensions indépendantes avec dates d'établissement, et produire une table de correspondance explicite seulement après configuration et autorisation. Ne jamais convertir « étape pédagogique 4 » en un quatrième bulletin.

## Version du programme et conformité

Associer `source_document_uri`, intitulé, section/pages, version, date d'application, langue, revue de la transposition et changements de programme. Si une référence est mise à jour, un nouveau mapping est créé; les observations historiques restent attachées à leur version d'origine. Aucun remplacement silencieux d'un objectif de 2026 par celui de 2027.
