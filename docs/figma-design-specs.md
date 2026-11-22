# 🎨 Figma Design System Specifications
## AUREUM • Haute Cave & Fine Spirits

Esta guía técnica permite a diseñadores UI/UX y desarrolladores frontend replicar o importar el sistema visual exacto de **AUREUM** en Figma y sincronizarlo con el código fuente.

---

## 1. Fundamentos del Sistema de Diseño

El concepto visual se denomina **"Obsidian & Liquid Gold"**: una atmósfera inmersiva de cava privada con acentos metálicos reflectantes, microinteracciones sutiles y tipografía con jerarquía editorial de alta gama.

---

## 2. Paleta de Colores (Color Tokens)

### Colores Primarios & Fondos
- **Obsidian Deep (Fondo principal):** `#0B0B0D`
- **Charcoal Surface (Superficies de tarjetas):** `#141418`
- **Charcoal Elevated (Modales y dropdowns):** `#1B1B22`
- **Border Subtle (Bordes de cristal templado):** `rgba(255, 255, 255, 0.08)`
- **Border Gold Highlight:** `rgba(212, 175, 55, 0.35)`

### Metálicos y Acentos de Oro
- **Liquid Gold (Primario):** `#D4AF37`
- **Champagne Light (Highlights y textos dorados):** `#EED9A4`
- **Antique Bronze (Hover y estados activos):** `#997D29`
- **Amber Glow (Sombras de resplandor):** `rgba(212, 175, 55, 0.15)`

### Textos y Contraste
- **Text Highest (Títulos y llamadas a la acción):** `#FBFBFC`
- **Text Medium (Cuerpo y notas de cata):** `#A3A3B2`
- **Text Muted (Metadatos y leyendas):** `#6B6B7B`

### Estados Semánticos
- **Crimson Velvet (Edición limitada / Agotado):** `#8B1E2F`
- **Emerald Reserve (En stock / Verificado):** `#1E6B4A`

---

## 3. Sistema Tipográfico

### Display / Títulos de Lujo
- **Familia Primaria:** *Cormorant Garamond* (o *Playfair Display*)
- **Pesos:** Light (300), Regular (400), SemiBold (600)
- **Escala:**
  - Hero Display: `56px` / Line-height `1.1` / Letter-spacing `-0.02em`
  - H1 Categoría: `40px` / Line-height `1.2`
  - H2 Subtítulo de Sección: `28px` / Line-height `1.3`
  - H3 Título de Producto: `20px` / Line-height `1.35` / Italic disponible para añadas

### Interfaz / Lectura / Botones
- **Familia:** *Plus Jakarta Sans* (o *Inter*)
- **Pesos:** Regular (400), Medium (500), SemiBold (600)
- **Escala:**
  - Body Large: `16px` / Line-height `1.6`
  - Body Regular: `14px` / Line-height `1.5`
  - Caption / Badges: `11px` / Uppercase / Letter-spacing `0.08em`

---

## 4. Grilla y Distribución Espacial

- **Contenedor Máximo:** `1320px` centrado con padding lateral de `24px` en desktop y `16px` en móvil.
- **Grilla de Columnas:** 12 columnas en Desktop (`gap: 24px`), 6 columnas en Tablet (`gap: 16px`), 4 columnas en Mobile (`gap: 12px`).
- **Ritmo Vertical:** Múltiplos estrictos de **8px** (8, 16, 24, 32, 48, 64, 96, 128px).

---

## 5. Componentes Clave en Figma

### 1. Luxury Product Card (Tarjeta de Producto)
- Contenedor con borde glassmorphic (`backdrop-filter: blur(20px)`).
- Relación de aspecto de imagen `3:4` con iluminación focal sobre fondo oscuro.
- Badges superiores flotantes: *"Rare Cask"*, *"Edición Limitada"*, *"D.O.C. Venezuela"*.
- Píldoras de notas organolépticas (e.g. *Roble Tostado*, *Cacao 70%*, *Vainilla de Madagascar*).
- Botón de compra rápida con microinteracción de deslizamiento dorado.

### 2. Sommelier AI Concierge
- Modal centrado o drawer inferior en móvil con animación de pulso áureo.
- Selectores por tarjetas interactivas de ocasiones (Cena Romántica, Brindis de Negocios, Regalo de Colección).
- Barra de presupuesto interactiva con actualización en tiempo real de recomendaciones.

### 3. Tasting Radar & Sensory Breakdown
- Desglose de 4 cuadrantes sensoriales: **Nariz (Aromas)**, **Boca (Textura y Ataque)**, **Final (Persistencia)**, **Maridaje Recomendado**.

---

## 6. Instrucciones para Importar a Figma

1. **Tokens Studio for Figma (Plugin):**
   - Abrir el plugin en Figma.
   - Seleccionar **Tools > Load from file** y cargar el archivo `figma-tokens.json` ubicado en este repositorio.
   - Automáticamente se crearán los estilos de color, tipografía y sombras en tu archivo de Figma.

2. **Importación Directa desde Código:**
   - Puedes abrir `index.html` en el navegador y utilizar plugins como **"html.to.design"** en Figma para capturar y convertir el mockup web interactivo en frames vectoriales con Auto Layout 100% nativo.
