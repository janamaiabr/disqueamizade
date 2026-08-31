const fs = require('fs');
const path = require('path');
const root = __dirname;
const indexPath = path.join(root, 'public/blog-posts/index.json');
const sitemapPath = path.join(root, 'public/sitemap.xml');
const additions = JSON.parse(fs.readFileSync(path.join(root, 'sprint_articles_2026-09-01.json'), 'utf8'));
const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));
const existing = new Set(index.map(p => p.slug));
const fresh = additions.filter(p => !existing.has(p.slug)).map((p, i) => ({...p, id: Math.max(...index.map(x => x.id || 0)) + i + 1}));
if (fresh.length !== additions.length) throw new Error('Duplicate slug detected');
fs.writeFileSync(indexPath, JSON.stringify(index.concat(fresh), null, 2) + '\n');
let sitemap = fs.readFileSync(sitemapPath, 'utf8');
for (const p of fresh) {
  const url = `https://disqueamizade.com.br/blog/${p.slug}`;
  if (!sitemap.includes(`<loc>${url}</loc>`)) sitemap = sitemap.replace('</urlset>', `  <url>\n    <loc>${url}</loc>\n    <lastmod>${p.lastModified}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n</urlset>`);
}
fs.writeFileSync(sitemapPath, sitemap);
console.log(`Added ${fresh.length} articles and updated sitemap`);
