"""Calculs pédagogiques exacts, sans évaluation officielle ni attribution de maîtrise.

La vérification locale fournit une preuve d'exercice, pas un statut Orgo ni une note.
"""
from __future__ import annotations
from decimal import Decimal
from .common import check
from .economy import bill

def invitation_paper(*, invitations: int, per_sheet: int, available_sheets: int) -> dict:
    for k,v in [('invitations',invitations),('per_sheet',per_sheet),('available_sheets',available_sheets)]:
        check(isinstance(v,int) and 0 <= v <= 10000, f'{k} entier positif requis')
    check(per_sheet > 0, 'une feuille produit au moins une invitation')
    needed=(invitations+per_sheet-1)//per_sheet
    missing=max(needed-available_sheets,0)
    return {'invitations':invitations,'per_sheet':per_sheet,'sheets_needed':needed,'sheets_available':available_sheets,
            'missing_sheets':missing,'curriculum_status':'practice_only','real_paper_waste_avoidance':True}

def lanterns(*, quantity:int, millilitres_each:int, container_ml:int) -> dict:
    for name, value in [('quantity',quantity),('millilitres_each',millilitres_each),('container_ml',container_ml)]:
        check(isinstance(value,int) and value>0 and value<=1000000, f'{name} entier positif requis')
    total=quantity*millilitres_each
    return {'total_ml':total,'containers_needed':(total+container_ml-1)//container_ml,'curriculum_status':'practice_only'}

def validate_numeric_answer(actual: str, expected: str) -> dict:
    """Un nombre exact, pas un jugement sur la démarche ou la maîtrise."""
    try: a=Decimal(actual.strip().replace(',','.')); e=Decimal(expected.strip().replace(',','.'))
    except Exception: return {'correct':False,'feedback':'Réponse numérique attendue'}
    return {'correct':a.is_finite() and e.is_finite() and a==e, 'feedback':'Vérification numérique uniquement'}
