# `share-buttons` — Boutons de partage (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_buttons_content : `share_buttons`:repeater[], `view`(icon-text|icon|text)[=icon-text], `show_label`:'yes'[=yes], `skin`(gradient|minimal|framed|boxed|flat)[=gradient], `shape`(square|rounded|circle)[=square], `columns`(0|1|2|3|4|5|6)[=0], `alignment`(left|center|right|justify), `share_url_type`(current_page|custom)[=current_page], `share_url`:url{url,is_external}

## onglet style
- section_buttons_style : `typography_typography`+GROUPE typo, `column_gap`:slider{unit,size}, `row_gap`:slider{unit,size}, `button_size`:slider{unit,size}, `icon_size`:slider{unit,size}, `button_height`:slider{unit,size}, `border_size`:slider{unit,size}, `color_source`(official|custom)[=official], `tabs_button_style`, `primary_color`:color, `secondary_color`:color, `primary_color_hover`:color, `secondary_color_hover`:color, `text_padding`:dim{t,r,b,l,unit,isLinked}
