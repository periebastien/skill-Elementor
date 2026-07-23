# `form` — Formulaire (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_form_fields : `form_name`:txt, `form_fields`, `input_size`(xs|sm|md|lg|xl)[=sm], `show_labels`:'yes'[=true], `mark_required`:'yes'
- section_buttons : `button_size`(xs|sm|md|lg|xl)[=sm], `button_width`(|100|80|75|70|66|60|50|40|33|…)[=100], `step_next_label`:txt[=Suivant], `step_previous_label`:txt[=Précédent], `button_text`:txt[=Envoyer], `selected_button_icon`:icons{value,library}, `button_icon_align`(row|row-reverse)[=row], `button_icon_indent`:slider{unit,size}, `button_css_id`:txt
- section_integration : `submit_actions`(save-to-database|email|email2|redirect|webhook|mailchimp|drip|activecampaign|getresponse|convertkit|…)
- section_submissions : `submissions_metadata`(remote_ip|user_agent)
- section_email : `email_to`:txt, `email_subject`:txt, `email_content`:txt[=[all-fields]], `email_from`:txt, `email_from_name`:txt[=revision], `email_reply_to`(), `email_to_cc`:txt, `email_to_bcc`:txt, `form_metadata`(date|time|page_url|user_agent|remote_ip|credit), `email_content_type`(html|plain)[=html]
- section_email_2 : `email_to_2`:txt, `email_subject_2`:txt, `email_content_2`:txt[=[all-fields]], `email_from_2`:txt, `email_from_name_2`:txt[=revision], `email_reply_to_2`(), `email_to_cc_2`:txt, `email_to_bcc_2`:txt, `form_metadata_2`(date|time|page_url|user_agent|remote_ip|credit), `email_content_type_2`(html|plain)[=html]
- section_redirect : `redirect_to`:txt
- section_webhook : `webhooks`:txt, `webhooks_advanced_data`:'yes'[=no]
- section_mailchimp : `mailchimp_api_key_source`(default|custom)[=default], `mailchimp_api_key`:txt, `mailchimp_list`, `mailchimp_groups`, `mailchimp_tags`:txt, `mailchimp_double_opt_in`:'yes', `mailchimp_fields_map`
- section_drip : `drip_api_token_source`(default|custom)[=default], `drip_custom_api_token`:txt, `drip_account`, `drip_fields_map`, `drip_custom_fields`:'yes'[=no], `tags`:txt
- section_activecampaign : `activecampaign_api_credentials_source`(default|custom)[=default], `activecampaign_api_key`:txt, `activecampaign_api_url`:txt, `activecampaign_list`, `activecampaign_fields_map`, `activecampaign_tags`:txt
- section_getresponse : `getresponse_api_key_source`(default|custom)[=default], `getresponse_custom_api_key`:txt, `getresponse_list`, `getresponse_dayofcycle`:nb, `getresponse_fields_map`
- section_convertkit : `convertkit_api_key_source`(default|custom)[=default], `convertkit_custom_api_key`:txt, `convertkit_form`, `convertkit_fields_map`, `convertkit_tags`
- section_mailerlite : `mailerlite_api_key_source`(default|custom)[=default], `mailerlite_custom_api_key`:txt, `mailerlite_group`, `mailerlite_fields_map`, `allow_resubscribe`:'yes'
- section_slack : `slack_webhook`:txt, `slack_channel`:txt, `slack_username`:txt, `slack_pretext`:txt, `slack_title`:txt, `slack_text`:txt, `slack_add_fields`:'yes'[=yes], `slack_add_ts`:'yes'[=yes], `slack_webhook_color`:color[=#D30C5C]
- section_discord : `discord_webhook`:txt, `discord_username`:txt, `discord_avatar_url`:txt, `discord_title`:txt, `discord_content`:txt, `discord_form_data`:'yes'[=yes], `discord_ts`:'yes'[=yes], `discord_webhook_color`:color[=#D30C5C]
- section_popup : `popup_action`(|open|close), `popup_action_popup_id`, `popup_action_do_not_show_again`:'yes'
- section_steps_settings : `step_type`(none|text|icon|number|progress_bar|number_text|icon_text)[=number_text], `step_icon_shape`(circle|square|rounded|none)[=circle]
- section_form_options : `form_id`:txt, `form_validation`(|custom), `custom_messages`:'yes', `success_message`:txt, `error_message`:txt, `server_message`:txt, `invalid_message`:txt, `required_field_message`:txt

## onglet style
- section_form_style : `label_typography_typography`+GROUPE typo, `html_typography_typography`+GROUPE typo, `column_gap`:slider{unit,size}, `row_gap`:slider{unit,size}, `label_spacing`:slider{unit,size}, `label_color`:color, `mark_required_color`:color, `html_spacing`:slider{unit,size}, `html_color`:color
- section_field_style : `field_typography_typography`+GROUPE typo, `field_text_color`:color, `field_background_color`:color[=#ffffff], `field_border_color`:color, `field_border_width`:dim{t,r,b,l,unit,isLinked}, `field_border_radius`:dim{t,r,b,l,unit,isLinked}
- section_button_style : `button_typography_typography`+GROUPE typo, `button_border_border`+GROUPE bordure, `button_align`(start|center|end|stretch)[=stretch], `button_content_align`(start|center|end|space-between), `tabs_button_style`, `button_background_color`:color, `button_text_color`:color[=#ffffff], `previous_button_background_color`:color, `previous_button_text_color`:color[=#ffffff], `previous_button_border_color`:color, `button_background_hover_color`:color, `button_hover_color`:color[=#ffffff], `button_hover_border_color`:color, `previous_button_background_color_hover`:color, `previous_button_text_color_hover`:color[=#ffffff], `previous_button_border_color_hover`:color, `hover_transition_duration`:slider{unit,size}, `button_hover_animation`, `button_border_radius`:dim{t,r,b,l,unit,isLinked}, `button_text_padding`:dim{t,r,b,l,unit,isLinked}
- section_messages_style : `message_typography_typography`+GROUPE typo, `success_message_color`:color, `error_message_color`:color, `inline_message_color`:color
- section_steps_style : `steps_typography_typography`+GROUPE typo, `step_progress_bar_percentage__typography_typography`+GROUPE typo, `steps_gap`:slider{unit,size}, `steps_icon_size`:slider{unit,size}, `steps_padding`:slider{unit,size}, `steps_state`, `step_inactive_primary_color`:color, `step_inactive_secondary_color`:color[=#ffffff], `step_active_primary_color`:color, `step_active_secondary_color`:color[=#ffffff], `step_completed_primary_color`:color, `step_completed_secondary_color`:color[=#ffffff], `step_divider_width`:slider{unit,size}, `step_divider_gap`:slider{unit,size}, `step_progress_bar_color`:color, `step_progress_bar_background_color`:color, `step_progress_bar_height`:slider{unit,size}, `step_progress_bar_border_radius`:slider{unit,size}, `step_progress_bar_percentage_color`:color
