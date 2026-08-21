import json, re
from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'public/blog-posts/index.json'
data = json.loads(p.read_text())
for post in data:
    if post.get('slug') == 'fazer-amigos-online-trabalho-turnos-rotina-invertida':
        post['content'] += '<p>Conexão sustentável é aquela que respeita o relógio e a energia de cada pessoa.</p>'
        post['wordCount'] = len(re.sub('<[^>]+>', ' ', post['content']).split())
        post['readTime'] = max(6, round(post['wordCount'] / 155))
p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print(next(x['wordCount'] for x in data if x.get('slug') == 'fazer-amigos-online-trabalho-turnos-rotina-invertida'))
