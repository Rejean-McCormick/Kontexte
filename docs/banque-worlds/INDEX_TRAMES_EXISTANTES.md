# Index transversal — ne pas confondre trame, mission et World

**60 trames neutres** sont déjà définies dans `Kontexte/data/trames/catalogue-neutral-v0.2.json`; chacune a une **déclinaison QC3** dans `Kontexte/data/locales/qc/fr-CA/grade3/overlays-60.json`. Elles sont des idées, **pas** 60 Worlds opérationnels.

En outre, `Kontexte` propose **34 micro-situations** et un **parcours indicatif de 36 semaines**. Les 11 fichiers de missions existants sont des objets `kontexte.mission/1` de granularité plus grande que les micro-situations, dont 9 simples ébauches, 1 pilote détaillé et 1 mission solo. Nos 6 nouvelles missions sont des **développements de trames déjà présentes**, pas 6 nouvelles familles conceptuelles.

| ID de trame neutre | Titre déjà présent | Déclinaison québécoise existante |
|---|---|---|
| `fete-commune` | La fête commune | Le rassemblement des ateliers |
| `spectacle-imprevu` | Le spectacle imprévu | Le petit spectacle de quartier |
| `repas-partage` | Le repas partagé | Le menu fictif des récoltes |
| `marche-des-creations` | Le marché des créations | Le mini-marché des œuvres |
| `bibliotheque-vivante` | La bibliothèque vivante | Les histoires à partager |
| `merci-collectif` | La cérémonie des mercis | Les cartes de gratitude |
| `commande-de-pains` | La commande de pains | La commande de la boulangerie fictive |
| `chapeau-de-papier` | Le chapeau de papier | Les chapeaux de papier |
| `pont-miniature` | Le pont miniature | Le pont de carton |
| `mecanisme-en-panne` | Le mécanisme en panne | Le mécanisme des décors |
| `atelier-metal` | Le projet du forgeron | La forge en papier |
| `costumes-recycles` | Les costumes réinventés | La malle de costumes réemployés |
| `message-fragmente` | Le message incomplet | L’invitation en morceaux |
| `plante-mystere` | La plante mystérieuse | Les semis inconnus |
| `carte-incomplete` | La carte incomplète | Le plan incomplet de l’école |
| `sons-des-lieux` | Les sons du quartier | La carte sonore du voisinage |
| `ombres-mobiles` | Le mystère des ombres | Les ombres de la cour |
| `colis-egare` | Le colis égaré | Le paquet de livres égaré |
| `coup-de-main` | La mission coup de main | Un coup de main à l’atelier |
| `tuteurs-temporaires` | Les ateliers solidaires | Les parrains de fabrication |
| `maquette-accessible` | La maquette inclusive | Le parcours accessible en maquette |
| `affiche-service` | L’affiche d’entraide | L’affiche du service d’entraide |
| `accueil-nouveaux` | Le guide des nouveaux | Bienvenue à notre école |
| `reparer-pour-un-autre` | L’atelier de réparation | L’atelier des objets de papier |
| `jardin-saisonnier` | Le jardin des saisons | Le potager des quatre saisons |
| `reserve-eau` | La réserve d’eau | La réserve d’eau du jardin |
| `foret-partagee` | La forêt partagée | L’usage partagé d’un boisé |
| `habitats-des-animaux` | Les habitats à protéger | Les abris des animaux du Québec |
| `lac-a-preserver` | Le lac à préserver | Le lac et ses visiteurs |
| `compost-collectif` | Le compost collectif | Le compost de l’école |
| `caisse-klownkoins` | La caisse des Klownkoins | La caisse de la fête |
| `budget-marche` | Le budget du marché | Le budget des kiosques |
| `stock-et-commande` | Le stock insuffisant | Les 24 invitations manquantes |
| `taxe-de-simulation` | La taxe fictive | La taxe imaginaire des Klownkoins |
| `troc-equitable` | L’échange équitable | L’échange des matériaux |
| `transport-commande` | Le trajet le plus utile | La tournée des fournitures |
| `invitation-multilingue` | L’invitation multilingue | L’invitation fr-CA / en-CA |
| `bulletin-local` | Le bulletin local | Les nouvelles de notre quartier |
| `journal-exploration` | Le carnet d’exploration | Carnet d’une exploration québécoise |
| `conte-partage` | Le conte mis en scène | Le conte inventé ensemble |
| `notice-ambigue` | La notice ambiguë | La notice difficile à suivre |
| `mode-emploi-visible` | Le mode d’emploi accessible | Le mode d’emploi illustré |
| `semis-compare` | Les semis comparés | Deux bacs de haricots |
| `ciel-en-cartes` | Les cartes du ciel | Le ciel de notre région |
| `station-meteo` | La station météo | La météo de la cour |
| `ponts-a-tester` | Les structures à tester | Le concours de ponts en carton |
| `temperatures-melangees` | Les mesures mélangées | Les relevés de température |
| `lumiere-et-couleurs` | Le laboratoire de lumière | La lumière de l’atelier |
| `messagers-en-mouvement` | Le relais des messages | Le relais des invitations |
| `salle-a-configurer` | La salle à préparer | Aménager la salle |
| `parcours-livraison` | Le parcours de livraison | La tournée du messager |
| `indices-dans-ecole` | Les indices dans l’école | La chasse aux indices calme |
| `itineraire-sur` | L’itinéraire sûr | Le plan d’un trajet sûr |
| `randonnee-symbolique` | La randonnée des découvertes | La randonnée des découvertes |
| `conseil-du-village` | Le conseil du village | Le conseil de la classe |
| `regles-ateliers` | Les règles de l’atelier | Les règles de travail commun |
| `ressources-a-partager` | La ressource partagée | Les matériaux partagés |
| `horaires-contradictoires` | Le calendrier des groupes | L’emploi du temps des ateliers |
| `photo-ou-pas` | La photo et le choix | Publier ou protéger une création |
| `vote-projet-commun` | Le projet commun | Choisir un projet de groupe |

## Raccordement des 6 nouvelles missions détaillées

| Fichier JSON proposé | Trames parentes **existantes** |
|---|---|
| `grand-menage-chez-mamie.json` | `coup-de-main`, `salle-a-configurer`, `ressources-a-partager` |
| `randonnee-a-velo.json` | `randonnee-symbolique`, `itineraire-sur`, `reparer-pour-un-autre` |
| `spectacle-des-histoires.json` | `conte-partage`, `spectacle-imprevu`, `vote-projet-commun` |
| `rallye-des-metiers.json` | `indices-dans-ecole`, `tuteurs-temporaires`, `regles-ateliers` |
| `mystere-de-la-bibliotheque.json` | `bibliotheque-vivante`, `message-fragmente`, `mode-emploi-visible` |
| `pique-nique-des-saisons.json` | `repas-partage`, `station-meteo`, `transport-commande` |

**Conséquence :** à terme, l'enseignant peut naviguer par famille de problèmes, notion à travailler, niveau, durée et potentiel coopératif, puis sélectionner une mission éditée comme candidat pour son propre World. On ne multiplie pas les Worlds au moment de cataloguer les 60 idées : ils sont créés seulement pour une instance de scénario sélectionnée et autorisée.
