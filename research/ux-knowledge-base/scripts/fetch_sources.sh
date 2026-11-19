#!/usr/bin/env bash
# Shallow-clones every open source repository the extractors read.
# Usage: ./fetch_sources.sh [target-dir]   (default: ../sources)
set -euo pipefail
DEST="${1:-$(dirname "$0")/../sources}"
mkdir -p "$DEST"
REPOS=(
  w3c/wcag w3c/wcag3 w3c/aria-practices w3c/coga act-rules/act-rules.github.io
  dequelabs/axe-core GoogleChrome/lighthouse a11yproject/a11yproject.com thedaviddias/Front-End-Checklist
  alphagov/govuk-design-system nhsuk/nhsuk-service-manual uswds/uswds-site carbon-design-system/carbon-website
  Shopify/polaris primer/design 18F/content-guide 18F/ux-guide 18F/accessibility 18F/methods
  GSA/plainlanguage.gov GSA/digitalgov.gov usds/playbook aruneshmathur/dark-patterns yamanalab/ec-darkpattern
)
for r in "${REPOS[@]}"; do
  d="$DEST/$(echo "$r" | tr '/' '_')"
  [ "$r" = "w3c/wcag" ] && d="$DEST/wcag"
  [ -d "$d" ] || git clone -q --depth 1 "https://github.com/$r.git" "$d" && echo "ok $r"
done
