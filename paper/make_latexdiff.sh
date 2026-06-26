#!/usr/bin/env bash
# Build the marked-up ("all changes highlighted") copies that the journal requests
# as the "Revised Manuscript - Marked Up File". Each current source is compared
# against its version at the comms_ai_comp tag (the originally submitted version).
#
# Note: the supplementary information was moved from si/main.tex to
# paper/supplementary.tex during these revisions, so it is diffed against its old
# path explicitly rather than through latexdiff-vc's git tracking.
set -euo pipefail

baseline="comms_ai_comp"

build_diff() {
  local old_source="$1" new_source="$2" stem="$3"
  git show "${baseline}:${old_source}" > "/tmp/${stem}_old.tex"
  latexdiff --allow-spaces "/tmp/${stem}_old.tex" "${new_source}" > "${stem}-diff.tex"
  pdflatex -interaction=nonstopmode "${stem}-diff.tex" > /dev/null
  bibtex "${stem}-diff" > /dev/null || true
  pdflatex -interaction=nonstopmode "${stem}-diff.tex" > /dev/null
  pdflatex -interaction=nonstopmode "${stem}-diff.tex" > /dev/null
  echo "wrote ${stem}-diff.pdf"
}

build_diff "paper/main.tex" "main.tex" "main"
build_diff "si/main.tex" "supplementary.tex" "supplementary"
