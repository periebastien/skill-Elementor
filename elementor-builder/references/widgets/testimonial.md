# `testimonial` — Témoignage (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_testimonial : `testimonial_content`:txt, `testimonial_image`:media{id,url}, `testimonial_image_size`(thumbnail|medium|medium_large|large|1536x1536|2048x2048|woocommerce_thumbnail|woocommerce_single|woocommerce_gallery_thumbnail|full|…)[=full], `testimonial_image_custom_dimension`, `testimonial_name`:txt[=Jean Dupont], `testimonial_job`:txt[=Concepteur], `link`:url{url,is_external}, `testimonial_image_position`(aside|top)[=aside], `testimonial_alignment`(start|center|end)[=center]

## onglet style
- section_style_testimonial_content : `content_typography_typography`+GROUPE typo, `content_content_color`:color, `content_shadow_text_shadow_type`, `content_shadow_text_shadow`:text_shadow
- section_style_testimonial_image : `image_border_border`+GROUPE bordure, `image_size`:slider{unit,size}, `image_border_radius`:dim{t,r,b,l,unit,isLinked}
- section_style_testimonial_name : `name_typography_typography`+GROUPE typo, `name_text_color`:color, `name_shadow_text_shadow_type`, `name_shadow_text_shadow`:text_shadow
- section_style_testimonial_job : `job_typography_typography`+GROUPE typo, `job_text_color`:color, `job_shadow_text_shadow_type`, `job_shadow_text_shadow`:text_shadow
