# `nested-tabs` — Onglets (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_tabs : `tabs`, `tabs_direction`(block-start|block-end|inline-end|inline-start), `tabs_justify_horizontal`(start|center|end|stretch), `tabs_justify_vertical`(start|center|end|stretch), `tabs_width`:slider{unit,size}, `title_alignment`(start|center|end)
- section_tabs_responsive : `horizontal_scroll`(disable|enable)[=disable], `breakpoint_selector`(none|mobile|tablet)[=mobile]

## onglet style
- section_tabs_style : `tabs_title_background_color_background`+GROUPE background, `tabs_title_border_border`+GROUPE bordure, `tabs_title_box_shadow_box_shadow_type`+GROUPE box_shadow, `tabs_title_background_color_hover_background`+GROUPE background, `tabs_title_border_hover_border`+GROUPE bordure, `tabs_title_box_shadow_hover_box_shadow_type`+GROUPE box_shadow, `tabs_title_background_color_active_background`+GROUPE background, `tabs_title_border_active_border`+GROUPE bordure, `tabs_title_box_shadow_active_box_shadow_type`+GROUPE box_shadow, `tabs_title_space_between`:slider{unit,size}, `tabs_title_spacing`:slider{unit,size}, `tabs_title_style`, `hover_animation`, `tabs_title_transition_duration`:slider{unit,size}, `tabs_title_border_radius`:dim{t,r,b,l,unit,isLinked}, `padding`:dim{t,r,b,l,unit,isLinked}
- section_title_style : `title_typography_typography`+GROUPE typo, `title_text_stroke_text_stroke_type`+GROUPE text_stroke, `title_text_stroke_hover_text_stroke_type`+GROUPE text_stroke, `title_text_stroke_active_text_stroke_type`+GROUPE text_stroke, `title_style`, `title_text_color`:color, `title_text_shadow_text_shadow_type`, `title_text_shadow_text_shadow`:text_shadow, `title_text_color_hover`:color, `title_text_shadow_hover_text_shadow_type`, `title_text_shadow_hover_text_shadow`:text_shadow, `title_text_color_active`:color, `title_text_shadow_active_text_shadow_type`, `title_text_shadow_active_text_shadow`:text_shadow
- icon_section_style : `icon_position`(block-start|inline-end|block-end|inline-start), `icon_size`:slider{unit,size}, `icon_spacing`:slider{unit,size}, `icon_style_states`, `icon_color`:color, `icon_color_hover`:color, `icon_color_active`:color
- section_box_style : `box_background_color_background`+GROUPE background, `box_border_border`+GROUPE bordure, `box_shadow_box_shadow_box_shadow_type`+GROUPE box_shadow, `box_border_radius`:dim{t,r,b,l,unit,isLinked}, `box_padding`:dim{t,r,b,l,unit,isLinked}
