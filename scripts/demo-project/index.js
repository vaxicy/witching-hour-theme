// Witching Hour Theme — pumpkin, slime and blood
import { readFile } from 'node:fs/promises';

const CAULDRON = {
  pumpkin: '#E8722A',
  slime: '#A8D06A',
  blood: '#B0303F',
  candle: '#E8C66A',
  night: '#1E1626',
};

export class Spellbook {
  constructor(name = 'Thirteenth page') {
    this.name = name;
    this.recipe = CAULDRON;
  }

  /** Stir two ingredients into a glowing brew. */
  brew(from, to, ratio = 0.5) {
    const parse = (hex) =>
      [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channel = (value, i) =>
      Math.round(value * (1 - ratio) + b[i] * ratio);
    const toHex = (value) => value.toString(16).padStart(2, '0');
    return '#' + a.map(channel).map(toHex).join('');
  }

  async readSpell(file) {
    const content = await readFile(file, 'utf8');
    const lines = content.split('\n').filter(Boolean);
    return {
      name: this.name,
      parts: Object.keys(this.recipe).length,
      lines: lines.length,
      content,
    };
  }
}

const book = new Spellbook();
const brew = book.brew(CAULDRON.slime, CAULDRON.pumpkin);

console.log(`brew glow: ${brew}`);
