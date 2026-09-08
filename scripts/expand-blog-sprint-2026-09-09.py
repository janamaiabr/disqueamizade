import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'public/blog-posts/index.json'
d=json.loads(p.read_text())
extra='''<h2>Como participar sem forçar a conexão</h2><p>Uma conversa online não precisa produzir amizade imediata para ter valor. Às vezes, você encontra uma informação útil, escuta uma experiência diferente ou passa alguns minutos com mais leveza. Entre com uma expectativa modesta: fazer uma pergunta, responder com atenção e perceber se existe reciprocidade. Se a pessoa responde apenas com monossílabos, muda de assunto constantemente ou demonstra desconforto, respeite o ritmo e não pressione.</p><p>Também vale lembrar que o contexto muda a qualidade do diálogo. Uma sala movimentada pode ser ótima para descobrir assuntos, enquanto uma conversa mais calma favorece histórias longas. Teste horários diferentes e observe quais ambientes combinam com você. O chat deve ampliar suas possibilidades, não criar uma obrigação de estar disponível o tempo todo.</p><h2>Segurança para continuar conversando</h2><p>Use um apelido se isso deixar você mais confortável, mantenha suas senhas privadas e desconfie de pedidos urgentes de dinheiro, códigos ou documentos. Não clique em links suspeitos e não aceite pressão para levar a conversa imediatamente para outro aplicativo. Caso alguém ultrapasse seus limites, encerre o contato, bloqueie e denuncie conforme os recursos disponíveis. Essas atitudes protegem você e ajudam a manter a comunidade saudável.</p>'''
slugs=['chat-online-trocar-livros-leitores-brasil','chat-online-condominio-vizinhos-convivencia-brasil','chat-online-historia-brasil-conversar-epocas']
for x in d:
 if x['slug'] in slugs:
  x['body']=x['body'].replace('<h2>Conclusão</h2>',extra+'<h2>Conclusão</h2>')
  x['content']=x['body']; x['wordCount']=len(x['body'].replace('<',' <').split()); x['readTime']=max(6,round(x['wordCount']/155))
  (ROOT/'public/blog-posts'/f"{x['slug']}.html").write_text(x['body'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print([(x['slug'],x['wordCount']) for x in d if x['slug'] in slugs])
