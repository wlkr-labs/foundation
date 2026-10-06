import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const require = createRequire(path.join(root, 'website/package.json'));
const sharp = require('sharp');
for (const mode of ['primary', 'reverse', 'black', 'white']) {
  for (const layout of ['mark', 'wordmark']) {
    const stats = await sharp(path.join(root, `brand/logos/${layout}-${mode}.png`)).stats();
    assert.equal(stats.channels[3].min, 0, `${layout}/${mode}: background must be transparent`);
    assert.equal(stats.channels[3].max, 255, `${layout}/${mode}: shapes must be opaque`);
  }
}
for (const mode of ['light', 'dark']) {
  const image = sharp(path.join(root, `brand/icons/avatar-${mode}.png`));
  if ((await image.metadata()).hasAlpha) {
    assert.equal((await image.stats()).channels[3].min, 255, `${mode}: avatar background must be opaque`);
  }
}
for (const mode of ['primary', 'reverse', 'black', 'white']) {
  const { data, info } = await sharp(path.join(root, `brand/logos/horizontal-${mode}.png`)).raw().toBuffer({ resolveWithObject: true });
  const columns = [], bounds = (start, end) => {
    let top = info.height, bottom = -1;
    for (let x = start; x <= end; x++) for (let y = 0; y < info.height; y++) {
      if (data[(y * info.width + x) * info.channels + 3] > 128) { top = Math.min(top, y); bottom = Math.max(bottom, y); }
    }
    return { height: bottom - top + 1, center: (top + bottom) / 2 };
  };
  for (let x = 0; x < info.width; x++) {
    for (let y = 0; y < info.height; y++) if (data[(y * info.width + x) * info.channels + 3] > 128) { columns.push(x); break; }
  }
  let split = 1;
  for (let i = 2; i < columns.length; i++) if (columns[i] - columns[i - 1] > columns[split] - columns[split - 1]) split = i;
  const symbol = bounds(columns[0], columns[split - 1]), name = bounds(columns[split], columns.at(-1));
  assert.ok(Math.abs(symbol.height / name.height - 1.16) < .015, `${mode}: rendered height ratio`);
  assert.ok(Math.abs((columns[split] - columns[split - 1] - 1) / name.height - .45) < .015, `${mode}: rendered gap`);
  assert.ok(Math.abs((name.center - symbol.center) / name.height - .06) < .015, `${mode}: rendered optical alignment`);
}
console.log('PASS: rendered horizontal proportions, gap and optical alignment in all four colorways');
console.log('PASS: transparent mark/wordmark alpha and opaque avatar canvases');
