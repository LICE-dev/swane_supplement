# SWANe Supplement agent instructions

This file is versioned with the repository so every trusted clone uses the same project guidance.

- Use `$swane-supplement-maintainer` for changes, reviews, packaging, or validation in this repository.
- Inspect the main SWANe consumers before changing exported names, filenames, relative paths, icons, NIfTI templates, or FLAT1 resources.
- Treat resource paths, image geometry, statistical templates, and `package_data` inclusion as stable contracts.
- Use synthetic or properly sourced non-clinical assets only; never add patient data, identifiers, credentials, local paths, or generated results.
- For scientific resources, verify provenance, affine, orientation, dimensions, dtype, and numerical range. Do not call a packaging check scientific validation.
- Preserve unrelated changes and create a `codex/<descriptive-name>` branch for versioned work starting from `dev` or `main`.
- Do not commit, push, publish, or modify the main SWANe repository unless explicitly requested.

The main application is normally available at `../swane`, but discover it from the workspace instead of assuming an absolute path.
