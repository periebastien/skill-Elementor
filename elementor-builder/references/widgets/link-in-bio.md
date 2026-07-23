# `link-in-bio` — Minimaliste (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- identity_section : `identity_image_style`(profile|cover)[=profile], `identity_image`:media{id,url}, `identity_image_position`(|center center|center left|center right|top center|top left|top right|bottom center|bottom left|bottom right)
- bio_section : `bio_heading`:txt[=Sara Parker], `bio_heading_tag`(h1|h2|h3|h4|h5|h6|div|span|p)[=h2], `bio_title`:txt, `bio_title_tag`(h1|h2|h3|h4|h5|h6|div|span|p)[=h3], `bio_description`:txt
- icons_section : `icon`:repeater[]
- cta_section : `cta_link`:repeater[]

## onglet style
- identity_section_style : `identity_image_size`:slider{unit,size}, `identity_image_shape`(circle|square)[=circle], `identity_image_show_border`:'yes', `identity_image_border_width`:slider{unit,size}, `identity_image_border_color`:color[=#000000], `identity_image_height`:slider{unit,size}, `identity_image_bottom_show_border`:'yes', `identity_image_bottom_border_width`:slider{unit,size}, `identity_image_bottom_border_color`:color[=#000000]
- bio_section_style : `bio_heading_typography_typography`+GROUPE typo, `bio_title_typography_typography`+GROUPE typo, `bio_description_typography_typography`+GROUPE typo, `bio_heading_text_color`:color, `bio_title_text_color`:color, `bio_description_text_color`:color
- icons_section_style : `icons_color`:color, `icons_size`(small|medium|large)[=small]
- cta_links_section_style : `cta_links_typography_typography`+GROUPE typo, `cta_links_type`(button|link)[=button], `cta_links_text_color`:color, `cta_links_background_color`:color, `cta_links_show_border`:'yes', `cta_links_border_width`:slider{unit,size}, `cta_links_border_color`:color[=#000000], `cta_links_corners`(round|rounded|sharp)[=rounded], `cta_links_padding`:dim{t,r,b,l,unit,isLinked}
- background_border_section_style : `background_border_background_group_background`+GROUPE background, `background_border_background_overlay_group_background`+GROUPE background, `background_overlay_opacity`:slider{unit,size}, `background_show_border`:'yes', `background_border_width`:slider{unit,size}, `background_border_color`:color[=#000000], `advanced_layout_full_width_custom`:'yes', `advanced_layout_width`:slider{unit,size}, `advanced_layout_content_width`:slider{unit,size}, `advanced_layout_full_screen_height`:'yes', `advanced_layout_full_screen_height_controls`(desktop|tablet|mobile)
