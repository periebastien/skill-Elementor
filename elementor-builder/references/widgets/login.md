# `login` — Connexion (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_fields_content : `show_labels`:'yes'[=yes], `input_size`(xs|sm|md|lg|xl)[=sm]
- section_button_content : `button_text`:txt[=Connexion], `button_size`(xs|sm|md|lg|xl)[=sm], `align`(start|center|end|stretch)
- section_login_content : `redirect_after_login`:'yes', `redirect_url`:url{url,is_external}, `redirect_after_logout`:'yes', `redirect_logout_url`:url{url,is_external}, `show_lost_password`:'yes'[=yes], `show_register`:'yes'[=yes], `show_remember_me`:'yes'[=yes], `show_logged_in_message`:'yes'[=yes], `custom_labels`:'yes', `user_label`:txt, `user_placeholder`:txt, `password_label`:txt[=Mot de passe], `password_placeholder`:txt[=Mot de passe]

## onglet style
- section_style : `row_gap`:slider{unit,size}, `links_color`:color, `links_hover_color`:color
- section_style_labels : `label_typography_typography`+GROUPE typo, `label_spacing`:slider{unit,size}, `label_color`:color
- section_field_style : `field_typography_typography`+GROUPE typo, `field_text_color`:color, `field_background_color`:color[=#ffffff], `field_border_color`:color, `field_border_width`:dim{t,r,b,l,unit,isLinked}, `field_border_radius`:dim{t,r,b,l,unit,isLinked}
- section_button_style : `button_typography_typography`+GROUPE typo, `button_background_background`+GROUPE background, `button_border_border`+GROUPE bordure, `button_background_hover_background`+GROUPE background, `tabs_button_style`, `button_text_color`:color, `button_border_radius`:dim{t,r,b,l,unit,isLinked}, `button_text_padding`:dim{t,r,b,l,unit,isLinked}, `button_hover_color`:color, `button_hover_border_color`:color, `button_hover_animation`, `button_hover_transition_duration`:slider{unit,size}
- section_style_message : `message_typography_typography`+GROUPE typo, `message_color`:color
