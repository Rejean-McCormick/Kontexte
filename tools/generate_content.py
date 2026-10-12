"""Génère des fichiers sources de catalogue de rôles pour Kontexte (outillage de dépôt)."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
raw=[
("sorciere","Sorcière","Witch","créer des objets imaginaires, enquêter, organiser une fête","créer une potion fictive, préparer des accessoires, organiser","chapeau, invitation, potion fictive","ingrédient manquant, fête à organiser","origamiste, messager, scientifique"),
("boulanger","Boulanger","Baker","préparer les commandes de la boulangerie","préparer des recettes, vendre, livrer","pain, recette, ticket","commande urgente, panne de four","fermier, livreur, comptable"),
("clown","Clown","Clown","préparer un spectacle comique","jongler, présenter, inviter","costume, scène, accessoires","spectacle incomplet, accessoires manquants","metteur-en-scene, photographe, musicien"),
("politicien","Politicien","Civic representative","proposer une décision collective","délibérer, expliquer, voter","ordre du jour, discours","désaccord, priorité concurrente","redacteur, lecteur, comptable"),
("menuisier","Menuisier","Carpenter","fabriquer des objets en bois fictif ou matériaux sécuritaires","mesurer, dessiner, assembler","plan, règle, planche de carton","pièce trop courte, plan incomplet","architecte, mecanicien, peintre"),
("mineur","Mineur","Miner","explorer un gisement fictif","cartographier, classer, compter","carte, cailloux, lampes factices","tunnel fermé, ressources rares","scientifique, explorateur, comptable"),
("coiffeuse","Coiffeuse","Hairdresser","concevoir des styles et services imaginaires","dessiner, écouter, organiser","modèle, ciseaux de papier, miroir","rendez-vous en retard","artiste, comptable, photographe"),
("forgeron","Forgeron","Blacksmith","fabriquer des outils fictifs en papier","concevoir, comparer, assembler","plan, métal fictif, carton","outil à réparer, matériau épuisé","chevalier, menuisier, inventeur"),
("pecheur","Pêcheur","Fisher","organiser une pêche simulée","mesurer, observer, classifier","carte, filet fictif, carnet","météo défavorable, capture limitée","scientifique, cuisinier, comptable"),
("peintre","Peintre","Painter","créer les affiches et décors","dessiner, colorier, exposer","affiche, pinceau, palette","panneau manquant, délais","metteur-en-scene, photographe, ecrivain"),
("ecrivain","Écrivain","Writer","écrire une histoire et des messages","rédiger, corriger, lire","cahier, invitation, manuscrit","information manquante, consigne floue","lecteur, traducteur, redacteur"),
("createur-jeux","Créateur de jeux vidéo","Video game designer","concevoir un petit jeu sur papier","décrire des règles, tester, déboguer","grille, personnage, carte","règle ambiguë, niveau bloqué","scientifique, inventeur, peintre"),
("mystique","Mystique","Mystic","explorer des symboles et contes imaginaires","interpréter, raconter, dessiner","symbole, conte, carte","énigme non résolue","sorciere, ecrivain, explorateur"),
("origamiste","Maître de l’origami","Origami master","fabriquer des objets par pliage","plier, compter, enseigner","papier, chapeau, étoile","papier insuffisant, pli complexe","sorciere, peintre, photographe"),
("fermier","Fermier","Farmer","organiser une ferme imaginaire","semer, mesurer, récolter","semences, pot, panier","sécheresse fictive, commandes","boulanger, jardinier, scientifique"),
("danseur","Danseur","Dancer","préparer une chorégraphie","compter les temps, répéter, présenter","musique, séquence, scène","rythme difficile, espace limité","musicien, metteur-en-scene, regisseur"),
("mecanicien","Mécanicien","Mechanic","réparer des objets simulés","diagnostiquer, mesurer, assembler","engrenage carton, vélo fictif, plan","pièce manquante, dysfonctionnement","inventeur, menuisier, scientifique"),
("scientifique","Scientifique","Scientist","tester une hypothèse","observer, calculer, comparer","carnet, tableau, mesure","résultat contradictoire, mesure incomplète","jardinier, sorciere, inventeur"),
("bucheron","Bûcheron","Forestry worker","planifier une récolte forestière durable fictive","mesurer, sélectionner, cartographier","carte, arbre, règle","forêt protégée, quotas","scientifique, fermier, menuisier"),
("chevalier","Chevalier","Knight","protéger et organiser un château imaginaire","planifier, aider, négocier","bouclier de papier, carte, lettre","pont endommagé, message secret","forgeron, architecte, messager"),
("extraterrestre","Extraterrestre","Alien","découvrir un monde et communiquer","décoder, observer, traduire","message, astronef de carton, carte","langage inconnu, signal incomplet","astronaute, traducteur, scientifique"),
("dresseur-animaux","Éducateur animalier","Animal educator","étudier les animaux avec respect","observer, classifier, expliquer","fiche espèce, schéma, habitat","animal stressé, alimentation spéciale","veterinaire, scientifique, fermier"),
("veterinaire","Vétérinaire","Veterinarian","soigner des animaux fictifs","observer, diagnostiquer fictivement, expliquer","dossier, peluche, balance","symptôme incompris, matériel manquant","dresseur-animaux, scientifique, comptable"),
("architecte","Architecte","Architect","imaginer des bâtiments","mesurer, dessiner, organiser","plan, maquette, règle","terrain étroit, budget limité","menuisier, regisseur, comptable"),
("musicien","Musicien","Musician","préparer une musique de fête","composer, rythmer, jouer","partition, instrument, chanson","rythme à synchroniser","danseur, clown, metteur-en-scene"),
("astronaute","Astronaute","Astronaut","planifier une mission spatiale fictive","calculer, explorer, communiquer","carte stellaire, fusée de papier","carburant imaginaire limité","scientifique, extraterrestre, explorateur"),
("inventeur","Inventeur","Inventor","résoudre des problèmes par des prototypes","concevoir, tester, réparer","prototype carton, croquis, mesures","prototype instable","mecanicien, scientifique, architecte"),
("cuisinier","Cuisinier","Cook","préparer un menu fictif","mesurer, lire, calculer","menu, recette, ingrédients fictifs","allergie simulée, commande large","fermier, boulanger, comptable"),
("explorateur","Explorateur","Explorer","explorer un territoire imaginaire","cartographier, observer, communiquer","carte, carnet, boussole","route fermée, message perdu","messager, scientifique, extraterrestre"),
("jardinier","Jardinier","Gardener","aménager un jardin scolaire","semer, mesurer, classer","graines, plante, arrosoir","manque de lumière, stock","fermier, scientifique, peintre"),
("messager","Messager","Messenger","livrer des messages et aider les autres","rencontrer, remettre, confirmer","invitation, carte, enveloppe","destinataire absent, message incomplet","sorciere, explorateur, redacteur"),
("metteur-en-scene","Metteur en scène","Director","orchestrer une représentation","planifier, coordonner, répéter","planning, scène, texte","intervenant absent, retard","redacteur, lecteur, regisseur"),
("redacteur","Rédacteur","Scriptwriter","écrire les textes d'une cérémonie","rédiger, corriger, adapter","discours, mandat, brouillon","informations manquantes","sorciere, metteur-en-scene, traducteur"),
("lecteur","Lecteur","Reader","dire le discours au public","lire, répéter, articuler","discours, micro factice, pupitre","prononciation difficile","redacteur, metteur-en-scene, traducteur"),
("regisseur","Régisseur","Stage manager","préparer la scène et les objets","installer, vérifier, coordonner","chaises, décor, plan","place insuffisante","metteur-en-scene, origamiste, peintre"),
("comptable","Comptable","Accountant","tenir le budget fictif","additionner, vérifier, présenter","facture, Klownkoins, registre","budget dépassé, taxe fictive","boulanger, sorciere, politicien"),
("photographe","Photographe","Photographer","documenter les productions avec permission","cadrer, classer, documenter","photo, galerie, métadonnées","refus de publication, tag erroné","origamiste, peintre, metteur-en-scene"),
("traducteur","Traducteur","Translator","produire des invitations bilingues","comparer, reformuler, relire","dictionnaire, texte, invitation","mot ambigu, manque de contexte","ecrivain, sorciere, messager"),
]
# Contents are authored simulation data, not professional descriptions or advice.
for key,fr,en,intro,actions,objects,problems,partners in raw:
 data={"format":"kontexte.role/1", "id":key,"name":{"fr-CA":fr,"en":en},"intro":{"fr-CA":intro,"en":f"You are playing the role of {en.lower()} in a learning story."},"theme":key if key in ("sorciere","boulanger") else "neutral", "actions":[x.strip() for x in actions.split(',')],"objects":[x.strip() for x in objects.split(',')],"problems":[x.strip() for x in problems.split(',')],"partners":[x.strip() for x in partners.split(',')]}
 (root/'data'/'roles'/f'{key}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Generated roles:',len(raw))
