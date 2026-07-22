---
name: elementor-builder
description: Construire/modifier des pages Elementor avec des widgets NATIFS via WP-CLI (générer _elementor_data), adapté du projet msrbuilds/elementor-mcp pour un usage direct sans plugin MCP.
---

# Construire des pages Elementor en widgets natifs (via WP-CLI)

Contexte : ce site tourne Elementor 4.x avec l'expérience **containers active** (flex/grid).
On ne passe PAS par le plugin elementor-mcp : on génère le JSON `_elementor_data` dans un
script PHP exécuté par `wp eval-file`. Règle d'or : **widgets natifs d'abord**, le widget
`html` est un dernier recours pour un micro-détail impossible nativement.

## Structure des éléments

```php
// Conteneur (flex par défaut)
[ 'id' => uid7(), 'elType' => 'container', 'isInner' => false,
  'settings' => [ 'container_type' => 'flex', 'content_width' => 'boxed', ... ],
  'elements' => [ ...enfants... ] ]

// Widget
[ 'id' => uid7(), 'elType' => 'widget', 'widgetType' => 'heading',
  'isInner' => false, 'settings' => [...], 'elements' => [] ]
```
`id` = 7 caractères hex aléatoires. `content_width`: 'boxed' | 'full'.

## Pièges connus (issus d'elementor-mcp)

1. **Clés flex préfixées** : utiliser `flex_direction`, `flex_justify_content`,
   `flex_align_items`, `flex_align_content`, `flex_gap` (`{'column':'20','row':'20','unit':'px'}`).
   Les clés non préfixées (`justify_content`…) sont IGNORÉES par le générateur CSS.
2. **Activateur de fond** : un `background_color`/`background_image` sans
   `background_background => 'classic'` n'est jamais rendu.
3. **`background_image`** : objet unique `{ 'id' => 123, 'url' => '...' }`, pas un tableau.
4. **Grid** : `container_type => 'grid'`, `grid_columns_grid => ['unit'=>'fr','size'=>4]`,
   `grid_gap => ['column'=>'20','row'=>'20','unit'=>'px']`, responsive via suffixes
   `_tablet` / `_mobile` (ex. `grid_columns_grid_tablet`).
5. **Typographie widget** : activer avec `typography_typography => 'custom'` puis
   `typography_font_family`, `typography_font_size => ['unit'=>'px','size'=>36]`,
   `typography_font_weight => '900'`, `typography_line_height`, `typography_letter_spacing`.
   Préfixe selon le contrôle : `title_typography_*` (icon-box), `typography_*` (heading).
6. **Advanced tab** : préfixe `_` → `_padding`, `_margin`, `_border_radius`,
   `_background_background`/`_background_color`, `_element_width => 'initial'` +
   `_element_custom_width`, `_position => 'absolute'` + `_offset_x/_offset_y`
   (+ `_offset_orientation_h => 'end'` pour ancrer à droite).
7. **Dimensions** : `['unit'=>'px','top'=>..,'right'=>..,'bottom'=>..,'left'=>..,'isLinked'=>false]`.
8. **Icônes SVG** : `selected_icon => ['value' => ['id'=>ID,'url'=>URL], 'library'=>'svg']`
   (les SVG du design system sont déjà en médiathèque, IDs 814-841, 887-898).
9. **Heading** : `title` accepte du HTML inline (`<em>`), `header_size` = h1…h6,
   `title_color`, `align` ('left'|'center').
10. **Button** : `text`, `link => ['url'=>..,'is_external'=>''], 'button_text_color',
    `background_color` (+ activateur non requis pour button), `border_radius`,
    `text_padding`, hover : `button_background_hover_color`.

## Espacements : TOUJOURS définir les gaps explicitement

Un conteneur flex ou grid sans `flex_gap`/`grid_gap` hérite du défaut Elementor
(20px colonnes / 20px lignes), ce qui fausse silencieusement la fidélité à la maquette.
Règle :

- **Toujours** poser `flex_gap` (flex) ou `grid_gap` (grid) sur chaque conteneur créé,
  même quand la valeur voulue est zéro.
- Par défaut, mettre le gap à **0/0** et contrôler les espacements par des **marges sur
  les widgets** (`_margin`), qui traduisent directement les valeurs de la maquette
  (ex. `margin-bottom: 20px` sous un titre). Le gap uniforme ne convient que quand la
  maquette espace réellement tous les enfants de la même valeur (grilles de cartes).

```php
'flex_gap' => [ 'column' => '0', 'row' => '0', 'unit' => 'px' ],   // flex
'grid_gap' => [ 'column' => '20', 'row' => '20', 'unit' => 'px' ], // grid : reprendre le gap réel de la maquette
```

## Éléments ronds (pastilles, avatars) : verrouiller largeur ET hauteur

`border-radius: 50%` ne donne un cercle que si largeur == hauteur. Un widget avec
largeur fixe (`_element_custom_width`) mais hauteur automatique devient une **ellipse**.
Pour un cercle de N px sur un heading/texte : soit fixer aussi la hauteur, soit calculer
le padding vertical → `padding_v = (N - hauteur_texte - bordure_totale) / 2`
(ex. cercle 56, texte 18px line-height 1, bordure 2+2 : `(56 - 18 - 4) / 2 = 17px`).

## Positionner un pseudo-élément par offset px : gare au padding par défaut (10px)

Les conteneurs Elementor (`.e-con`) ont un **padding par défaut de 10px sur les 4 côtés**
(`--container-default-padding-*`). Un `::after` positionné en absolu se réfère à la
**padding-box** du conteneur relatif : `top:0` = bord intérieur de la bordure, mais les
enfants en flux normal commencent APRÈS le padding-top. Donc un offset `top` calculé
« au centre du premier enfant » est faux de la valeur du padding-top (souvent 10px) si on
ne la neutralise pas.

Règle pour une ligne/connecteur centré sur un élément :
`top = padding-top du conteneur + (hauteur de l'élément cible / 2)`.
Le plus simple et déterministe : **forcer explicitement le padding-bloc du conteneur à 0**
(clé `padding`), puis `top = hauteur_cible / 2`. Sinon, prévoir toujours l'offset du
padding par défaut. Toujours vérifier dans le CSS généré (`--padding-top`) après coup.

## Classes CSS personnalisées et niveaux de CSS

- **Classe sur un widget** : clé `_css_classes` (AVEC underscore) — champ Avancé →
  Classes CSS de l'éditeur. Sur un **conteneur** : clé `css_classes` (SANS underscore).
  Méthode privilégiée pour créer des composants réutilisables : poser une classe sur le
  widget porteur (ex. la pastille d'un stepper) et styler via CSS global.
- **Trois niveaux de CSS personnalisé** (Elementor Pro) :
  1. **Élément** : settings `custom_css` (mot-clé `selector`) — portée : cet élément seul.
  2. **Page** : `_elementor_page_settings['custom_css']` de la page — portée : la page.
  3. **Site** : `_elementor_page_settings['custom_css']` du **kit actif**
     (`wp option get elementor_active_kit`) — portée : tout le site. À privilégier pour les
     classes réutilisables ; baliser chaque bloc d'un commentaire marqueur pour pouvoir le
     remplacer par script sans écraser le reste.
- **Pseudo-éléments** (`::before`/`::after`) : impossibles via les réglages natifs → CSS
  personnalisé. Pour styler le parent d'un widget porteur de classe : `:has()`
  (ex. `.e-con:has(> .elementor-widget-heading.ma-classe)::after{...}`).

## ⚠️ Éditeur Elementor ouvert = patchs perdus

Si l'utilisateur a l'éditeur Elementor ouvert sur la page pendant un patch en base,
sa prochaine sauvegarde réécrit tout le `_elementor_data` avec l'état chargé AVANT le
patch : les modifications sont silencieusement perdues. Toujours demander la fermeture
de l'éditeur avant de patcher, et revérifier les clés après coup si un doute existe.

## Effets au survol (hover) — onglet Avancé, applicables à quasi tous les widgets

Clés vérifiées en inspectant le JSON produit par l'éditeur Elementor (préfixe `_`,
suffixe `_hover`). Trois mécanismes combinables :

```php
// 1. Transform (ex. translation verticale au survol)
'_transform_translate_popover'       => 'transform',   // activateur état normal
'_transform_translate_popover_hover' => 'transform',   // activateur état hover (OBLIGATOIRE)
'_transform_translateX_effect_hover' => [ 'unit' => 'px', 'size' => 0,  'sizes' => [] ],
'_transform_translateY_effect_hover' => [ 'unit' => 'px', 'size' => -1, 'sizes' => [] ],
'_transform_transition_hover'        => [ 'unit' => 'px', 'size' => 200, 'sizes' => [] ], // durée en MS malgré unit px

// 2. Bordure au survol
'_border_hover_border' => 'solid',
'_border_hover_width'  => [ 'unit' => 'px', 'top' => '1', 'right' => '1', 'bottom' => '1', 'left' => '1', 'isLinked' => true ],
'_border_hover_color'  => '#20C4C3',
'__globals__'          => [ '_border_hover_color' => '' ], // vide le global éventuel qui écraserait la couleur locale

// 3. Ombre portée au survol
'_box_shadow_hover_box_shadow_type' => 'yes',   // activateur
'_box_shadow_hover_box_shadow'      => [ 'horizontal' => 0, 'vertical' => 0, 'blur' => 70, 'spread' => -23, 'color' => 'rgba(32,196,195,0.22)' ],
```

Pièges : chaque mécanisme a son **activateur** (`_popover_hover => 'transform'`,
`_box_shadow_type => 'yes'`, `_border_hover_border => 'solid'`) sans lequel rien n'est rendu ;
la durée de transition transform s'exprime en millisecondes bien que `unit` soit `px` ;
poser aussi l'activateur transform de l'état normal pour une transition aller-retour fluide.

## Modifier une page existante sans l'écraser

Ne JAMAIS regénérer entièrement une page qui a pu être retouchée à la main dans
l'éditeur : décoder le `_elementor_data` existant, parcourir récursivement les
`elements`, cibler les widgets par `widgetType` + un champ discriminant
(`text`, `title_text`…), fusionner les settings (`array_merge`), ré-encoder, sauver,
purger le cache. Toujours faire une sauvegarde BDD avant.

## Theme Builder (header/footer) : conditions d'affichage

- Template Elementor Pro : `_elementor_template_type` = `header`/`footer`, condition dans
  `_elementor_conditions` (tableau de chaînes : `include/general`, `include/singular/page/{id}`,
  `exclude/singular/page/{id}`…).
- **Ne pas se fier au départage automatique** entre un `include/general` et un `include`
  plus spécifique : pour garantir qu'un template spécifique (ex. footer d'une section)
  reste seul sur sa cible, ajouter un **`exclude` explicite** sur le template général,
  miroir de la condition du template spécifique
  (`[ 'include/general', 'exclude/singular/page/14' ]`).
- Après modif : régénérer le cache
  `\ElementorPro\Plugin::instance()->modules_manager->get_modules('theme-builder')->get_conditions_manager()->get_cache()->regenerate();`
  puis vider le cache fichiers.
- **Vérifier** via l'option `elementor_pro_theme_builder_conditions` (map location→template→conditions),
  PAS via `is_page()` en WP-CLI (le contexte frontend n'existe pas en CLI, la résolution runtime est faussée).

## Sauvegarde (obligatoire dans cet ordre)

```php
update_post_meta( $id, '_elementor_data', wp_slash( wp_json_encode( $data ) ) );
update_post_meta( $id, '_elementor_edit_mode', 'builder' );
update_post_meta( $id, '_elementor_template_type', 'wp-page' );
update_post_meta( $id, '_elementor_version', ELEMENTOR_VERSION );
update_post_meta( $id, '_wp_page_template', 'elementor_header_footer' ); // ou 'elementor_canvas'
\Elementor\Plugin::$instance->files_manager->clear_cache(); // régénère le CSS
```

## Vérification après build

- `wp post meta get <ID> _elementor_data | python3 -m json.tool > /dev/null` (JSON valide)
- `curl -sk <url> | grep` un texte attendu + vérifier qu'aucun widget ne rend vide
- Ouvrir la page dans l'éditeur Elementor : si le JSON est invalide, l'éditeur affiche une page blanche — c'est le signal d'un settings mal formé.

## Design system Altitude Révision (tokens)

Jaune CTA `#ffbd20` (hover `#e0a800`) · Teal `#20c4c3` (dark `#189998`, light `#d0f4f4`)
· Encre `#1a1a1a`/`#292728` · Texte secondaire `#555`/`#666` · Police **Nunito**
(400-900) · Radius 8-20px · Sections py 96px · max-width 1280px.
Référence complète : projet Claude Design "Altitude Révision Design System",
fichier `colors_and_type.css`.
