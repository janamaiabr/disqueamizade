import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'public/blog-posts/index.json'
d=json.loads(p.read_text())
extras={
'etiqueta-bate-papo-online-como-conversar-respeito': '<h2>Quando é melhor sair da conversa</h2><p>Encerrar uma interação também é uma habilidade social. Você pode dizer “foi bom conversar, mas vou sair agora” sem justificar cada detalhe. Se a pessoa insistir, repita o limite uma vez e use o bloqueio. Não é falta de educação proteger seu tempo, sua privacidade e sua segurança. Em um ambiente de chat online brasil, milhares de estilos convivem; uma conversa que não funciona hoje não precisa virar conflito.</p>',
'chat-online-por-interesses-encontrar-pessoas-parecidas': '<h2>Da primeira afinidade à amizade</h2><p>Depois de algumas conversas, proponha uma atividade leve ligada ao interesse: trocar recomendações de livros, comentar um campeonato, montar uma playlist ou conversar sobre um filme. Atividades dão um objetivo à interação sem exigir confidências. Observe se o vínculo é recíproco e se você se sente confortável. Fazer amigos online é um processo, não uma corrida por quantidade de contatos.</p>',
'chat-online-acessibilidade-pessoas-deficiencia-conversar': '<h2>Inclua sem criar um espetáculo</h2><p>Uma comunidade acessível não coloca a pessoa com deficiência no papel de professora o tempo todo. Pergunte quando precisar, agradeça a orientação e aprenda com consistência. Também vale lembrar que acessibilidade beneficia pessoas temporariamente lesionadas, quem está em um ambiente barulhento, quem tem internet limitada e quem simplesmente prefere ler. Quanto mais opções de comunicação existirem, mais pessoas conseguem participar com autonomia.</p>'}
extras['etiqueta-bate-papo-online-como-conversar-respeito'] += '<p>Também vale cuidar do horário e do volume de mensagens. Uma comunicação respeitosa considera que a outra pessoa pode estar trabalhando, estudando ou cuidando da família. O melhor bate papo online é aquele que deixa vontade de voltar, não a sensação de obrigação.</p>'
extras['chat-online-por-interesses-encontrar-pessoas-parecidas'] += '<p>Se o interesse mudar, tudo bem. Amizades não precisam permanecer presas ao primeiro assunto que aproximou vocês. A conversa pode passar de livros para rotina, de jogos para carreira, ou terminar naturalmente. Liberdade para mudar de tema é parte da conexão.</p>'
extras['chat-online-acessibilidade-pessoas-deficiencia-conversar'] += '<p>Antes de avaliar uma ferramenta, teste diferentes formatos e ouça relatos variados. A mesma solução pode funcionar para uma pessoa e atrapalhar outra. Inclusão prática nasce de escolhas e ajustes contínuos, não de uma promessa genérica colocada na página inicial.</p>'
for x in d:
    if x['slug'] in extras and not any(k in x['content'] for k in ['Quando é melhor sair','Da primeira afinidade','Inclua sem criar']):
        x['content']=x['content'].replace('<h2>Conclusão</h2>',extras[x['slug']]+'<h2>Conclusão</h2>')
        import re
        x['wordCount']=len(re.sub('<[^>]+>',' ',x['content']).split())
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print([(x['slug'],x['wordCount']) for x in d[-3:]])
