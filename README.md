# Ascension Technologies Landing Page

Growth-ready Astro site for the Ascension Technologies developer recruitment campaign. The site is inspired by atdao.org, keeps the approved copy intact, and introduces a polished hero experience, product pillars, value sections, and contribution calls-to-action.

## Local development

```bash
npm install
npm run dev
```

The dev server runs at http://localhost:4321 with hot reload.

## Production build

```bash
npm run build
npm run preview # optional sanity check of the dist/ folder
```

## Deployment via GitHub Pages

A workflow at `.github/workflows/deploy.yml` builds the site on every push to `main` and publishes the `dist/` output to GitHub Pages. To finish wiring it up:

1. Push this project to a GitHub repository (e.g., `neoandromeda/ascension-site`).
2. In the repo settings:
   - Enable GitHub Pages with the "GitHub Actions" deployment source.
   - Make sure Pages has permission to deploy (the workflow already requests `pages: write`).
3. Adjust `astro.config.mjs` with the final `site` (and `base` if deploying under a subpath) once the GitHub Pages URL is known.

The workflow can also be triggered manually from the Actions tab (`workflow_dispatch`).

## Project layout

```
web/ascension-site
├── public          # static assets (logo, favicons)
├── src
│   ├── layouts     # Global layout + typography
│   └── pages       # Landing page content & styles
├── package.json    # npm scripts + deps
├── astro.config.mjs
└── .github/workflows/deploy.yml
```

## Next steps

- Update `astro.config.mjs` once the production URL is final.
- Add additional pages or sections as the AT V2 content expands.
- Drop in analytics, forms, or CMS integration when required.
- When you're ready for a custom domain, point DNS to GitHub Pages and update the `site` config accordingly.
