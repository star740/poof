# POOF Junk Removal & Cleanouts

Static site published with GitHub Pages: https://star740.github.io/poof/

## Editing

`generate.py` is the source of truth. **Do not edit the .html files directly.**
They are overwritten on every build.

```bash
python3 generate.py      # writes index.html + estimate.html
git add -A && git commit -m "..." && git push origin main
```

- `generate.py`: shared shell (head/nav/footer) plus each page body
- `style.css`  : all brand tokens live in `:root`
- `app.js`     : scroll reveal + estimate form handling
- `assets/`    : images, logo, favicons

## Outstanding

Contact details are LIVE and real: (571) 490-2098 and poof.help@gmail.com.
Do not replace these with placeholders.

- Logo file: nav/footer wordmark is CSS-rendered placeholder
- Estimator backend (Cloudflare Worker holding the API key): form is inert
- Pricing inputs: truck rental, dump fees per ton, minimum charge
