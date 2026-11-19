#!/usr/bin/env bash
# Rebuilds the whole knowledge base: extract open sources, write curated sets, assemble outputs.
set -euo pipefail
cd "$(dirname "$0")"
pip install -q beautifulsoup4 lxml pyyaml openpyxl >/dev/null
[ -d ../sources ] || ./fetch_sources.sh ../sources
for s in wcag standards2 designsystems misc curated_laws curated_heuristics curated_biases curated_darkpatterns curated_metrics curated_rules bibliography build; do
  python3 "$s.py"
done
