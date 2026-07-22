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
   avec l'ID d'attachment WordPress d'un SVG déjà importé en médiathèque (`wp media import`).
   Pour une icône de la bibliothèque Font Awesome fournie par Elementor :
   `selected_icon => ['value' => 'fas fa-arrow-right', 'library' => 'fa-solid']`.
9. **Heading** : `title` accepte du HTML inline (`<em>`), `header_size` = h1…h6,
   `title_color`, `align` ('left'|'center').
10. **Button** : `text`, `link => ['url'=>..,'is_external'=>''], 'button_text_color',
    `background_color` (+ activateur non requis pour button), `border_radius`,
    `text_padding`, hover : `button_background_hover_color`.

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

## Tokens design (à adapter par projet)

Renseigner ici les couleurs, la police et les rayons/espacements du design system du
projet en cours (souvent disponibles dans un fichier `colors_and_type.css` ou équivalent
si le projet vient de Claude Design), pour que les widgets générés reprennent les bonnes
valeurs sans avoir à les redemander à chaque page. Exemple de structure :

- Couleurs primaire/accent/CTA (+ variantes hover)
- Couleur d'encre (texte principal) et texte secondaire/muted
- Police(s) et graisses disponibles
- Rayons de bordure et espacements de section standards
- Largeur max de conteneur (`content_width`)
