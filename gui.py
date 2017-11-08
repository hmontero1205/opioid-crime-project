from appJar import gui
import dataGrapher as d

def press(button):
    if button == "Close":
        window.stop()
    if button == "Search":
        d.pylab.clf()
        zipCode = window.getEntry("ZipCode")
        window.startSubWindow(str(zipCode) + " Crimes")
        d.plotCrimeData(zipCode)
        window.addImage(str(zipCode) + "c", 'crimes.png')
        window.stopSubWindow()
        window.startSubWindow(str(zipCode) + " Deaths")
        d.plotOpioidData(zipCode)
        window.addImage(str(zipCode) + "d", "deaths.png")
        window.showSubWindow(str(zipCode) + " Crimes")
        window.showSubWindow(str(zipCode) + " Deaths")
    if button == "Lowest":
        d.pylab.clf()
        zipCode = '80104'
        window.startSubWindow(str(zipCode) + " Crimes")
        d.plotCrimeData(zipCode)
        window.addImage(str(zipCode) + "c", 'crimes.png')
        window.stopSubWindow()
        window.startSubWindow(str(zipCode) + " Deaths")
        d.plotOpioidData(zipCode)
        window.addImage(str(zipCode) + "d", "deaths.png")
        window.showSubWindow(str(zipCode) + " Crimes")
        window.showSubWindow(str(zipCode) + " Deaths")
    if button == "Highest":
        d.pylab.clf()
        zipCode = '34601'
        window.startSubWindow(str(zipCode) + " Crimes")
        d.plotCrimeData(zipCode)
        window.addImage(str(zipCode) + "c", 'crimes.png')
        window.stopSubWindow()
        window.startSubWindow(str(zipCode) + " Deaths")
        d.plotOpioidData(zipCode)
        window.addImage(str(zipCode) + "d", "deaths.png")
        window.showSubWindow(str(zipCode) + " Crimes")
        window.showSubWindow(str(zipCode) + " Deaths")
window = gui("Opioid Crisis Tool", "400x400")
window.addLabel("title", "Opioid Deaths vs Crime")
window.setFont(25)
window.addEntry("ZipCode")
window.setEntryDefault("ZipCode", "Input the zip code here")
window.addButtons( ["Search", "Highest", "Lowest", "Close"], press, colspan=2)
window.go()
