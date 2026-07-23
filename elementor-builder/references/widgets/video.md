# `video` — Vidéo (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_video : `video_type`(youtube|vimeo|dailymotion|videopress|hosted)[=youtube], `youtube_url`:txt, `vimeo_url`:txt, `dailymotion_url`:txt, `insert_url`:'yes', `hosted_url`:media{id,url}, `external_url`:url{url,is_external}, `videopress_url`:txt, `start`:nb, `end`:nb, `autoplay`:'yes', `mute`:'yes', `loop`:'yes', `controls`:'yes'[=yes], `showinfo`:'yes'[=yes], `cc_load_policy`:'yes', `logo`:'yes'[=yes], `yt_privacy`:'yes', `lazy_load`:'yes', `rel`(|yes), `vimeo_title`:'yes'[=yes], `vimeo_portrait`:'yes'[=yes], `vimeo_byline`:'yes'[=yes], `color`:color, `download_button`:'yes', `preload`(metadata|auto|none)[=metadata], `poster`:media{id,url}
- section_image_overlay : `show_image_overlay`:'yes', `image_overlay`:media{id,url}, `image_overlay_size`(thumbnail|medium|medium_large|large|1536x1536|2048x2048|woocommerce_thumbnail|woocommerce_single|woocommerce_gallery_thumbnail|full|…)[=full], `image_overlay_custom_dimension`, `show_play_icon`:'yes'[=yes], `play_icon`:icons{value,library}, `lightbox`:'yes'

## onglet style
- section_video_style : `aspect_ratio`(169|219|43|32|11|916)[=169], `css_filters_css_filter`, `css_filters_blur`:slider{unit,size}, `css_filters_brightness`:slider{unit,size}, `css_filters_contrast`:slider{unit,size}, `css_filters_saturate`:slider{unit,size}, `css_filters_hue`:slider{unit,size}
- section_image_overlay_style : `play_icon_color`:color, `play_icon_size`:slider{unit,size}, `play_icon_text_shadow_text_shadow_type`, `play_icon_text_shadow_text_shadow`:text_shadow
- section_lightbox_style : `lightbox_color`:color, `lightbox_ui_color`:color, `lightbox_ui_color_hover`:color, `lightbox_content_animation`, `lightbox_video_width`:slider{unit,size}, `lightbox_content_position`(|top)
