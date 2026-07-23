# `star-rating` — Évaluation par étoiles (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_rating : `rating_scale`(5|10)[=5], `rating`:nb[=5], `star_style`(star_fontawesome|star_unicode)[=star_fontawesome], `unmarked_star_style`(solid|outline)[=solid], `title`:txt, `align`(start|center|end|justify)

## onglet style
- section_title_style : `title_typography_typography`+GROUPE typo, `title_color`:color, `title_shadow_text_shadow_type`, `title_shadow_text_shadow`:text_shadow, `title_gap`:slider{unit,size}
- section_stars_style : `icon_size`:slider{unit,size}, `icon_space`:slider{unit,size}, `stars_color`:color, `stars_unmarked_color`:color
