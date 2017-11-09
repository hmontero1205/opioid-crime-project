from appJar import gui
import pip as p
import dataGrapher as d
import random

p.main(['install', 'appJar'])

def press(button):
    if button == "Close":
        window.stop()
    if button == "Search":
        d.pylab.clf()
        windowId = random.randrange(1,100000)
        zipCode = window.getEntry("ZipCode")
        window.startSubWindow(str(windowId) + " Crimes")
        d.plotCrimeData(zipCode)
        window.addImage(str(windowId) + "c", 'images/crimes.png')
        window.stopSubWindow()
        window.startSubWindow(str(windowId) + " Deaths")
        d.plotOpioidData(zipCode)
        window.addImage(str(windowId) + "d", "images/deaths.png")
        window.showSubWindow(str(windowId) + " Crimes")
        window.showSubWindow(str(windowId) + " Deaths")
    if button == "Lowest":
        d.pylab.clf()
        zipCode = '80104'
        windowId = random.randrange(1,100000)
        window.startSubWindow(str(windowId) + " Crimes")
        d.plotCrimeData(zipCode)
        window.addImage(str(windowId) + "c", 'images/crimes.png')
        window.stopSubWindow()
        window.startSubWindow(str(windowId) + " Deaths")
        d.plotOpioidData(zipCode)
        window.addImage(str(windowId) + "d", "images/deaths.png")
        window.showSubWindow(str(windowId) + " Crimes")
        window.showSubWindow(str(windowId) + " Deaths")
    if button == "Highest":
        d.pylab.clf()
        zipCode = '34601'
        windowId = random.randrange(1,100000)
        window.startSubWindow(str(windowId) + " Crimes")
        d.plotCrimeData(zipCode)
        window.addImage(str(windowId) + "c", 'images/crimes.png')
        window.stopSubWindow()
        window.startSubWindow(str(windowId) + " Deaths")
        d.plotOpioidData(zipCode)
        window.addImage(str(windowId) + "d", "images/deaths.png")
        window.showSubWindow(str(windowId) + " Crimes")
        window.showSubWindow(str(windowId) + " Deaths")
window = gui("Opioid Crisis Tool", "400x400")
window.addLabel("title", "Opioid Deaths vs Crime")
window.setFont(25)
window.addEntry("ZipCode")
window.setEntryDefault("ZipCode", "Input the zip code here")
window.addButtons( ["Search", "Highest", "Lowest", "Close"], press, colspan=2)
window.go()
