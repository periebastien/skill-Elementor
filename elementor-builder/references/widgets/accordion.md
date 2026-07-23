# `accordion` — Accordéon (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_title : `tabs`:repeater[], `selected_icon`:icons{value,library}, `selected_active_icon`:icons{value,library}, `title_html_tag`(h1|h2|h3|h4|h5|h6|div)[=div], `faq_schema`:'yes'

## onglet style
- section_title_style : `border_width`:slider{unit,size}, `border_color`:color
- section_toggle_style_title : `title_typography_typography`+GROUPE typo, `text_stroke_text_stroke_type`+GROUPE text_stroke, `title_background`:color, `title_color`:color, `tab_active_color`:color, `title_shadow_text_shadow_type`, `title_shadow_text_shadow`:text_shadow, `title_padding`:dim{t,r,b,l,unit,isLinked}
- section_toggle_style_icon : `icon_align`(left|right)[=left], `icon_color`:color, `icon_active_color`:color, `icon_space`:slider{unit,size}
- section_toggle_style_content : `content_typography_typography`+GROUPE typo, `content_background_color`:color, `content_color`:color, `content_shadow_text_shadow_type`, `content_shadow_text_shadow`:text_shadow, `content_padding`:dim{t,r,b,l,unit,isLinked}
