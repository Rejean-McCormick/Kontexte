# 06 — Confidentialité, tags, médias et identité des enfants

## Principe central : refus = absence de données publiques

Un « voile de confidentialité » **n'est pas** un flou CSS sur une photo déjà téléchargée. Si un refus, une absence d'autorisation ou un retrait s'applique, le service public ne doit recevoir **ni le média source, ni miniature reconnaissable, ni tag révélateur, ni lien direct**. Les contrôles sont côté serveur/publicateur/stockage; le navigateur affiche seulement un emplacement neutre facultatif.

## Classification des objets

| Objet | Protection | Public autorisé ? |
| --- | --- | --- |
| Portrait ou voix d'un enfant | identifiant direct | non par défaut; approbations spécifiques requises |
| Photo d'origami sans nom ni visage | création pédagogique | publication possible après vérification des droits, du contexte et des métadonnées |
| `artifact_id -> learner_ref` | correspondance identité privée | **jamais** dans un export public |
| Preuve de maîtrise et adaptations | donnée scolaire confidentielle | **jamais** dans galerie publique |
| Alias public d'auteur d'une œuvre | potentiellement identifiant indirect | optionnel et autorisé pour **chaque portée** |
| Tags d'activité (« origami », « sorcière ») | thématiques non sensibles en elles-mêmes | si le regroupement ne révèle pas une personne protégée |

## États proposés

`permission_state`: `unknown` (défaut), `refused`, `granted`, `revoked`, `expired`.  
`visibility_scope`: `private_teacher`, `class_group`, `school_internal`, `public`; portée maximale **autorisée**, pas consigne automatique de publier.  
`media_state`: `quarantined`, `reviewed`, `publishable`, `published`, `suppressed`, `withdrawn`.

Une publication suppose : autorisation du titulaire des droits + consentements/autorisations légalement applicables pour **chaque personne identifiable**, adéquation du public cible, vérification des métadonnées, revue humaine nécessaire, expéditeur habilité, preuve de version d'autorisation, durée, possibilité de révocation. Si une condition manque : **fail closed**.

## Pipeline recommandé

```text
Prise de vue / import -> Quarantaine privée -> Extraction métadonnées EXIF
       -> Classification œuvre/personnes/voix/tags
       -> Consentement et revue -> Produit dérivé autorisé + tags filtrés
       -> Prévisualisation responsable -> Publication contrôlée
       -> Révocation -> Retrait source publique, dérivés, index et caches maîtrisés
```

Ne jamais confondre **photo du chapeau** et **photo de l'enfant portant le chapeau**. Une permission pour partager l'œuvre n'accorde pas automatiquement une permission pour publier le visage ou le nom de l'auteur. L'enseignant peut documenter l'accomplissement sans diffuser la photo au public.

## Schéma logique d'une production (identités en coffre séparé)

```json
{
  "artifact_id": "work-origami-012",
  "kind": "origami_hat",
  "mission_run_id": "run-fete-001",
  "owner_ref_private": "learner-opaque-0042",
  "media_ref_private": "vault://media/opaque-123",
  "public_tags_candidate": ["origami", "chapeau", "fete-etoiles"],
  "permission_state": "unknown",
  "visibility_scope": "private_teacher",
  "media_state": "quarantined",
  "public_url": null
}
```

Les URL `vault://` sont purement **illustratives**, sans service existant garanti.

## Sécurité pratique

- Authentification et contrôle d'accès à **chaque téléchargement**, pas seulement à la page galerie.
- Buckets/dossiers séparés privé/public, interdiction de « direct link » contournant les permissions.
- Enfants tagués seulement sous identifiants opaques dans l'espace privé; noms de fichiers aléatoires; suppression EXIF (géolocalisation, identifiants d'appareil).
- Limiter les recherches, vignettes, journaux, index et caches; vérifier les mélanges entre classes et Worlds.
- Les équipes ne voient pas les profils de soutien; une photo ne sert pas de note automatique.
- Historiser qui a approuvé ou refusé la diffusion; fournir un mécanisme de correction de tags et retrait par personnes habilitées.
- L'archive destinée à durer reste subordonnée à une politique de conservation, d'effacement et de retrait; une publication publique ne peut pas être promise « éternelle ».
- Les dispositions québécoises, obligations scolaires et fondements du consentement doivent être validés par l'établissement et son responsable de protection des renseignements personnels; cette architecture **n'est pas un avis juridique**.

## Tests de non-divulgation critiques

1. Inconnu/refusé/révoqué -> HTTP/public export **ne contient pas** le fichier, miniature, URL, nom ou association d'auteur.
2. Une personne visible dans une photo refuse -> photo collective non publiée, même si les autres acceptent.
3. Retrait après publication -> suppression des dérivés, mise à jour des index, invalidation des caches sous contrôle et journal de l'opération.
4. Dans l'export statique Élève, chercher tout `learner_ref`, note, tag nominatif, `media_ref_private`, secret/jeton; résultat attendu : aucune occurrence.
5. Un utilisateur d'une autre classe/World ne peut pas lire une galerie privée ni deviner un objet par son ID.
