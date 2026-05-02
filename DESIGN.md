---
name: Aurelian Corporate
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#44474f'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0ef'
  outline: '#747780'
  outline-variant: '#c4c6d0'
  surface-tint: '#425e90'
  primary: '#00224e'
  on-primary: '#ffffff'
  primary-container: '#193868'
  on-primary-container: '#87a2d9'
  inverse-primary: '#abc7ff'
  secondary: '#745a27'
  on-secondary: '#ffffff'
  secondary-container: '#fedb9b'
  on-secondary-container: '#795f2b'
  tertiary: '#272317'
  on-tertiary: '#ffffff'
  tertiary-container: '#3d382b'
  on-tertiary-container: '#aaa190'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#abc7ff'
  on-primary-fixed: '#001b3f'
  on-primary-fixed-variant: '#294677'
  secondary-fixed: '#ffdea4'
  secondary-fixed-dim: '#e4c285'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5a4312'
  tertiary-fixed: '#ebe1cf'
  tertiary-fixed-dim: '#cfc6b3'
  on-tertiary-fixed: '#1f1b10'
  on-tertiary-fixed-variant: '#4c4638'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  headline-xl:
    fontFamily: Manrope
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-max: 1280px
  section-padding: 120px
  gutter: 24px
  card-gap: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style

This design system embodies a sophisticated, executive-level professional aesthetic that blends high-trust corporate stability with modern technological precision. The brand personality is authoritative yet approachable, positioning itself as a premium partner for enterprise-grade automation and strategic growth.

The visual direction follows a **Corporate / Modern** style with an emphasis on high-end editorial layouts. It utilizes a warm, parchment-inspired canvas to differentiate from the cold whites of typical SaaS products, evoking a sense of heritage and permanence. The aesthetic is defined by structured clarity, intentional whitespace, and a harmonious balance between deep navy tones and metallic gold accents, creating an atmosphere of "quiet luxury" in a digital space.

## Colors

The palette is anchored by a triad of high-contrast, professional tones. The primary color is a deep, authoritative navy used for typography and high-impact UI elements. The secondary color is a muted gold, reserved for strategic highlights, calls to action, and decorative iconography, providing a premium "gold-leaf" effect.

The background strategy moves away from pure white, instead using a warm cream (#F0E6D3) as the foundational surface color. This reduces eye strain and reinforces the sophisticated brand narrative. Neutral tones are used sparingly for secondary body text to maintain high legibility against the warm background.

## Typography

The design system relies exclusively on **Manrope** to deliver a clean, geometric, and modern feel. The typographic hierarchy is characterized by significant scale shifts between hero headlines and body copy. 

Headlines use heavy weights (Bold/ExtraBold) with tight letter spacing to create a strong visual impact and an "editorial" look. Body text is optimized for readability with generous line heights. To maintain the sophisticated aesthetic, secondary headlines often utilize the gold accent color or a combination of navy and gold to emphasize specific phrases within a sentence.

## Layout & Spacing

The layout utilizes a **fixed grid** system centered on a 1280px container. Large vertical "breathing room" (120px section padding) is critical to the premium feel, ensuring content never feels cluttered. 

A modular card-based layout is employed to organize information. These cards typically follow a 3 or 4-column distribution. Elements within sections are vertically stacked using a consistent 8px-based rhythm, while section headers are centered to maintain a formal, balanced composition.

## Elevation & Depth

This design system avoids heavy shadows, instead using **tonal layers** and **low-contrast outlines** to establish depth. Hierarchy is created by placing elements on slightly varied shades of the base cream color.

Cards utilize a very subtle, thin border (1px) in a slightly darker tan or a soft, low-opacity ambient shadow to lift them from the background. In specific high-impact areas, "inverted" elevation is used where a card becomes a solid block of primary navy, creating a deep recessed effect that draws the eye immediately.

## Shapes

The shape language is defined by **rounded** corners that soften the corporate geometry. A consistent radius is applied to cards and containers to create a modern, approachable feel. 

Interactive elements like buttons and status badges utilize "pill-shaped" (fully rounded) geometry, which provides a distinct contrast to the more structured rectangular card grids. This juxtaposition ensures that actionable elements are instantly recognizable.

## Components

### Buttons
Primary buttons are pill-shaped, using the dark navy background with white or cream text. Secondary buttons utilize a ghost style with a thin navy or gold border. Hover states should include a subtle scale increase or a slight shift in background saturation.

### Cards
Cards are the primary container. They feature generous internal padding (40px) and a consistent corner radius. Two variants exist:
1.  **Light Variant:** A soft tan background with navy text, used for feature lists and testimonials.
2.  **Solid Variant:** A primary navy background with white and gold text, used for high-priority service offerings.

### Chips & Tags
Used for "eyebrow" labels above headlines. These are small, pill-shaped, and feature a light gold background with dark text to draw attention without disrupting the headline hierarchy.

### Input Fields
Inputs follow the card aesthetic: light backgrounds, subtle borders, and Manrope typography. Focus states are indicated by a gold border highlight.

### Icons
Icons should be thin-stroke or "Material Icons" style, always rendered in the gold accent color to maintain a cohesive visual thread throughout the system. They are often housed within small circular or rounded-square containers with a light tan fill.