from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from baseclass.dashboard import DashBoard
from baseclass.mainrtp import MainRtp
from baseclass.settingsscreen import SettingsScreen
from baseclass.ultimo import Ultimo
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt 
import math

class MyApp(MDApp):
    def build(self):
        self.title="primera app"
        self.theme_cls.primary_palette="Green"
        self.name_archivo="exp_5.png"
        self.temp_archivo="temp_"+self.name_archivo
        self.temp_matriz=[]
        self.temp_image= cv2.imread(self.name_archivo)
        cv2.imshow('imagen inicial',self.temp_image)
        cv2.imwrite('./'+self.temp_archivo,self.temp_image)
        return Builder.load_file("main.kv")
    def save(self):
        cv2.imwrite('./out_'+self.name_archivo,self.temp_matriz)
        

MyApp().run()