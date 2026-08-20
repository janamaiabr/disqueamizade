import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'public/blog-posts/index.json'
d=json.loads(p.read_text())
extras={
'etiqueta-bate-papo-online-como-conversar-respeito': '<h2>Quando é melhor sair da conversa</h2><p>Encerrar uma interação também é uma habilidade social. Você pode dizer “foi bom conversar, mas vou sair agora” sem justificar cada detalhe. Se a pessoa insistir, repita o limite uma vez e use o bloqueio. Não é falta de educação proteger seu tempo, sua privacidade e sua segurança. Em um ambiente de chat online brasil, milhares de estilos convivem; uma conversa que não funciona hoje não precisa virar conflito.</p>',
'chat-online-por-interesses-encontrar-pessoas-parecidas': '<h2>Da primeira afinidade à amizade</h2><p>Depois de algumas conversas, proponha uma atividade leve ligada ao interesse: trocar recomendações de livros, comentar um campeonato, montar uma playlist ou conversar sobre um filme. Atividades dão um objetivo à interação sem exigir confidências. Observe se o vínculo é recíproco e se você se sente confortável. Fazer amigos online é um processo, não uma corrida por quantidade de contatos.</p>',
'chat-online-acessibilidade-pessoas-deficiencia-conversar': '<h2>Inclua sem criar um espetáculo</h2><p>Uma comunidade acessível não coloca a pessoa com deficiência no papel de professora o tempo todo. Pergunte quando precisar, agradeça a orientação e aprenda com consistência. Também vale lembrar que acessibilidade beneficia pessoas temporariamente lesionadas, quem está em um ambiente barulhento, quem tem internet limitada e quem simplesmente prefere ler. Quanto mais opções de comunicação existirem, mais pessoas conseguem participar com autonomia.</p>'}
for x in d:
    if x['slug'] in extras and not any(k in x['content'] for k in ['Quando é melhor sair','Da primeira afinidade','Inclua sem criar']):
        x['content']=x['content'].replace('<h2>Conclusão</h2>',extras[x['slug']]+'<h2>Conclusão</h2>')
        x['wordCount']=len(x['content'].replace('<',' <').split())
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print([(x['slug'],x['wordCount']) for x in d[-3:]])
