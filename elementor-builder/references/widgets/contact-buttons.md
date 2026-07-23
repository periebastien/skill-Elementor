# `contact-buttons` — Discussion unique (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- chat_button_section : `chat_aria_label`:txt[=Élément flottant], `chat_button_platform`(WhatsApp|Messenger|Email|SMS|VIBER|Skype)[=WhatsApp], `chat_button_mail`:txt, `chat_button_mail_subject`:txt, `chat_button_mail_body`:txt, `chat_button_number`:txt, `chat_button_username`:txt, `chat_button_viber_action`(chat|contact)[=chat], `chat_button_waze`:url{url,is_external}, `chat_button_url`:url{url,is_external}, `chat_button_show_dot`:'yes'[=yes]
- top_bar_section : `top_bar_title`:txt[=Robert Dupont], `top_bar_subtitle`:txt, `top_bar_image`:media{id,url}, `top_bar_show_dot`:'yes'[=yes]
- message_bubble_section : `message_bubble_name`:txt[=Robert], `message_bubble_body`:txt, `chat_button_time_format`(12h|24h)[=12h], `chat_button_show_animation`:'yes'[=yes]
- send_button_section : `send_button_text`:txt

## onglet style
- style_chat_button : `style_chat_button_box_shadow_box_shadow_type`+GROUPE box_shadow, `style_chat_button_size`(small|medium|large)[=small], `style_button_color_tabs`, `style_button_color_select`(default|custom)[=default], `style_button_color_icon`:color, `style_button_color_background`:color, `style_button_color_select_hover`(default|custom)[=default], `style_button_color_icon_hover`:color, `style_button_color_background_hover`:color, `style_button_color_hover_animation`[=grow], `style_chat_button_animation`, `style_chat_button_animation_duration`(slow|normal|fast)[=normal], `style_chat_button_animation_delay`:nb
- style_top_bar_section : `style_top_bar_title_typography_typography`+GROUPE typo, `style_top_bar_subtitle_typography_typography`+GROUPE typo, `style_top_bar_image_size`(small|medium|large)[=medium], `style_top_bar_colors`(default|custom)[=default], `style_top_bar_title_color`:color, `style_top_bar_subtitle_color`:color, `style_top_bar_close_button_color`:color, `style_top_bar_background_color`:color
- style_bubble_section : `style_bubble_name_typography_typography`+GROUPE typo, `style_bubble_message_typography_typography`+GROUPE typo, `style_bubble_time_typography_typography`+GROUPE typo, `style_bubble_colors`(default|custom)[=default], `style_bubble_name_color`:color, `style_bubble_message_color`:color, `style_bubble_time_color`:color, `style_bubble_background_color`:color, `style_bubble_chat_color`:color
- style_send_section : `style_send_typography_typography`+GROUPE typo, `style_send_tabs`, `style_send_normal_colors`(default|custom)[=default], `style_send_normal_icon_color`:color, `style_send_normal_background_color`:color, `style_send_hover_colors`(default|custom)[=default], `style_send_hover_icon_color`:color, `style_send_hover_background_color`:color, `style_send_hover_animation`[=grow], `style_chat_button_padding`:dim{t,r,b,l,unit,isLinked}
- style_chat_box_section : `style_chat_box_box_shadow_box_shadow_type`+GROUPE box_shadow, `style_chat_box_bg_select`(default|custom)[=default], `style_chat_box_bg_color`:color, `style_chat_box_width`:slider{unit,size}, `style_chat_box_corners`(round|rounded|sharp)[=rounded], `style_chat_box_entrance_animation`, `style_chat_box_exit_animation`, `style_chat_box_animation_duration`(slow|normal|fast)[=normal]

## onglet advanced-tab-floating-buttons
- advanced_layout_section : `advanced_horizontal_position`(start|center|end)[=end], `advanced_horizontal_offset`:slider{unit,size}, `advanced_vertical_position`(top|middle|bottom)[=bottom], `advanced_vertical_offset`:slider{unit,size}
- advanced_custom_controls_section : `advanced_custom_css_id`:txt, `advanced_custom_css_classes`:txt
