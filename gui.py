from appJar import gui
import pip as p
import dataGrapher as d
import random

p.main(['install', 'appJar'])
popUpNames = dict()
def press(button):
    global popUpNames
    if button == "Close":
        window.stop()
    if button == "Search":
        d.pylab.clf()
        windowId = random.randrange(1,100000)
        zipCode = window.getEntry("ZipCode")
        if not(str(zipCode).isdigit()):
            print("Invalid entry!")
            return
        if not(str(zipCode) in popUpNames.keys()):
            popUpNames[str(zipCode)] = 1
            extraText = ""
        else:
            extraText = "(" + str(popUpNames[str(zipCode)]) + ")"
            print(extraText)
            popUpNames[zipCode] += 1
            
        window.startSubWindow(str(zipCode) + " Crimes " + extraText)
        result = d.plotCrimeData(zipCode)
        if not(result):
            print("No crime data found!")
            return
        window.addImage(str(zipCode) + "c" + extraText, 'images/crimes.png')
        window.stopSubWindow()
        window.startSubWindow(str(zipCode) + " Deaths " + extraText)
        result = d.plotOpioidData(zipCode)
        if not(result):
            print("No opioid data found!")
            return
        window.addImage(str(zipCode) + "d" + extraText, "images/deaths.png")
        window.showSubWindow(str(zipCode) + " Crimes " + extraText)
        window.showSubWindow(str(zipCode) + " Deaths " + extraText)
    if button == "Lowest":
        d.pylab.clf()
        zipCode = '80104'
        
        if not(zipCode in popUpNames.keys()):
            popUpNames[zipCode] = 1
            extraText = ""
        else:
            extraText = "(" + str(popUpNames[zipCode]) + ")"
            popUpNames[zipCode] += 1
            
        windowId = random.randrange(1,100000)
        window.startSubWindow(str(zipCode) + " Crimes " + extraText)
        d.plotCrimeData(zipCode)
        window.addImage(str(zipCode) + "c" + extraText, 'images/crimes.png')
        window.stopSubWindow()
        window.startSubWindow(str(zipCode) + " Deaths " + extraText)
        d.plotOpioidData(zipCode)
        window.addImage(str(zipCode) + "d"+ extraText, "images/deaths.png")
        window.showSubWindow(str(zipCode) + " Crimes " + extraText)
        window.showSubWindow(str(zipCode) + " Deaths " + extraText)
    if button == "Highest":
        d.pylab.clf()
        zipCode = '34601'
        if not(zipCode in popUpNames.keys()):
            popUpNames[zipCode] = 1
            extraText = ""
        else:
            extraText = "(" + str(popUpNames[zipCode]) + ")"
            popUpNames[zipCode] += 1
        windowId = random.randrange(1,100000)
        window.startSubWindow(str(zipCode) + " Crimes " + extraText)
        d.plotCrimeData(zipCode)
        window.addImage(str(zipCode) + "c"+ extraText, 'images/crimes.png')
        window.stopSubWindow()
        window.startSubWindow(str(zipCode) + " Deaths" + extraText)
        d.plotOpioidData(zipCode)
        window.addImage(str(zipCode) + "d"+ extraText, "images/deaths.png")
        window.showSubWindow(str(zipCode) + " Crimes" + extraText)
        window.showSubWindow(str(zipCode) + " Deaths" + extraText)
window = gui("Opioid Crisis Tool", "400x400")
window.addLabel("title", "Opioid Deaths vs Crime")
window.setFont(25)
window.addEntry("ZipCode")
window.setEntryDefault("ZipCode", "Input the zip code here")
window.addButtons( ["Search", "Highest", "Lowest", "Close"], press, colspan=2)
window.go()
