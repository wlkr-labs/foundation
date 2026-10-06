import { readFile, readdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const brand = path.join(root, 'brand');
const require = createRequire(path.join(root, 'website/package.json'));
const sharp = require('sharp');

async function png(relative, output, width) {
  await sharp(path.join(brand, relative), { density: 144 })
    .resize({ width }).png().toFile(path.join(brand, output));
}

for (const directory of ['logos', 'icons', 'social', 'print']) {
  for (const name of await readdir(path.join(brand, directory))) {
    if (!name.endsWith('.svg') || name === 'favicon-adaptive.svg') continue;
    const input = `${directory}/${name}`;
    const metadata = await sharp(path.join(brand, input)).metadata();
    const printWidth = directory === 'print'
      ? Number((await readFile(path.join(brand, input), 'utf8')).match(/viewBox="0 0 ([\d.]+)/)[1]) : null;
    await png(input, input.replace(/\.svg$/, '.png'),
      directory === 'logos' ? metadata.width * 2 : directory === 'print' ? Math.round(printWidth * 300 / 72) : metadata.width);
  }
}
await png('overview.svg', 'overview.png', 2400);
for (const size of [16, 32, 48, 64, 180, 192, 256, 512]) {
  await png('icons/app-light.svg', `icons/icon-${size}.png`, size);
}
await png('icons/avatar-light.svg', 'icons/apple-touch-icon.png', 180);

const sizes = [16, 32, 48, 64, 256];
const images = await Promise.all(sizes.map(size => readFile(path.join(brand, `icons/icon-${size}.png`))));
const header = Buffer.alloc(6 + 16 * sizes.length);
header.writeUInt16LE(1, 2);
header.writeUInt16LE(sizes.length, 4);
let offset = header.length;
for (let i = 0; i < sizes.length; i++) {
  const cursor = 6 + i * 16;
  header[cursor] = sizes[i] % 256;
  header[cursor + 1] = sizes[i] % 256;
  header.writeUInt16LE(1, cursor + 4);
  header.writeUInt16LE(32, cursor + 6);
  header.writeUInt32LE(images[i].length, cursor + 8);
  header.writeUInt32LE(offset, cursor + 12);
  offset += images[i].length;
}
await writeFile(path.join(brand, 'icons/favicon.ico'), Buffer.concat([header, ...images]));
