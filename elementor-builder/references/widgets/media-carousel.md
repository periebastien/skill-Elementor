# `media-carousel` — Carrousel de médias (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_slides : `skin`(carousel|slideshow|coverflow)[=carousel], `slides_name`:txt[=Diapositives], `slides`:repeater[], `effect`(slide|fade|cube)[=slide], `slideshow_height`:slider{unit,size}, `slides_per_view`(|1|2|3|4|5|6|7|8|9|…), `slideshow_slides_per_view`(|1|2|3|4|5|6|7|8|9|…), `thumbs_ratio`(169|219|43|11)[=219], `centered_slides`:'yes', `slides_to_scroll`(|1|2|3|4|5|6|7|8|9|…), `height`:slider{unit,size}, `width`:slider{unit,size}
- section_additional_options : `show_arrows`:'yes'[=yes], `pagination`(|bullets|fraction|progressbar)[=bullets], `speed`:nb[=500], `autoplay`:'yes'[=yes], `autoplay_speed`:nb[=5000], `loop`:'yes'[=yes], `pause_on_hover`:'yes'[=yes], `pause_on_interaction`:'yes'[=yes], `overlay`(|text|icon), `caption`(title|caption|description)[=title], `icon`(search-plus|plus-circle|eye|link)[=search-plus], `overlay_animation`(fade|slide-up|slide-down|slide-right|slide-left|zoom-in)[=fade], `image_size_size`(thumbnail|medium|medium_large|large|1536x1536|2048x2048|woocommerce_thumbnail|woocommerce_single|woocommerce_gallery_thumbnail|full|…)[=full], `image_size_custom_dimension`, `image_fit`(|contain|auto), `lazyload`:'yes'

## onglet style
- section_slides_style : `space_between`:slider{unit,size}, `slide_background_color`:color, `slide_border_size`:dim{t,r,b,l,unit,isLinked}, `slide_border_radius`:slider{unit,size}, `slide_border_color`:color, `slide_padding`:dim{t,r,b,l,unit,isLinked}
- section_navigation : `arrows_size`:slider{unit,size}, `arrows_color`:color, `pagination_position`(outside|inside)[=outside], `pagination_gap`:slider{unit,size}, `pagination_size`:slider{unit,size}, `pagination_color_inactive`:color, `pagination_color`:color, `play_icon_color`:color, `play_icon_size`:slider{unit,size}, `play_icon_text_shadow_text_shadow_type`, `play_icon_text_shadow_text_shadow`:text_shadow
- section_overlay : `caption_typography_typography`+GROUPE typo, `overlay_background_color`:color, `overlay_color`:color, `icon_size`:slider{unit,size}
- section_lightbox_style : `lightbox_color`:color, `lightbox_ui_color`:color, `lightbox_ui_hover_color`:color, `lightbox_video_width`:slider{unit,size}
