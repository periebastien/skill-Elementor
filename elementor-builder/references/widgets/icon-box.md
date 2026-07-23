# `icon-box` — Boîte d’icône (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_icon : `selected_icon`:icons{value,library}, `view`(default|stacked|framed)[=default], `shape`(square|rounded|circle)[=circle], `title_text`:txt, `description_text`:txt, `link`:url{url,is_external}, `title_size`(h1|h2|h3|h4|h5|h6|div|span|p)[=h3]

## onglet style
- section_style_box : `position`(inline-start|inline-end|block-start|block-end)[=block-start], `content_vertical_alignment`(top|middle|bottom)[=top], `text_align`(start|center|end|justify), `icon_space`:slider{unit,size}, `title_bottom_space`:slider{unit,size}
- section_style_icon : `icon_colors`, `primary_color`:color, `secondary_color`:color, `hover_primary_color`:color, `hover_secondary_color`:color, `hover_icon_colors_transition_duration`:slider{unit,size}, `hover_animation`, `icon_size`:slider{unit,size}, `icon_padding`:slider{unit,size}, `rotate`:slider{unit,size}, `border_width`:dim{t,r,b,l,unit,isLinked}, `border_radius`:dim{t,r,b,l,unit,isLinked}
- section_style_content : `title_typography_typography`+GROUPE typo, `text_stroke_text_stroke_type`+GROUPE text_stroke, `description_typography_typography`+GROUPE typo, `title_shadow_text_shadow_type`, `title_shadow_text_shadow`:text_shadow, `icon_box_title_colors`, `title_color`:color, `hover_title_color`:color, `hover_title_color_transition_duration`:slider{unit,size}, `description_shadow_text_shadow_type`, `description_shadow_text_shadow`:text_shadow, `description_color`:color
