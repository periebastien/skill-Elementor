<?php
// Dump all registered Elementor widgets + their controls as JSON.
// Force full control registration (Elementor 4.x skips style controls outside the editor).
$ref = new ReflectionProperty( \Elementor\Core\Frontend\Performance::class, 'is_frontend' );
$ref->setAccessible( true );
$ref->setValue( null, false );
\Elementor\Core\Frontend\Performance::set_use_style_controls( true );
$widgets = \Elementor\Plugin::$instance->widgets_manager->get_widget_types();
$out = [];
foreach ( $widgets as $name => $w ) {
	$entry = [
		'name'     => $name,
		'title'    => $w->get_title(),
		'pro'      => ( strpos( get_class( $w ), 'ElementorPro' ) === 0 ),
		'class'    => get_class( $w ),
		'controls' => [],
	];
	$controls = $w->get_controls();
	foreach ( $controls as $cid => $c ) {
		$type = $c['type'] ?? '';
		if ( in_array( $type, [ 'section', 'tab', 'heading', 'raw_html', 'divider', 'deprecated_notice', 'alert', 'notice', 'button', 'hidden' ], true ) ) continue;
		$entry['controls'][] = [
			'id'      => $cid,
			'type'    => $type,
			'tab'     => $c['tab'] ?? '',
			'section' => $c['section'] ?? '',
			'options' => ( isset( $c['options'] ) && is_array( $c['options'] ) ) ? array_keys( $c['options'] ) : null,
			'default' => $c['default'] ?? null,
		];
	}
	$out[] = $entry;
}
$dest = $args[0] ?? getcwd() . '/widgets-dump.json'; // wp eval-file <script> <dest>
file_put_contents( $dest, wp_json_encode( $out ) );
echo count( $out ) . " widgets dumped\n";
