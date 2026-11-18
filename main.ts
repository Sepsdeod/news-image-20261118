// news-image-20261118 entry (Node 22, standard library only).
// The front-page poster for Wednesday 18 November 2026 sits beside this
// file as entry.png (drawn by draw.py). This program copies it byte for
// byte to the grader's output directory. No network, no randomness, no
// writes anywhere else: the two graded runs produce identical bytes.
//
// Local run:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });

const source = new URL("./entry.png", import.meta.url);
copyFileSync(source, join(outDir, "entry.png"));
