# Publishing the English GitHub Wiki

All pages in the repository's `wiki/` folder are **English Markdown source files** arranged for a GitHub Wiki. GitHub does **not** automatically show a `wiki/` directory as the repository's separate Wiki product.

## Contents

- `Home.md` — default GitHub Wiki landing page.
- `_Sidebar.md` — navigation links using GitHub Wiki page slugs.
- `_Footer.md` — project status reminder.
- Individual `*.md` pages such as `Architecture.md`, `Quebec-Grade-3.md` and `Orgo-Integration.md`.

All Wiki links assume these files are at the **root of a GitHub Wiki repository**, not within a nested directory.

## Option A — separate GitHub Wiki repository

1. Create your GitHub repository for Kontexte (after resolving the rights and visibility policy).
2. Enable the Wiki in repository settings, if available for your account/repository settings.
3. Initialize the Wiki from GitHub's interface if needed, so its `.wiki.git` remote exists.
4. Clone the actual Wiki remote for your organization and repository, e.g.:

   ```bash
   git clone https://github.com/OWNER/REPOSITORY.wiki.git kontexte-github-wiki
   ```

5. Copy the **contents** of `Kontexte/wiki/` to the root of that clone (not the folder itself).
6. Review links and confidential contents, then commit and push:

   ```bash
   cd kontexte-github-wiki
   git add .
   git commit -m "Add English Kontexte Wiki"
   git push
   ```

`OWNER/REPOSITORY` is an example placeholder: replace it with the real repository name. Publishing is a deliberate user action; these instructions do not connect or push to GitHub.

## Option B — keep documentation only in the source repository

You can leave `wiki/` as ordinary Markdown and link to `wiki/Home.md` from the root README. It is browsable as source content but is not automatically the GitHub Wiki UI.

## Update policy

When code and documentation diverge, **label planned versus implemented capabilities explicitly**. Keep scenario and curriculum versions visible, and never publish `teacher-only/`, private student data, keys, or real-child media along with the Wiki. Maintain the upstream French technical documents in `docs/` as provenance unless their owners approve changes.
