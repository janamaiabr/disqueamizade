import json,re
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'public/blog-posts/index.json'; d=json.loads(p.read_text())
add={
'chat-online-para-leitores-clube-livros-brasil':'<p>Para facilitar, leve três perguntas prontas: qual trecho ficou na memória, que personagem você gostaria de conhecer e para quem recomendaria a obra. Elas funcionam com romance, biografia, fantasia e não ficção. Se ninguém conhecer o título, explique em duas frases e convide o grupo a contar o que está lendo agora. Assim, a conversa continua mesmo quando a lista de livros é diferente.</p>',
'video-chat-gratis-familia-distancia-conectar':'<p>Antes de encerrar, combine o próximo encontro ou deixe uma pergunta para responder depois. Esse fechamento dá continuidade sem criar cobrança. Lembre que uma pessoa pode participar apenas ouvindo, usando câmera desligada ou entrando por poucos minutos. Inclusão prática é permitir que cada familiar esteja presente de um jeito possível naquele dia.</p>',
'fazer-amigos-online-por-hobbies-interesses-comuns':'<p>Se não houver uma sala dedicada ao seu hobby, use uma sala geral e explique o interesse em uma frase. Muitas boas conversas começam quando alguém pergunta por curiosidade. Você pode ainda combinar uma troca de referências, como uma playlist, receita ou tutorial, sem exigir que a outra pessoa aceite contato fora da plataforma. Pequenos passos preservam a espontaneidade e a segurança.</p>'}
for x in d:
 if x['date']=='2026-09-02' and x['slug'] in add:
  x['content']+=add[x['slug']]; x['wordCount']=len(re.findall(r"\b[\wÀ-ÿ'-]+\b",re.sub('<[^>]+>',' ',x['content']))); x['readTime']=max(6,round(x['wordCount']/180))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n'); print([(x['slug'],x['wordCount']) for x in d if x['date']=='2026-09-02'])
