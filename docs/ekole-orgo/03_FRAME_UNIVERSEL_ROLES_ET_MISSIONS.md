# 03 — Frame réutilisable pour les rôles et les missions

## Un rôle est une grammaire d'actions, pas un exercice

Un `RoleFrame` répond à : **qui suis-je, que puis-je faire, qu'est-ce que j'achète, répare, fabrique, échange, publie, à qui ai-je besoin de parler et quel problème peut surgir?**

```text
RoleFrame
  identité et univers (réel, historique, imaginaire)
  verbes + objets + transformations (entrée -> action -> sortie)
  ressources et contraintes (temps, stock, budget, règles de sécurité)
  réseaux de collaboration (offre, demande, reçoit, aide, valide)
  tensions typiques (pénurie, panne, malentendu, délai, refus, choix éthique)
  réalisations textuelles fr-CA / en (champs sourcés, revus)
  tokens CSS, accessibilité et apparences (non-évaluatifs)
  facultés de classe approuvables (jamais permissions serveur)
```

### Mini-matrice d'actions transposables

| Rôle | Achète/emprunte | Fabrique/répare | Dépend de | Tension intéressante |
| --- | --- | --- | --- | --- |
| Sorcière | papier, plantes fictives, contenants | chapeau, invitation, décor, potion fictive | origamiste, rédacteur, messager | invité introuvable, manque de contenants |
| Boulanger | farine factice, outils, ingrédients | recette, boîtes, commande | fermier, comptable, livreur | mauvaise proportion, livraison tardive |
| Clown | accessoires, billets fictifs | numéro, affiche, spectacle | metteur en scène, régisseur | scène trop courte, consigne mal transmise |
| Mécanicien | pièces et outils sécuritaires | maquette, roue, dispositif | demandeur, technicien, vérificateur | une pièce manque, plan incomplet |
| Origamiste | papier de formats différents | chapeau, étoile, décoration | organisateur, photographe | quantité, symétrie, temps |
| Photographe | matériel prêté/approuvé | reportage, catalogue des œuvres | auteur des objets, responsable consentement | autorisation de diffusion refusée |
| Comptable | registre et jetons fictifs | paiement, bilan, facture simulée | membres de l'équipe, professeur | écart entre total et caisse |
| Messager | adresse et invitations | livraison et accusé de réception | équipe destinataire | mauvais destinataire, ordre modifié |

Les actions dangereuses (forgeron, chasseur, mineur, bûcheron, dresseur de lions) sont **simulées** ou remplacées par matériaux et représentations sécuritaires.

## Trame universelle d'une mission (état indépendant du rôle)

1. **Appel / enjeu** — besoin concret, destinataire et sens social.
2. **Tension calibrée** — manque, contrainte, contradiction, délai raisonnable; marche franchissable.
3. **Choix de rôle** — facultatif, réversible, apparence non révélatrice du profil.
4. **Préparation** — lecture, plan, outils, informations/indices réservés aux bons destinataires.
5. **Production** — artefact concret, texte, calcul, construction, présentation.
6. **Rencontre** — demander aide, aider d'abord le camarade si son mandat le requiert, remettre une information ou un objet.
7. **Coopération** — équipe ou binôme, les compétences sont complémentaires.
8. **Vérification** — critères séparés par compétence; validation de l'état logistique distincte du résultat scolaire.
9. **Conséquence** — argent fictif, événement, nouveau besoin, quête conditionnelle; transition idempotente.
10. **Bilan et trace** — réflexion, rapport de preuve, publication opt-in d'un média.

Une mission peut commencer à l'étape 5 si la situation le justifie; ce n'est **pas** un parcours rigide de 10 écrans. Des branches et des retours sont normaux.

## Fragments et intelligence collective

- Chaque `InfoFragment` est versionné, possède un détenteur/éligibilité, un intérêt cognitif et une règle de partage. L'élève A ne doit pas posséder tout ce dont il a besoin pour conclure.
- Le graphe de mission modélise la jointure `A + B -> possibilité de décision`, avec une **condition de preuve** indépendante des messages eux-mêmes.
- Interaction réelle : écouter, expliquer, aider, formuler une demande, transmettre une ressource. Le moteur ne doit pas obliger l'élève à « acheter » l'aide du camarade.
- Si le partenaire est absent, refuse ou rencontre une difficulté, un substitut enseignant/mode asynchrone garantit le droit d'apprendre.

## Adaptation privée à profils de besoins variés

Le profil n'est **pas une catégorie médicale ni un classement public**. Décrire les réglages utiles par tâche : longueur de consigne, supports visuels, oral/écrit/manipulation, pauses, nombre de variables, temps, décomposition, indices, outil d'assistance, choix de difficulté, transfert demandé.

| Paramètre | Accès guidé | Parcours courant | Approfondissement |
| --- | --- | --- | --- |
| Visuel public | même rôle et même intrigue | même rôle et même intrigue | même rôle et même intrigue |
| Lecture | phrases courtes, audio disponible | texte standard | documents à comparer |
| Calcul | petits nombres, matériel, décomposition | opérations adaptées à l'objectif | contrainte supplémentaire, justification |
| Interaction | binôme aidé / messager de substitution | échange A/B | négociation d'alternatives |
| Preuve | capacité réellement observable, soutien décrit | autonomie mesurée | transfert explicite |

Aucune récompense ou récit collectif ne doit révéler quel enfant a reçu quelle adaptation. **Même mission visible ≠ certification du même niveau de maîtrise.** Éviter la vitesse imposée et le concours de perfection comme condition d'accès à une activité essentielle.

## Séparation utile entre « réussite » et « privilège »

Une action de classe réelle (spectacle de clown, atelier, événement, collation) est une **demande facultative** soumise à autorisation. Pas de récompense obligeant le professeur à payer, pas de nourriture sans règles locales appropriées, pas de pénalité sociale si une tâche est inachevée. Les Klownkoins n'achètent ni notes ni aide indispensable.
