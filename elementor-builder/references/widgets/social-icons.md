# `social-icons` — Icônes réseaux sociaux (core)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_social_icon : `social_icon_list`:repeater[], `shape`(square|rounded|circle)[=rounded], `columns`(0|1|2|3|4|5|6)[=0], `align`(left|center|right)[=center]

## onglet style
- section_social_style : `image_border_border`+GROUPE bordure, `icon_color`(default|custom)[=default], `icon_primary_color`:color, `icon_secondary_color`:color, `icon_size`:slider{unit,size}, `icon_padding`:slider{unit,size}, `icon_spacing`:slider{unit,size}, `row_gap`:slider{unit,size}, `border_radius`:dim{t,r,b,l,unit,isLinked}
- section_social_hover : `hover_primary_color`:color, `hover_secondary_color`:color, `hover_border_color`:color, `hover_animation`
