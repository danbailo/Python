#Code ----------------STARTS HERE--------------------------------

import tkinter as tk
from time import sleep

class mainframe(tk.Frame):
 def __init__(self, master):
  super().__init__(master)
  self.master = master
  self.bg = "black"
  self.pack()
  self.setwidgets()
  self.config(bg = "#111111")
  self.place(x = 0, y = 0, width = 170, height = 230)
  self.chance = 0
  self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  

 def packall(self):
  for x in self.buttonlist:
   x.pack()

 def resettheicons(self):
  for x in self.buttonlist:
   x.config(text = "")
  self.chance = 0
  self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  print(self.result)

 def resetthescore(self):
  self.resettheicons()
  self.result = [0, 0]
  self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))

 def checkvictory(self):
  if self.state[0] == 1 and self.state[3] == 1 and self.state[6] == 1:
   self.result[0] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("X has \n won.")
  elif self.state[0] == 2 and self.state[3] == 2 and self.state[6] == 2:
   self.result[1] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("O has \n won.")

  elif self.state[1] == 1 and self.state[4] == 1 and self.state[7] == 1:
   self.result[0] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("X has \n won.")
  elif self.state[1] == 2 and self.state[4] == 2 and self.state[7] == 2:
   self.result[1] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("O has \n won.")

  elif self.state[2] == 1 and self.state[5] == 1 and self.state[8] == 1:
   self.result[0] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("X has \n won.")
  elif self.state[2] == 2 and self.state[5] == 2 and self.state[8] == 2:
   self.result[1] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("O has \n won.")
  
  elif self.state[0] == 1 and self.state[1] == 1 and self.state[2] == 1:
   self.result[0] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("X has \n won.")
  elif self.state[0] == 2 and self.state[1] == 2 and self.state[2] == 2:
   self.result[1] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("O has \n won.")

  elif self.state[3] == 1 and self.state[4] == 1 and self.state[5] == 1:
   self.result[0] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("X has \n won.")
  elif self.state[3] == 2 and self.state[4] == 2 and self.state[5] == 2:
   self.result[1] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("O has \n won.")

  elif self.state[6] == 1 and self.state[7] == 1 and self.state[8] == 1:
   self.result[0] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("X has \n won.")
  elif self.state[6] == 2 and self.state[7] == 2 and self.state[8] == 2:
   self.result[1] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("O has \n won.")

  elif self.state[0] == 1 and self.state[4] == 1 and self.state[8] == 1:
   self.result[0] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("X has \n won.")
  elif self.state[0] == 2 and self.state[4] == 2 and self.state[8] == 2:
   self.result[1] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("O has \n won.")

  elif self.state[6] == 1 and self.state[4] == 1 and self.state[2] == 1:
   self.result[0] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("X has \n won.")
  elif self.state[6] == 2 and self.state[4] == 2 and self.state[2] == 2:
   self.result[1] += 1
   self.score.config(text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]))
   self.resettheicons()
   self.showmessage("O has \n won.")

  elif self.state[0] != 0 and self.state[1] != 0 and self.state[2] != 0 and self.state[3] != 0 and self.state[4] != 0 and self.state[5] != 0 and self.state[6] != 0 and self.state[7] != 0 and self.state[8] != 0:
   self.resettheicons()
   self.showmessage("It is\n a tie.")
  else:
   pass
  

 def showmessage(self, message):
  self.labelx = tk.Label(text = "{}".format(message), fg = "white", bg = "black", font = ("calibri", 45))
  self.labelx.place(x = 0, y = 0, width = 170, height = 230)
  self.labelx.bind("<Button-1>", lambda x: self.labelx.destroy() )
 
 def changestate(self, button):
  print(str(button))
  if self.chance == 0 or self.chance == 1:
   if self.state[button] == 0:
    self.buttonlist[button].config(text = "X")
    self.state[button] = 1
    self.chance = 2
   else:
    pass

  elif self.chance == 0 or self.chance == 2:
   if self.state[button] == 0:
    self.buttonlist[button].config(text = "O")
    self.state[button] = 2
    self.chance = 1
   else:
    pass
  else:
   raise "There is a bloody error."

  self.checkvictory()

  
 def setwidgets(self):
  self.buttonlist = []
  for x in range(9):
   self.buttonlist.append(tk.Button(self, text = "", fg = "white", bg = "black", relief = "flat"))
   self.buttonlist[x].config(font = ("TimesNewRoman", 20))

    
  self.packall()
  self.result = [0, 0]

  self.buttonlist[0].place(x = 5, y = 5, height = 50, width = 50)
  self.buttonlist[0].config(command = lambda: self.changestate(0))

  self.buttonlist[1].place(x = 5, y = 60, height = 50, width = 50)
  self.buttonlist[1].config(command = lambda: self.changestate(1))

  self.buttonlist[2].place(x = 5, y = 115, height = 50, width = 50)
  self.buttonlist[2].config(command = lambda: self.changestate(2))


  self.buttonlist[3].place(x = 60, y = 5, height = 50, width = 50)
  self.buttonlist[3].config(command = lambda: self.changestate(3))

  self.buttonlist[4].place(x = 60, y = 60, height = 50, width = 50)
  self.buttonlist[4].config(command = lambda: self.changestate(4))

  self.buttonlist[5].place(x = 60, y = 115, height = 50, width = 50)
  self.buttonlist[5].config(command = lambda: self.changestate(5))


  self.buttonlist[6].place(x = 115, y = 5, height = 50, width = 50)
  self.buttonlist[6].config(command = lambda: self.changestate(6))

  self.buttonlist[7].place(x = 115, y = 60, height = 50, width = 50)
  self.buttonlist[7].config(command = lambda: self.changestate(7))

  self.buttonlist[8].place(x = 115, y = 115, height = 50, width = 50)
  self.buttonlist[8].config(command = lambda: self.changestate(8))

  self.score = tk.Label(self, text = "{}".format(self.result[0]) + " : " + "{}".format(self.result[1]), bg = "black", fg = "white", font = ("Courier", 20))
  self.score.pack()
  self.score.place(x = 5, y = 170, height = 50, width = 105)

  self.reset = tk.Button(self, text = "RESET", bg = "black", fg = "white", command = lambda: self.resetthescore())
  self.reset.pack()
  self.reset.place(x = 115, y = 170, height = 50, width = 50)



root = tk.Tk()
root.config(height = 230, width = 170)
root.resizable(0, 0)
root.geometry("170x230")
app = mainframe(master = root)
app.mainloop()

#CODE ---------------------------------------ENDS HERE---------------------------------------------
