# Privacy, Consent and Media

**The current repository is not a secure child-data platform.** It includes no student accounts, no media-hosting service, no production identity mapping and no completed consent-withdrawal system. All demonstrations should use synthetic data.

## Core rule: prevent release at the source

If consent to publish is missing, refused, expired or withdrawn, a public export must include **none** of the affected person's or work's restricted media:

- no original photo or video;
- no thumbnail or blurred copy;
- no embedded identifying metadata (including EXIF);
- no identifying tags, names or links to their work.

A CSS veil applied to a public URL is **not** adequate: the original bytes would still be accessible. A proper future service must remove or block the actual asset, derivative copies, CDN caches and searchable metadata as appropriate.

## Current prototype

The `privacy` CLI command uses `src/kontexte/media.py` to produce a conservative **manifest decision** from an asset description, intended audience and consent records. It does not host, move, delete, blur, or purge media files.

```bash
PYTHONPATH=src python -m kontexte privacy \
  --input examples/consent-refusal.json \
  --out /tmp/privacy-result.json
```

The example demonstrates a refused publication request using fictional metadata. It is not a real consent register.

## Publishing scopes

A future design may distinguish teacher-only, group, school and public audiences, with consent scoped separately per asset and participant. **These proposed scopes are not currently a completed permissions service.** Each publication request should verify current authorization, relevant guardianship and institutional obligations, and every identifiable participant in the media.

Tags linking a child to a project deserve the same privacy protection as a face. A neutral role ID is not an authenticated identity and cannot be used to grant publication rights.

## Information fragments and teacher answers

The same non-disclosure principle applies to hidden puzzle clues and answer keys: do not make them downloadable and then hide them visually. Exclude `teacher-only/` and individual evidence from student/public exports. A trusted Orgo/Ekole integration must authorize each actual recipient.

## Real-world supervision

Any physical handoff, visit to another class, furniture movement, workshop tool, food sharing or media capture needs real educator oversight and locally approved policies. The software must never pretend to monitor a child's real-world position or safety automatically.

Read [Orgo Integration](Orgo-Integration) and [Governance and Licensing](Governance-and-Licensing).
