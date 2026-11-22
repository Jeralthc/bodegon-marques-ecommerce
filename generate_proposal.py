import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = docx.Document()

# Page Margins (0.9 inch)
for section in doc.sections:
    section.top_margin = Inches(0.85)
    section.bottom_margin = Inches(0.85)
    section.left_margin = Inches(0.85)
    section.right_margin = Inches(0.85)

# Brand Color Palette
COLOR_GOLD = RGBColor(197, 160, 89)      # #C5A059 Imperial Gold
COLOR_DARK = RGBColor(18, 18, 23)        # #121217 Charcoal Dark
COLOR_MUTED = RGBColor(114, 114, 130)    # #727282 Muted Gray
COLOR_GREEN = RGBColor(30, 94, 65)       # #1E5E41 Habanos Green
COLOR_BLACK = RGBColor(25, 25, 28)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_callout(doc, text_list, title="NOTA ESTRATÉGICA", fill_hex="F9F7F1", border_color="C5A059"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_background(cell, fill_hex)
    set_cell_margins(cell, top=160, bottom=160, left=240, right=200)
    
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    cell._tc.get_or_add_tcPr().append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    r_tit = p.add_run(f"✦ {title}\n")
    r_tit.bold = True
    r_tit.font.name = "Georgia"
    r_tit.font.size = Pt(10)
    r_tit.font.color.rgb = COLOR_GOLD if border_color == "C5A059" else COLOR_GREEN

    for item in text_list:
        p_item = cell.add_paragraph()
        p_item.paragraph_format.space_before = Pt(2)
        p_item.paragraph_format.space_after = Pt(2)
        p_item.paragraph_format.line_spacing = 1.15
        r = p_item.add_run(item)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.color.rgb = COLOR_BLACK

# Header Banner Table
header_table = doc.add_table(rows=1, cols=1)
header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
header_table.autofit = False
h_cell = header_table.cell(0, 0)
h_cell.width = Inches(6.8)
set_cell_background(h_cell, "121217")
set_cell_margins(h_cell, top=260, bottom=260, left=260, right=260)

hp = h_cell.paragraphs[0]
hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
hp.paragraph_format.space_after = Pt(4)
r_tag = hp.add_run("PROPUESTA TÉCNICA Y COMERCIAL • DESARROLLO A MEDIDA\n")
r_tag.font.name = "Arial"
r_tag.font.size = Pt(9.5)
r_tag.font.bold = True
r_tag.font.color.rgb = COLOR_GOLD

r_title = hp.add_run("BODEGÓN MARQUÉS\n")
r_title.font.name = "Georgia"
r_title.font.size = Pt(24)
r_title.font.bold = True
r_title.font.color.rgb = RGBColor(255, 255, 255)

r_sub = hp.add_run("CASA DE LICORES • HABANOS POINT • DELICATESSEN\n")
r_sub.font.name = "Georgia"
r_sub.font.size = Pt(11)
r_sub.font.color.rgb = COLOR_GOLD

r_meta = hp.add_run("Plataforma E-Commerce Boutique & Sistema de Pedidos Inteligente\nC.C. Terracota, Planta Baja, Local 4 • Mérida, Venezuela")
r_meta.font.name = "Arial"
r_meta.font.size = Pt(9)
r_meta.font.color.rgb = RGBColor(180, 180, 195)

doc.add_paragraph().paragraph_format.space_after = Pt(8)

# Metadatos del Documento
meta_table = doc.add_table(rows=2, cols=2)
meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_table.autofit = False
meta_table.rows[0].cells[0].width = Inches(3.4)
meta_table.rows[0].cells[1].width = Inches(3.4)
meta_table.rows[1].cells[0].width = Inches(3.4)
meta_table.rows[1].cells[1].width = Inches(3.4)

meta_data = [
    ("Cliente:", "Bodegón Marqués (@bodegonmarques)"),
    ("Ubicación:", "C.C. Terracota, PB, Local 4, Av. Las Américas, Mérida"),
    ("Contacto Oficial:", "+58 412-2702505 (WhatsApp Concierge)"),
    ("Modalidad:", "Desarrollo Llave en Mano • Precio Único Cerrado")
]

for idx, (label, val) in enumerate(meta_data):
    r_idx = idx // 2
    c_idx = idx % 2
    cell = meta_table.cell(r_idx, c_idx)
    set_cell_background(cell, "F9F9FB")
    set_cell_margins(cell, 70, 70, 100, 100)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r1 = p.add_run(label + " ")
    r1.font.name = "Arial"
    r1.font.size = Pt(9)
    r1.bold = True
    r1.font.color.rgb = COLOR_MUTED
    r2 = p.add_run(val)
    r2.font.name = "Arial"
    r2.font.size = Pt(9)
    r2.bold = True
    r2.font.color.rgb = COLOR_BLACK

doc.add_paragraph().paragraph_format.space_after = Pt(10)

# 1. RESUMEN EJECUTIVO & DIAGNÓSTICO
h1 = doc.add_heading(level=1)
r_h1 = h1.add_run("1. Resumen Ejecutivo y Diagnóstico Comercial")
r_h1.font.name = "Georgia"
r_h1.font.size = Pt(14)
r_h1.font.color.rgb = COLOR_DARK
h1.paragraph_format.space_before = Pt(10)
h1.paragraph_format.space_after = Pt(4)

p_diag = doc.add_paragraph()
p_diag.paragraph_format.space_after = Pt(6)
p_diag.paragraph_format.line_spacing = 1.15
p_diag.add_run(
    "Bodegón Marqués goza de un posicionamiento de élite indiscutible en Mérida gracias a su impecable sede en el C.C. Terracota, "
    "su prestigiosa certificación como Punto Oficial Habanos Point (Kukenan Tobacco / Habanos S.A.) y su selecto portafolio de Rones D.O.C., "
    "whiskies de malta y delicatessen. Sin embargo, su operación de ventas digitales enfrenta actualmente una fricción crítica:"
)

diag_bullets = [
    ("Atención por WhatsApp Saturada y Manual: ", "Los clientes deben preguntar precio por precio, disponibilidad de cosechas y tasa del día. Si el personal de tienda está ocupado despachando en el mostrador del C.C. Terracota, el cliente digital espera y la venta de alto ticket se enfría."),
    ("Tasa de Cambio Volátil: ", "Manejar listas de precios en dólares que cambian a bolívares genera confusión si no hay un cotizador automático en vivo con la tasa oficial BCV."),
    ("Pérdida de Compras Nocturnas y de Fin de Semana: ", "Empresarios, turistas y amantes del buen licor desean ver el stock a las 11:00 PM o domingos, armar su pedido y tenerlo listo para Delivery o Pick-Up sin esperar que alguien conteste un mensaje."),
    ("El Valor Diferencial del Humidor: ", "Tener tabacos cubanos certificados (Cohiba, Montecristo, Partagás) es una ventaja monumental que debe lucirse con fichas de cata interactivas y accesorios de corte y encendido.")
]

for b_tit, b_desc in diag_bullets:
    p_b = doc.add_paragraph(style='List Bullet')
    p_b.paragraph_format.space_after = Pt(3)
    p_b.paragraph_format.line_spacing = 1.15
    r_bt = p_b.add_run(b_tit)
    r_bt.bold = True
    r_bt.font.name = "Arial"
    r_bt.font.size = Pt(9.5)
    r_bd = p_b.add_run(b_desc)
    r_bd.font.name = "Arial"
    r_bd.font.size = Pt(9.5)

add_callout(
    doc,
    [
        "El objetivo no es crear una web lenta o genérica que nadie use. El objetivo es entregarle a Bodegón Marqués una herramienta de venta rápida y elegante: un catálogo interactivo de lujo que atienda 24/7, calcule precios al instante y envíe comandas perfectas y listas para cobrar directo al WhatsApp de la tienda."
    ],
    title="LA OPORTUNIDAD DE CIERRE",
    fill_hex="FAF6ED",
    border_color="C5A059"
)

doc.add_paragraph().paragraph_format.space_after = Pt(6)

# 2. ALCANCE DE LA SOLUCIÓN
h2 = doc.add_heading(level=1)
r_h2 = h2.add_run("2. Alcance del Desarrollo (Solución Integral Llave en Mano)")
r_h2.font.name = "Georgia"
r_h2.font.size = Pt(14)
r_h2.font.color.rgb = COLOR_DARK
h2.paragraph_format.space_before = Pt(12)
h2.paragraph_format.space_after = Pt(4)

modules = [
    ("Módulo 1: Tienda Web Boutique PWA Ultra Rápida", [
        "Diseño a medida 'Dark Luxury' con identidad de Bodegón Marqués (Dorado Imperial, fondo carbón obsidiana y corona heráldica).",
        "Funciona en teléfonos (Android y iPhone) como si fuera una aplicación nativa, además de tablets y computadoras.",
        "Carga instantánea en menos de 0.8 segundos, incluso bajo conexiones lentas de Mérida o datos móviles."
    ]),
    ("Módulo 2: Las 3 Secciones Estratégicas del Bodegón", [
        "Rones D.O.C. & Whiskies de Malta: Catálogo de licores premium con notas de cata, grados alcohólicos y maridajes.",
        "Humidor & Habanos Certificados: Sección exclusiva Habanos Point con vitolas cubanas legítimas, calibres, cepos y accesorios de corte y fuego.",
        "Delicatessen & Snacks Gourmet: Crocanti mix, jamón ibérico, quesos madurados y chocolates bean-to-bar listos para armonizar."
    ]),
    ("Módulo 3: Cotizador Multimoneda Automático (USD / VES / EUR)", [
        "El cliente visualiza los precios en Dólares ($), Bolívares (Bs. a tasa oficial BCV) o Euros (€) con un solo clic.",
        "Evita discrepancias de cobro y simplifica la contabilidad de la tienda."
    ]),
    ("Módulo 4: Carrito Inteligente con Despacho y WhatsApp Directo", [
        "El cliente selecciona si desea Delivery Express en la ciudad de Mérida o Retiro Pick-Up en C.C. Terracota (PB, Local 4).",
        "Al presionar 'Finalizar Pedido', se genera un mensaje de WhatsApp formateado con la lista de productos, total y datos del cliente enviado directo al 0412-270.25.05."
    ]),
    ("Módulo 5: Asesor Virtual 'Sommelier Marqués'", [
        "Asistente interactivo integrado en la web que guía al cliente recomendando qué ron o whisky regalar según presupuesto, o qué puro encender según la ocasión."
    ]),
    ("Módulo 6: Panel de Administración Sencillo e Intuitivo", [
        "Panel privado donde el encargado de Bodegón Marqués puede subir productos nuevos, cambiar precios y pausar existencias desde su teléfono en 30 segundos, sin depender de programadores."
    ])
]

for mod_title, mod_items in modules:
    p_mt = doc.add_paragraph()
    p_mt.paragraph_format.space_before = Pt(6)
    p_mt.paragraph_format.space_after = Pt(2)
    r_mtt = p_mt.add_run(mod_title)
    r_mtt.font.name = "Georgia"
    r_mtt.font.size = Pt(11)
    r_mtt.bold = True
    r_mtt.font.color.rgb = COLOR_DARK

    for item in mod_items:
        p_mi = doc.add_paragraph(style='List Bullet')
        p_mi.paragraph_format.space_after = Pt(2)
        p_mi.paragraph_format.line_spacing = 1.15
        r_txt = p_mi.add_run(item)
        r_txt.font.name = "Arial"
        r_txt.font.size = Pt(9.2)

doc.add_paragraph().paragraph_format.space_after = Pt(8)

# 3. PROPUESTA ECONÓMICA REALISTA (UN SOLO PRECIO CERRADO)
h3 = doc.add_heading(level=1)
r_h3 = h3.add_run("3. Propuesta Económica Realista (Inversión Única Cerrada)")
r_h3.font.name = "Georgia"
r_h3.font.size = Pt(14)
r_h3.font.color.rgb = COLOR_DARK
h3.paragraph_format.space_before = Pt(12)
h3.paragraph_format.space_after = Pt(4)

p_econ = doc.add_paragraph()
p_econ.paragraph_format.space_after = Pt(6)
p_econ.paragraph_format.line_spacing = 1.15
p_econ.add_run(
    "Entendiendo la dinámica comercial de Mérida y la conveniencia de una inversión accesible, transparente y de rápida amortización, "
    "hemos descartado tarifas infladas de agencias de la capital ($850 - $1,500 USD). Presentamos un "
)
r_res = p_econ.add_run("ÚNICO PRECIO INTEGRAL Y CERRADO")
r_res.bold = True
r_res.font.color.rgb = COLOR_DARK
p_econ.add_run(" con todo incluido, diseñado para que la decisión sea inmediata y rentable desde el primer mes.")

# Single Price Showcase Box
price_table = doc.add_table(rows=1, cols=1)
price_table.alignment = WD_TABLE_ALIGNMENT.CENTER
price_table.autofit = False
pr_cell = price_table.cell(0, 0)
pr_cell.width = Inches(6.8)
set_cell_background(pr_cell, "121217")
set_cell_margins(pr_cell, top=200, bottom=200, left=240, right=240)

borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="C5A059"/><w:top w:val="single" w:sz="24" w:space="0" w:color="C5A059"/><w:right w:val="single" w:sz="24" w:space="0" w:color="C5A059"/><w:bottom w:val="single" w:sz="24" w:space="0" w:color="C5A059"/></w:tcBorders>')
pr_cell._tc.get_or_add_tcPr().append(borders)

pr_p = pr_cell.paragraphs[0]
pr_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
pr_p.paragraph_format.space_after = Pt(2)

r_badge = pr_p.add_run("★ PAQUETE COMPLETO BODEGÓN MARQUÉS • LLAVE EN MANO\n")
r_badge.font.name = "Arial"
r_badge.font.size = Pt(10)
r_badge.font.bold = True
r_badge.font.color.rgb = COLOR_GOLD

r_big_price = pr_p.add_run("$450 USD\n")
r_big_price.font.name = "Georgia"
r_big_price.font.size = Pt(32)
r_big_price.font.bold = True
r_big_price.font.color.rgb = COLOR_GOLD

r_sub_price = pr_p.add_run("INVERSIÓN TOTAL ÚNICA • SIN LETRA PEQUEÑA\n")
r_sub_price.font.name = "Arial"
r_sub_price.font.size = Pt(9.5)
r_sub_price.font.bold = True
r_sub_price.font.color.rgb = RGBColor(255, 255, 255)

r_facil = pr_p.add_run("Facilidad de Pago en 2 Partes Iguales: 50% ($225) al arrancar + 50% ($225) contra entrega formal\nTiempo de entrega: 2 a 3 semanas (15 días laborables)")
r_facil.font.name = "Arial"
r_facil.font.size = Pt(9)
r_facil.font.color.rgb = RGBColor(190, 190, 205)

doc.add_paragraph().paragraph_format.space_after = Pt(8)

# Qué incluye la inversión
h_inc = doc.add_paragraph()
h_inc.paragraph_format.space_before = Pt(6)
h_inc.paragraph_format.space_after = Pt(2)
r_hinc = h_inc.add_run("¿Qué incluye exactamente esta inversión de $450 USD?")
r_hinc.font.name = "Georgia"
r_hinc.font.size = Pt(11)
r_hinc.bold = True
r_hinc.font.color.rgb = COLOR_DARK

inc_items = [
    "Diseño y desarrollo completo de la plataforma web e-commerce boutique con branding de Bodegón Marqués.",
    "Las 3 páginas especializadas: Rones & Whiskies de Malta, Humidor Habanos Point y Delicatessen Gourmet.",
    "Módulo Sommelier Marqués interactivo para recomendación y maridaje.",
    "Cotizador multimoneda automático (Dólares, Bolívares BCV y Euros).",
    "Integración directa de pedidos a WhatsApp Business con la comanda lista para facturar y despachar.",
    "Soporte para métodos de pago venezolanos: Pago Móvil C2P, Zelle, Transferencias y Efectivo.",
    "Panel de administración autogestionable para actualizar inventario y precios desde el celular.",
    "Carga inicial de hasta 100 productos de alta rotación con imágenes optimizadas y fichas de cata.",
    "Configuración del dominio, certificado de seguridad SSL y despliegue en la nube.",
    "Capacitación presencial o virtual al personal de C.C. Terracota (1 hora práctica).",
    "30 días continuos de garantía técnica post-lanzamiento sin ningún costo adicional."
]

for inc in inc_items:
    p_inc = doc.add_paragraph(style='List Bullet')
    p_inc.paragraph_format.space_after = Pt(2)
    p_inc.paragraph_format.line_spacing = 1.15
    r_it = p_inc.add_run(inc)
    r_it.font.name = "Arial"
    r_it.font.size = Pt(9)

doc.add_paragraph().paragraph_format.space_after = Pt(8)

# 4. MANTENIMIENTO & COSTO MENSUAL
h4 = doc.add_heading(level=1)
r_h4 = h4.add_run("4. Costo Operativo Mensual (Mínimo y Transparente)")
r_h4.font.name = "Georgia"
r_h4.font.size = Pt(14)
r_h4.font.color.rgb = COLOR_DARK
h4.paragraph_format.space_before = Pt(12)
h4.paragraph_format.space_after = Pt(4)

p_mant = doc.add_paragraph()
p_mant.paragraph_format.space_after = Pt(6)
p_mant.paragraph_format.line_spacing = 1.15
p_mant.add_run(
    "A diferencia de plataformas antiguas (Magento, WooCommerce en hosting compartido) que exigen $80 a $150 mensuales en servidores pesados, "
    "nuestra arquitectura moderna en la nube permite un costo de operación mínimo de apenas: "
)
r_cost = p_mant.add_run("$15 USD al mes")
r_cost.bold = True
r_cost.font.color.rgb = COLOR_GREEN
p_mant.add_run(". Este monto cubre:")

mant_items = [
    "Servidores Edge de máxima velocidad en la nube con 99.9% de operatividad ininterrumpida.",
    "Base de datos de productos segura con respaldos automáticos semanales.",
    "Certificado de seguridad SSL (HTTPS) renovado automáticamente.",
    "Soporte técnico preferencial para resolver cualquier inquietud operativa de la tienda."
]
for item in mant_items:
    p_mi = doc.add_paragraph(style='List Bullet')
    p_mi.paragraph_format.space_after = Pt(2)
    p_mi.paragraph_format.line_spacing = 1.15
    r_mi = p_mi.add_run(item)
    r_mi.font.name = "Arial"
    r_mi.font.size = Pt(9)

doc.add_paragraph().paragraph_format.space_after = Pt(8)

# 5. RETORNO DE INVERSIÓN (ROI)
h5 = doc.add_heading(level=1)
r_h5 = h5.add_run("5. Análisis de Rentabilidad y Retorno de Inversión (ROI)")
r_h5.font.name = "Georgia"
r_h5.font.size = Pt(14)
r_h5.font.color.rgb = COLOR_DARK
h5.paragraph_format.space_before = Pt(12)
h5.paragraph_format.space_after = Pt(4)

add_callout(
    doc,
    [
        "¿Cómo se paga sola esta plataforma en Mérida?",
        "• Un solo pedido de un whisky premium (ej. The Macallan $98) o un ron de solera con delicatessen y un puro Partagás D4 ($150) genera un margen comercial significativo.",
        "• Con solo captar 4 a 6 compras al mes que antes se perdían por no tener catálogo online ni respuesta nocturna inmediata, la plataforma se paga sola en los primeros 45 a 60 días.",
        "• Además, el personal de C.C. Terracota ahorra entre 15 y 20 horas mensuales al no tener que enviar fotos y precios manualmente por chat."
    ],
    title="RENTABILIDAD GARANTIZADA",
    fill_hex="FAF6ED",
    border_color="C5A059"
)

doc.add_paragraph().paragraph_format.space_after = Pt(8)

# 6. CÓMO ARRANCAR
h6 = doc.add_heading(level=1)
r_h6 = h6.add_run("6. Pasos para Iniciar de Inmediato")
r_h6.font.name = "Georgia"
r_h6.font.size = Pt(14)
r_h6.font.color.rgb = COLOR_DARK
h6.paragraph_format.space_before = Pt(12)
h6.paragraph_format.space_after = Pt(4)

add_callout(
    doc,
    [
        "Para comenzar el desarrollo hoy mismo, el procedimiento es directo y sin burocracia:",
        "1. Aprobación de la propuesta y pago del 50% de anticipo ($225 USD vía Zelle, Efectivo o Pago Móvil).",
        "2. Envío del listado inicial de productos o inventario para comenzar la carga y personalización final.",
        "3. En 10 días se presenta la versión funcional privada para pruebas conjuntas.",
        "4. En el día 15 se conecta el dominio oficial, se capacita al equipo y se liquida el 50% restante ($225 USD)."
    ],
    title="PRÓXIMOS PASOS DE ARRANQUE",
    fill_hex="F2F8F5",
    border_color="1E5E41"
)

# Output paths
docx_path = "/home/jeralthc/Proyectos/bodegon-marques-ecommerce/Propuesta_Comercial_Bodegon_Marques.docx"
doc.save(docx_path)
print(f"Propuesta comercial actualizada con éxito en: {docx_path}")
