import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const require = createRequire(path.join(root, 'website/package.json'));
const sharp = require('sharp');
for (const mode of ['primary', 'reverse', 'black', 'white']) {
  const stats = await sharp(path.join(root, `brand/logos/mark-${mode}.png`)).stats();
  assert.equal(stats.channels[3].min, 0, `${mode}: background must be transparent`);
  assert.equal(stats.channels[3].max, 255, `${mode}: mark must be opaque`);
}
for (const mode of ['light', 'dark']) {
  const image = sharp(path.join(root, `brand/icons/avatar-${mode}.png`));
  if ((await image.metadata()).hasAlpha) {
    assert.equal((await image.stats()).channels[3].min, 255, `${mode}: avatar background must be opaque`);
  }
}
console.log('PASS: transparent mark alpha and opaque avatar canvases');
