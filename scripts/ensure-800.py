import json,re
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'public/blog-posts/index.json'; d=json.loads(p.read_text())
for x in d:
 if x['slug']=='chat-online-acessibilidade-pessoas-deficiencia-conversar' and 'Acessibilidade se constrói' not in x['content']:
  x['content']=x['content'].replace('<h2>Conclusão</h2>','<p>Acessibilidade se constrói nas decisões pequenas: uma legenda, uma descrição, uma pausa e um limite respeitado.</p><h2>Conclusão</h2>')
  x['wordCount']=len(re.sub('<[^>]+>',' ',x['content']).split())
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(d[-1]['wordCount'])
