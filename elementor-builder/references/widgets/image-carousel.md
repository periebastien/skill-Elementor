# `image-carousel` — Carrousel d’images (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_image_carousel : `carousel_name`:txt, `carousel`:gallery[{id,url}], `thumbnail_size`(thumbnail|medium|medium_large|large|1536x1536|2048x2048|woocommerce_thumbnail|woocommerce_single|woocommerce_gallery_thumbnail|full|…)[=thumbnail], `thumbnail_custom_dimension`, `slides_to_show`(|1|2|3|4|5|6|7|8|9|…), `slides_to_scroll`(|1|2|3|4|5|6|7|8|9|…), `image_stretch`(no|yes)[=no], `navigation`(both|arrows|dots|none)[=both], `navigation_previous_icon`:icons{value,library}, `navigation_next_icon`:icons{value,library}, `link_to`(none|file|custom)[=none], `link`:url{url,is_external}, `open_lightbox`(default|yes|no)[=default], `caption_type`(|title|caption|description)
- section_additional_options : `lazyload`:'yes', `autoplay`:'yes'[=yes], `pause_on_hover`:'yes'[=yes], `pause_on_interaction`:'yes'[=yes], `autoplay_speed`:nb[=5000], `infinite`:'yes'[=yes], `effect`(slide|fade)[=slide], `speed`:nb[=500], `direction`(ltr|rtl)[=ltr]

## onglet style
- section_style_navigation : `arrows_position`(inside|outside)[=inside], `arrows_size`:slider{unit,size}, `arrows_color`:color, `dots_position`(outside|inside)[=outside], `dots_gap`:slider{unit,size}, `dots_size`:slider{unit,size}, `dots_inactive_color`:color, `dots_color`:color
- section_style_image : `image_border_border`+GROUPE bordure, `gallery_vertical_align`(flex-start|center|flex-end), `image_spacing`(|custom), `image_spacing_custom`:slider{unit,size}, `image_border_radius`:dim{t,r,b,l,unit,isLinked}
- section_caption : `caption_typography_typography`+GROUPE typo, `caption_align`(start|center|end|justify)[=center], `caption_text_color`:color, `caption_shadow_text_shadow_type`, `caption_shadow_text_shadow`:text_shadow, `caption_space`:slider{unit,size}
