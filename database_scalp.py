from tkinter import *
import sys
global saves
global linesperobj
linesperobj=3

class website_dataobj():
    website_name=""
    addcartbutton=""
    checkoutbutton=""
    def __init__(self, x, y, z):
        self.setwebsite(x)
        self.setaddcart(y)
        self.setcheckout(z)
        
    def setaddcart(self, x):
        self.addcartbutton=x
    def setcheckout(self, x):
        self.checkoutbutton=x
    def setwebsite(self, x):
        self.website_name=x
    def getaddcart(self):
        return self.addcartbutton
    def getcheckout(self):
        return self.checkoutbutton
    def getwebsite(self):
        return self.website_name
def main():
    global saves
    saves=open("scalper_website_info", "r+")
def getsaves():
    global saves
    listobj=saves.readlines()
    return listobj
def converttoobj(stuff, num_start):
    global linesperobj
    obj=website_dataobj(stuff[num_start], stuff[num_start+1], stuff[num_start+2])
    return obj
    #obj_data_send=[]
    """for s in range(num_start, num_start+linesperobj):
        
        obj_data_send.append(stuff[s])"""
def initconnverttoobj(stuff):
    obj_data_send=[]
    s=0
    while s < len(stuff):
        obj_data_send.append(converttoobj(stuff, s))
        s+3
    return obj_data_send