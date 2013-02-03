# Import Standard Libraries #
import os
import sys

# Import Third Party Libraries #
from wx import *
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
from wx import wizard as wiz
from wx.lib.wordwrap import wordwrap

name = ""
risk = ""

progVer = 1.0

class Diabeetus(wx.Frame):
	def __init__(self, parent, title):
		super(Diabeetus, self).__init__(None, title="Diabeetus")
		self.InitUI()

	def InitUI(self):
		iconFile = "./images/DiabeetusCat.jpg"
		mainIcon = wx.Icon(iconFile, wx.BITMAP_TYPE_JPEG)
		self.SetIcon(mainIcon)		

		# Menu Bar #
		self.mainMenu = wx.MenuBar()

		fileMenu = wx.Menu()
		fileNew = fileMenu.Append(wx.ID_ANY, "New Test", "Run a new test.")
		fileMenu.AppendSeparator()
		fileQuit = fileMenu.Append(wx.ID_EXIT, "Quit", "Exit the Program.")
		self.mainMenu.Append(fileMenu, "&File")

		helpMenu = wx.Menu()
		aboutItem = helpMenu.Append(wx.ID_ABOUT, "About Diabeetus", "About this program...")
		self.mainMenu.Append(helpMenu, "&Help")

		self.SetMenuBar(self.mainMenu)

		# End Menu Bar #
		
		# Create Toolbar #
		toolbar = self.CreateToolBar()
		newTool = toolbar.AddLabelTool(wx.ID_NEW, 'New', wx.ArtProvider.GetBitmap(wx.ART_NEW))
		toolbar.AddSeparator()
		quitTool = toolbar.AddLabelTool(wx.ID_EXIT, 'Quit', wx.ArtProvider.GetBitmap(wx.ART_QUIT))
		toolbar.Realize()
		# End Toolbar #
		
		#Binding#
		self.Bind(wx.EVT_TOOL, self.OnQuit, quitTool)
		self.Bind(wx.EVT_MENU, self.OnQuit, fileQuit)
		self.Bind(wx.EVT_MENU, self.OnNew, fileNew)
		self.Bind(wx.EVT_TOOL, self.OnNew, newTool)
		self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
		

		self.userList = AutoWidthListCtrl(self)
		self.userList.setResizeColumn(0)
		self.userList.InsertColumn(0, "User", width=150)
		self.userList.InsertColumn(1, "Risk", width=200)
		
		self.Center()
		self.Show()
		
	def OnNew(self, e):
		NewTest(None)
		
	def Refresh(self, e):
		self.userList.InsertStringItem(0, name)
		self.userList.SetStringItem(0, 1, risk)
		
	def OnQuit(self, e):
		app.Exit()
		
	def OnAbout(self, e):
		description = """Diabeetus is a FDA-not-approved application on checking if you have diabetes."""

		licence = """Copyright (c) 2013 Cody Dostal, Pivotraze

        Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. The end-user documentation included with the redistribution, if any, must include the following acknowledgment: "This product includes software developed by Cody Dostal https://github.com/codywd and its contributors", in the same place and form as other third-party acknowledgments. Alternatively, this acknowledgment may appear in the software itself, in the same form and location as other such third-party acknowledgments.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

		info = wx.AboutDialogInfo()

		info.SetIcon(wx.Icon('./images/DiabeetusCat.jpg', wx.BITMAP_TYPE_JPEG))
		info.SetName('Diabeetus')
		info.SetVersion(str(progVer))
		info.SetDescription(description)
		info.SetCopyright("(C) 2012 Cody Dostal (a.k.a. Pivotraze)")
		info.SetWebSite("https://www.github.com/codywd")
		info.SetLicence(wordwrap(licence, 350, wx.ClientDC(self)))
		info.AddDeveloper('Cody Dostal')
		info.AddDeveloper('Tonte Owusu (Algorithm for checking for diabetes)')
		info.AddDocWriter('Cody Dostal')
		info.AddArtist('Google')
		info.AddTranslator('Cody Dostal (English)')

		wx.AboutBox(info)
		
class NewTest(wx.Frame):
	def __init__(self, parent):
		super(NewTest, self).__init__(None)
		self.InitUI()

	def InitUI(self):
		wizard = wx.wizard.Wizard(None, -1, "New Test Wizard")
		page1 = TitledPage(wizard, "Welcome")
		page1.Sizer.Add(wx.StaticText(page1, -1, "Welcome to the Diabeetus Test App. This application\ntests your lifestyle and predicts how likely you are\nto get diabetes. This is not a replacement\nfor an actual exam by a doctor. This may also\noverestimate the risk in people younger than 25.\n\nClick Next to Begin."))
		
		page3 = TitledPage(wizard, "Sex")
		page3.Sizer.Add(wx.StaticText(page3, -1, "Are you male or female?"))
		male = wx.RadioButton(page3, -1, "Male")
		female = wx.RadioButton(page3, -1, "Female")
		page3.Sizer.Add(male)
		page3.Sizer.Add(female)
		
		page4 = TitledPage(wizard, "Age")
		page4.Sizer.Add(wx.StaticText(page4, -1, "What age range are you within?"))
		a35less = wx.RadioButton(page4, -1, "35 or younger")
		a36to44 = wx.RadioButton(page4, -1, "36 - 44")
		a45to55 = wx.RadioButton(page4, -1, "45 - 55")
		a56to65 = wx.RadioButton(page4, -1, "56 - 65")
		a66above = wx.RadioButton(page4, -1, "66 or older.")
		page4.Sizer.Add(a35less)
		page4.Sizer.Add(a36to44)
		page4.Sizer.Add(a45to55)
		page4.Sizer.Add(a56to65)
		page4.Sizer.Add(a66above)
		
		page5 = TitledPage(wizard, "Smoke")
		page5.Sizer.Add(wx.StaticText(page5, -1, "Do you smoke?"))
		yesSmoke = RadioButton(page5, -1, "Yes")
		noSmoke = RadioButton(page5, -1, "No")
		page5.Sizer.Add(yesSmoke)
		page5.Sizer.Add(noSmoke)
		
		page6 = TitledPage(wizard, "Family History")
		page6.Sizer.Add(wx.StaticText(page6, -1, "Have either of your parents, or any of your brothers\nor sisters been diagnosed with diabetes?"))
		yesDiag = wx.RadioButton(page6, -1, "Yes")
		noDiag = wx.RadioButton(page6, -1, "No")
		page6.Sizer.Add(yesDiag)
		page6.Sizer.Add(noDiag)
		
		page7 = TitledPage(wizard, "Medication")
		page7.Sizer.Add(wx.StaticText(page7, -1, "Are you currently taking medication for\nhigh blood pressure?"))
		yesMed = wx.RadioButton(page7, -1, "Yes")
		noMed = wx.RadioButton(page7, -1, "No")
		page7.Sizer.Add(yesMed)
		page7.Sizer.Add(noMed)
		
		page8 = TitledPage(wizard, "Diet")
		page8.Sizer.Add(wx.StaticText(page8, -1, "How often do you eat fruits and/or vegetables?"))
		everyday = wx.RadioButton(page8, -1, "Everyday")
		neveryday = wx.RadioButton(page8, -1, "Not Everyday")
		page8.Sizer.Add(everyday)
		page8.Sizer.Add(neveryday)
		
		page9 = TitledPage(wizard, "Physical Activity")
		page9.Sizer.Add(wx.StaticText(page9, -1, "On average, do you achieve at least 2.5 hours of physical\nactivity every week?"))
		yesPA = wx.RadioButton(page9, -1, "Yes")
		noPA = wx.RadioButton(page9, -1, "No")
		page9.Sizer.Add(yesPA)
		page9.Sizer.Add(noPA)
		
		page10 = TitledPage(wizard, "High Blood Sugar")
		page10.Sizer.Add(wx.StaticText(page10, -1, "Have you ever been found to have high blood glucose?\n (For example, in a health examination, during an illness,\nduring pregnancy?"))
		yesHBS = wx.RadioButton(page10, -1, "Yes")
		noHBS = wx.RadioButton(page10, -1, "No")
		page10.Sizer.Add(yesHBS)
		page10.Sizer.Add(noHBS)
		
		page11 = TitledPage(wizard, "Calculating...")
		page11.Sizer.Add(wx.StaticText(page11, -1, "Congratulations on completing the test. \nPress Finish for us to calculate your results."))
		
		
		wx.wizard.WizardPageSimple.Chain(page1, page3)
		wx.wizard.WizardPageSimple.Chain(page3, page4)
		wx.wizard.WizardPageSimple.Chain(page4, page5)
		wx.wizard.WizardPageSimple.Chain(page5, page6)
		wx.wizard.WizardPageSimple.Chain(page6, page7)
		wx.wizard.WizardPageSimple.Chain(page7, page8)
		wx.wizard.WizardPageSimple.Chain(page8, page9)
		wx.wizard.WizardPageSimple.Chain(page9, page10)
		wx.wizard.WizardPageSimple.Chain(page10, page11)
		wizard.FitToPage(page1)
		if wizard.RunWizard(page1):
			points = 0
			if male:
				points += 3
			else:
				points += 0
			
			if a35less:
				points += 0
			elif a36to44:
				points += 2
			elif a45to55:
				points +=  4
			elif a56to65:
				points += 6
			else:
				points += 8
				
			if yesSmoke:
				points += 2
			else:
				points += 0
			
			if yesDiag:
				points += 3
			else:
				points += 0
				
			if yesMed:
				points += 2
			else:
				points += 0
				
			if everyday:
				points += 0
			else:
				points += 1
			
			if yesPA:
				points += 0
			else:
				points += 2
				
			if yesHBS:
				points += 6
			else:
				points += 0
				
			if points <= 5:
				risk = "low"
				riskAmt = " approximately one person in every 100 will develop diabetes."
			elif 6 <= points <= 11:
				risk = "intermediate"
				if 6 <= points <= 8:
					riskAmt = " approximately one person in every 50 will develop diabetes."
				elif 9 <= points <= 11:
					riskAmt = " approximately one person in every 30 will develop diabetes."
			elif points > 12:
				risk = "high"
				if 12 <= points <= 15:
					riskAmt = " approximately one person in every 14 will develop diabetes."
				elif 16 <= points <= 19:
					riskAmt = "  approximately one person in every seven will develop diabetes."
				elif points >= 20:
					riskAmt = "  approximately one person in every three will develop diabetes."
					
				
			nameDlg = wx.TextEntryDialog(self, "What is your name?", "Name", "")
			if nameDlg.ShowModal() == wx.ID_OK:
				name = nameDlg.GetValue()
			
				
			wx.MessageBox(name + ", your risk of diabetes is " + risk + ". At your risk level," + riskAmt, risk.capitalize() + " risk")
			
			dia = Diabeetus(None, title="Diabeetus")
			dia.userList.InsertStringItem(0, name)
			dia.userList.SetStringItem(0, 1, risk)
		else:
			pass
		wizard.Destroy()

class AutoWidthListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
	def __init__(self, parent):
		wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
		ListCtrlAutoWidthMixin.__init__(self)
		
class TitledPage(wiz.WizardPageSimple):
	def __init__(self, parent, title):
		wiz.WizardPageSimple.__init__(self, parent)

		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)

		title = wx.StaticText(self, -1, title)
		title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
		sizer.Add(title, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5)
		sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND|wx.ALL, 5)
if __name__ == "__main__":
	app = wx.App()
	Diabeetus(None, title="Diabeetus")
	app.MainLoop()