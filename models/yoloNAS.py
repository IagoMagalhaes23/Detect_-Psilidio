'''
    Yolo NAS
    Autores: Iago Magalhães, Larissa Ferreira e Iális Calvalcante
    Data: 13/05/2024
    Descrição: Classe para treinamento do modelo customizado do Yolo NAS.
'''

import os
from IPython.display import Image

class YoloV9():
    def __init__(self, **kw):
        super().__init__(**kw)
        self.yoloVersion = ''
        self.dataset = ''
        self.epochs = 10
        self.matrizConfusao = ''
        self.results = ''
        self.valBatch = ''
        self.model = ''
        self.conf = 0.25
        self.datasetTest = ''

    def configYoloV9(self):
        '''
        
        '''
        os.system('')
    
    def trainYoloV9(self):
        '''
            Function trainYoloV9
            Chama a função para treinamento do Yolo V9.
            :param yoloVersion: recebe a versão e formato do Yolo que será treinada;
            :param dataset: recebe o caminho do arquivo data.yaml;
            :param epochs: recebe o número de épocas para o treinamento;
            :return: retorna o modelo do Yolo V9 treinado com o dataset customizado.
        '''
        os.system('yolo task=detect mode=train model={self.yoloVersion} data={self.dataset} epochs={self.epochs} imgsz=640 plots=True')
        %cd {HOME}/yolov9

!python train.py \
--batch 16 --epochs 25 --img 640 --device 0 --min-items 0 --close-mosaic 15 \
--data {dataset.location}/data.yaml \
--weights {HOME}/weights/gelan-c.pt \
--cfg models/detect/gelan-c.yaml \
--hyp hyp.scratch-high.yaml
    
    def plotMC(self):
        '''
            Function plotMC
            Exibe a matriz de confusão gerada com o treinamento do modelo customizado
            :param matrizConfusao: recebe o caminho do arquivo da matriz de confusão;
            :return: retorna a imagem da matriz de confusão do Yolo V9 treinado com o dataset customizado.
        '''
        Image(filename=f'{self.matrizConfusao}', width=600)
        Image(filename=f"{HOME}/yolov9/runs/train/exp/confusion_matrix.png", width=1000)
    
    def plotResults(self):
        '''
            Function plotResults
            Exibe os resultados de diferentes métricas geradas com o treinamento do modelo customizado
            :param results: recebe o caminho do arquivo da imagem de resultados;
            :return: retorna a imagem dos resultados do Yolo V9 treinado com o dataset customizado.
        '''
        Image(filename=f'{self.results}', width=600)
        Image(filename=f"{HOME}/yolov9/runs/train/exp/results.png", width=1000)
    
    def plotVal(self):
        '''
            Function plotVal
            Exibe uma pequena amostra das detecções geradas com o modelo customizado
            :param valBatch: recebe o caminho do arquivo da matriz de confusão;
            :return: retorna a imagem da ValBatch do Yolo V9 treinado com o dataset customizado.
        '''
        Image(filename=f'{self.valBatch}', width=600)
        Image(filename=f"{HOME}/yolov9/runs/train/exp/val_batch0_pred.jpg", width=1000)
    
    def testModel(self):
        '''
            Function testModel
            Testa o modelo customizado com imagens do conjunto de teste
            :param model: recebe o caminho do arquivo do modelo customizado;
            :param dataset: recebe o caminho do arquivo data.yaml;
            :return: retorna algumas métricas do Yolo V9 treinado com o dataset customizado.
        '''
        os.system('yolo task=detect mode=val model={self.model} data={self.dataset}')
        !python val.py \
--img 640 --batch 32 --conf 0.001 --iou 0.7 --device 0 \
--data {dataset.location}/data.yaml \
--weights {HOME}/yolov9/runs/train/exp/weights/best.pt
    
    def predictModel(self):
        '''
            Function predictModel
            Realiza predições com o modelo customizado com imagens do conjunto de teste
            :param model: recebe o caminho do arquivo do modelo customizado;
            :param conf: recebe o valor de confiaça do modelo;
            :param datasetTest: recebe o caminho da pasta para as imagens de teste/validação;
            :return: retorna a quantidade de detecções, boundbox e o tempo para a detecção com Yolo V9 treinado com o dataset customizado.
        '''
        os.system('!yolo task=detect mode=predict model={self.model} conf={self.conf} source={self.datasetTest} save=True')
        !python detect.py \
--img 1280 --conf 0.1 --device 0 \
--weights {HOME}/yolov9/runs/train/exp/weights/best.pt \
--source {dataset.location}/test/images