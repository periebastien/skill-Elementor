# `text-editor` — Éditeur de texte (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_editor : `editor`:html, `drop_cap`:'yes', `text_columns`(|1|2|3|4|5|6|7|8|9|…), `column_gap`:slider{unit,size}

## onglet style
- section_style : `typography_typography`+GROUPE typo, `align`(start|center|end|justify), `text_shadow_text_shadow_type`, `text_shadow_text_shadow`:text_shadow, `paragraph_spacing`:slider{unit,size}, `link_colors`, `text_color`:color, `link_color`:color, `link_hover_color`:color, `link_hover_color_transition_duration`:slider{unit,size}
- section_drop_cap : `drop_cap_typography_typography`+GROUPE typo, `drop_cap_view`(default|stacked|framed)[=default], `drop_cap_primary_color`:color, `drop_cap_secondary_color`:color, `drop_cap_shadow_text_shadow_type`, `drop_cap_shadow_text_shadow`:text_shadow, `drop_cap_size`:slider{unit,size}, `drop_cap_space`:slider{unit,size}, `drop_cap_border_radius`:slider{unit,size}, `drop_cap_border_width`:dim{t,r,b,l,unit,isLinked}
