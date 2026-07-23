# `countdown` — Compte à rebours (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_countdown : `countdown_type`(due_date|evergreen)[=due_date], `due_date`:datetime[=2026-08-23 10:06], `evergreen_counter_hours`:nb[=47], `evergreen_counter_minutes`:nb[=59], `show_days`:'yes'[=yes], `show_hours`:'yes'[=yes], `show_minutes`:'yes'[=yes], `show_seconds`:'yes'[=yes], `show_labels`:'yes'[=yes], `custom_labels`:'yes', `label_days`:txt[=Jours], `label_hours`:txt[=Heures], `label_minutes`:txt[=Minutes], `label_seconds`:txt[=Secondes], `expire_actions`(redirect|hide|message), `message_after_expire`:txt, `expire_redirect_url`:url{url,is_external}

## onglet style
- section_countdown_style : `box_border_border`+GROUPE bordure, `box_shadow_box_shadow_type`+GROUPE box_shadow, `label_display`(block|inline)[=block], `container_width`:slider{unit,size}, `boxes_alignment`(start|center|end), `box_spacing`:slider{unit,size}, `box_padding`:dim{t,r,b,l,unit,isLinked}, `box_background_color`:color, `box_border_radius`:dim{t,r,b,l,unit,isLinked}
- section_content_style : `digits_typography_typography`+GROUPE typo, `label_typography_typography`+GROUPE typo, `text_stroke_text_stroke_type`+GROUPE text_stroke, `digits_color`:color, `digits_text_shadow_text_shadow_type`, `digits_text_shadow_text_shadow`:text_shadow, `label_color`:color, `label_text_shadow_text_shadow_type`, `label_text_shadow_text_shadow`:text_shadow
- section_expire_message_style : `typography_typography`+GROUPE typo, `align`(start|center|end), `text_color`:color, `message_text_shadow_text_shadow_type`, `message_text_shadow_text_shadow`:text_shadow, `message_padding`:dim{t,r,b,l,unit,isLinked}
