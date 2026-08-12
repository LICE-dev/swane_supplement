---
name: swane-supplement-maintainer
description: Maintain the swane_supplement Python package, including distributed icons, NIfTI templates, FLAT1 resources, package_data, resource paths, and compatibility with SWANe ResourceManager consumers. Use for changes, reviews, releases, or validation in the swane_supplement repository.
---

# SWANe Supplement Maintainer

Preserve the packaged resource contract consumed by SWANe.

## Work safely

- Inspect the live `swane_supplement` package and the consuming SWANe `ResourceManager` or imports before changing a resource.
- Treat exported variable names, relative paths, filenames, image geometry, and package-data inclusion as stable contracts.
- Never replace scientific templates or statistical maps without documenting provenance and verifying dimensions, affine, orientation, dtype, and expected numerical range.
- Never add clinical data, identifiers, credentials, local paths, generated archives, or build output.
- Preserve unrelated changes and use a dedicated `codex/` branch for versioned work starting from `dev` or `main`.

## Validate proportionally

1. Compile `swane_supplement`.
2. Import the package and verify every exported resource path exists.
3. Build or inspect package contents when package metadata or resources change.
4. Check the main SWANe consumers when filenames, paths, icons, or scientific assets change.
5. Distinguish packaging checks from scientific validation.

Do not commit, push, publish a package, or modify the public repository unless the user explicitly requests it.
