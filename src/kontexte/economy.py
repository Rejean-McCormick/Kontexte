"""Calcul exact de Klownkoins fictifs, sans connexion monétaire."""
from decimal import Decimal, ROUND_HALF_UP
from .common import check

CENT = Decimal("0.01")

def amount(value: str | int) -> Decimal:
    d = Decimal(str(value))
    check(d.is_finite() and d >= 0, "montant non négatif et fini requis")
    return d.quantize(CENT, rounding=ROUND_HALF_UP)

def bill(lines: list[dict], *, fictional_tax_rate: str = "0") -> dict:
    rate = Decimal(fictional_tax_rate)
    check(rate.is_finite() and Decimal(0) <= rate <= Decimal(1), "taux fictif 0..1")
    details=[]; base=Decimal(0)
    for line in lines:
        qty = line["quantity"]
        check(isinstance(qty, int) and 0 <= qty <= 10000, "quantité entière 0..10000")
        subtotal = amount(line["unit_price"]) * qty
        base += subtotal
        details.append({"description": str(line["description"])[:100], "quantity":qty, "unit_price":str(amount(line["unit_price"])), "subtotal":str(subtotal)})
    tax = (base * rate).quantize(CENT, rounding=ROUND_HALF_UP)
    return {"currency": "Klownkoins", "fictional": True, "items": details,
            "subtotal": str(base), "fictional_tax_rate": str(rate), "tax": str(tax), "total": str(base+tax),
            "legal_notice": "Jeu pédagogique, aucune monnaie réelle ni taxe fiscale officielle."}
