from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt 
import math
class Ultimo(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.app=MDApp.get_running_app()
        self.sub_title = "Operador "
        self.texto_raw = "ingresar"
        self.imagen=self.app.temp_archivo
    def llamada(self):
        self.app.inicio()
    def pixel(self,lst):
        return((float(lst[0])+float(lst[1])+float(lst[2]))/3)
    def op_exp(self,imname,b,c):
        b=int(b)
        c=int(c)
        img = cv2.imread(imname)
        if img is not None:
            #creamos una imagen en negro
            out=np.zeros(shape=img.shape,dtype=np.uint8)

            #aplicamos el Histogram equalization en los 3 canales
            for i in range(len(img[0][0])):
                for j in range(img.shape[0]):
                    for k in range(img.shape[1]):
                        vtmp=c*((b**img[j][k][i])-1)
                        if vtmp>255:
                            vtmp=255
                        if vtmp<0:
                            vtmp=0
                        out[j][k][i]=vtmp

            self.app.temp_matriz=out
            cv2.imshow('imagen final',out)
            cv2.waitKey()
            cv2.imwrite('./'+imname,out)
    def op_rtp(self,imname,c,r):
        img = cv2.imread(imname)
        if img is not None:
            #creamos una imagen en negro
            out=np.zeros(shape=img.shape,dtype=np.uint8)

            #aplicamos el Histogram equalization en los 3 canales
            for i in range(len(img[0][0])):
                for j in range(img.shape[0]):
                    for k in range(img.shape[1]):
                        vtmp=c*((img[j][k][i])**r)
                        if vtmp>255:
                            vtmp=255
                        if vtmp<0:
                            vtmp=0
                        out[j][k][i]=vtmp
            self.app.temp_matriz=out
            cv2.imshow('imagen final',out)
            cv2.waitKey()
            cv2.imwrite('./'+imname,out)