# Detector de Psilidio em goiabeiras

## Introdução
O seguinte projeto visa desenvolver um detector de objetos para identificação de ataque de psilidios em goiabeiras. Buscando identificar áreas atigindas (folhas) por estes insetos e classificar se ou ocorreu ou não ataque. Assim, será possível auxiliar produtores na identificação desta praga de forma automatizada.

## Objetivos

### Objetivo Geral
- Desenvolver um aplicativo para identificação de ataque de psilidos em goiabeiras com base em técnicas de Deep Learning.

### Objetivos especificos
- Montar dataset com imagens de folhas de goiabeira que sofreram ataque de psilidios;
- Avaliar melhores técnicas para expansão de dataset;
- Avaliar desempenho das redes CNN: Yolo V5, Yolo V8, Yolo V9, Yolo NAS, Detectron 2 e ViT;
- Aplicar algoritmo de Grad CAM para visualização de áreas utilizadas pela rede para classificação;
- Desenvolvimento de um APP simples para aquisição de imagens e exibição de resultados.

## Dataset
- Original
- Editado

## Como usar
- 

## Roteiro de atividades
- [x] Coleta do dataset
- [x] Marcação dos das folhas doentes com Roboflow
- [x] Estrutura para leitura das imagens
- [x] Reprodução dos algortimos para detecção de imagens
- [x] Análise dos resultados
- [X] Utilização do EigenCAM para rede com melhor desempenho

## Fluxograma de trabalho
<img src="assets/Fluxograma de projeto.png">

## Metodologia
Avaliar desempenho dos modelos com base nas métricas:
- Precisão média (AP): A AP calcula a área sob a curva de precisão-recuperação, fornecendo um valor único que engloba o desempenho de precisão e recuperação do modelo.
- Precisão média média (mAP): A mAP alarga o conceito de AP calculando os valores médios de AP em várias classes de objectos. Isto é útil em cenários de deteção de objectos multi-classe para fornecer uma avaliação abrangente do desempenho do modelo.
- Pontuação F1: A pontuação F1 é a média harmónica da precisão e da recuperação, fornecendo uma avaliação equilibrada do desempenho de um modelo, considerando tanto os falsos positivos como os falsos negativos.
- Curva de precisão-recuperação (PR_curve.png): Uma visualização integral para qualquer problema de classificação, esta curva mostra os compromissos entre a precisão e a recuperação em limites variados. Torna-se especialmente significativa quando lida com classes desequilibradas.
- P (Precisão): A precisão dos objectos detectados, indicando quantas detecções estavam correctas.
- R (Recall): A capacidade do modelo para identificar todas as instâncias de objectos nas imagens.
- mAP50: Precisão média calculada com um limiar de intersecção sobre união (IoU) de 0,50. É uma medida da precisão do modelo considerando apenas as detecções "fáceis".
- mAP50-95: A média da precisão média calculada em diferentes limiares de IoU, variando de 0,50 a 0,95. Dá uma visão abrangente do desempenho do modelo em diferentes níveis de dificuldade de deteção.

## Resultados

## Conclusão

## Autores
- [Iago Magalhães](https://github.com/IagoMagalhaes23)
- [Larissa Rodrigues](https://larissafrodrigues.github.io/)

## Links úteis
- [Overleaf](https://www.overleaf.com/6564786631gxyfgcwkvtrk#edd727)
- [Roboflow](https://universe.roboflow.com/mucosas/psilidios-em-goiabeiras)
- [YOLO Métricas de desempenho](https://docs.ultralytics.com/pt/guides/yolo-performance-metrics/#conclusion)
