# Jasmine Goodsaid — Portfolio

## Open the website
Unzip this folder and double-click `index.html`. Everything needed to display the site is included. No build, package installation, WordPress, Divi, or server is required.

## Files
- `index.html`: page content, project descriptions, experience, speaking links, and contact details.
- `css/styles.css`: complete responsive styling; palette variables are at the top.
- `js/main.js`: mobile navigation, accessible project filters, scroll-triggered count-up statistics, and current footer year.
- `assets/favicon.svg`: original initials icon.
- `assets/Jasmine-Goodsaid-Resume.pdf`: supplied resume, available through the download buttons.

## Edit
Edit the HTML text directly to change content. Project details use native HTML disclosures (`details` / `summary`). Category names in `data-category` connect each project with the filter buttons. The main accent colors are set in `:root` in the CSS.

## Publish
Upload the contents of this folder to any static web host, keeping the relative folder structure. `index.html` must be at the hosting root. This package has not been deployed. A mail link opens the visitor's configured email app; it is not a backend contact form. PDF download behavior can vary by browser.

## Content and design notes
Content is based on the supplied two-page resume. Project graphics are original HTML/CSS conceptual diagrams, not screenshots of client systems. No invented testimonials, performance metrics, or stock portraits are used. Speaking resources are the corresponding URLs embedded in the resume; external destinations were not independently verified. The LinkedIn profile URL comes from the resume's embedded profile link.

Design direction is adapted from the supplied Elegant Themes Digital Product About reference (blue/purple gradients, orange accents, staggered cards, angled dividers). The implementation is independently written and includes no Divi, WooCommerce, third-party template JavaScript, remote fonts, or external visual assets.

Before publishing, review public contact information and the included resume PDF (which contains your phone number). Replace the source resume PDF in `assets` if you prefer a public version without that number. The page itself uses email and LinkedIn for contact.

## Verification
JavaScript syntax and all local file and section references were checked. Browser visual testing was unavailable in the build environment; review the page in your preferred browser before publication. Mobile layouts are defined at 1050px, 800px, and 540px. Reduced-motion preferences, keyboard focus, skip navigation, and no-JavaScript content access are supported.

## Count-up animation
Statistics animate once on scroll, from zero to their original HTML values, preserving the plus signs. Change `const duration = 1600` in `js/main.js` to adjust the speed (milliseconds). Edit the numbers directly in the `.stats` section of `index.html` to change the targets. Reduced-motion preferences skip the animation; screen readers receive stable final values.
