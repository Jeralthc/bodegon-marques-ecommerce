# 🎨 Manual de Marca y Design System Figma • Bodegón Marqués
## "Marqués Casa de Licores • Habanos & Delicatessen" • Instagram: @bodegonmarques

Este manual establece la identidad visual oficial, los tokens cromáticos y las pautas de accesibilidad tipográfica para el equipo de UI/UX en Figma de **Bodegón Marqués** (C.C. Terracota, Mérida):

---

## 1. Fundamentos y Arquetipo de Marca

- **Nombre Comercial:** **Bodegón Marqués** (Marqués Casa de Licores).
- **Heráldica:** Inspirado en la nobleza y la distinción que confiere el título de "Marqués", representado con una **corona nobiliaria de 4 florones heráldica**.
- **Canal Oficial de Redes:** **[@bodegonmarques](https://www.instagram.com/bodegonmarques)**.
- **Sede Física Real:** **Centro Comercial Terracota, Planta Baja, Local 4, Av. Las Américas (cruce con Av. Urdaneta), Mérida, Estado Mérida**.
- **Atención Directa WhatsApp:** **+58 412-2702505**.
- **Distintivo Oficial:** Punto de venta autorizado **Habanos Point** (puros cubanos certificados por Kukenan Tobacco / Habanos S.A.).

---

## 2. Paleta Cromática Institucional & Accesibilidad (WCAG AAA)

| Token | Código HEX | RGB | HSL | Ratio de Contraste | Uso y Aplicación en el Diseño |
|---|---|---|---|---|---|
| **Blanco Puro** | `#FFFFFF` | `rgb(255, 255, 255)` | `hsl(0, 0%, 100%)` | **18.5:1 (AAA)** | Tipografía principal, títulos H1/H2/H3/H4, precios y logo de máxima legibilidad. |
| **Rosa Arena Claro** | `#F5EBE8` | `rgb(245, 235, 232)` | `hsl(12, 42%, 94%)` | **14.2:1 (AAA)** | Cuerpo de texto, descripciones, notas de cata y enlaces de acción para lectura sin fatiga. |
| **Rosa Arena** | `#D8ABA2` | `rgb(216, 171, 162)` | `hsl(10, 41%, 74%)` | **8.5:1 (AA)** | Acentos de marca, etiquetas secundarias, micro-bordes y detalles gráficos. |
| **Vinotinto Claro** | `#831226` | `rgb(131, 18, 38)` | `hsl(349, 76%, 29%)` | - | Botones primarios, llamadas a la acción (CTA) y acentos vivos. |
| **Vinotinto Base** | `#66091C` | `rgb(102, 9, 28)` | `hsl(348, 84%, 22%)` | - | Tono medio dominante y corazón de la identidad corporativa. |
| **Vinotinto Profundo** | `#510215` | `rgb(81, 2, 21)` | `hsl(346, 95%, 16%)` | - | Sombras, degradados profundos y atmósfera nocturna de cava. |
| **Negro Cálido Cava** | `#0D0306` | `rgb(13, 3, 6)` | `hsl(342, 62%, 3%)` | - | Fondo base que sustituye al negro frío anterior, aportando calidez y confort visual. |
| **Superficie Cálida** | `#1A070E` | `rgb(26, 7, 14)` | - | - | Superficie para tarjetas de catálogo (`glass-marques`), modales y cajón de compras. |

---

## 3. Escala y Reglas Tipográficas para Máxima Claridad

- **Títulos y Display:** *Cormorant Garamond* (romana de serif refinado, con peso `font-bold` para trazos nítidos).
- **Lectura e Interfaz:** *Plus Jakarta Sans* (claridad en listas de precios en bolívares/dólares, notas organolépticas y checkout).
- **Regla de Legibilidad Mínima:** 
  - Ningún texto informativo es menor a `12px` (`text-xs`).
  - Textos de lectura general y notas de cata se configuran en `14px` (`text-sm`) con `leading-relaxed` (1.6) y peso normal/medio (nunca `font-light`).
  - Títulos de tarjeta en `text-xl` (`20px`) en Blanco Puro `#FFFFFF`.

---

## 4. Cómo Importar y Diseñar en Figma

1. **Importación con Plugin "html.to.design":**
   - En Figma, crea un lienzo nuevo.
   - Ejecuta el plugin **html.to.design**.
   - Coloca la URL pública:
     ```
     https://jeralthc.github.io/bodegon-marques-ecommerce/
     ```
   - Obtendrás todos los frames, componentes vectoriales y Auto Layout listos para Desktop y Mobile con la tipografía de alto contraste.
2. **Carga de Tokens en Figma:**
   - Carga el archivo [`figma-tokens.json`](file:///home/jeralthc/Proyectos/bodegon-marques-ecommerce/figma-tokens.json) mediante el plugin **Tokens Studio for Figma** para tener los estilos de color y tipografía vinculados.
