# `nested-accordion` — Accordéon (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_items : `items`, `accordion_item_title_position_horizontal`(start|center|end|stretch), `accordion_item_title_icon_position`(start|end), `accordion_item_title_icon`:icons{value,library}, `accordion_item_title_icon_active`:icons{value,library}, `title_tag`(h1|h2|h3|h4|h5|h6|div|span|p)[=div], `faq_schema`:'yes'[=no]
- section_interactions : `default_state`(expanded|all_collapsed)[=expanded], `max_items_expended`(one|multiple)[=one], `n_accordion_animation_duration`:slider{unit,size}

## onglet style
- section_accordion_style : `accordion_background_normal_background`+GROUPE background, `accordion_border_normal_border`+GROUPE bordure, `accordion_background_hover_background`+GROUPE background, `accordion_border_hover_border`+GROUPE bordure, `accordion_background_active_background`+GROUPE background, `accordion_border_active_border`+GROUPE bordure, `accordion_item_title_space_between`:slider{unit,size}, `accordion_item_title_distance_from_content`:slider{unit,size}, `accordion_border_and_background`, `accordion_border_radius`:dim{t,r,b,l,unit,isLinked}, `accordion_padding`:dim{t,r,b,l,unit,isLinked}
- section_header_style : `title_typography_typography`+GROUPE typo, `title_normal_stroke_text_stroke_type`+GROUPE text_stroke, `title_hover_stroke_text_stroke_type`+GROUPE text_stroke, `title_active_stroke_text_stroke_type`+GROUPE text_stroke, `header_title_color_style`, `normal_title_color`:color, `title_normal_text_shadow_text_shadow_type`, `title_normal_text_shadow_text_shadow`:text_shadow, `hover_title_color`:color, `title_hover_text_shadow_text_shadow_type`, `title_hover_text_shadow_text_shadow`:text_shadow, `active_title_color`:color, `title_active_text_shadow_text_shadow_type`, `title_active_text_shadow_text_shadow`:text_shadow, `icon_size`:slider{unit,size}, `icon_spacing`:slider{unit,size}, `header_icon_color_style`, `normal_icon_color`:color, `hover_icon_color`:color, `active_icon_color`:color
- section_content_style : `content_background_background`+GROUPE background, `content_border_border`+GROUPE bordure, `content_border_radius`:dim{t,r,b,l,unit,isLinked}, `content_padding`:dim{t,r,b,l,unit,isLinked}
