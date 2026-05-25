# Animed - Reconhecimento de Pets (Visão Computacional)

Protótipo de **Visão Computacional** para o Challenge FIAP 2026 — disciplina **Disruptive Architectures: IoT, IoB & Generative IA (1ª Sprint)**.

Projeto **Animed** — solução para o Challenge da empresa parceira **Clyvo VET**.

## 🎯 Ideia central

O Animed transforma o cuidado com o pet em uma jornada contínua e gamificada. Este módulo de **visão computacional** reconhece automaticamente **cães e gatos** em imagens ou pela câmera, habilitando dois usos no ecossistema:

- **Check-in automático em pet shops/clínicas parceiras:** a câmera identifica o pet e registra a visita, gerando pontos de gamificação sem o tutor precisar fazer nada.
- **Monitoramento de bem-estar:** base para futuras análises de comportamento do pet (integração com as "coleiras inteligentes" do roadmap).

> O próprio enunciado sugere **"Reconhecimento Pet"** como exemplo de aplicação de visão computacional.

## 👥 Integrantes
- Erick Bernardes Bradaschia — RM 565733
- Gabriel Santos Claudino — RM 564054
- Jonathan Moreira Gomes — RM 565060
- Kaiky de Oliveira Silva (líder) — RM 566067
- Lucas Fortes de Lima — RM 559523

## 🧰 Tecnologias utilizadas
- **Python 3**
- **YOLOv8** (Ultralytics) — detecção de objetos, modelo pré-treinado no dataset **COCO**
- **OpenCV** — leitura de imagem/câmera e renderização visual

A detecção usa as classes COCO `cat` (gato) e `dog` (cachorro), desenhando *bounding boxes* com a confiança de cada detecção.

## ▶️ Como executar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Detectar em uma imagem (padrão)
```bash
python detectar_pets.py --fonte exemplos/pet.jpg
```
A imagem anotada é salva em `resultados/` (ex.: `deteccao_1.jpg`).

### 3. Detectar pela webcam (ao vivo)
```bash
python detectar_pets.py --fonte 0
```
Aponte a câmera para um pet (ou uma foto) — as caixas aparecem em tempo real. Pressione `q` para sair.

**Parâmetros:** `--fonte`/`-f` (imagem, vídeo ou `0` para webcam) · `--conf` (confiança mínima, padrão `0.4`).

## 📊 Resultados parciais
Rodando sobre `exemplos/pet.jpg`, o modelo reconhece o pet e gera a imagem anotada `resultados/deteccao_1.jpg`, com a *bounding box* e o rótulo + confiança (ex.: `dog 0.82`). O terminal também imprime um resumo dos pets reconhecidos.

## 🗂️ Estrutura
```
.
├── detectar_pets.py     # script principal de detecção
├── requirements.txt     # dependências
├── exemplos/            # imagens de entrada (pet.jpg)
├── resultados/          # imagens anotadas (saída/evidência)
└── README.md
```

## 🚀 Próximas sprints
- Fine-tuning para raças específicas.
- Integração com a API Animed (check-in automático + pontos de gamificação).
- Embarque em câmera de borda (*edge*) na entrada dos parceiros.
