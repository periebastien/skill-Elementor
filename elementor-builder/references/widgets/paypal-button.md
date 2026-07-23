# `paypal-button` — Bouton PayPal (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_account : `email`:txt, `sdk_token`:txt, `type`(checkout|donation|subscription)[=checkout], `product_name`:txt, `product_sku`:txt, `product_price`:nb[=0.00], `donation_type`(any|fixed)[=fixed], `donation_amount`:nb[=1], `currency`(AUD|CAD|CZK|DKK|EUR|HKD|HUF|ILS|JPY|MXN|…)[=USD], `billing_cycle`(days|weeks|months|years)[=months], `auto_renewal`:'yes'[=yes], `quantity`:nb[=1], `shipping_price`:nb[=0], `tax_type`(|percentage), `tax_rate`:nb[=0]
- section_button : `text`:txt[=Buy Now], `selected_icon`:icons{value,library}, `icon_align`(row|row-reverse)[=row], `icon_indent`:slider{unit,size}, `button_css_id`:txt
- section_settings : `redirect_after_success`:url{url,is_external}, `sandbox_mode`:'yes'[=no], `sandbox_email`:txt, `open_in_new_window`:'yes'[=yes], `custom_messages`:'yes', `error_message_global`:txt, `error_message_payment`:txt

## onglet style
- section_style : `typography_typography`+GROUPE typo, `background_background`+GROUPE background, `button_box_shadow_box_shadow_type`+GROUPE box_shadow, `button_background_hover_background`+GROUPE background, `button_hover_box_shadow_box_shadow_type`+GROUPE box_shadow, `border_border`+GROUPE bordure, `align`(left|center|right|justify), `content_align`(start|center|end|space-between), `text_shadow_text_shadow_type`, `text_shadow_text_shadow`:text_shadow, `tabs_button_style`, `button_text_color`:color[=#FFF], `hover_color`:color, `button_hover_border_color`:color, `button_hover_transition_duration`:slider{unit,size}, `hover_animation`, `border_radius`:dim{t,r,b,l,unit,isLinked}, `text_padding`:dim{t,r,b,l,unit,isLinked}
- section_messages_style : `message_typography_typography`+GROUPE typo, `message_color_global`:color, `message_color_payment`:color
