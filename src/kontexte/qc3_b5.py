"""B5 -- Québec 3: audited scenario mapping and *non-operational* bakeries.

Kontexte specifies situation and role perspectives. It never releases private
clues, operates Orgo tasks, or validates curriculum attainment.
"""
from __future__ import annotations

import csv
import hashlib
from html import escape
import json
from pathlib import Path

from .common import KontexteError, check, load_json, dump_json
from .models import curriculum_index

REL = Path('data/locales/qc/fr-CA/grade3')
SOURCE = 'commande-de-pains'
ROLES = ('boulanger', 'fermier', 'comptable')
GOALS = ('qc3.ma.multiplication', 'qc3.ma.addition', 'qc3.fr.lire-consigne', 'qc3.st.matiere')


def canonical_sha(obj:dict) -> str:
    """The pre-existing overlay uses sorted, non-ASCII, default JSON spacing."""
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode('utf-8')).hexdigest()


def gather(repo:Path) -> dict:
    repo = repo.resolve()
    source_path = repo/'data/trames/catalogue-neutral-v0.2.json'
    neutral_doc = load_json(source_path)
    overlays_doc = load_json(repo/REL/'overlays-60.json')
    objective_doc = load_json(repo/REL/'objectifs-candidats.json')
    year_doc = load_json(repo/REL/'parcours-36-semaines.json')
    micro_doc = load_json(repo/REL/'micro-situations-34.json')
    declared_audit = load_json(repo/REL/'audit-couverture.json')
    courses = curriculum_index(load_json(repo/'data/catalogue/202_kristals.json'))
    roles = {f.stem:load_json(f) for f in (repo/'data/roles').glob('*.json')}
    missions = {f.stem:load_json(f) for f in (repo/'data/missions').glob('*.json')}
    base = neutral_doc.get('scenarios',[])
    localized=overlays_doc.get('items',[])
    goals=objective_doc.get('objectifs',[])
    weeks=year_doc.get('semaines',[])
    micro=micro_doc.get('modules',[])
    check(hashlib.sha256(source_path.read_bytes()).hexdigest() == overlays_doc.get('parent_catalogue_hash'),
          'L’empreinte du catalogue neutre ne correspond plus à la surcouche Québec')
    check(len(base)==60 and len(localized)==60,'60 scénarios neutres et 60 adaptations attendus')
    check(len(roles)==38 and len(missions)==11,'Inventaire de rôles/missions différent de la base B5')
    check(len(goals)==83 and len(micro)==34 and len(weeks)==36,'Inventaire Québec 3 différent de la base B5')
    check(len(courses)==202,'Le catalogue interne de référence doit contenir 202 Kristals')
    def unique(seq,label):
        check(len(seq)==len(set(seq)),f'Doublons: {label}')
    unique([x['id'] for x in base],'scénarios neutres')
    unique([x['overlay_id'] for x in localized],'overlays')
    unique([x['base_trame_id'] for x in localized],'parent trames')
    unique([x['id'] for x in goals],'objectifs')
    unique([x['id'] for x in micro],'microsituations')
    check(sorted(x['semaine_pedagogique'] for x in weeks)==list(range(1,37)), 'Calendrier incomplet ou semaines dupliquées')
    nb={x['id']:x for x in base};ov={x['base_trame_id']:x for x in localized};g={x['id']:x for x in goals}
    check(set(nb)==set(ov),'Il manque une adaptation culturelle à une trame neutre')
    core=set(sum(year_doc['trames_pilotes_par_etape'].values(),[]))
    check(len(core)==32 and set(core)<=set(nb),'32 scénarios principaux attendus')
    weeks_for={x['trame_principale']:x['semaine_pedagogique'] for x in weeks if x.get('trame_principale')}
    check(set(weeks_for)==core,'Le calendrier ne correspond pas aux 32 scénarios principaux')
    check(all(x['trame_principale'] is not None or x['semaine_pedagogique'] in (9,18,27,36) for x in weeks), 'Semaines sans scénario inattendues')
    check(all(x['etape_interne_ekole']==(x['semaine_pedagogique']-1)//9+1 for x in weeks),'Étape interne incorrecte')
    candidate_ids=set(g)
    for neutral in base:
        frame=ov[neutral['id']]
        check(frame['neutral_parent']['catalogue_sha256']==overlays_doc['parent_catalogue_hash'],
              f"{neutral['id']}: empreinte catalogue invalide")
        check(frame['neutral_parent']['trame_sha256']==canonical_sha(neutral),f"{neutral['id']}: parent neutre modifié")
        check(all(role in roles for role in neutral.get('roles',[])),f"{neutral['id']}: rôle inconnu")
        check(set(frame['objectifs_candidats'])<=candidate_ids,f"{neutral['id']}: objectif inconnu")
        check(set(frame['adaptation'].get('autres_roles',[]))<=set(roles),f"{neutral['id']}: rôle local absent")
    for goal in goals:
        check(goal['ekole_kristal_id'] in courses,f"{goal['id']}: Kristal absent")
        check(goal['statut_correspondance']=='candidat_a_valider_avec_progression_3e',f"{goal['id']}: statut non attendu")
    for m in micro:check(m['objet_pedagogique'] in g,f"{m['id']}: objectif inconnu")
    used={goal for sid in core for goal in ov[sid]['objectifs_candidats']}
    remaining=set(g)-used
    check(len(used)==49 and len(remaining)==34,'Couverture 32 scénarios modifiée; réviser l’audit historique')
    check(remaining=={m['objet_pedagogique'] for m in micro},'Micro-situations ne couvrent pas exactement les objectifs complémentaires prévus')
    check(remaining==set(declared_audit['objectifs_non_mobilises_dans_32']),'Audit historique désynchronisé')
    check(all(m['type']=='enseignement_obligatoire_encadre' for m in micro if m['objet_pedagogique'] in {
          'qc3.ccq.prevention','qc3.ccq.genre','qc3.ccq.spiritualite','qc3.ccq.cycle-vie'}),'CCQ: enseignement encadré requis')
    for week in weeks:
        for rid in week.get('micro_situations_supplementaires',[]):
            check(rid in {m['id'] for m in micro},f'Semaine {week["semaine_pedagogique"]}: micro-situation inconnue')
    return dict(repo=repo,neutral=nb,overlays=ov,goals=g,year=year_doc,
                micro=micro,courses=courses,roles=roles,missions=missions,
                core=core, weeks_for=weeks_for,used=used,remaining=remaining,
                catalogue_sha256=overlays_doc['parent_catalogue_hash'])


def audit(repo:Path) -> tuple[dict,list[dict]]:
    ctx=gather(repo)
    source_rows=[]
    for sid,base in sorted(ctx['neutral'].items()):
        local=ctx['overlays'][sid]
        ids=local['objectifs_candidats']
        source_rows.append({'scenario_id':sid,'overlay_id':local['overlay_id'],
            'titre_qc':local['titre_qc'],'famille':base['famille'],
            'statut_annee':'principal_32' if sid in ctx['core'] else 'banque_optionnelle_28',
            'semaine_planifiee':ctx['weeks_for'].get(sid),
            'etape_suggeree':local['etape_suggeree'],
            'roles':base['roles'], 'objectifs_candidats':ids,
            'kristals_candidats':sorted({ctx['goals'][g]['ekole_kristal_id'] for g in ids}),
            'statut_validation':local.get('statut','statut_inconnu'),
            'catalogue_sha256':ctx['catalogue_sha256'],
            'neutral_frame_sha256':local['neutral_parent']['trame_sha256']})
    goal_rows=[]
    micro_index={m['objet_pedagogique']:m for m in ctx['micro']}
    for gid,v in sorted(ctx['goals'].items()):
        goal_rows.append({'objectif_id':gid,'discipline':v['discipline'],'notion':v['notion_de_travail'],
              'ekole_kristal_id':v['ekole_kristal_id'],'scenario_principaux':[sid for sid in sorted(ctx['core']) if gid in ctx['overlays'][sid]['objectifs_candidats']],
              'micro_situation_id':micro_index[gid]['id'] if gid in micro_index else None,
              'statut':'candidat_non_valide','preuve_attendue':v['preuve_attendue']})
    role_rows=[{'role_id':rid,'nom':role['name']['fr-CA'],
           'scenarios_neutres':[sid for sid,frame in sorted(ctx['neutral'].items()) if rid in frame['roles']],
           'scenarios_principaux':[sid for sid in sorted(ctx['core']) if rid in ctx['neutral'][sid]['roles']],
           'missions_historiques':[mid for mid,m in sorted(ctx['missions'].items()) if rid in m['roles']]}
           for rid,role in sorted(ctx['roles'].items())]
    result={'format':'kontexte.b5-audit/1','statut':'audit_referentiel_interne_non_officiel',
            'statistiques':{'roles':len(ctx['roles']),'missions':len(ctx['missions']),
             'scenarios_neutres':len(ctx['neutral']),'overlays_qc':len(ctx['overlays']),
             'scenarios_principaux':len(ctx['core']), 'scenarios_optionnels':len(ctx['neutral'])-len(ctx['core']),
             'semaines_planifiees':len(ctx['year']['semaines']),'semaines_sans_trame_principale':4,
             'objectifs_internes_candidats':len(ctx['goals']),
             'objectifs_cites_dans_32':len(ctx['used']),
             'objectifs_complementaires_prevus':len(ctx['remaining']),
             'micro_situations_planifiees':len(ctx['micro']),
             'cours_internes_de_reference':len(ctx['courses'])},
            'avertissement':'Les correspondances sont des hypothèses; aucun cours réalisé, acquis ou conformité ministérielle n’est attesté.',
            'provenance':{'catalogue_neutre_sha256':ctx['catalogue_sha256'],
              'overlays':'data/locales/qc/fr-CA/grade3/overlays-60.json',
              'objectifs':'data/locales/qc/fr-CA/grade3/objectifs-candidats.json',
              'plan':'data/locales/qc/fr-CA/grade3/parcours-36-semaines.json'},
            'semaines':[{'semaine':w['semaine_pedagogique'],'etape':w['etape_interne_ekole'],
                'scenario_id':w.get('trame_principale'),'micro_situations':w.get('micro_situations_supplementaires',[])}
                for w in ctx['year']['semaines']],
            'scenarios':source_rows,'objectifs':goal_rows,'roles':role_rows,
            'missions':[{'id':mid,'titre':m['title'].get('fr-CA',''),
                    'roles':m['roles'],'statut':m.get('status','statut_non_documente')} for mid,m in sorted(ctx['missions'].items())]}
    return result, source_rows


def export_audit(repo:Path,out:Path):
    data,rows=audit(repo)
    out.mkdir(parents=True,exist_ok=True)
    dump_json(data,out/'audit-b5.json')
    with (out/'index-scenarios-b5.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.writer(f,delimiter=';')
        writer.writerow(['scenario_id','overlay_id','titre_qc','famille','statut_annee','semaine_planifiee','etape_suggeree','roles','objectifs_candidats','kristals_candidats','statut_validation'])
        for row in rows:
            writer.writerow([row[k] if not isinstance(row[k],list) else '|'.join(row[k]) for k in (
               'scenario_id','overlay_id','titre_qc','famille','statut_annee','semaine_planifiee','etape_suggeree','roles','objectifs_candidats','kristals_candidats','statut_validation')])
    with (out/'index-objectifs-b5.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.writer(f,delimiter=';');writer.writerow(['objectif_id','discipline','notion','ekole_kristal_id','scenario_principaux','micro_situation_id','statut','preuve_attendue'])
        for row in data['objectifs']:
            writer.writerow([row[k] if not isinstance(row[k],list) else '|'.join(row[k]) for k in (
                'objectif_id','discipline','notion','ekole_kristal_id','scenario_principaux','micro_situation_id','statut','preuve_attendue')])
    with (out/'index-roles-b5.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.writer(f,delimiter=';');writer.writerow(['role_id','nom','scenarios_neutres','scenarios_principaux','missions_historiques'])
        for row in data['roles']:
            writer.writerow([row[k] if not isinstance(row[k],list) else '|'.join(row[k]) for k in (
                'role_id','nom','scenarios_neutres','scenarios_principaux','missions_historiques')])
    with (out/'calendrier-b5.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.writer(f,delimiter=';');writer.writerow(['semaine','etape','scenario_id','micro_situations'])
        for row in data['semaines']:
            writer.writerow([row[k] if not isinstance(row[k],list) else '|'.join(row[k]) for k in (
                'semaine','etape','scenario_id','micro_situations')])
    return data


def pilot(repo:Path) -> tuple[dict,dict]:
    ctx=gather(repo)
    check(ctx['weeks_for'][SOURCE]==10,'La boulangerie doit rester en semaine 10 du plan source')
    overlay=ctx['overlays'][SOURCE]
    check(set(GOALS)==set(overlay['objectifs_candidats']),'Objectifs du pilote divergents de la source')
    check(set(ROLES)==set(overlay['adaptation']['autres_roles']),'Rôles du pilote divergents de la source')
    original_exercises=load_json(ctx['repo']/REL/'exercices-deterministes.json')['exercices']
    exercise=next(e for e in original_exercises if e['scenario_id']==SOURCE)
    check(exercise['operands']==[6,4] and exercise['answer']==24,'Exercice source boulangerie modifié')
    provenance={'base_trame_id':SOURCE,'overlay_id':overlay['overlay_id'],
       'overlay_file':'data/locales/qc/fr-CA/grade3/overlays-60.json',
       'parent_catalogue_sha256':ctx['catalogue_sha256'],
       'parent_trame_sha256':overlay['neutral_parent']['trame_sha256'],
       'semaine_indicative':10}
    student={'format':'kontexte.b5-preview-eleve/1','id':'b5-qc3-boulangerie','audience':'student_preview',
             'statut':'prototype_pour_relecture_non_publie',
             'titre':'La commande de la boulangerie','niveau':'primaire-3',
             'intro':'La boulangerie du village a reçu une commande. Il faut préparer les plateaux de pains en carton.',
             'tache':'Représente les plateaux avec des dessins ou des jetons. Explique comment tu comptes les groupes égaux.',
             'mode_solo_sans_fragments':{'indication':'Exercice simplifié créé pour B5 : il ne remplace pas la situation source 6 × 4.',
                 'plateaux':3,'pains_par_plateau':4,
                 'question':'Dessine 3 plateaux avec 4 pains chacun. Combien de pains au total ?',
                 'aide_publique':'Tu peux dessiner les plateaux puis compter les jetons un à un.',
                 'statut':'simulation_solo_sans_etat_orgo'},
             'mission_collective':{'statut':'description_seulement_ne_pas_lancer_sans_orgo',
                 'message':'Pour une activité en équipe, certaines informations doivent être distribuées par l’enseignant dans un système autorisé.'},
             'roles':[{'id':rid,'nom':ctx['roles'][rid]['name']['fr-CA'],
                 'description':ctx['roles'][rid]['intro']['fr-CA']} for rid in ROLES],
             'objectifs_candidats':[{'id':'qc3.ma.multiplication','notion':'Faire des groupes égaux'},
                                     {'id':'qc3.ma.addition','notion':'Compter avec des additions répétées'},
                                     {'id':'qc3.fr.lire-consigne','notion':'Comprendre la consigne'}],
             'provenance':provenance}
    teacher={'format':'kontexte.b5-plan-enseignant/1','id':'b5-qc3-boulangerie',
       'audience':'teacher_only','statut':'prototype_a_valider_humainement',
       'titre':overlay['titre_qc'],'source_origine':{
          'scenario':SOURCE,'overlay':overlay['overlay_id'],'mission_historique':'boulangerie',
          'remarque':'La mission historique parle de 12 pains; la surcouche QC3 parle de six plateaux de quatre. Aucune des deux n’a été modifiée.'},
       'niveau':'primaire-3','semaine_indicative':10,'roles_suggeres':list(ROLES),
       'objectifs_candidats':list(GOALS),'kristals_candidats':{x:ctx['goals'][x]['ekole_kristal_id'] for x in GOALS},
       'statut_correspondances':'candidat_a_valider_avec_progression_3e',
       'scenario_complet_source':{'plateaux':6,'pains_par_plateau':4,
         'objectif':'Rassembler les deux renseignements pour trouver le nombre total de pains en carton.',
         'fragments_prives_a_distribuer_uniquement_par_orgo':overlay['relais_orchestration']['pieces_information'],
         'jointure_intention':overlay['relais_orchestration']['jonction'],
         'correction_reservee':{'total_pains':exercise['answer'], 'justification':exercise['check']}},
       'differenciation':{'accompagne':'Représenter 3 plateaux de 4 pains et compter avec des jetons.',
           'standard':'Résoudre le problème source 6 plateaux de 4 pains avec un dessin ou une addition répétée.',
           'approfondi':'Présenter deux méthodes et discuter un changement de quantité sans calcul automatique de maîtrise.'},
       'etapes_suggerees':[
         {'id':'mise-en-situation','action':'Lire la commande fictive; expliquer la mission avec les mots de l’enfant','validation':'réponse orale ou dessin'},
         {'id':'representation','action':'Représenter des groupes égaux avec carton, jetons ou crayons','validation':'groupes visibles'},
         {'id':'recherche','action':'Chercher la quantité totale sans dévoiler le corrigé','validation':'démarche montrée'},
         {'id':'retour','action':'Comparer deux démarches et formuler le résultat avec l’unité','validation':'relecture par un enseignant'}],
       'preuves_proposees':['schéma de groupes','addition répétée ou multiplication','explication et unité'],
       'evaluation':'pratique_candidate; maîtrise non présumée; validation par enseignant requise',
       'restrictions':['Ne pas partager les fragments privés dans un HTML public',
                       'Ne pas publier le corrigé dans une vue enfant',
                       'Ne pas considérer la fin de mission comme une preuve de maîtrise',
                       'Conserver les adaptations privées et non stigmatisantes',
                       'Aucune opération réelle, achat ou denrée alimentaire obligatoire'],
       'integration_future':{'orgo':'autorisations et transitions, non exécutées ici',
           'ekole':'liaisons pédagogiques candidates et preuves validées par un humain',
           'kompose':'dépendance exploratoire hors B5, ne pas déclencher de coordination'},
       'provenance':provenance}
    return student,teacher


def _html(title,body,notice):
    return ('<!doctype html><html lang="fr-CA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
      '<title>'+escape(title)+'</title><style>body{font:18px/1.55 system-ui;color:#193543;background:#f2f7fa;max-width:850px;margin:auto;padding:20px}'
      'article{background:#fff;border:1px solid #d5e7ee;border-radius:16px;padding:clamp(16px,3vw,28px)}'
      'h1{font-size:clamp(1.6rem,4vw,2.25rem)}h2{font-size:1.25rem}li{padding:.22rem}small{color:#4e6975}'
      '.warning{border-left:4px solid #b78422;padding:9px 15px;background:#fff5dc}a{color:#0c627d}</style></head><body>'
      '<p class="warning">'+escape(notice)+'</p><article><h1>'+escape(title)+'</h1>'+body+'</article></body></html>')


def export_pilot(repo:Path,out:Path):
    student,teacher=pilot(repo)
    sdir=out/'student-preview';tdir=out/'teacher-only';sdir.mkdir(parents=True,exist_ok=True);tdir.mkdir(parents=True,exist_ok=True)
    dump_json(student,sdir/'boulangerie.json')
    dump_json(teacher,tdir/'boulangerie-plan.json')
    studentbody='<p>'+escape(student['intro'])+'</p><h2>Ton défi</h2><p>'+escape(student['mode_solo_sans_fragments']['question'])+'</p>'
    studentbody+='<p>Tu peux utiliser des jetons ou dessiner sur une feuille.</p><h2>Dans une équipe, chacun peut avoir un rôle</h2><ul>'
    studentbody+=''.join('<li><strong>'+escape(x['nom'])+'</strong> — '+escape(x['description'])+'</li>' for x in student['roles'])+'</ul>'
    studentbody+='<p><small>'+escape(student['mission_collective']['message'])+'</small></p>'
    (sdir/'boulangerie.html').write_text(_html(student['titre'],studentbody,
         'Aperçu élève fictif non publié, à relire par un enseignant. Ceci ne lance pas une mission Orgo.'),encoding='utf8')
    teacherbody='<h2>Objectifs candidats</h2><ul>'
    teacherbody+=''.join('<li>'+escape(oid)+' → '+escape(cid)+'</li>' for oid,cid in teacher['kristals_candidats'].items())+'</ul>'
    teacherbody+='<h2>Leçon à préparer</h2><ol>'
    teacherbody+=''.join('<li><strong>'+escape(x['id'])+'</strong> : '+escape(x['action'])+'</li>' for x in teacher['etapes_suggerees'])+'</ol>'
    teacherbody+='<p>'+escape(teacher['source_origine']['remarque'])+'</p><p><strong>Corrigé interne :</strong> '+escape(teacher['scenario_complet_source']['correction_reservee']['justification'])+'</p>'
    teacherbody+='<p><strong>Non opérationnel : </strong>les fragments et transitions réels relèvent d’Orgo.</p>'
    (tdir/'boulangerie-enseignant.html').write_text(_html('Préparer : '+teacher['titre'],teacherbody,
          'Document réservé à l’enseignant : corrigé et objectifs candidats. Ne pas publier dans la galerie des élèves.'),encoding='utf8')
    return student,teacher
