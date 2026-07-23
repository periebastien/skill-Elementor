# `counter` — Compteur (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_counter : `starting_number`:nb[=0], `ending_number`:nb[=100], `prefix`:txt, `suffix`:txt, `duration`:nb[=2000], `thousand_separator`:'yes'[=yes], `thousand_separator_char`(|.| |_|'), `title`:txt[=Numéro cool], `title_tag`(h1|h2|h3|h4|h5|h6|div|span|p)[=div]

## onglet style
- section_counter_style : `title_position`(before|after|start|end), `title_horizontal_alignment`(start|center|end), `title_vertical_alignment`(start|center|end), `title_gap`:slider{unit,size}, `number_position`(start|center|end|stretch), `number_alignment`(start|center|end), `number_gap`:slider{unit,size}
- section_number : `typography_number_typography`+GROUPE typo, `number_stroke_text_stroke_type`+GROUPE text_stroke, `number_color`:color, `number_shadow_text_shadow_type`, `number_shadow_text_shadow`:text_shadow
- section_title : `typography_title_typography`+GROUPE typo, `title_stroke_text_stroke_type`+GROUPE text_stroke, `title_color`:color, `title_shadow_text_shadow_type`, `title_shadow_text_shadow`:text_shadow
