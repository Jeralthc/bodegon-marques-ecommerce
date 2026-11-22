# 🥃 AUREUM • Haute Cave & Fine Spirits
> **Proyecto:** Análisis de Ingeniería Inversa a Licores Mundiales & Propuesta Arquitectónica Next-Gen con Mockup Web Interactivo y Design System para Figma.

[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)
[![Stack](https://img.shields.io/badge/Architecture-Composable%20%2F%20Headless-D4AF37.svg)](#)
[![Design](https://img.shields.io/badge/Design%20System-Obsidian%20%26%20Gold-0B0B0D.svg)](#)

---

## 📌 Contenido del Repositorio

1. **`index.html`**: **Mockup Web Interactivo de Alta Gama**, listo para abrir en cualquier navegador o desplegar en la web. Incluye:
   - Verificación de edad elegante (18+/21+).
   - Selector multimoneda interactivo (USD, Bs, EUR).
   - **Sommelier Virtual con IA** (asistente de maridaje interactivo).
   - Catálogo filtrable por categorías exclusivas (Single Malts, Rones Solera, Champagne Grand Cru, Agave Extra Añejo).
   - Fichas organolépticas detalladas con notas de **Nariz, Boca, Final y Maridaje**.
   - **Shopping Bag Drawer** con cálculo de entrega (Valet Express Caracas vs Retiro en Bóveda) y múltiples métodos de pago (Zelle, Pago Móvil, Stripe, Cripto).
2. **`docs/analisis-licoresmundiales.md`**: Investigación técnica profunda sobre el sitio actual `licoresmundiales.com` (stack Magento, PHP, MySQL, integración con ERP físico, modelo de negocio e historia desde 1973).
3. **`docs/propuesta-arquitectura-nextgen.md`**: Estudio de arquitectura para construir una plataforma que supere a la competencia: Headless Commerce (Next.js 15 + MedusaJS/Shopify Storefront + Meilisearch + Edge Caching + Conciliación automatizada multirail).
4. **`docs/figma-design-specs.md`**: Especificaciones exhaustivas para el equipo de diseño UI/UX en Figma (tokens, escalas, grillas, componentes).
5. **`figma-tokens.json`**: Archivo de Design Tokens listo para importar directamente en **Figma** usando el plugin *Tokens Studio*.

---

## 🚀 Cómo Visualizar el Mockup Web

### Opción 1: Abrir localmente
Simplemente abre el archivo `index.html` en tu navegador web preferido:
```bash
# En Linux/Ubuntu:
xdg-open index.html

# En macOS:
open index.html

# O ejecutando un servidor local ligero:
python3 -m http.server 8000
# Luego abrir: http://localhost:8000
```

### Opción 2: Importar en Figma
1. Abre Figma y crea un lienzo en blanco.
2. Utiliza el plugin **"html.to.design"** y apunta al archivo local o servidor web para obtener el diseño vectorial editable con Auto Layout.
3. Carga `figma-tokens.json` mediante el plugin **"Tokens Studio for Figma"** para tener las variables de color, tipografía y espaciado vinculadas.

---

## 🏛️ Comparación Arquitectónica Resumida

```
┌───────────────────────────────────────┬──────────────────────────────────────────┐
│      Licores Mundiales (Actual)       │          AUREUM (Propuesta Next-Gen)     │
├───────────────────────────────────────┼──────────────────────────────────────────┤
│ • Monolito Magento (PHP / MySQL)      │ • Headless Composable (Next.js 15 / Edge)│
│ • TTFB: 800ms - 1,800ms               │ • TTFB: < 65ms a nivel global            │
│ • Dependencia de Varnish para caché   │ • Edge Caching + Server Components       │
│ • Estética de catálogo genérico       │ • Look & Feel de Alta Cava / Lujo Obscuro│
│ • Búsqueda textual tradicional        │ • Sommelier AI Concierge + Meilisearch   │
│ • Reporte manual de pagos             │ • Conciliación automática de Zelle & P.M.│
└───────────────────────────────────────┴──────────────────────────────────────────┘
```

---

Desarrollado con estándares de ingeniería de software enterprise.
