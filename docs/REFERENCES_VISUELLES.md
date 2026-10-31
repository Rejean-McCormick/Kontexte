# Références visuelles des rôles

Les 38 rôles existants conservent leurs identifiants, actions, objets, partenaires et missions. Chacun ajoute une référence `visual_id`, exactement `role-<id>`, sans URL ni chemin propre au Québec.

Une illustration par rôle est réutilisée entre les activités, sans variantes d’année ni de pose. Les médias sont détenus par le paquet de contenu : pour Québec, `ekole-quebec/personnages/catalogue.json`. Le champ reste facultatif dans le format v1 pour accepter les anciens rôles; lorsqu’il existe, le validateur exige sa correspondance exacte avec l’identifiant.

`explorateur` et `extraterrestre` restent deux rôles distincts. Un compagnon peut être associé à un rôle par le catalogue du paquet, mais cela ne modifie ni la définition du rôle, ni ses capacités, ni ses autorisations.

Kompose ne change pas : ses projections fournissent déjà les identifiants des rôles. Ekole peut donc retrouver la référence canonique sans faire transiter les médias dans Kompose.

Vérification depuis le dépôt :

```sh
PYTHONPATH=src python -m unittest discover -s tests
```

Les définitions restent textuelles; aucune image ni donnée d’élève n’est ajoutée à Kontexte.
