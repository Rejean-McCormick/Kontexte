from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]/'data'/'missions'

def L(fr,en):return {'fr-CA':fr,'en':en}
def step(id,role,fr,en,kind='object',deps=(),courses=(),validation='human_review'):
 return {'id':id,'role':role,'instruction':L(fr,en),'kind':kind,'depends_on':list(deps),'curriculum_ids':list(courses),'validation':validation}
def frag(id,role,fr,en):return {'id':id,'holder_role':role,'content':L(fr,en),'release':'orgo_authorized','visibility':'participant'}
profiles={'accompagne':{'instruction':'Consignes courtes, pictogrammes et aide disponible, sans étiquette publique.'},'standard':{'instruction':'Autonomie progressive et défis adaptés.'},'approfondi':{'instruction':'Information partielle, décisions en plusieurs étapes et justification.'}}
main={
 'format':'kontexte.mission/1','id':'fete-sorciere','version':'1.0.0','synthetic':True,'title':L('La fête de la sorcière','The witch’s celebration'),
 'fiction':L('La sorcière prépare la fête du village, mais aucune personne ne possède toutes les informations.','The witch plans a village celebration, but nobody has all the information.'),'year_suggestion':3,
 'roles':['sorciere','origamiste','traducteur','messager','metteur-en-scene','redacteur','lecteur','regisseur','comptable','photographe'],
 'fragments':[
  frag('besoin-invitations','sorciere','Il faut 6 invitations et une invitation par personne.','We need 6 invitations, one per guest.'),
  frag('papier-disponible','messager','Une feuille produit 2 invitations. Il reste 2 feuilles.','One sheet makes 2 invitations. Two sheets remain.'),
  frag('budget','comptable','La fête dispose de 55 Klownkoins fictifs.','The party budget is 55 imaginary Klownkoins.'),
  frag('tarifs','regisseur','Le décor coûte 8 Klownkoins; chacun des quatre artistes gagne 6 Klownkoins.','Decor costs 8 Klownkoins; four artists earn 6 each.'),
 ],
 'steps':[
  step('origami','origamiste','Plie un chapeau de sorcière selon une séquence; décris les figures obtenues.','Fold a witch hat and describe its shapes.',courses=['qc-pri-ap-003']),
  step('invitation','sorciere','Rédige une invitation claire avec le lieu, le jour et le thème.','Write an invitation with place, date and theme.',courses=['qc-pri-fr-021']),
  step('bilingue','traducteur','Prépare une version anglaise simple de l’invitation.','Prepare a short English version.',deps=['invitation'],courses=['qc-pri-als-006']),
  step('echange-indices','messager','Rencontre le partenaire désigné, aide-le à finir sa tâche et partage l’indice du papier.','Meet the assigned partner, help them and exchange the paper clue.',deps=['bilingue'],kind='encounter'),
  step('repartition','sorciere','Ensemble, calcule le nombre de feuilles nécessaires et le manque de papier.','Together calculate the sheets needed and missing.',deps=['echange-indices'],validation='deterministic_practice',courses=['qc-pri-ma-009']),
  step('mandat','metteur-en-scene','Répartis quatre mandats pour une présentation commune.','Assign four presentation jobs.',deps=['repartition'],kind='message',courses=['qc-pri-ad-001']),
  step('discours','redacteur','Écris un discours de quatre phrases pour la cérémonie.','Write a four-sentence speech.',deps=['mandat'],kind='document',courses=['qc-pri-fr-021']),
  step('lecture','lecteur','Entraîne-toi à lire le discours devant le groupe.','Practise reading the speech aloud.',deps=['discours'],kind='performance',courses=['qc-pri-ad-001']),
  step('scene','regisseur','Place les chaises et le décor selon un plan approuvé.','Arrange seating and decor using an approved plan.',deps=['mandat'],kind='object'),
  step('budget-final','comptable','Combine les tarifs et le budget; calcule les paiements et une taxe strictement fictive.','Combine rates and budget; compute payments and a fictional tax.',deps=['lecture','scene'],kind='payment',validation='deterministic_practice',courses=['qc-pri-ma-006']),
  step('galerie','photographe','Documente les productions, puis soumets les médias au contrôle de consentement.','Document work and submit it for consent review.',deps=['origami'],kind='review',validation='logistical_only'),
 ],
 'joins':[{'id':'jointure-papier','fragment_ids':['besoin-invitations','papier-disponible'],'unlock_step':'repartition'},
          {'id':'jointure-budget','fragment_ids':['budget','tarifs'],'unlock_step':'budget-final'}],
 'adaptation':profiles,'safety':{'real_spending':False,'real_taxes':False,'publication_default':'private','teacher_approval_for':['furniture_moving','real_food','media_publication']},
 'constraints':{'virtual_reward_only':True,'participant_absent_fallback':'teacher_proxy','private_support_level':True}
}
other={
 'boulangerie':('La boulangerie du village','Village bakery',['boulanger','fermier','comptable'],['Commander la farine','Préparer 12 pains','Faire les comptes'],['qc-pri-ma-006','qc-pri-ma-009']),
 'atelier-mecanique':('L’atelier du mécanicien','Mechanic workshop',['mecanicien','inventeur','scientifique'],['Inspecter la roue','Mesurer la pièce','Tester le prototype'],['qc-pri-ma-006']),
 'spectacle-clown':('Le spectacle du clown','Clown show',['clown','metteur-en-scene','musicien'],['Inventer le numéro','Préparer le rythme','Présenter'],['qc-pri-ad-001']),
 'jardin-fermier':('Le jardin du fermier','Farm garden',['fermier','jardinier','scientifique'],['Observer la graine','Mesurer les pousses','Comparer'],['qc-pri-ma-006']),
 'conseil-village':('Le conseil du village','Village council',['politicien','redacteur','lecteur'],['Proposer une règle','Écrire les arguments','Délibérer'],['qc-pri-fr-021']),
 'chantier-maquette':('Le chantier de l’architecte','Architect model',['architecte','menuisier','regisseur'],['Dessiner le plan','Fabriquer la maquette','Installer'],['qc-pri-ap-003']),
 'laboratoire':('Le laboratoire','Laboratory',['scientifique','inventeur','photographe'],['Poser une hypothèse','Tester un objet fictif','Documenter'],['qc-pri-ma-006']),
 'salon-coiffure':('Le salon de coiffure','Hair salon',['coiffeuse','comptable','photographe'],['Préparer un rendez-vous','Établir un tarif','Documenter un dessin'],['qc-pri-ma-006']),
 'expedition':('L’expédition','Expedition',['explorateur','messager','scientifique'],['Tracer le chemin','Transmettre un indice','Rendre compte'],['qc-pri-fr-021'])
}

def save(m):
 (root/(m['id']+'.json')).write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
save(main)
for ident,(fr,en,roles,titles,courseids) in other.items():
 steps=[step('phase-'+str(i+1),r,t,t,kind='document' if i==0 else 'object',deps=['phase-'+str(i)] if i else [],courses=[courseids[0]],validation='human_review') for i,(r,t) in enumerate(zip(roles,titles))]
 m={'format':'kontexte.mission/1','id':ident,'version':'0.1.0','synthetic':True,'title':L(fr,en),'fiction':L('Mission de simulation du monde '+fr+'.', 'Simulation mission: '+en+'.'), 'year_suggestion':3,'roles':roles,'steps':steps,
    'fragments':[frag('indice-un',roles[0],'Le premier groupe détient une mesure.','The first group has a measurement.'),frag('indice-deux',roles[1],'Le deuxième groupe détient une quantité.','The second group has a quantity.')],
    'joins':[{'id':'jointure-infos','fragment_ids':['indice-un','indice-deux'],'unlock_step':'phase-3'}], 'adaptation':profiles,
    'status':'scenario_skeleton_requires_pedagogical_review'}
 save(m)
# Solo: distinct workflow one person
save({'format':'kontexte.mission/1','id':'sorciere-solo','version':'1.0.0','synthetic':True,'title':L('Le chaudron des mesures','Measuring the cauldron'),
'fiction':L('Mila veut remplir quatre fioles avec la même quantité de potion imaginaire.','Mila wants to fill four equal bottles with imaginary potion.'),'year_suggestion':3,'roles':['sorciere'],
'fragments':[frag('indice-mesure','sorciere','Une fiole contient 125 mL.','Each bottle holds 125 mL.')],
'steps':[step('mesurer','sorciere','Calcule 4 × 125 mL et explique ta démarche.','Calculate 4 × 125 mL and explain.',courses=['qc-pri-ma-006'],validation='deterministic_practice'),
         step('expliquer','sorciere','Rédige une phrase qui explique ta solution.','Write a sentence explaining your solution.',deps=['mesurer'],kind='document',courses=['qc-pri-fr-021'])],
'joins':[],'adaptation':profiles})
print('generated 11 missions')
