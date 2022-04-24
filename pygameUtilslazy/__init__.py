import pygame

class main:
    def __init__(self, run= True, width=500, height=500, winColor = (255,255,255), fps=60, caption="Window"):
        self.run = run
        self.WIN = pygame.display.set_mode((width, height))
        self.color = winColor
        self.caption = caption
        self.fps = fps

        self.clock = pygame.time.Clock()
        
        
    def exitfunc(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            self.GetInpAndExecuteFuncs()
            
    def drawOnScreen(self):
        pass

    def GetInpAndExecuteFuncs(self):
        pass

    def main_loop(self):
        pass
    
    def draw_screen(self):
        pygame.display.set_caption(self.caption)

        self.WIN.fill(self.color)
    
    def update_screen(self):
        pygame.display.update()

    def draw_rect(self, width, height, color, x, y, surface):
        pygame.draw.rect(surface=surface, color=color, rect=[x, y, width, height])


    # def seticon(self):
    #     if self.icon:
    #         pygame.display.set_icon(self.icon)
    # def get_oreesed_keys(,):
       
    # TODO:
    # def conduct_task_based_on_inp(self,self, WANTED_input_keys_andthirefunc):
    #     self.key_state = pygame.key.get_pressed()
    #     self.keysstate=[]
    #     self.wntedinp=WANTED_input_keys_andthirefunc[:0]
    #     for i in self.wntedinp:
    #         self.keysstate.append(self.key_state[i])

    # def inputmange(self, inputkeys, task):
    #     self.inpkeys = inputkeys
         
