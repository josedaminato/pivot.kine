# PIVOT Kinesiología — Sitio web

Landing estática (HTML + CSS + JS) para el centro de kinesiología PIVOT (San Juan, Argentina).

## URL pública (para el cliente)

Tiene que ser **exactamente** esta (con el nombre del repo y la barra final):

### https://josedaminato.github.io/pivot.kine/

**Ojo:** si abrís solo `https://josedaminato.github.io/` (sin `/pivot.kine/`) GitHub muestra **404** porque ahí no hay sitio: el proyecto vive **dentro** de la carpeta del repositorio.

---

## Publicar en GitHub Pages (elegí una opción)

### Opción A — Desde la rama `main` (la más simple)

1. Repo → **Settings** → **Pages**.
2. **Build and deployment** → **Source**: **Deploy from a branch**.
3. Branch: **main**, carpeta: **/ (root)** → **Save**.
4. Esperá 1–3 minutos y probá de nuevo la URL de arriba.

### Opción B — GitHub Actions

1. **Settings** → **Pages** → **Source**: **GitHub Actions**.
2. Hacé push a `main` o ejecutá el workflow a mano en **Actions**.

No actives las dos a la vez si te da error: usá **solo** rama **o** solo **Actions**.

---

## Si sigue en 404

- Revisá **Settings** → **Pages** y fijate que diga que el sitio está publicado (URL verde).
- Probá en ventana de incógnito o borrá caché.
- Esperá unos minutos después del primer deploy.

## Desarrollo local

Abrí `index.html` en el navegador o:

```bash
npx --yes serve -p 3000
```

Luego `http://localhost:3000`.
