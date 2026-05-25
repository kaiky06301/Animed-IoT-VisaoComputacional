# Roteiro do Vídeo Pitch — IoT / Visão Computacional (Animed)

**Duração alvo:** ~5 minutos · **720p ou mais** · com **narração do grupo** (o enunciado penaliza vídeo 100% feito por IA — o grupo precisa aparecer/falar).

---

## 1. Abertura (~40s)
- "Olá, somos o grupo do projeto **Animed**, solução para o Challenge da empresa parceira **Clyvo VET**."
- Apresentem os integrantes (nome + RM).
- "Nosso módulo de IoT/IA é um sistema de **Visão Computacional para Reconhecimento de Pets**."

## 2. O problema (~40s)
- A jornada de cuidado do pet é fragmentada; o tutor esquece de registrar visitas e as clínicas/pet shops perdem recorrência.
- "E se o próprio ambiente reconhecesse o pet **automaticamente**?"

## 3. A solução + por que essa tecnologia (~60s)
- Visão computacional reconhece **cães e gatos** pela câmera.
- Aplicação no Animed: **check-in automático** em pet shops/clínicas parceiras → gera pontos de gamificação sem esforço do tutor; e base para **monitorar bem-estar**.
- Justificativa: usa **câmeras comuns** (sem hardware caro) para automatizar o reconhecimento.

## 4. Tecnologias (~40s)
- **Python + YOLOv8 (Ultralytics)**, modelo pré-treinado no dataset **COCO**; **OpenCV** para imagem/câmera.
- Detecta as classes `cat`/`dog` e desenha *bounding boxes* com a confiança.

## 5. Demonstração funcional (~90s) — PARTE MAIS IMPORTANTE
- Rode na tela e narre:
  ```bash
  python detectar_pets.py --fonte exemplos/pet.jpg
  ```
- Abra a imagem `resultados/deteccao_1.jpg` e mostre a caixa com **`dog 0.82`**.
- (Bônus impressionante) Rode pela webcam e aponte para uma foto de pet:
  ```bash
  python detectar_pets.py --fonte 0
  ```

## 6. Viabilidade + próximos passos (~30s)
- Prova de conceito **funcionando hoje**; próximos passos: integração com a API Animed (check-in + pontos), fine-tuning de raças, câmera de borda (*edge*).

## 7. Encerramento (~20s)
- "Esse foi o protótipo de visão computacional do Animed. Obrigado!"

---

### Checklist antes de publicar
- [ ] Vídeo em 720p+ com narração clara
- [ ] O grupo aparece/fala (não pode ser 100% IA)
- [ ] Publicado no YouTube em **modo Não Listado**
- [ ] Link colado em `ENTREGA_IOT_ANIMED.txt`
