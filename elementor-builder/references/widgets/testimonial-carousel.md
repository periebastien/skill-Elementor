# `testimonial-carousel` — Carrousel de témoignages (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_slides : `slides_name`:txt[=Diapositives], `slides`:repeater[], `skin`(default|bubble)[=default], `layout`(image_inline|image_stacked|image_above|image_left|image_right)[=image_inline], `alignment`(left|center|right)[=center], `slides_per_view`(|1|2|3|4|5|6|7|8|9|…), `slides_to_scroll`(|1|2|3|4|5|6|7|8|9|…), `width`:slider{unit,size}
- section_additional_options : `show_arrows`:'yes'[=yes], `pagination`(|bullets|fraction|progressbar)[=bullets], `speed`:nb[=500], `autoplay`:'yes'[=yes], `autoplay_speed`:nb[=5000], `loop`:'yes'[=yes], `pause_on_hover`:'yes'[=yes], `pause_on_interaction`:'yes'[=yes], `image_size_size`(thumbnail|medium|medium_large|large|1536x1536|2048x2048|woocommerce_thumbnail|woocommerce_single|woocommerce_gallery_thumbnail|full|…)[=full], `image_size_custom_dimension`, `lazyload`:'yes'

## onglet style
- section_slides_style : `space_between`:slider{unit,size}, `slide_background_color`:color, `slide_border_size`:dim{t,r,b,l,unit,isLinked}, `slide_border_radius`:slider{unit,size}, `slide_border_color`:color, `slide_padding`:dim{t,r,b,l,unit,isLinked}
- section_content_style : `content_typography_typography`+GROUPE typo, `text_stroke_text_stroke_type`+GROUPE text_stroke, `name_typography_typography`+GROUPE typo, `title_typography_typography`+GROUPE typo, `content_gap`:slider{unit,size}, `content_color`:color, `content_text_shadow_text_shadow_type`, `content_text_shadow_text_shadow`:text_shadow, `name_color`:color, `title_color`:color
- section_image_style : `image_size`:slider{unit,size}, `image_gap`:slider{unit,size}, `image_border`:'yes', `image_border_color`:color[=#000], `image_border_width`:slider{unit,size}, `image_border_radius`:slider{unit,size}
- section_navigation : `arrows_size`:slider{unit,size}, `arrows_color`:color, `pagination_gap`:slider{unit,size}, `pagination_size`:slider{unit,size}, `pagination_color_inactive`:color, `pagination_color`:color
- section_skin_style : `background_color`:color, `text_padding`:dim{t,r,b,l,unit,isLinked}, `border_radius`:dim{t,r,b,l,unit,isLinked}, `border`:'yes', `border_color`:color[=#000], `border_width`:slider{unit,size}
