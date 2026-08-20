import json,re
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'public/blog-posts/index.json'; d=json.loads(p.read_text())
add={
'etiqueta-bate-papo-online-como-conversar-respeito':'<p>Se houver dúvida, escolha a gentileza: leia novamente, reduza a pressão e deixe a pessoa decidir. Essa regra simples funciona em qualquer sala, cidade ou dispositivo.</p>',
'chat-online-por-interesses-encontrar-pessoas-parecidas':'<p>Uma boa pergunta vale mais que uma apresentação perfeita. Demonstre atenção, responda com honestidade e permita que a outra pessoa conduza parte do caminho. É assim que afinidade vira confiança.</p>',
'chat-online-acessibilidade-pessoas-deficiencia-conversar':'<p>Essa postura não exige conhecimento técnico avançado. Exige atenção, flexibilidade e disposição para corrigir o percurso. O resultado é uma conversa mais confortável, autônoma e humana para todos.</p>'}
for x in d:
 if x['slug'] in add and 'Essa postura não exige' not in x['content'] and 'Uma boa pergunta vale' not in x['content'] and 'Se houver dúvida' not in x['content']:
  x['content']=x['content'].replace('<h2>Conclusão</h2>',add[x['slug']]+'<h2>Conclusão</h2>')
  x['wordCount']=len(re.sub('<[^>]+>',' ',x['content']).split())
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print([(x['slug'],x['wordCount']) for x in d[-3:]])
