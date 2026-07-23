# `post-navigation` — Navigation de publication (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_post_navigation_content : `show_label`:'yes'[=yes], `prev_label`:txt[=Précédent], `next_label`:txt[=Suivant], `show_arrow`:'yes'[=yes], `arrow_previous_icon`:icons{value,library}, `arrow_next_icon`:icons{value,library}, `show_title`:'yes'[=yes], `show_borders`:'yes'[=yes], `in_same_term`(post|product), `post_taxonomy`(category|post_tag|post_format), `product_taxonomy`(product_brand|product_type|product_visibility|product_cat|product_tag|product_shipping_class|pos_product_visibility)

## onglet style
- label_style : `label_typography_typography`+GROUPE typo, `tabs_label_style`, `label_color`:color, `label_hover_color`:color, `label_hover_color_transition_duration`:slider{unit,size}
- title_style : `title_typography_typography`+GROUPE typo, `tabs_post_navigation_style`, `text_color`:color, `hover_color`:color, `hover_color_transition_duration`:slider{unit,size}
- arrow_style : `tabs_post_navigation_arrow_style`, `arrow_color`:color, `arrow_hover_color`:color, `arrow_hover_color_transition_duration`:slider{unit,size}, `arrow_size`:slider{unit,size}, `arrow_padding`:slider{unit,size}
- borders_section_style : `sep_color`:color, `borders_width`:slider{unit,size}, `borders_spacing`:slider{unit,size}
