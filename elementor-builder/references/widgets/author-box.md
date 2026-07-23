# `author-box` — Boîte d’auteur/autrice (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_author_info : `source`(current|custom)[=current], `show_avatar`:'yes'[=yes], `avatar_size`:nb[=300], `author_avatar`:media{id,url}, `show_name`:'yes'[=yes], `author_name`:txt[=John Doe], `author_name_tag`(h1|h2|h3|h4|h5|h6|div|span)[=h4], `link_to`(|website|posts_archive), `show_biography`:'yes'[=yes], `show_link`:'yes'[=no], `author_website`:url{url,is_external}, `author_bio`:txt, `posts_url`:url{url,is_external}, `link_text`:txt, `layout`(left|above|right), `alignment`(left|center|right)

## onglet style
- section_image_style : `input_box_shadow_box_shadow_type`+GROUPE box_shadow, `image_vertical_align`(top|middle), `image_size`:slider{unit,size}, `image_gap`:slider{unit,size}, `image_border`:'yes', `image_border_color`:color[=#000], `image_border_width`:slider{unit,size}, `image_border_radius`:slider{unit,size}
- section_text_style : `name_typography_typography`+GROUPE typo, `bio_typography_typography`+GROUPE typo, `name_color`:color, `name_gap`:slider{unit,size}, `bio_color`:color, `bio_gap`:slider{unit,size}
- section_style_button : `button_typography_typography`+GROUPE typo, `tabs_button_style`, `button_text_color`:color, `button_background_color`:color, `button_hover_color`:color, `button_background_hover_color`:color, `button_hover_transition_duration`:slider{unit,size}, `button_hover_animation`, `button_border_width`:slider{unit,size}, `button_border_radius`:slider{unit,size}, `button_text_padding`:dim{t,r,b,l,unit,isLinked}
