# `slides` — Diapositives (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_slides : `slides_name`:txt[=Diapositives], `slides`:repeater[], `slides_height`:slider{unit,size}, `slides_title_tag`(h1|h2|h3|h4|h5|h6|div|span|p)[=div], `slides_description_tag`(h1|h2|h3|h4|h5|h6|div|span|p)[=div]
- section_slider_options : `navigation`(both|arrows|dots|none)[=both], `autoplay`:'yes'[=yes], `pause_on_hover`:'yes'[=yes], `pause_on_interaction`:'yes'[=yes], `autoplay_speed`:nb[=5000], `infinite`:'yes'[=yes], `transition`(slide|fade)[=slide], `transition_speed`:nb[=500], `content_animation`[=fadeInUp]

## onglet style
- section_style_slides : `content_max_width`:slider{unit,size}, `slides_padding`:dim{t,r,b,l,unit,isLinked}, `slides_horizontal_position`(left|center|right)[=center], `slides_vertical_position`(top|middle|bottom)[=middle], `slides_text_align`(start|center|end)[=center], `text_shadow_text_shadow_type`, `text_shadow_text_shadow`:text_shadow
- section_style_title : `heading_typography_typography`+GROUPE typo, `heading_spacing`:slider{unit,size}, `heading_color`:color
- section_style_description : `description_typography_typography`+GROUPE typo, `description_spacing`:slider{unit,size}, `description_color`:color
- section_style_button : `button_typography_typography`+GROUPE typo, `button_background_background`+GROUPE background, `button_hover_background_background`+GROUPE background, `button_size`(xs|sm|md|lg|xl)[=sm], `button_border_width`:slider{unit,size}, `button_border_radius`:slider{unit,size}, `button_tabs`, `button_text_color`:color, `button_border_color`:color, `button_hover_text_color`:color, `button_hover_border_color`:color, `button_hover_transition_duration`:slider{unit,size}
- section_style_navigation : `arrows_position`(inside|outside)[=inside], `arrows_size`:slider{unit,size}, `arrows_color`:color, `dots_position`(outside|inside)[=inside], `dots_gap`:slider{unit,size}, `dots_size`:slider{unit,size}, `dots_color_inactive`:color, `dots_color`:color
