# Réconciliation de `MANIFEST.sha256` — 23 novembre 2026

Le manifeste racine contient **202 chemins présents** dans le snapshot du lot 4. L'audit a constaté **56 empreintes périmées** et aucun fichier absent; les chemins et l'ordre ont été conservés, leurs empreintes SHA-256 ont été réalignées sur les octets du snapshot. L'original doit rester dans la sauvegarde de l'installateur (`koa_overlay_backups\lot4_*`).

**Précondition d'installation :** l'overlay vérifie le SHA-256 des 202 fichiers suivis avant de remplacer le manifeste. Si un fichier local a changé depuis le SmartDump, l'installation s'arrête **avant toute écriture**; il faudra créer un nouveau manifeste à partir de la nouvelle source, pas forcer des empreintes périmées.

Ce manifeste est une liste d'intégrité de fichiers, **pas** un contrat pédagogique, une autorisation de publication, ni une validation du parcours `qc-pri-ma-006` / `qc-pri-ma-008`. Aucun scénario ou cours n'est modifié.

Vérification PowerShell 7 (après installation) :

```powershell
cd C:\mycode\Ekole\Kontexte
Get-Content .\MANIFEST.sha256 | ForEach-Object {
    $m = [regex]::Match($_, '^([0-9a-f]{64})  (.+)$')
    if (-not $m.Success) { throw "Ligne invalide : $_" }
    $file = Join-Path (Get-Location).Path $m.Groups[2].Value
    if ((Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLowerInvariant() -ne $m.Groups[1].Value) {
        throw "SHA-256 différent : $file"
    }
}
'202/202 empreintes vérifiées'
```

Les fichiers de documentation ajoutés après la capture ne figurent pas automatiquement dans ce manifeste figé au 23 novembre 2026.
