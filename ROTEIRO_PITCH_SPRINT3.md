# Roteiro do Vídeo Pitch — Sprint 3 (IoT, IoB & Generative IA)

**Duração alvo: ~5 minutos** · Publicar no YouTube em modo **não listado** · Narração por voz

> Fala em tom de apresentação para banca, não de leitura. Cada bloco abaixo tem o tempo e o que precisa aparecer na tela.

---

## Bloco 1 — Abertura (0:00 – 0:30)

**Na tela:** capa com "Animed — Componente de IA" e os nomes/RMs do grupo.

**Fala:**
> "Boa tarde. Somos o grupo do projeto Animed, do Challenge da Clyvo VET. Nesta sprint a gente definiu qual é o componente de inteligência artificial da nossa solução, e é isso que eu vou apresentar: o problema que essa IA resolve, como ela funciona e o que ela muda para o tutor e para a clínica."

---

## Bloco 2 — O problema (0:30 – 1:20)

**Na tela:** a frase da Clyvo — *jornada fragmentada, episódica e reativa*.

**Fala:**
> "A Clyvo definiu a dor: a jornada de saúde do pet é fragmentada, episódica e reativa. O tutor só aparece quando o pet já está doente.
>
> O Animed já ataca isso com gamificação — cada cuidado vira ponto, o tutor sobe de nível e ganha desconto. Mas a gamificação tem um limite: ela recompensa o que o tutor lembrou de fazer. Ela não diz o que ele deveria fazer.
>
> Hoje, um Golden de 9 anos com sobrepeso e vacina atrasada recebe o mesmo lembrete que um SRD de 2 anos saudável. É aí que a jornada volta a ser genérica — e é exatamente esse buraco que a IA preenche."

---

## Bloco 3 — O que a IA faz (1:20 – 2:20)

**Na tela:** as três perguntas (do documento, seção 1).

**Fala:**
> "Nossa IA responde três perguntas que hoje ficam sem resposta.
>
> Para o tutor: o que eu devo fazer pelo meu pet nesta semana, e por quê.
>
> Para o doutor: quais dos meus pacientes estão com o risco subindo agora.
>
> E para os dois: como explicar isso de um jeito que o tutor entenda e aja.
>
> Ela faz isso calculando um Score de Risco Preventivo para cada pet, de 0 a 100, e devolvendo não só o número, mas o motivo: vacina vencida há tantos dias, ganho de peso de tanto por cento, tanto tempo sem consulta."

---

## Bloco 4 — A abordagem e o porquê (2:20 – 3:30)

**Na tela:** a tabela de justificativa (documento, seção 3).

**Fala:**
> "A gente escolheu uma arquitetura híbrida, em duas camadas, e isso foi decisão consciente.
>
> A primeira camada junta um motor de regras com um modelo preditivo. As regras cuidam do que é protocolo veterinário — prazo de vacina, vermifugação, periodicidade de check-up. O modelo preditivo cuida do que depende de padrão: tendência de peso, intervalo entre consultas, adesão do tutor.
>
> Por que não só um modelo? Por três motivos. Segurança clínica: saúde animal não admite recomendação inventada, prazo de vacina é norma, não predição. Explicabilidade: o doutor precisa saber por que aquele paciente subiu na fila. E dados escassos: um produto novo não tem histórico, e o motor de regras já funciona desde o primeiro pet cadastrado.
>
> A segunda camada é a IA generativa. Ela não decide o que é risco — ela comunica o que a primeira camada decidiu, em linguagem natural, no tom de conversa de mensageiro. Isso prende o modelo a fatos que vieram do banco e elimina o risco de alucinação clínica."

---

## Bloco 5 — Arquitetura e dados (3:30 – 4:20)

**Na tela:** o diagrama de fluxo do documento (seção 5).

**Fala:**
> "O fluxo é este. O tutor registra uma vacina no app. O app manda para a API, que grava no Oracle e credita os pontos. Esse evento dispara o recálculo do score: as regras conferem os protocolos, o modelo reavalia as tendências.
>
> O score volta com os motivos, a camada generativa transforma esses motivos em mensagem, e o tutor recebe a recomendação. Ao mesmo tempo, aquele pet muda de posição na fila de risco do painel do doutor.
>
> E tudo isso usa os dados que já modelamos nas sprints anteriores — as sete tabelas do nosso banco Oracle. Não precisamos coletar nada novo.
>
> O ciclo se fecha: a ação do tutor alimenta a IA, e a IA devolve a próxima ação. É isso que transforma a jornada de episódica em contínua."

---

## Bloco 6 — Benefícios e fechamento (4:20 – 5:00)

**Na tela:** os quatro benefícios (documento, seção 7).

**Fala:**
> "O que isso entrega: o tutor para de receber lembrete genérico e passa a receber orientação sobre o pet dele, explicada em linguagem comum. O pet deixa de depender só da memória do dono. A clínica age antes da emergência, o que recupera recorrência e reduz abandono de tratamento.
>
> E para a Clyvo, cada interação alimenta uma base longitudinal de saúde animal que nenhum concorrente tem — quanto mais o sistema é usado, mais preciso ele fica.
>
> Na Sprint 4 a gente implementa e integra esse componente. Obrigado."

---

## Checklist antes de gravar

- [ ] Documento aberto para mostrar o diagrama e as tabelas na tela
- [ ] Áudio claro, sem ruído de fundo
- [ ] Testar 1 minuto e ouvir antes de gravar tudo
- [ ] Publicar no YouTube como **não listado**
- [ ] Colocar o link no README e no .zip da entrega

## O que entregar no .zip

- Link do vídeo no YouTube (não listado)
- Link deste repositório no GitHub
- README atualizado apontando para o `DOCUMENTO_IA_SPRINT3.md`
