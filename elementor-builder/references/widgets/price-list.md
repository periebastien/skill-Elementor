# `price-list` — Liste de prix (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_list : `price_list`:repeater[], `title_tag`(h1|h2|h3|h4|h5|h6|div|span|p)[=span], `description_tag`(h1|h2|h3|h4|h5|h6|div|span|p)[=p], `image_size_size`(thumbnail|medium|medium_large|large|1536x1536|2048x2048|woocommerce_thumbnail|woocommerce_single|woocommerce_gallery_thumbnail|full|…)[=thumbnail], `image_size_custom_dimension`

## onglet style
- section_list_style : `vertical_align`(top|center|bottom)[=top], `row_gap`:slider{unit,size}, `image_spacing`:slider{unit,size}, `content_spacing`:slider{unit,size}
- section_content_style : `heading_typography_typography`+GROUPE typo, `text_stroke_text_stroke_type`+GROUPE text_stroke, `price_typography_typography`+GROUPE typo, `description_typography_typography`+GROUPE typo, `heading_color`:color, `price_color`:color, `description_color`:color, `separator_style`(none|solid|dotted|dashed|double)[=dotted], `separator_weight`:slider{unit,size}, `separator_color`:color, `separator_spacing`:slider{unit,size}
- section_image_style : `border_radius`:dim{t,r,b,l,unit,isLinked}
