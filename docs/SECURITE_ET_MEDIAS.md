# Sécurité, confidentialité et médias d'enfants

**Prototype non destiné à stocker ni publier de vrais dossiers d'élèves.**

1. Aucune photo n'est présente dans ce dépôt. Aucune photo ne doit être embarquée dans un site public de démonstration.
2. Les rôles éducatifs ne confèrent aucune permission informatique. La propriété `role` n'est jamais une identité authentifiée.
3. Une galerie publique ne doit contenir **ni original, ni miniature, ni EXIF, ni vignette floutée, ni tag identifiant** si le consentement spécifique fait défaut. La suppression des métadonnées seule est insuffisante.
4. Consentement distinct par œuvre et public cible; refus prioritaire; autorisations du personnel et responsables légaux selon les exigences et le contexte. Retrait doit déclencher retrait/cache purge des publications précédentes dans le service futur, pas uniquement un masque CSS.
5. Le catalogue public ne montre que les pages de présentation, jamais les banques de solutions et preuves individuelles.
6. Les mécanismes de droits, sécurité des enfants et stockage des données doivent passer en revue de menace avant pilotes réels. Aucune attribution de diagnostic à partir d'un parcours.
7. Les trajets et rencontres d'élèves sont toujours supervisés par des adultes, jamais planifiés comme une localisation en direct autonome.
8. Les Klownkoins ne sont pas convertibles, transférables à des comptes réels, ni échangeables contre des ressources indispensables à l'apprentissage.

`media.py` n'héberge pas les binaires : il produit une décision de manifest fail-closed. L'intégration média complète, avec retrait et purge, reste à concevoir dans un service sécurisé.
