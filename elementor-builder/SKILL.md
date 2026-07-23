---
name: elementor-builder
description: Intégrer une maquette / un design en pages Elementor avec des widgets NATIFS, en générant _elementor_data par script WP-CLI, sur n'importe quel site WordPress. Utiliser dès qu'il faut créer ou modifier une page, un header ou un footer Elementor autrement qu'à la main dans l'éditeur.
---

# Intégrer un design en widgets Elementor natifs (via WP-CLI)

**Objectif unique de cette skill** : traduire une maquette en pages Elementor composées de
widgets natifs, par script. Elle est **générique** — aucun site, thème ou design system
particulier n'y est supposé. Toute donnée propre à un projet (IDs de médias, tokens de
couleurs, IDs de pages, chemins, identifiants d'accès) reste dans le projet, jamais ici.

Prérequis : Elementor avec l'expérience **containers** active (flex/grid) — le défaut
depuis Elementor 3.16. On ne passe PAS par un plugin MCP : on génère le JSON
`_elementor_data` dans un script PHP exécuté par `wp eval-file`.

Règle d'or : **widgets natifs d'abord**, le widget `html` est un dernier recours pour un
micro-détail impossible nativement.

## Au démarrage sur un projet

1. Relever la version d'Elementor et la présence d'Elementor **Pro**
   (`wp plugin list --status=active | grep elementor`) : le CSS personnalisé par
   élément/page/site et le Theme Builder sont des fonctions Pro.
2. **Sauvegarder la base** avant tout patch (`wp db export`).
3. Récupérer les tokens du design (couleurs, polices, rayons, rythme vertical) et les
   médias déjà en médiathèque depuis les sources du projet — les noter dans le contexte
   du projet (CLAUDE.md / mémoire), pas dans cette skill.

## Référentiel des widgets et de leurs contrôles (dossier `references/`)

Une clé de settings inconnue est **ignorée en silence** par Elementor — ne jamais deviner
un nom de contrôle. Consulter, dans cet ordre et **à la demande seulement** (ne pas tout
charger) :

1. `references/widgets-index.md` — liste 1-ligne de tous les widgets core + Pro : choisir
   le bon `widgetType`.
2. `references/widgets/<nom>.md` — contrôles spécifiques du widget qu'on va utiliser
   (onglets content/style, options des selects, défauts). Charger uniquement ceux-là.
3. `references/common-controls.md` — formats de valeurs (slider, dimensions, media, icons…),
   groupes de contrôles (typo, bordure, background, ombres : activateur + sous-clés) et
   onglet Avancé `_*` communs à tous les widgets.

Ces fichiers sont générés depuis Elementor 4.2.0 / Pro 4.2.0. Sur un site avec une autre
version, ils restent une bonne approximation ; pour les régénérer exactement :
`wp eval-file tools/extract-widgets.php /tmp/dump.json` puis
`python3 tools/generate-widget-refs.py /tmp/dump.json references/ <version>`.

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
   ⚠️ **Les rangées valent `repeat(2,1fr)` par défaut** (`--e-con-grid-template-rows` dans le
   CSS de base d'Elementor) : une grille d'une seule rangée logique rend une **2e rangée vide
   de même hauteur** (gros blanc fantôme sous les cartes). TOUJOURS poser explicitement
   `grid_rows_grid => ['unit'=>'fr','size'=>N]` (+ `grid_auto_flow => 'row'`).
4bis. **Diagnostiquer le padding d'un conteneur** : la règle qui consomme les variables est
   `.e-con-full, .e-con > .e-con-inner { padding-block-…: var(--padding-…) }`. Sur un
   conteneur **boxed**, le padding s'applique donc à l'`e-con-inner`, PAS à l'élément
   `.e-con` lui-même : `getComputedStyle` sur l'e-con boxed renvoie `padding: 0` alors que
   tout est normal. Ne pas « corriger » ça ; si un blanc anormal apparaît, chercher d'abord
   une rangée de grille vide (piège 4).
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
   où ID/URL sont ceux de la médiathèque du site (les relever avec
   `wp post list --post_type=attachment --post_mime_type=image/svg+xml --fields=ID,post_title,guid`).
   Pour une icône de bibliothèque : `['value' => 'fas fa-check', 'library' => 'fa-solid']`.
9. **Heading** : `title` accepte du HTML inline (`<em>`), `header_size` = h1…h6,
   `title_color`, `align` ('left'|'center').
10. **Button** : `text`, `link => ['url'=>..,'is_external'=>''], 'button_text_color',
    `background_color` (+ activateur non requis pour button), `border_radius`,
    `text_padding`, hover : `button_background_hover_color`.
    - **JAMAIS de caractère spécial en guise d'icône** dans `text` (`↓`, `→`, `✓`… = moche).
      Toujours une vraie icône via `selected_icon` (+ `icon_align => 'row-reverse'` pour la
      placer après le texte, `icon_indent` pour l'espacement). Si l'icône manque en
      médiathèque : créer le SVG depuis les tracés de la maquette (wrapper
      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
      stroke-linecap="round" stroke-linejoin="round">…</svg>` + `wp media import`) ; à défaut,
      poser une icône de bibliothèque proche que l'utilisateur remplacera.
    - **Alignement optique texte/icône** : l'icône SVG est centrée géométriquement, mais un
      libellé **sans lettre descendante** (« Réserver mon contrôle ») paraît trop haut : la
      boîte de ligne réserve l'espace du jambage sous la baseline. Toutes les boîtes ont beau
      être parfaitement centrées au `getBoundingClientRect`, l'œil voit le texte plus haut que
      l'icône. Correctif : classe sur le widget + CSS
      `.ma-classe .elementor-button-text { transform: translateY(1.5px); }` (~ descente/2 à la
      taille utilisée ; 1–2px à 14–15px). Vérifier par capture **zoomée** sur le bouton —
      le décalage est invisible sur une capture pleine page.

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

## Colonnes flex : largeur EXPLICITE en %, jamais en px ni « auto »

Un conteneur imbriqué dans un conteneur flex **retombe en largeur 100 % par défaut** et
s'empile verticalement au lieu de se placer en rangée. Toujours donner à chaque colonne
une largeur **explicite en pourcentage** (jamais en px : le px ne s'adapte pas et casse
la rangée). Pour N colonnes égales → `100/N %` chacune ; ajuster librement si une colonne
doit être plus large (ex. 31 / 23 / 23 / 23 pour un bloc marque + 3 colonnes de liens).

Règles :
- Largeurs desktop qui **somment à 100 %** et `flex_gap` colonne = **0** (le pourcentage
  fait tout le travail). Mixer % + gap px fixe fait déborder et enrouler la rangée.
- Toujours prévoir le responsive : `width_tablet` (souvent 50 %) et `width_mobile` (100 %),
  + `flex_gap` ligne (ex. 40px) pour l'espacement vertical une fois enroulé.
- L'espacement horizontal vient de la largeur du contenu plus étroite que la colonne, ou
  d'un padding interne (border-box : le padding reste dans le %). Vérifier `--width` dans
  le CSS généré après coup.

```php
'width'        => [ 'unit' => '%', 'size' => 23 ],
'width_tablet' => [ 'unit' => '%', 'size' => 50 ],
'width_mobile' => [ 'unit' => '%', 'size' => 100 ],
```

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
'_border_hover_color'  => '#0073AA', // couleur d'accent du projet
'__globals__'          => [ '_border_hover_color' => '' ], // vide le global éventuel qui écraserait la couleur locale

// 3. Ombre portée au survol
'_box_shadow_hover_box_shadow_type' => 'yes',   // activateur
'_box_shadow_hover_box_shadow'      => [ 'horizontal' => 0, 'vertical' => 0, 'blur' => 70, 'spread' => -23, 'color' => 'rgba(0,115,170,0.22)' ],
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

## Vérification après build : TOUJOURS contrôler visuellement

Le `curl`+grep valide le contenu, jamais le rendu. Après chaque build/patch visuel :

1. `wp post meta get <ID> _elementor_data | python3 -m json.tool > /dev/null` (JSON valide)
2. `curl -sk <url> | grep` un texte attendu + vérifier qu'aucun widget ne rend vide
3. **Prendre une capture d'écran** (outil navigateur) et la comparer à la maquette,
   section par section. Les bugs de layout (colonnes qui replient, contenu centré au
   lieu d'aligné, pseudo-éléments qui débordent) sont invisibles dans le HTML.
4. En cas d'anomalie, **inspecter les styles calculés** via le navigateur
   (`getComputedStyle`) sur l'élément fautif plutôt que de deviner : trouver quelle
   règle gagne, puis corriger la bonne cible.
5. Recharger en contournant le cache (le CSS du kit est versionné mais le navigateur
   et le cache d'éléments Elementor peuvent servir l'ancien rendu).
- Ouvrir la page dans l'éditeur Elementor : si le JSON est invalide, l'éditeur affiche
  une page blanche — c'est le signal d'un settings mal formé.

## Pièges de rendu vérifiés (source d'erreurs réelles)

- **`::before`/`::after` sur un conteneur Elementor (`.e-con`) : INTERDIT.** Elementor
  les réserve aux overlays de fond (dimensionnés 100 %×100 %) — un badge posé là devient
  une ellipse géante. Poser le pseudo-élément sur un **widget** enfant (ou son contenu),
  jamais sur le conteneur.
- **Bouton en bas de carte** : `flex-grow:1` sur le widget central (sélecteur
  `.ma-carte > .ma-liste` avec `!important` si le thème/plugin fixe `flex-grow:0`).
- (Les pièges propres à JetEngine — gap de grille, flex centré des dynamic-fields,
  liens à paramètres — sont dans la SECTION JETENGINE.)
- **Widget image = `<img>` étiré à 100 %** : avec `height` (slider) + `object-fit`, l'image
  garde `width:100%` du widget → un logo `contain` flotte centré dans un grand rectangle
  invisible (faux « décalage »). Pour un logo à hauteur fixe : CSS
  `img { width:auto; height:Npx }` via la classe du widget (le contrôle `width` du widget
  ne fait pas ça).
- **Widgets stylés dans l'éditeur par l'utilisateur** : re-lire `_elementor_data` avant
  tout nouveau patch (il a pu changer depuis le dernier build) et patcher
  chirurgicalement le JSON existant, jamais regénérer.

# ── SECTION JETENGINE (Crocoblock) ─────────────────────────────────

Tout ce qui touche aux contenus dynamiques JetEngine dans Elementor. Chaîne complète :
**Query (Query Builder) → Composant Listing (template d'un item) → widget
`jet-listing-grid` (posé dans la page, référence les deux)**.

## Query Builder : inspecter ET créer des queries par script

Les queries ne sont PAS des posts. Stockage : table **`{prefix}jet_post_types`** avec
`status = 'query'` ; colonnes `labels` (serialize `['name' => '...']`) et `args`
(serialize de toute la config, clé `query_type` = `posts|sql|terms|...` + un sous-tableau
du même nom contenant les args type WP_Query).

- **Inspecter** : `\Jet_Engine\Query_Builder\Manager::instance()->get_queries()` /
  `get_query_by_id( $id )` → propriété `->query` = args (post_type, tax_query, orderby…).
- **Créer en autopilote** : le plus fiable est de partir d'une query existante du même
  `query_type` — lire sa ligne, désérialiser `args`, modifier (tax_query/terms, orderby,
  post_type…), réinsérer :

```php
global $wpdb;
$t   = $wpdb->prefix . 'jet_post_types';
$src = $wpdb->get_row( "SELECT * FROM $t WHERE id = 3", ARRAY_A ); // modèle
$args = maybe_unserialize( $src['args'] );
$args['posts']['tax_query'][0]['terms'] = 21;      // nouvelle catégorie
$wpdb->insert( $t, [
	'slug' => '', 'status' => 'query',
	'labels' => serialize( [ 'name' => 'Produits Réparations' ] ),
	'args' => serialize( $args ), 'meta_fields' => '',
] );
echo $wpdb->insert_id; // = _query_id à référencer dans le listing
```

  ⚠️ Le Manager enregistre les queries au bootstrap : une query insérée n'est **pas
  visible dans le même process PHP** (`get_query_by_id` renvoie false). Vérifier dans un
  **nouveau** `wp eval` : `get_query_by_id( $new_id )->get_items()` doit retourner les
  items (testé : copie de query + tax modifiée → items OK au process suivant).
- Le tri/filtre vit dans la **query**, jamais dans le widget grille.

## Composant Listing (template d'un item) : créer par script

Post type **`jet-engine`**, `post_status publish`, avec ces metas (relevées sur un
composant réel) :

```php
$listing_id = wp_insert_post( [ 'post_type' => 'jet-engine', 'post_status' => 'publish',
	'post_title' => 'Carte produit X' ] );
update_post_meta( $listing_id, '_entry_type',   'listing' );
update_post_meta( $listing_id, '_listing_type', 'elementor' );
update_post_meta( $listing_id, '_listing_data', [ 'source' => 'query',
	'post_type' => 'post', 'tax' => 'category' ] );
update_post_meta( $listing_id, '_query_id', (string) $query_id );
update_post_meta( $listing_id, '_elementor_page_settings', [
	'listing_source' => 'query', 'listing_post_type' => 'post',
	'listing_tax' => 'category', '_query_id' => (string) $query_id ] );
update_post_meta( $listing_id, '_elementor_template_type', 'jet-listing-items' );
update_post_meta( $listing_id, '_wp_page_template', 'default' );
// puis _elementor_data comme n'importe quelle page (conteneur racine = la carte),
// + _elementor_edit_mode 'builder' + _elementor_version + clear_cache()
```

## Widget `jet-listing-grid` (dans la page)

- `lisitng_id` (SIC — la faute de frappe est dans JetEngine, ne pas « corriger ») = ID
  du composant listing.
- `columns` / `columns_tablet` / `columns_mobile` (les 3 explicitement),
  `equal_columns_height => 'yes'`, `not_found_message`.
- **Gap : OBLIGATOIREMENT via le widget** — `horizontal_gap` / `vertical_gap`
  (`['unit'=>'px','size'=>22,'sizes'=>[]]`). JAMAIS un `gap` CSS sur
  `.jet-listing-grid__items` : JetEngine calcule les largeurs d'items en % sans le
  connaître → les colonnes replient (3 deviennent 2).
- Vérifier au `curl` : les settings réellement appliqués sont sérialisés dans l'attribut
  `data-nav` du markup.

## Widget `jet-listing-dynamic-field` (dans le listing)

- `dynamic_field_source => 'object'` + `dynamic_field_post_object =>
  'post_title'|'post_content'|'post_excerpt'|...` ; produits WooCommerce : les méthodes
  `get_description`, `get_price_html`… fonctionnent aussi comme valeur de `post_object`.
- Meta : ajouter `dynamic_field_post_meta_custom => 'ma_meta'` (prioritaire sur
  `post_object`).
- `dynamic_field_format => '%s €'` (sprintf).
- `post_content` passe par `the_content` → un `<ul>` saisi dans la description d'un
  produit ressort en vrai `<ul>` stylable en CSS. Harmoniser les descriptions des items
  (toutes en liste) pour des cartes homogènes.
- **Rendu = `display:flex; align-items:center` par défaut** : dans une carte à hauteur
  égalisée le contenu paraît centré verticalement — forcer `align-items:flex-start` via
  la classe custom du widget. En mode « optimized DOM », la classe
  `jet-listing-dynamic-field` n'est PAS posée sur l'élément (seulement
  `jet-listing-dynamic-field-optimized-dom`) : cibler la classe custom (`_css_classes`),
  pas la classe du plugin. Le conteneur interne `.jet-listing-dynamic-field__content`
  existe dans tous les modes.

## Widget `jet-listing-dynamic-link` (bouton/lien par item)

Pour un lien portant un paramètre par item (ex. `/demande/?svc=<ID>`):

```php
[ 'widgetType' => 'jet-listing-dynamic-link', 'settings' => [
	'link_label' => 'Commander',
	'dynamic_link_source_custom' => 'meta_inexistante', // → URL vide
	'url_prefix' => '/demande-intervention/',           // la base statique
	'add_query_args' => 'yes',
	'query_args' => 'svc=%current_id%',                 // macros OK, une par ligne
] ]
```

Markup rendu : `.jet-listing-dynamic-link__link` (styler celui-là, pas le wrapper).

## Markup, ciblage CSS et variantes

- Chaque item = `.jet-listing-grid__item` ; l'arbre Elementor du listing est rendu
  dedans (`> .elementor` — lui donner `height:100%` pour les cartes pleine hauteur).
- **Variante « mise en avant »** d'une carte : si l'ordre de la query est déterministe
  (tri par meta), cibler `.jet-listing-grid__item:nth-child(N)` en CSS. Poser le badge
  en `::before` sur un **widget** de la carte (pas sur le conteneur — voir pièges
  Elementor). Documenter la dépendance à l'ordre de la query.

# ── FIN SECTION JETENGINE ──────────────────────────────────────────

## Accordéon natif Elementor (`nested-accordion`) — FAQ

- `widgetType => 'nested-accordion'` : les **titres** vivent dans `settings.items`
  (tableau `{item_title, _id}`) et le **contenu** de chaque item est le N-ième conteneur
  enfant du widget (`elements[N]`) — garder items et conteneurs alignés (même nombre,
  même ordre).
- Settings utiles : `accordion_item_title_icon` / `_icon_active` (chevrons),
  `accordion_item_title_icon_position => 'end'`, `faq_schema => 'yes'` (rich snippet),
  `default_state` (premier item ouvert par défaut).
- Markup rendu : `<details class="e-n-accordion-item"><summary class="e-n-accordion-item-title">`
  → styler en CSS via une classe posée sur le widget (`_css_classes`) :
  `.ma-faq .e-n-accordion-item { ... }`, état ouvert `.e-n-accordion-item[open]`,
  icône `.e-n-accordion-item-title-icon`. Penser à neutraliser le padding par défaut des
  conteneurs de contenu (`--container-default-padding-*`).

## Tokens du design : où les mettre

Cette skill ne contient **aucun token** (couleurs, polices, rayons, espacements) : ils
changent à chaque projet. Au début d'une intégration, extraire les tokens de la maquette
et les consigner côté projet (CLAUDE.md, mémoire projet, ou un fichier CSS de référence),
puis les câbler dans Elementor de préférence via le **kit actif**
(`wp option get elementor_active_kit`) → couleurs et polices globales, pour que les
widgets y fassent référence au lieu de dupliquer des valeurs en dur.
