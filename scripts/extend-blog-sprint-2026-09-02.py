import json, re
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'public/blog-posts/index.json'
d=json.loads(p.read_text())
extra={
'chat-online-para-leitores-clube-livros-brasil': '<h2>Um ritual simples para continuar lendo</h2><p>Depois da conversa, anote uma recomendação e o motivo pelo qual ela chamou sua atenção. Na semana seguinte, volte para contar se começou a leitura. Esse pequeno retorno transforma uma mensagem isolada em uma história compartilhada. Você também pode propor desafios leves, como escolher um conto curto ou cada pessoa apresentar um autor da própria região. O importante é manter a atividade voluntária e acolher quem está lendo em outro ritmo.</p><p>Se o grupo ficar muito grande, não tente responder a tudo. Escolha uma mensagem e faça uma pergunta cuidadosa. Qualidade cria mais conexão do que velocidade. Leitores também podem usar o chat para descobrir eventos, feiras e bibliotecas, mas confirme informações diretamente com a organização antes de sair de casa.</p>',
'video-chat-gratis-familia-distancia-conectar': '<h2>Como tornar o encontro memorável</h2><p>Escolha uma atividade que possa ser compartilhada pela tela: cozinhar a mesma receita, mostrar fotos antigas, fazer um quiz sobre a família ou contar uma história em turnos. O encontro fica mais natural quando as pessoas fazem algo juntas, em vez de apenas preencher silêncio. Se a conexão cair, retome por mensagem e marque outro horário; tecnologia deve servir ao vínculo, não controlar o humor da família.</p><p>Também vale alternar quem escolhe o tema. Assim, a conversa não fica centrada sempre na mesma pessoa e cada geração pode trazer algo próprio. Um calendário simples no grupo da família reduz esquecimentos e evita que o planejamento dependa de quem já está sobrecarregado.</p>',
'fazer-amigos-online-por-hobbies-interesses-comuns': '<h2>Como evitar que o hobby vire competição</h2><p>Comunidades de interesse podem ficar hostis quando experiência é confundida com superioridade. Prefira explicar em vez de corrigir, e pergunte antes de oferecer uma crítica. Quem está começando precisa de espaço para experimentar sem medo de ser ridicularizado. Você pode dizer “uma forma que funcionou para mim foi...” em vez de apresentar sua preferência como regra universal.</p><p>Uma amizade também não depende de participar todos os dias. Avise quando precisar sair, silencie notificações se necessário e preserve tempo para sua vida offline. O hobby deve ampliar sua rotina, não ocupar todo o espaço dela. Quando essa medida existe, as conversas permanecem prazerosas e sustentáveis.</p>'}
for x in d:
 if x['slug'] in extra and x['date']=='2026-09-02':
  x['content'] += extra[x['slug']]
  x['wordCount']=len(re.findall(r"\b[\wÀ-ÿ'-]+\b", re.sub('<[^>]+>',' ',x['content'])))
  x['readTime']=max(6,round(x['wordCount']/180))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print([(x['slug'],x['wordCount']) for x in d if x['date']=='2026-09-02'])
