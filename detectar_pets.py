"""
Animed - Reconhecimento de Pets (Visao Computacional)
Challenge FIAP 2026 - Disruptive Architectures: IoT, IoB & Generative IA
Projeto Animed - solucao para o Challenge da empresa parceira Clyvo VET.

Detecta caes e gatos em imagens ou pela webcam usando YOLOv8 (pre-treinado COCO),
desenhando bounding boxes com a confianca de cada deteccao.

Uso no ecossistema Animed:
  - Check-in automatico do pet em pet shops/clinicas parceiras (gera pontos).
  - Base para monitoramento de bem-estar do animal.
"""
import argparse
import os

import cv2
from ultralytics import YOLO

# Classes COCO de interesse para o Animed
CLASSES_PET = {"cat": "Gato", "dog": "Cachorro"}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Animed - Reconhecimento de Pets (Visao Computacional)"
    )
    parser.add_argument(
        "--fonte", "-f", default="exemplos/pet.jpg",
        help="Imagem/video ou '0' para webcam. Padrao: exemplos/pet.jpg",
    )
    parser.add_argument(
        "--conf", type=float, default=0.4,
        help="Confianca minima da deteccao (0 a 1). Padrao: 0.4",
    )
    args = parser.parse_args()

    print("[Animed] Carregando modelo YOLOv8n (pre-treinado COCO)...")
    modelo = YOLO("yolov8n.pt")  # baixa automaticamente na 1a execucao

    fonte = 0 if args.fonte == "0" else args.fonte
    webcam = fonte == 0

    print(f"[Animed] Detectando pets em: {args.fonte}")
    resultados = modelo.predict(source=fonte, conf=args.conf, show=webcam, verbose=False)

    os.makedirs("resultados", exist_ok=True)
    indice = 0
    for r in resultados:
        nomes = r.names
        contagem = {}
        for c in r.boxes.cls.tolist():
            classe = nomes[int(c)]
            if classe in CLASSES_PET:
                rotulo = CLASSES_PET[classe]
                contagem[rotulo] = contagem.get(rotulo, 0) + 1

        if contagem:
            resumo = ", ".join(f"{v}x {k}" for k, v in contagem.items())
            print(f"[Animed]  Pet(s) reconhecido(s): {resumo}")
        else:
            print("[Animed]  Nenhum pet (cao/gato) reconhecido neste frame.")

        if not webcam:
            indice += 1
            anotada = r.plot()  # numpy BGR com as bounding boxes desenhadas
            destino = os.path.join("resultados", f"deteccao_{indice}.jpg")
            cv2.imwrite(destino, anotada)
            print(f"[Animed]  Imagem anotada salva em: {destino}")


if __name__ == "__main__":
    main()
