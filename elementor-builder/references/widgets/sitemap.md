# `sitemap` — Plan de site (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- sitemap_section : `sitemap_items`:repeater[], `sitemap_columns`(1|2|3|4|5|6)[=4], `sitemap_title_tag`(h1|h2|h3|h4|h5|h6|div|span|p)[=h2], `sitemap_add_nofollow`:'yes'
- sitemap_query_section : `sitemap_exclude`(current_post|manual_selection), `sitemap_exclude_ids`, `sitemap_password_protected`:'yes'

## onglet style
- section_sitemap_style : `sitemap_title_typography_typography`+GROUPE typo, `sitemap_list_item_typography_typography`+GROUPE typo, `sitemap_list_indent`:slider{unit,size}, `sitemap_section_padding`:dim{t,r,b,l,unit,isLinked}, `sitemap_title_color`:color, `sitemap_list_item_color`:color, `sitemap_bullet_color`:color, `sitemap_list_item_bullet_style`(disc|circle|square|none)[=disc]
