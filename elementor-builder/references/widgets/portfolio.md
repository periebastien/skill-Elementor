# `portfolio` — Portfolio (Pro)

`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.

## onglet content
- section_layout : `columns`(1|2|3|4|5|6)[=3], `posts_per_page`:nb[=6], `thumbnail_size_size`(thumbnail|medium|medium_large|large|1536x1536|2048x2048|woocommerce_thumbnail|woocommerce_single|woocommerce_gallery_thumbnail|full)[=medium], `masonry`:'yes', `item_ratio`:slider{unit,size}, `show_title`:'yes'[=yes], `title_tag`(h1|h2|h3|h4|h5|h6|div|span|p)[=h3]
- section_query : `posts_post_type`(post|page|product|by_id|current_query|related)[=post], `posts_query_args`, `posts_posts_ids`, `posts_include`(terms|authors), `posts_include_term_ids`, `posts_related_taxonomies`(category|post_tag|post_format|product_brand|product_type|product_visibility|product_cat|product_tag|product_shipping_class|pos_product_visibility), `posts_include_authors`, `posts_exclude`(current_post|manual_selection|terms|authors), `posts_exclude_ids`, `posts_exclude_term_ids`, `posts_exclude_authors`, `posts_avoid_duplicates`:'yes', `posts_offset`:nb[=0], `posts_related_fallback`(fallback_none|fallback_by_id|fallback_recent)[=fallback_none], `posts_fallback_ids`, `posts_select_date`(anytime|today|week|month|quarter|year|exact)[=anytime], `posts_date_before`:datetime, `posts_date_after`:datetime, `posts_orderby`(post_date|post_title|menu_order|modified|comment_count|rand)[=post_date], `posts_order`(asc|desc)[=desc], `posts_ignore_sticky_posts`:'yes'[=yes], `posts_query_id`:txt
- filter_bar : `show_filter_bar`:'yes', `taxonomy`(|category|post_tag|product_brand|product_cat|product_tag)

## onglet style
- section_design_layout : `item_gap`:slider{unit,size}, `column_gap`:slider{unit,size}, `row_gap`:slider{unit,size}, `border_radius`:dim{t,r,b,l,unit,isLinked}
- section_design_overlay : `typography_title_typography`+GROUPE typo, `color_background`:color, `color_title`:color
- section_design_filter : `typography_filter_typography`+GROUPE typo, `color_filter`:color, `color_filter_active`:color, `filter_item_spacing`:slider{unit,size}, `filter_spacing`:slider{unit,size}
