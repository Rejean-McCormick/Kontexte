# 05 — Pilote complet : « La fête de la sorcière » (3e année)

**Objectif de design :** vérifier une mission qui mélange fabrication, communication bilingue, déplacement/entraide, coordination théâtrale, économie fictive et publication prudente, **sans écran ou période séparé par matière**. Nombres, taxes et correspondances curriculaires sont **des paramètres pilotes**, non des exigences officielles de 3e année.

## Fiction d'entrée (courte)

La sorcière Mila prépare une fête dans le village. Elle souhaite offrir des chapeaux de papier et inviter tout le monde. Mais son équipe est occupée, et personne ne possède seul le plan complet. Pour ouvrir les portes à temps, Mila devra fabriquer, communiquer, aider, organiser et tenir les comptes.

## Distribution des responsabilités

| Participant / rôle | Mandat réel | Information distinctive | Production |
| --- | --- | --- | --- |
| Mila / sorcière | organise la fête, fabrique un premier chapeau | thème « étoiles » et besoins de la fête | chapeau + ordre de mission |
| Origamiste (ou Mila) | concevoir et plier les accessoires | modèle + taille de papier | accessoires étiquetés |
| Rédacteur/traducteur (ou Mila) | écrire invitation FR/EN | modèle de carte et lexique approuvé | invitation bilingue imprimable |
| Messager (ou Mila) | trouver le destinataire désigné; **aider à finir sa tâche avant de livrer** | destination et contrainte de la tâche | livraison confirmée + aide observable |
| Équipe de 4 | metteur en scène; auteur du discours; lecteur/orateur; régisseur décor/chaises | chaque membre reçoit sa portion du plan | scène prête + présentation |
| Comptable + enseignant | payer en Klownkoins et calculer le bilan | tarifs/autorité de caisse | registre et total vérifié |
| Photographe | documenter les accessoires, pas surveiller les enfants | autorisations explicites de diffusion | médias privés; publications filtrées |

Un élève peut remplir plusieurs fonctions au besoin; les mandats restent modulaires, la mission ne suppose pas 10 enfants ni des professions permanentes. Les rôles scolaires sont facultatifs.

## Graphe des étapes et déclencheurs

```text
S0 Invitation à la fête
  -> S1 Origami (suivre étapes / créer chapeau)
  -> S2 Invitation FR + anglais contrôlé
  -> S3 Orgo propose destinataire disponible selon consentement et contexte
       -> si sa tâche non finie : aide adaptée (ne pas exiger que l'enfant la fasse à sa place)
       -> S4 remise des invitations, accusé de réception
  -> S5 remise du thème/mandat à une équipe de 4
       -> S6a metteur en scène      -> plan et horaire
       -> S6b rédacteur discours   -> texte
       -> S6c lecteur/orateur      -> présentation
       -> S6d régisseur           -> chaises / décor
       -> jointure S6a-d + critères de sécurité -> S7 représentation
  -> S8 paiements simulés en Klownkoins + comptes avec enseignant
  -> S9 photographe documente les œuvres; contrôles d'autorisation
  -> S10 bilan de mission + propositions de nouvelles quêtes
```

Ne pas forcer l'ordre strict entre S1 et S2 si deux enfants travaillent en parallèle. Les gardes règlent les dépendances importantes : aucune scène sans espace sécuritaire; aucune invitation distribuée avant validation du lieu/horaire; aucune publication sans consentement.

## La tension mobilisatrice et les informations distribuées

**A : la sorcière** possède la liste de six personnes à inviter et le thème « étoiles ». Elle ne sait pas combien d'invitations pourront être imprimées.  
**B : le responsable des impressions** possède la règle « une feuille permet deux invitations » et le stock de deux feuilles; il ne connaît pas la liste des invités.  
**Jointure A+B :** 6 invitations / 2 par feuille = **3 feuilles nécessaires**; 2 feuilles disponibles -> **il manque 1 feuille**.  
**Nouvelle quête** : demander à l'origamiste si une feuille recyclable supplémentaire est disponible ou proposer une invitation collective au tableau, avec accord du professeur.

Chacun contribue un renseignement nécessaire. En absence d'un partenaire, l'enseignant peut fournir le fragment manquant par le mode de secours, sans pénalité.

## Origami

- suivre un modèle approuvé, plier sans outil dangereux, expliquer une séquence et vérifier que le chapeau tient sur une maquette ou qu'il est décoratif;
- mesurage optionnel du côté d'une feuille, comparaison de plis et symétrie observable; attention, **ne pas promettre une symétrie exacte** d'un modèle qui n'a pas été vérifié;
- preuve : photo de l'**objet seul**, grille de suivi des étapes, explication courte orale ou écrite.

## Invitation bilingue

**Version de travail fr-CA** (exemple non certifié) : « Tu es invité à la Fête des étoiles! Rendez-vous vendredi à 14 h dans la classe. Apporte ton chapeau de papier. »  
**Version de travail en** (à réviser pour l'âge et contexte) : “You are invited to the Star Party! Meet us on Friday at 2 p.m. in our classroom. Bring your paper hat.”

Les deux utilisent un même contrat de données `{date, time, location, theme, audience}` validé et des messages localisés; ne pas écrire deux horaires différents librement. Avant impression : contrôles d'orthographe, accord de l'enseignant, droit de contact/distribution.

## Équipe de quatre : livrables distincts

1. **Metteur en scène** — ordre de passage et signal de départ.
2. **Rédacteur** — discours bref avec ouverture, message central et conclusion.
3. **Lecteur** — préparation et lecture orale, expression intelligible; possibilité de soutiens.
4. **Régisseur** — plan simple de salle, installation des chaises sans charge dangereuse et décor accessible.

Une équipe ne livre « scène prête » qu'après réception des quatre sorties utiles. L'évaluation pédagogique examine séparément expression orale, écrit, repérage spatial, coopération et organisation; pas de note de groupe imposée à tous.

## Klownkoins : vraie arithmétique, économie fictive

**Paramètres d'une variante pilote** : budget initial 70 Klownkoins; mises en scène rémunérées selon une grille autorisée. Les pièces sont purement pédagogiques, sans convertibilité en argent réel. La « taxe » est **fictive** et ne représente pas la TPS/TVQ.

| Service | Tarif fictif |
| --- | ---: |
| Metteur en scène | 12 Klownkoins |
| Rédacteur | 10 Klownkoins |
| Lecteur | 8 Klownkoins |
| Régisseur | 10 Klownkoins |
| Photographe (œuvres seulement) | 10 Klownkoins |
| **Sous-total** | **50 Klownkoins** |

Calculs : `12 + 10 + 8 + 10 + 10 = 50`. Règle fictive simplifiée : **1 Klownkoin de taxe pour chaque groupe complet de 10 Klownkoins de services** : `50 ÷ 10 = 5`; `50 + 5 = 55`; `70 − 55 = 15` Klownkoins restants.

Le professeur peut faire observer le lien **10 % = 1 sur 10** mais ne doit pas déduire la maîtrise des pourcentages pour un enfant de 3e année (le cours Ekole `qc-pri-ma-017` est suggéré pour la 6e, affectation non validée). Variant plus simple : dix jetons par ligne, additions successives; variante enrichie : factures, budget révisé, taxes calculées comme pourcentage **si et seulement si adéquat** au profil et à l'objectif suivi.

Une écriture de grand livre auditable comprend `entry_id`, montant entier non négatif, émetteur, destinataire, motif, référence mission, authorisation et contre-écriture éventuelle. Pas de frappe libre permettant de fabriquer une monnaie réelle. Aucune récompense pédagogique essentielle ne dépend de la richesse fictive d'un autre enfant.

## Photographie et galerie permanente

1. Photographier en priorité **les créations sans enfants ni données identifiantes**.
2. Associer `artifact_id`, type de création et auteur par pseudonyme interne.
3. Ne proposer « publication école » ou « public » que si chaque personne identifiable et titulaire des droits applicable l'autorise; un auteur peut aussi refuser la diffusion de son œuvre.
4. Si consentement refusé/inconnu : conserver en coffre privé selon les règles d'établissement, **ne pas livrer l'image ni ses métadonnées à l'espace public**. Une vignette de substitution neutre peut représenter l'existence d'une production sans l'identifier.
5. Le retrait d'un consentement révoque les publications sous contrôle d'Ekole et déclenche les suppressions/caches prévus. Le caractère « permanent » de la galerie signifie une adresse durable **conditionnée à la possibilité de retrait**, pas un droit de diffusion irrévocable.

## Correspondances scolaires candidates pour cette mission

| Étape | Pistes d'IDs locaux Ekole (vérifiées dans le catalogue) | Preuve réellement nécessaire |
| --- | --- | --- |
| Invitation FR | `qc-pri-fr-021` | texte produit/révisé selon un critère d'écrit |
| Anglais social | `qc-pri-als-006` | interaction orale observée; la copie d'un texte EN ne suffit pas |
| Arts / composition | `qc-pri-ap-003` | composition observée et trace d'intention |
| Calcul facture | `qc-pri-ma-006`, `qc-pri-ma-008`, `qc-pri-ma-007` | opérations réellement réalisées, non seulement recopiées |
| Géométrie / formes | `qc-pri-ma-023` | reconnaissance et description de formes dans l'objet |
| Expression scénique | `qc-pri-ad-001` | démonstration adaptée avec grille d'observation |
| Taxes en pourcentage | `qc-pri-ma-017` | **approfondissement hors présomption de maîtrise 3e** |

Ces liens ne sont **pas** des références PFEQ officielles; la revue du CurriculumMap décidera si le rattachement est correct et à quelle année/compétence il correspond.

## Bilan de fin de journée

Le professeur consulte : travaux réalisés, enfants ayant besoin d'un autre essai, pièces manquantes, livre de Klownkoins, demandes média en attente, critères validés, mission suivante éventuelle. Les élèves peuvent raconter ce qu'ils ont fait plutôt que recevoir une liste de « notes par matière ».
