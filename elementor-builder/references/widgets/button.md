# `button` — Bouton (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_button : `button_type`(|info|success|warning|danger), `text`:txt[=Cliquez ici], `link`:url{url,is_external}, `size`(xs|sm|md|lg|xl)[=sm], `selected_icon`:icons{value,library}, `icon_align`(row|row-reverse)[=row], `icon_indent`:slider{unit,size}, `button_css_id`:txt

## onglet style
- section_style : `typography_typography`+GROUPE typo, `background_background`+GROUPE background, `button_box_shadow_box_shadow_type`+GROUPE box_shadow, `button_background_hover_background`+GROUPE background, `button_hover_box_shadow_box_shadow_type`+GROUPE box_shadow, `border_border`+GROUPE bordure, `align`(left|center|right|justify), `content_align`(start|center|end|space-between), `text_shadow_text_shadow_type`, `text_shadow_text_shadow`:text_shadow, `tabs_button_style`, `button_text_color`:color, `hover_color`:color, `button_hover_border_color`:color, `button_hover_transition_duration`:slider{unit,size}, `hover_animation`, `border_radius`:dim{t,r,b,l,unit,isLinked}, `text_padding`:dim{t,r,b,l,unit,isLinked}
