# `lottie` — Lottie (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- lottie : `source`(media_file)[=media_file], `source_json`:media{id,url}, `align`(left|center|right)[=center], `caption_source`(none|title|caption|custom)[=none], `caption`:txt, `link_to`(none|custom)[=none], `custom_link`:url{url,is_external}
- settings : `trigger`(arriving_to_viewport|on_click|on_hover|bind_to_scroll|none), `viewport`:slider{unit,size}, `effects_relative_to`(viewport|page)[=viewport], `loop`:'yes', `number_of_times`:nb, `link_timeout`:nb, `on_hover_out`(default|reverse|pause)[=default], `hover_area`(animation|column|section|container)[=animation], `play_speed`:slider{unit,size}, `start_point`:slider{unit,size}, `end_point`:slider{unit,size}, `reverse_animation`:'yes', `renderer`(svg|canvas)[=svg], `lazyload`:'yes'

## onglet style
- style : `width`:slider{unit,size}, `space`:slider{unit,size}, `image_effects`, `opacity`:slider{unit,size}, `css_filters_css_filter`, `css_filters_blur`:slider{unit,size}, `css_filters_brightness`:slider{unit,size}, `css_filters_contrast`:slider{unit,size}, `css_filters_saturate`:slider{unit,size}, `css_filters_hue`:slider{unit,size}, `opacity_hover`:slider{unit,size}, `css_filters_hover_css_filter`, `css_filters_hover_blur`:slider{unit,size}, `css_filters_hover_brightness`:slider{unit,size}, `css_filters_hover_contrast`:slider{unit,size}, `css_filters_hover_saturate`:slider{unit,size}, `css_filters_hover_hue`:slider{unit,size}, `background_hover_transition`:slider{unit,size}
- section_style_caption : `caption_typography_typography`+GROUPE typo, `caption_align`(left|center|right)[=center], `text_color`:color, `caption_space`:slider{unit,size}
