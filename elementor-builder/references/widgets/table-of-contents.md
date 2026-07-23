# `table-of-contents` — Table des matières (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- table_of_contents : `title`:txt, `html_tag`(h2|h3|h4|h5|h6|div)[=h4], `include_exclude_tags`, `headings_by_tags`(h1|h2|h3|h4|h5|h6), `container`:txt, `exclude_headings_by_selector`:txt, `marker_view`(numbers|bullets)[=numbers], `icon`:icons{value,library}, `no_headings_message`:txt
- additional_options : `word_wrap`:'yes', `minimize_box`:'yes'[=yes], `expand_icon`:icons{value,library}, `collapse_icon`:icons{value,library}, `minimized_on`(mobile|tablet|desktop)[=tablet], `hierarchical_view`:'yes'[=yes], `collapse_subitems`:'yes'

## onglet style
- box_style : `box_shadow_box_shadow_type`+GROUPE box_shadow, `background_color`:color, `border_color`:color, `loader_color`:color, `border_width`:slider{unit,size}, `border_radius`:slider{unit,size}, `header_separator_width`:slider{unit,size}, `padding`:slider{unit,size}, `min_height`:slider{unit,size}
- header_style : `header_typography_typography`+GROUPE typo, `header_text_align`(start|center|end)[=start], `header_background_color`:color, `header_text_color`:color, `toggle_button_color`:color, `toggle_button_position`(row-reverse|row)[=row], `heading_gap`:slider{unit,size}
- list_style : `list_typography_typography`+GROUPE typo, `max_height`:slider{unit,size}, `list_indent`:slider{unit,size}, `item_text_style`, `item_text_color_normal`:color, `item_text_underline_normal`:'yes', `item_text_color_hover`:color, `item_text_underline_hover`:'yes'[=yes], `item_text_hover_transition_duration`:slider{unit,size}, `item_text_color_active`:color, `item_text_underline_active`:'yes', `marker_color`:color, `marker_size`:slider{unit,size}
