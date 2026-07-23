# `alert` — Alerte (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_alert : `alert_type`(info|success|warning|danger)[=info], `alert_title`:txt, `alert_description`:txt, `show_dismiss`:'yes'[=show], `dismiss_icon`:icons{value,library}

## onglet style
- section_type : `background`:color, `border_color`:color, `border_left-width`:slider{unit,size}
- section_title : `alert_title_typography`+GROUPE typo, `title_color`:color, `title_shadow_text_shadow_type`, `title_shadow_text_shadow`:text_shadow
- section_description : `alert_description_typography`+GROUPE typo, `description_color`:color, `description_shadow_text_shadow_type`, `description_shadow_text_shadow`:text_shadow
- section_dismiss_icon : `dismiss_icon_size`:slider{unit,size}, `dismiss_icon_vertical_position`:slider{unit,size}, `dismiss_icon_horizontal_position`:slider{unit,size}, `dismiss_icon_colors`, `dismiss_icon_normal_color`:color, `dismiss_icon_hover_color`:color, `dismiss_icon_hover_transition_duration`:slider{unit,size}
