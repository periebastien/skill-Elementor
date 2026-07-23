# `image-gallery` — Galerie basique (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_gallery : `wp_gallery`:gallery[{id,url}], `thumbnail_size`(thumbnail|medium|medium_large|large|1536x1536|2048x2048|woocommerce_thumbnail|woocommerce_single|woocommerce_gallery_thumbnail|full)[=thumbnail], `gallery_columns`(1|2|3|4|5|6|7|8|9|10)[=4], `gallery_display_caption`(none|), `gallery_link`(file|attachment|none)[=file], `open_lightbox`(default|yes|no)[=default], `gallery_rand`(|rand)

## onglet style
- section_gallery_images : `image_border_border`+GROUPE bordure, `image_spacing`(|custom), `image_spacing_custom`:slider{unit,size}, `image_border_radius`:dim{t,r,b,l,unit,isLinked}
- section_caption : `typography_typography`+GROUPE typo, `align`(start|center|end|justify)[=center], `text_color`:color, `caption_shadow_text_shadow_type`, `caption_shadow_text_shadow`:text_shadow, `caption_space`:slider{unit,size}
