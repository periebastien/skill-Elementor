# `off-canvas` — Off-Canvas (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_layout : `editing_mode`:'yes'[=yes], `off_canvas_name`:txt[=Off-Canvas], `horizontal_position`(flex-start|center|flex-end), `vertical_position`(flex-start|center|flex-end), `width`:slider{unit,size}, `height`(fit-content|custom)[=custom], `custom_height`:slider{unit,size}
- section_settings : `entrance_animation`, `exit_animation`, `offcanvas_animation_duration`:slider{unit,size}, `is_not_close_on_overlay`:'yes', `is_not_close_on_esc_overlay`:'yes', `prevent_scroll`:'yes', `wrapper_html_tag`(div|main|article|header|footer|section|aside|nav)[=div]

## onglet style
- section_background : `background_background`+GROUPE background, `border_border`+GROUPE bordure, `box_shadow_box_shadow_type`+GROUPE box_shadow, `border_radius`:dim{t,r,b,l,unit,isLinked}
- section_overlay : `overlay_background_background`+GROUPE background, `has_overlay`:'yes'[=yes]
