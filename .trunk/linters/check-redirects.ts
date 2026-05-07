/// <reference types="node" />
import * as fs from "node:fs";
import * as path from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const yaml = require("js-yaml");

interface Redirects {
  [key: string]: string;
}

const gitbookFile = process.argv[2];
if (!gitbookFile) {
  console.error("Usage: check-redirects.ts <.gitbook.yaml>");
  process.exit(1);
}

const content = fs.readFileSync(gitbookFile, "utf-8");
const doc = yaml.load(content) as { redirects?: Redirects };
const redirects = doc.redirects || {};

const lines = content.split("\n");
const errors: Array<{ line: number; key: string; target: string }> = [];

// Build a map of redirect values to line numbers
const valueToLines: Map<string, number[]> = new Map();
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  const colonIdx = line.indexOf(":");
  if (colonIdx === -1) continue;

  const val = line.substring(colonIdx + 1).trim();
  if (!val) continue;

  for (const redirectValue of Object.values(redirects)) {
    if (val === redirectValue || val === `"${redirectValue}"`) {
      if (!valueToLines.has(redirectValue)) {
        valueToLines.set(redirectValue, []);
      }
      valueToLines.get(redirectValue)!.push(i + 1);
    }
  }
}

// Check each redirect target
for (const [key, target] of Object.entries(redirects)) {
  let resolvedTarget = target;
  if (resolvedTarget.startsWith("/")) {
    resolvedTarget = resolvedTarget.slice(1);
  }

  const filePath = path.resolve(process.cwd(), resolvedTarget);
  if (!fs.existsSync(filePath)) {
    const lineNum = valueToLines.get(target)?.[0] || 1;
    errors.push({ line: lineNum, key, target });
  }
}

// Output in trunk format
for (const err of errors) {
  console.log(
    `${gitbookFile}:${err.line}:1: [error] Redirect target does not exist: ${err.target} (missing-redirect-target)`,
  );
}

process.exit(0);
