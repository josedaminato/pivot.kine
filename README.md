# PIVOT Kinesiología — Sitio web

Landing estática (HTML + CSS + JS) para el centro de kinesiología PIVOT (San Juan, Argentina).

## Ver el sitio en vivo (cliente)

1. En GitHub: **Settings** → **Pages** (menú izquierdo).
2. En **Build and deployment** → **Source**: elegí **GitHub Actions** (no “Deploy from a branch”).
3. Volvé al repo → pestaña **Actions**: el workflow “Desplegar sitio en GitHub Pages” debería ejecutarse solo al pushear a `main`.
4. Cuando termine (ícono verde), el sitio queda en:

   **https://josedaminato.github.io/pivot.kine/**

   (Si no carga a la primera, esperá 1–2 minutos y recargá.)

## Desarrollo local

Abrí `index.html` en el navegador o usá un servidor estático, por ejemplo:

```bash
npx --yes serve -p 3000
```

Luego entrá a `http://localhost:3000`.
