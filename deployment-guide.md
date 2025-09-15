# SCHH Commons - Landing Page and Collections Setup

## Files to Create/Update

### 1. Configuration Files
- Update `_config.yml` with the enhanced configuration
- Add landing page settings and collection definitions

### 2. Layout Files
- Create `_layouts/landing.html` for the landing page
- Create `_layouts/podcast.html` for podcast-specific layout

### 3. Include Files
- Create `_includes/collection-preview.html` for landing page sections
- Create `_includes/audio-player.html` for podcast audio controls

### 4. Page Files
- Update `index.html` to conditionally use landing layout
- Create `articles.html` for articles archive
- Create `maps.html` for maps archive  
- Create `podcasts.html` for podcasts archive

### 5. Navigation Tabs
Create these tab files in the `_tabs/` directory:
- `_tabs/articles.md`
- `_tabs/maps.md`
- `_tabs/podcasts.md`

### 6. Collection Directories
Create these directories for your content:
```
_articles/
_maps/
_podcasts/
assets/img/
assets/audio/
```

### 7. Styling
Add the landing page CSS to your existing `_sass/addon/commons.scss` file or create it if it doesn't exist.

## Usage Instructions

### Landing Page
- Set `landing_page.enabled: true` in `_config.yml` to enable the landing page
- Customize hero section content in the config
- Add hero background image to `/assets/img/hero-bg.jpg`
- Adjust sections displayed on landing page

### Collections
- Add content to `_articles/`, `_maps/`, and `_podcasts/` directories
- Use the example front matter provided for consistency
- For podcasts, add `audio_file` and `duration` fields
- For maps, consider adding `map_embed` field for interactive maps

### Navigation
- The tab files will automatically appear in your site navigation
- Adjust `order` values to control tab sequence
- Use Font Awesome icons in the `icon` field

## Testing
1. Run `bundle exec jekyll serve` locally
2. Visit `http://localhost:4000` to see the landing page
3. Navigate to `/articles/`, `/maps/`, and `/podcasts/` to test collections
4. Add sample content files to test the preview sections

## Customization Tips
- Modify landing page sections in `_config.yml`
- Adjust hero styling in the CSS file
- Customize collection preview limits
- Add additional metadata fields as needed
- Consider adding search functionality for larger collections