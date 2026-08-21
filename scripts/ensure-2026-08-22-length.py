import json, re
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'public/blog-posts/index.json'
data = json.loads(p.read_text())
extras = {
 'video-chat-gratis-poucos-dados-internet-limitada': '''<h2>Uma conversa boa não depende de pixels</h2><p>É fácil confundir qualidade técnica com qualidade humana. Imagem nítida ajuda, mas não substitui escuta, humor e respeito. Se a conexão estiver limitada, combine um formato simples e continue. Uma frase bem respondida por texto pode aproximar mais do que uma chamada travando a cada cinco segundos.</p><p>Antes de entrar, confira o saldo de dados e a bateria. Depois, encerre o aplicativo quando terminar, especialmente se ele continuar usando câmera ou microfone em segundo plano. Pequenos cuidados evitam surpresas na conta e deixam o próximo video chat mais tranquilo.</p>''',
 'bate-papo-online-no-transporte-publico-conversar-deslocamento': '''<h2>Respeite também quem está ao redor</h2><p>Conversa pública precisa considerar o espaço compartilhado. Fale baixo, use fones e evite conteúdo que possa constranger passageiros. Se a chamada exigir concentração, espere chegar ao destino. O bate-papo deve melhorar o seu deslocamento sem transformar a viagem de outras pessoas em parte involuntária da conversa.</p><p>Quando você mantém limites claros, o transporte vira apenas o contexto, não o centro da interação. A cidade continua sendo observada, o celular permanece sob controle e a conversa pode continuar depois, em um ambiente mais confortável.</p>''',
 'fazer-amigos-online-trabalho-turnos-rotina-invertida': '''<h2>Amizade também cabe na recuperação</h2><p>Uma rotina invertida costuma cobrar um preço físico. Sono, alimentação e descanso não devem ser sacrificados para manter uma conversa. Avise seus contatos quando estiver encerrando e aceite que uma amizade madura não exige presença permanente. A pessoa certa entende que sua disponibilidade varia.</p><p>Com o tempo, você pode encontrar um pequeno grupo que conhece esse ritmo: alguém que responde no café da manhã, outra pessoa que aparece na madrugada e alguém que conversa nas folgas. Essa previsibilidade leve cria pertencimento sem transformar o chat em mais uma escala de trabalho.</p>'''
}
for post in data:
    if post.get('slug') in extras:
        post['content'] += extras[post['slug']]
        post['wordCount'] = len(re.sub('<[^>]+>', ' ', post['content']).split())
        post['readTime'] = max(6, round(post['wordCount'] / 155))
p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print([(x['slug'], x['wordCount']) for x in data if x.get('slug') in extras])
