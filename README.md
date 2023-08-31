# Cam - Mouse: Controle de Mouse por Gestos

Cam - Mouse é um projeto Python que permite controlar o cursor do mouse usando gestos capturados por uma webcam. O projeto utiliza as bibliotecas OpenCV, Mediapipe e PyAutoGUI para realizar a detecção de mãos, interpretar os gestos e interagir com o sistema operacional para realizar ações do mouse.

## WARNING!

Do you need pratice from using this project.

This gestures used is [here](https://github.com/ahmed-0egy/Hand-Gesture-Recognition-for-Cursor-Controlling/tree/main/gestures)

## Bibliotecas Necessárias

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [Mediapipe](https://mediapipe.dev/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)

## Objetivos

- Integrar o projeto com sistemas operacionais Windows e Linux.
- Implementar um sistema de calibração automática para otimizar a detecção de gestos.
- Daemonizar o aplicativo para execução em segundo plano.

## Como Funciona

1. O projeto utiliza o OpenCV para capturar o fluxo de vídeo da webcam.
2. Uma calibração automática é realizada inicialmente para determinar o fundo vazio.
3. A biblioteca Mediapipe é utilizada para detectar a mão e seus landmarks.
4. Os gestos da mão são interpretados com base nos landmarks e movimentos.
5. Os movimentos da mão são convertidos em movimentos do mouse e cliques usando o PyAutoGUI.
6. O aplicativo é projetado para ser compatível tanto com Windows quanto Linux.

## Executando o Projeto

1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale as bibliotecas necessárias executando o comando `pip install opencv-python mediapipe pyautogui`.
3. Execute o código principal do projeto.

```bash
python main.py
```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

## Licença

Este projeto é licenciado sob a Licença BSD3.
