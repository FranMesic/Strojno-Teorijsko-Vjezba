import pygame
import tkinter
import tkinter.filedialog
import sys
import os
from pygame.rect import Rect

class Menu:
    def __init__(self) -> None:
        self.FilePath = ""
        self.Mode = ""
        self.scroll_y = 0
        self.Topics = []

    def SelectAllTopics(self,topics):
        self.Topics = topics

    def SelectTopic(self,topic):
        self.Topics.append(topic)

    def RemoveTopic(self,topic):
        self.Topics.remove(topic)

    def PromptFile(self):
        top = tkinter.Tk()
        top.withdraw()
        self.FilePath = tkinter.filedialog.askdirectory(parent=top)
        top.destroy()
        return 

    def MouseDownEvent(self,buttons):
        for button in buttons:

            buttonData = button[0]
            buttonAction = button[1]
            buttonArgs = button[2]

            if buttonData.left <= self.mousePosition[0] <= buttonData.right and buttonData.top+self.scroll_y <= self.mousePosition[1] <= buttonData.bottom + self.scroll_y: 
                
                return buttonAction(buttonArgs)

    def QuitGameReturnPressedButton(self,buttonName = None):
        self.run = False
        if buttonName == None:
            return
        return buttonName
    
    def DrawButtonWithText(self,screen,x_pos,y_pos,width,height,primaryColor,hoverColor,text):

        if x_pos <= self.mousePosition[0] <= x_pos+width and y_pos+self.scroll_y <= self.mousePosition[1] <= y_pos+height+self.scroll_y: 
            rect = pygame.draw.rect(screen,hoverColor,[x_pos,y_pos,width,height]) 
        else: 
            rect = pygame.draw.rect(screen,primaryColor,[x_pos,y_pos,width,height])
        text = pygame.font.SysFont('Corbel',20).render(text , True , (0,0,0))
        screen.blit(text , text.get_rect(center = rect.center))

        return rect

    def CenterInfoText(self,screen,y_pos,textSize,textData):
        screenWidth = screen.get_rect().width
        chunkSize = screenWidth//(textSize//2)
        if len(textData) > chunkSize:
            iteration = 0
            while True:
                startIndex = chunkSize*iteration
                endIndex = chunkSize*(iteration+1)
                if endIndex >= len(textData):
                    endIndex = len(textData)-1
                    textChunk = textData[startIndex:endIndex]
                    text = pygame.font.SysFont('Corbel',textSize).render(textChunk , True , (255,255,255))
                    screen.blit(text , text.get_rect(centerx = screen.get_rect().centerx,centery = y_pos+iteration*textSize))
                    break
                textChunk = textData[startIndex:endIndex]
                text = pygame.font.SysFont('Corbel',textSize).render(textChunk , True , (255,255,255))
                screen.blit(text , text.get_rect(centerx = screen.get_rect().centerx,centery = y_pos+iteration*textSize))
                iteration += 1
        else:
            text = pygame.font.SysFont('Corbel',textSize).render(textData , True , (255,255,255))
            screen.blit(text , text.get_rect(centerx = screen.get_rect().centerx,centery = y_pos))

    
        

    def MainMenu(self):

        pygame.init()
        display = (200, 200)
        screen = pygame.display.set_mode(display)
        self.run = True
        buttons = []
        while self.run:

            for ev in pygame.event.get(): 
          
                if ev.type == pygame.QUIT:
                    
                    self.run = False
                    pygame.quit()
                    sys.exit()
                    
                if ev.type == pygame.MOUSEBUTTONDOWN:  

                    returnData = self.MouseDownEvent(buttons)
                        
            buttons.clear()
                        
            screen.fill((0,0,0)) 
            self.mousePosition = pygame.mouse.get_pos()

            #Create data source button
            if self.FilePath == "":
                buttons.append([self.DrawButtonWithText(screen,0,0,200,40,(255,255,255),(200,200,200),"Choose Data Source"),lambda x: self.QuitGameReturnPressedButton("Data Source"),None])
            else:
                buttons.append([self.DrawButtonWithText(screen,0,0,200,40,(111,194,118),(200,200,200),"Choose Data Source"),lambda x: self.QuitGameReturnPressedButton("Data Source"),None])

            #Create topics button
            if self.FilePath == "":
                buttons.append([self.DrawButtonWithText(screen,0,40,200,40,(255,155,155),(200,200,200),"Choose Topics"),lambda x: x,None])
            elif len(self.Topics) == 0:
                buttons.append([self.DrawButtonWithText(screen,0,40,200,40,(255,255,255),(200,200,200),"Choose Topics"),lambda x: self.QuitGameReturnPressedButton("Topics"),None])
            else:
                buttons.append([self.DrawButtonWithText(screen,0,40,200,40,(111,194,118),(200,200,200),"Choose Topics"),lambda x: self.QuitGameReturnPressedButton("Topics"),None])

            #Create mode button
            if self.FilePath == "":
                buttons.append([self.DrawButtonWithText(screen,0,80,200,40,(255,155,155),(200,200,200),"Choose Mode"),lambda x: x,None])
            elif self.Mode == "":
                buttons.append([self.DrawButtonWithText(screen,0,80,200,40,(255,255,255),(200,200,200),"Choose Mode"),lambda x: self.QuitGameReturnPressedButton("Mode"),None])
            else:
                buttons.append([self.DrawButtonWithText(screen,0,80,200,40,(111,194,118),(200,200,200),"Choose Mode"),lambda x: self.QuitGameReturnPressedButton("Mode"),None])
            

            #Create start button
            if self.Mode == "" or len(self.Topics) == 0:
                buttons.append([self.DrawButtonWithText(screen,0,120,200,40,(255,155,155),(200,200,200),"Start"),lambda x: x,None])
            else:
                buttons.append([self.DrawButtonWithText(screen,0,120,200,40,(255,255,255),(200,200,200),"Start"),lambda x: self.QuitGameReturnPressedButton("Start"),None])
            
            pygame.display.update()
        
        pygame.quit()
        return returnData

    def FilePathInput(self):
        pygame.init()
        display = (300, 210)
        screen = pygame.display.set_mode(display)
        self.run = True
        buttons = []
        self.FilePath = ""
        while self.run:
            for ev in pygame.event.get(): 
          
                if ev.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()
                
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    
                    returnData = self.MouseDownEvent(buttons)
                
                if ev.type == pygame.KEYDOWN: 
                    if ev.key == pygame.K_RETURN:
                        self.run = False
            
            buttons.clear()
            screen.fill((0,0,0)) 
            self.mousePosition = pygame.mouse.get_pos()

            #screen.blit(pygame.font.SysFont('Corbel',20).render('Please select data source :' , True , (255,255,255)) , (screen.get_rect().centerx,10))
            self.CenterInfoText(screen,30,20,"Please select data source :")
            self.CenterInfoText(screen,50,20,self.FilePath)

            #Create select file button
            buttons.append([self.DrawButtonWithText(screen,50,130,200,40,(255,255,255),(200,200,200),"Select Directory"),lambda x: self.PromptFile(),None])

            #Create done button
            buttons.append([self.DrawButtonWithText(screen,50,170,200,40,(255,255,255),(200,200,200),"Done"),lambda x: self.QuitGameReturnPressedButton(),None])

            pygame.display.flip()
        
        pygame.quit()
        return
    
    def TopicSelection(self):
        allTopics = [os.path.split(x[0])[-1] for x in os.walk(self.FilePath)][1:]
        pygame.init()
        display = (500, 500)
        intermediate = pygame.surface.Surface((500, (len(allTopics)+2)*40))
        screen = pygame.display.set_mode(display)
        self.run = True
        buttons = []
        self.scroll_y = 0
        while self.run:

            for ev in pygame.event.get(): 
          
                if ev.type == pygame.QUIT:
                    
                    self.run = False
                    pygame.quit()
                    sys.exit()
                    
                if ev.type == pygame.MOUSEBUTTONDOWN:  
                    if ev.button == 1:
                        returnData = self.MouseDownEvent(buttons)
                    if ev.button == 4:
                        self.scroll_y = min(self.scroll_y + 15, 0)
                    if ev.button == 5:
                        self.scroll_y = max(self.scroll_y - 15, -300)

            buttons.clear()
                        
            screen.fill((0,0,0)) 
            self.mousePosition = pygame.mouse.get_pos()

            buttons.append([self.DrawButtonWithText(intermediate,0,0,500,40,(255,255,255),(200,200,200),"Done"),lambda x: self.QuitGameReturnPressedButton(),None])
              
            buttons.append([self.DrawButtonWithText(intermediate,0,40,500,40,(255,255,255),(200,200,200),"SelectAll"),lambda x: self.SelectAllTopics(allTopics.copy()),None])
                
            buttonHeight = 80
            for topic in allTopics:
                if topic in self.Topics:
                    buttons.append([self.DrawButtonWithText(intermediate,0,buttonHeight,500,40,(111,194,118),(200,200,200),topic),lambda x: self.RemoveTopic(x),topic])
                else:
                    buttons.append([self.DrawButtonWithText(intermediate,0,buttonHeight,500,40,(255,255,255),(200,200,200),topic),lambda x: self.SelectTopic(x),topic])
                buttonHeight+=40

            screen.blit(intermediate, (0, self.scroll_y))
            pygame.display.update()
        
        pygame.quit()

    def ModeSelection(self):
        pygame.init()
        display = (300, 300)
        screen = pygame.display.set_mode(display)
        self.run = True
        buttons = []
        self.scroll_y = 0
        while self.run:

            for ev in pygame.event.get(): 
          
                if ev.type == pygame.QUIT:
                    
                    self.run = False
                    pygame.quit()
                    sys.exit()
                    
                if ev.type == pygame.MOUSEBUTTONDOWN:  
                    if ev.button == 1:
                        self.Mode = self.MouseDownEvent(buttons)

            buttons.clear()
                        
            screen.fill((0,0,0)) 
            self.mousePosition = pygame.mouse.get_pos()

            buttons.append([self.DrawButtonWithText(screen,0,0,300,40,(255,255,255),(200,200,200),"All Ordered"),lambda x: self.QuitGameReturnPressedButton("All Ordered"),None])
              
            buttons.append([self.DrawButtonWithText(screen,0,40,300,40,(255,255,255),(200,200,200),"All Random"),lambda x: self.QuitGameReturnPressedButton("All Random"),None])
            
            buttons.append([self.DrawButtonWithText(screen,0,80,300,40,(255,255,255),(200,200,200),"Test Like"),lambda x: self.QuitGameReturnPressedButton("Test Like"),None])
                
            pygame.display.update()
        
        pygame.quit()

    
