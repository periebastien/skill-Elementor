# `price-table` — Table de prix (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_header : `heading`:txt[=Saisir le titre], `sub_heading`:txt, `heading_tag`(h2|h3|h4|h5|h6)[=h3]
- section_pricing : `currency_symbol`(|dollar|euro|baht|franc|guilder|krona|lira|peseta|peso|…)[=dollar], `currency_symbol_custom`:txt, `price`:txt[=39.99], `currency_format`(|,), `sale`:'yes', `original_price`:nb[=59], `period`:txt[=Mensuellement]
- section_features : `features_list`:repeater[]
- section_footer : `button_text`:txt[=Cliquer ici], `link`:url{url,is_external}, `footer_additional_info`:txt
- section_ribbon : `show_ribbon`:'yes'[=yes], `ribbon_title`:txt[=Populaire], `ribbon_horizontal_position`(left|right)

## onglet style
- section_header_style : `heading_typography_typography`+GROUPE typo, `sub_heading_typography_typography`+GROUPE typo, `header_bg_color`:color, `header_padding`:dim{t,r,b,l,unit,isLinked}, `heading_color`:color, `sub_heading_color`:color
- section_pricing_element_style : `price_typography_typography`+GROUPE typo, `original_price_typography_typography`+GROUPE typo, `period_typography_typography`+GROUPE typo, `pricing_element_bg_color`:color, `pricing_element_padding`:dim{t,r,b,l,unit,isLinked}, `price_color`:color, `currency_size`:slider{unit,size}, `currency_position`(before|after)[=before], `currency_vertical_position`(top|middle|bottom)[=top], `fractional-part_size`:slider{unit,size}, `fractional_part_vertical_position`(top|middle|bottom)[=top], `original_price_color`:color, `original_price_vertical_position`(top|middle|bottom)[=bottom], `period_color`:color, `period_position`(below|beside)[=below]
- section_features_list_style : `features_list_typography_typography`+GROUPE typo, `features_list_bg_color`:color, `features_list_padding`:dim{t,r,b,l,unit,isLinked}, `features_list_color`:color, `features_list_alignment`(start|center|end), `item_width`:slider{unit,size}, `list_divider`:'yes'[=yes], `divider_style`(solid|double|dotted|dashed)[=solid], `divider_color`:color[=#ddd], `divider_weight`:slider{unit,size}, `divider_width`:slider{unit,size}, `divider_gap`:slider{unit,size}
- section_footer_style : `button_typography_typography`+GROUPE typo, `button_background_background`+GROUPE background, `button_border_border`+GROUPE bordure, `button_background_hover_background`+GROUPE background, `additional_info_typography_typography`+GROUPE typo, `footer_bg_color`:color, `footer_padding`:dim{t,r,b,l,unit,isLinked}, `button_size`(xs|sm|md|lg|xl)[=md], `tabs_button_style`, `button_text_color`:color, `button_border_radius`:dim{t,r,b,l,unit,isLinked}, `button_text_padding`:dim{t,r,b,l,unit,isLinked}, `button_hover_color`:color, `button_hover_border_color`:color, `button_hover_animation`, `additional_info_color`:color, `additional_info_margin`:dim{t,r,b,l,unit,isLinked}
- section_ribbon_style : `ribbon_typography_typography`+GROUPE typo, `box_shadow_box_shadow_type`+GROUPE box_shadow, `ribbon_bg_color`:color, `ribbon_distance`:slider{unit,size}, `ribbon_text_color`:color[=#ffffff]
