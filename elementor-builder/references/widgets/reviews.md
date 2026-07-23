# `reviews` — Avis (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_slides : `slides_name`:txt[=Diapositives], `slides`:repeater[], `slides_per_view`(|1|2|3|4|5|6|7|8|9|…), `slides_to_scroll`(|1|2|3|4|5|6|7|8|9|…), `width`:slider{unit,size}
- section_additional_options : `show_arrows`:'yes'[=yes], `pagination`(|bullets|fraction|progressbar)[=bullets], `speed`:nb[=500], `autoplay`:'yes'[=yes], `autoplay_speed`:nb[=5000], `loop`:'yes'[=yes], `pause_on_hover`:'yes'[=yes], `pause_on_interaction`:'yes'[=yes], `image_size_size`(thumbnail|medium|medium_large|large|1536x1536|2048x2048|woocommerce_thumbnail|woocommerce_single|woocommerce_gallery_thumbnail|full|…)[=full], `image_size_custom_dimension`, `lazyload`:'yes'

## onglet style
- section_slides_style : `space_between`:slider{unit,size}, `slide_background_color`:color, `slide_border_size`:dim{t,r,b,l,unit,isLinked}, `slide_border_radius`:slider{unit,size}, `slide_border_color`:color, `slide_padding`:dim{t,r,b,l,unit,isLinked}, `header_background_color`:color, `content_gap`:slider{unit,size}, `show_separator`:'yes'[=has-separator], `separator_color`:color, `separator_size`:slider{unit,size}
- section_content_style : `name_typography_typography`+GROUPE typo, `title_typography_typography`+GROUPE typo, `content_typography_typography`+GROUPE typo, `name_color`:color, `title_color`:color, `content_color`:color
- section_image_style : `image_size`:slider{unit,size}, `image_gap`:slider{unit,size}, `image_border_radius`:slider{unit,size}
- section_icon_style : `icon_color`(default|custom)[=default], `icon_custom_color`:color, `icon_size`:slider{unit,size}
- section_rating_style : `star_style`(star_fontawesome|star_unicode)[=star_fontawesome], `unmarked_star_style`(solid|outline)[=solid], `star_size`:slider{unit,size}, `star_space`:slider{unit,size}, `stars_color`:color, `stars_unmarked_color`:color
- section_navigation : `arrows_size`:slider{unit,size}, `arrows_color`:color, `pagination_gap`:slider{unit,size}, `pagination_size`:slider{unit,size}, `pagination_color_inactive`:color, `pagination_color`:color
