# Contrôles communs à (quasi) tous les widgets Elementor + formats de valeurs

Référence générée/vérifiée sur Elementor 4.2. Une clé inconnue est **ignorée en silence**
(pas d'erreur) : toujours copier les clés d'ici ou du fichier du widget, jamais les deviner.

## Formats de valeurs (partout)

| Type | Format PHP |
|---|---|
| slider | `['unit'=>'px','size'=>36]` (unit: px/%/em/rem/vw/custom) |
| dimensions | `['unit'=>'px','top'=>'8','right'=>'16','bottom'=>'8','left'=>'16','isLinked'=>false]` |
| couleur | `'#0B3550'` ou `'rgba(0,0,0,.5)'` |
| media | `['id'=>123,'url'=>'https://…']` (objet unique, PAS un tableau) |
| icons | `['value'=>'fas fa-check','library'=>'fa-solid']` ou SVG : `['value'=>['id'=>ID,'url'=>URL],'library'=>'svg']` |
| url | `['url'=>'/page/','is_external'=>'','nofollow'=>'','custom_attributes'=>'']` |
| switcher | `'yes'` ou `''` |
| repeater | tableau d'items, chaque item = `['_id'=>uid7(), …champs…]` |
| gallery | `[['id'=>1,'url'=>…], …]` |
| responsive | même clé + suffixe `_tablet` / `_mobile` (parfois `_widescreen`, `_laptop`…) |
| globals | `'__globals__' => ['title_color'=>'globals/colors?id=primary']` ; chaîne vide pour DÉBRANCHER le global et laisser la valeur locale gagner |

## Groupes de contrôles (notés `x`+GROUPE dans les fichiers widgets)

Un groupe = un **activateur** + des sous-clés partageant son préfixe. Sans l'activateur,
RIEN n'est rendu. `{p}` = le stem indiqué dans le fichier du widget
(ex. `title_typography_typography` → `{p}` = `title_typography`).

- **GROUPE typo** — activateur `{p}_typography => 'custom'` puis `{p}_font_family`,
  `{p}_font_size` (slider), `{p}_font_weight` ('100'…'900'), `{p}_text_transform`,
  `{p}_font_style`, `{p}_text_decoration`, `{p}_line_height` (slider, unit 'em' ou 'px'),
  `{p}_letter_spacing`, `{p}_word_spacing`.
- **GROUPE bordure** — activateur `{p}_border => 'solid'|'dashed'|'dotted'|'double'` puis
  `{p}_width` (dimensions), `{p}_color`.
- **GROUPE background** — activateur `{p}_background => 'classic'|'gradient'` puis
  `{p}_color`, `{p}_image` (media), `{p}_position`, `{p}_repeat`, `{p}_size` ;
  gradient : `{p}_color_b`, `{p}_color_stop`, `{p}_color_b_stop`, `{p}_gradient_type`,
  `{p}_gradient_angle`. (Sous-clés vidéo/diaporama existent aussi : `{p}_video_link`,
  `{p}_slideshow_gallery`… — rarement utiles par script.)
- **GROUPE box_shadow** — activateur `{p}_box_shadow_type => 'yes'` puis `{p}_box_shadow =>
  ['horizontal'=>0,'vertical'=>8,'blur'=>24,'spread'=>0,'color'=>'rgba(…)']` et
  `{p}_box_shadow_position => ''|'inset'`.
- **GROUPE text_shadow** — activateur `{p}_text_shadow_type => 'yes'` puis `{p}_text_shadow =>
  ['horizontal'=>…,'vertical'=>…,'blur'=>…,'color'=>…]`.
- **GROUPE text_stroke** — activateur `{p}_text_stroke_type` puis `{p}_text_stroke` (slider),
  `{p}_stroke_color`.

## Onglet Avancé (préfixe `_`) — présent sur TOUS les widgets

- Layout : `_margin`, `_padding` (dimensions) ; `_element_width => ''|'auto'|'initial'` +
  `_element_custom_width` (slider) ; `_flex_size`, `_align_self`, `_order` (dans un parent flex) ;
  `_element_vertical_align`.
- Position : `_position => ''|'absolute'|'fixed'` + `_offset_x`/`_offset_y` (slider),
  `_offset_orientation_h => 'start'|'end'`, `_offset_orientation_v` ; `_z_index`.
- Identité : `_element_id` (id CSS), `_css_classes` (classes, séparées par espaces),
  `_attributes` (attributs custom `key|value`, un par ligne), `_element_cache`.
- Fond/bordure du widget : mêmes groupes que ci-dessus avec `{p}` = `_background`,
  `_background_hover`, `_border`, `_border_hover` (+ `_border_radius` dimensions,
  `_box_shadow…`, `_box_shadow_hover…`) ; `_border_hover_transition` (slider, secondes).
- Masque : `_mask_switch => 'yes'` + `_mask_shape`, `_mask_size`, `_mask_position`.
- Transform (normal et hover) : activateurs `_transform_translate_popover[(_hover)] => 'transform'`,
  `_transform_rotate_popover…`, `_transform_scale_popover…`, `_transform_skew_popover…` puis
  `_transform_translateX_effect[_hover]`, `_transform_translateY_effect[_hover]`,
  `_transform_rotateZ_effect…`, `_transform_scale_effect…` (sliders) ;
  `_transform_transition_hover` (durée en **millisecondes** malgré unit 'px').
- Visibilité responsive : `hide_desktop`/`hide_tablet`/`hide_mobile => 'hidden-desktop'|'yes'`.
- Animation d'entrée : `_animation` (ex. 'fadeInUp'), `_animation_delay`, `animation_duration
  => 'slow'|''|'fast'`.
- Motion effects (Pro) : `motion_fx_motion_fx_scrolling => 'yes'` + familles
  `motion_fx_translateY_*`, `motion_fx_opacity_*`, `motion_fx_blur_*`, `motion_fx_rotateZ_*`,
  `motion_fx_scale_*` (chacune : `_effect => 'yes'`, `_direction`, `_speed`/`_level`, `_range`) ;
  souris : `motion_fx_motion_fx_mouse => 'yes'` + `motion_fx_mouseTrack_*`, `motion_fx_tilt_*`.
- Sticky (Pro) : `sticky => 'top'|'bottom'`, `sticky_on => ['desktop','tablet','mobile']`,
  `sticky_offset`, `sticky_effects_offset`, `sticky_parent => 'yes'`.
- CSS custom (Pro) : `custom_css` (mot-clé `selector` = l'élément).

## Conteneurs (rappels — détail dans SKILL.md)

Clés SANS underscore : `css_classes`, `padding`, `margin`, `background_background`…
Flex : `flex_direction`, `flex_justify_content`, `flex_align_items`, `flex_gap
{column,row,unit}`, `flex_wrap`. Grid : `grid_columns_grid {unit:'fr',size:N}`, `grid_gap`.
Largeur d'une colonne : `width {unit:'%',size:N}` (+ `_tablet`/`_mobile`).
