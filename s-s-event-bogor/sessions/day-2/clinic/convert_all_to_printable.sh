#!/bin/bash
# Convert all clinic markdown files to GOAP-styled printable Word documents.
# Uses the improved md_to_docx converter with proper list, code fence, and rule handling.

CONVERTER="/Users/mariaalarcon/GitHub/ocean-accounts-expert/s-s-event-bogor/sessions/day-2/clinic/md_to_docx_improved.py"
TEMPLATE="/Users/mariaalarcon/GitHub/ocean-accounts-expert/goap-templates/GOAP Word templates/GOAP-REPORT TEMPLATE.docx"
CLINIC="/Users/mariaalarcon/GitHub/ocean-accounts-expert/s-s-event-bogor/sessions/day-2/clinic"

echo "Converting clinic markdown files to GOAP Word documents (improved converter)..."
echo ""

# Extent
mkdir -p "$CLINIC/extent/printable-versions"
for f in extent-guide extent-exercise extent-slides; do
    echo "  extent/$f.md"
    python3 "$CONVERTER" "$CLINIC/extent/$f.md" \
        -o "$CLINIC/extent/printable-versions/$f.docx" \
        -t "$TEMPLATE" \
        --header "Ocean Accounting Clinic -- Extent Accounts"
done

# Condition
mkdir -p "$CLINIC/condition/printable-versions"
for f in condition-guide condition-exercise condition-slides; do
    echo "  condition/$f.md"
    python3 "$CONVERTER" "$CLINIC/condition/$f.md" \
        -o "$CLINIC/condition/printable-versions/$f.docx" \
        -t "$TEMPLATE" \
        --header "Ocean Accounting Clinic -- Condition Accounts"
done

# Services
mkdir -p "$CLINIC/services/printable-versions"
for f in services-guide services-exercise services-slides data-sources-by-service; do
    echo "  services/$f.md"
    python3 "$CONVERTER" "$CLINIC/services/$f.md" \
        -o "$CLINIC/services/printable-versions/$f.docx" \
        -t "$TEMPLATE" \
        --header "Ocean Accounting Clinic -- Ecosystem Services"
done

echo ""
echo "Done! All printable versions created."
find "$CLINIC" -path "*/printable-versions/*.docx" | sort
