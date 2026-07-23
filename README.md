# skill-Elementor

Skill Claude Code pour construire et modifier des pages **Elementor** avec des
**widgets natifs** (containers flex/grid, heading, button, icon-box, image, etc.)
directement depuis WP-CLI, sans passer par un plugin ou un serveur MCP installé
sur le site WordPress.

Le contenu technique (structure des éléments, pièges des paramètres flex/background/
grid/typographie, procédure de sauvegarde de `_elementor_data` et purge du cache)
a été étudié et réécrit à partir du projet [msrbuilds/elementor-mcp](https://github.com/msrbuilds/elementor-mcp),
qui expose ces mêmes techniques via un serveur MCP embarqué dans un plugin WordPress.
Ici, la même connaissance est empaquetée en **skill Claude Code** utilisable sans
installer quoi que ce soit sur le site cible.

## Utilisation

Copier le dossier `elementor-builder/` :

- soit dans `~/.claude/skills/` pour l'avoir **globalement**, sur tous les projets (recommandé) ;
- soit dans `.claude/skills/` à la racine d'un projet WordPress + Elementor donné.

Puis charger la skill `elementor-builder` avant de construire une page. WP-CLI doit être
disponible sur le site cible.

La skill est volontairement **générique** : elle ne contient aucune donnée propre à un
projet (tokens de couleurs, IDs de médias ou de pages, chemins, identifiants d'accès).
Ces éléments restent dans le contexte du projet concerné.

## Mise à jour

Ce repo est amené à évoluer au fil des projets : nouveaux widgets rencontrés,
nouveaux pièges de paramètres, nouvelles conventions. Chaque correction constatée
sur un projet doit être reportée ici pour bénéficier aux projets suivants.
