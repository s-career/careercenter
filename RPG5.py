import pyxel


class App:
    def __init__(self):
        #Font set
        self.font_list = {
         "a":[0,0],
         "A":[8,0],
         "i":[16,0],
         "I":[24,0],
         "u":[32,0],
         "U":[40,0],
         "e":[48,0],
         "E":[56,0],
         "o":[64,0],
         "O":[72,0],
         "KA":[80,0],
         "GA":[88,0],
         "KI":[96,0],
         "GI":[104,0],
         "KU":[112,0],
         "GU":[120,0],
         "KE":[128,0],
         "GE":[136,0],
         "KO":[144,0],
         "GO":[152,0],
         "SA":[160,0],
         "ZA":[168,0],
         "SI":[176,0],
         "JI":[184,0],
         "SU":[192,0],
         "ZU":[200,0],
         "SE":[208,0],
         "ZE":[216,0],
         "SO":[224,0],
         "ZO":[232,0],
         "TA":[240,0],
         "DA":[248,0],
         "TI":[0,8],
         "DI":[8,8],
         "tu":[16,8],
         "TU":[24,8],
         "DU":[32,8],
         "TE":[40,8],
         "DE":[48,8],
         "TO":[56,8],
         "DO":[64,8],
         "NA":[72,8],
         "NI":[80,8],
         "NU":[88,8],
         "NE":[96,8],
         "NO":[104,8],
         "HA":[112,8],
         "BA":[120,8],
         "PA":[128,8],
         "HI":[136,8],
         "BI":[144,8],
         "PI":[152,8],
         "HU":[160,8],
         "BU":[168,8],
         "PU":[176,8],
         "HE":[184,8],
         "BE":[192,8],
         "PE":[200,8],
         "HO":[208,8],
         "BO":[216,8],
         "PO":[224,8],
         "MA":[232,8],
         "MI":[240,8],
         "MU":[248,8],
         "ME":[0,16],
         "MO":[8,16],
         "ya":[16,16],
         "YA":[24,16],
         "yu":[32,16],
         "YU":[40,16],
         "yo":[48,16],
         "YO":[56,16],
         "RA":[64,16],
         "RI":[72,16],
         "RU":[80,16],
         "RE":[88,16],
         "RO":[96,16],
         "wa":[104,16],
         "WA":[112,16],
         "WI":[120,16],
         "WE":[128,16],
         "WO":[136,16],
         "NN":[144,16],
         }
    
        #System status
        self.game_start = False 
        self.talking = False 
        self.answered = False
        self.paused = False
        self.switched = False
        self.start_message = False
        self.quit_flag = False
        self.finished_flag = False
     
        #ここで起動時の処理をします                                
        pyxel.init(128, 128)        
        pyxel.load('./sample03.pyxres')  
        pyxel.mouse(False)
        #pyxel.mouse(True) # for debug
        self.dog_color = pyxel.rndi(0,5)
        self.player_pos = [16, 16]         
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_S):
            self.game_start = True
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        #ここで毎フレームの更新作業をします
        #コントロール部分###################
        leftClick = rightClick = upClick = downClick = False
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.paused == False:
                if 10*8 < pyxel.mouse_x <= 12*8 and (12*8 < pyxel.mouse_y <= 14*8 or 12*8 + 16*8 < pyxel.mouse_y <= 14*8 + 16*8):
                    leftClick = True
                elif 14*8 < pyxel.mouse_x <= 16*8 and (12*8 < pyxel.mouse_y <= 14*8 or 12*8 + 16*8 < pyxel.mouse_y <= 14*8 + 16*8):
                    rightClick = True
                elif 12*8 < pyxel.mouse_x <= 14*8 and (10*8 < pyxel.mouse_y <= 12*8 or 10*8 +16*8 < pyxel.mouse_y <= 14*8 + 16*8):
                    upClick = True
                elif 12*8 < pyxel.mouse_x <= 14*8 and (14*8 < pyxel.mouse_y <= 16*8 or 14*8 + 16*8< pyxel.mouse_y <= 16*8 + 16*8):
                    downClick = True
                elif 70 < pyxel.mouse_y <= 78:
                    self.game_start = True
                elif 80 < pyxel.mouse_y <= 88:
                    self.quit_flag = True
                    #pyxel.quit()
                elif self.start_message == False and self.quit_flag == False and 8*11 < pyxel.mouse_y <= 8*15:
                    self.start_message = True
                elif self.quit_flag == True:
                    pyxel.quit()
            else:
                if 8*11 < pyxel.mouse_y <= 8*15:
                    self.answered = True
            if self.finished_flag == True:
                pyxel.quit()
                            
        if pyxel.btnp(pyxel.KEY_RIGHT) or rightClick:
            if self.move_check(self.player_pos[0]+8, self.player_pos[1]):
                self.player_pos[0] += 8
            else:
                self.event_check(self.player_pos[0]+8, self.player_pos[1])
        elif pyxel.btnp(pyxel.KEY_LEFT) or leftClick:
            if self.move_check(self.player_pos[0]-8, self.player_pos[1]):
                self.player_pos[0] -= 8
            else:
                self.event_check(self.player_pos[0]-8, self.player_pos[1])                
        elif pyxel.btnp(pyxel.KEY_UP) or upClick:
            if self.move_check(self.player_pos[0], self.player_pos[1]-8):
                self.player_pos[1] -= 8
            else:
                self.event_check(self.player_pos[0], self.player_pos[1]-8)                
        elif pyxel.btnp(pyxel.KEY_DOWN) or downClick:
            if self.move_check(self.player_pos[0], self.player_pos[1]+8):
                self.player_pos[1] += 8
            else:
                self.event_check(self.player_pos[0], self.player_pos[1]+8)                

    def move_check(self, x, y):        
        if pyxel.tilemaps[0].pget(x//8, y//8)[1] > 0:
            return False
        else:
            return True
        
    def event_check(self, x, y):
        t = pyxel.tilemaps[0].pget(x//8, y//8)
        if t == (0, 4):
            pyxel.tilemaps[0].pset(8, 13, (1, 4))
            pyxel.tilemaps[0].pset(7, 9, (2, 0))
            pyxel.tilemaps[0].pset(8, 9, (3, 0))
            self.switched = True
        elif t == (1, 4):
            pyxel.tilemaps[0].pset(8, 13, (0, 4))
            pyxel.tilemaps[0].pset(7, 9, (0, 3))
            pyxel.tilemaps[0].pset(8, 9, (1, 3))
        elif t == (2, 3) or t == (3, 3):
            self.player_pos = [7*8, 22*8]
            pyxel.camera(0, 16*8)
        elif t == (4, 3) or t == (5, 3):
            self.player_pos = [7*8, 7*8]
            pyxel.camera(0, 0)
            self.talking = False
        elif t == (4, 5):
            self.talking = True
            self.Draw_textbox(1)
        else:
            pass

    def draw(self):
        #ここで毎フレームの描画作業をします
        pyxel.cls(0) 
        
        pyxel.bltm(0, 0, 0, 0, 0, 128, 256)       
        #pyxel.blt(self.player_pos[0], self.player_pos[1], 0, 0, 0, 8, 8, 14)
        pyxel.blt(self.player_pos[0], self.player_pos[1], 0, 8*self.dog_color, 0, 8, 8, 14)

        #Draw title text
        if self.game_start == False:
            pyxel.cls(0)
            pyxel.text(35, 40, "SHUKATSU QUEST", 7)
            pyxel.text(8*2, 70, "S = ", 7)
            self.Draw_fonts(["SI","yu","U","KA","TU","WO","HA","JI","ME","RU"], 8*4, 70)
            pyxel.text(8*2, 85, "Q = ", 7)
            self.Draw_fonts(["WA","a","HO","RI","NI","I","KU"], 8*4, 85)
        elif self.start_message == False:
            self.Draw_textbox(0)
            self.Draw_fonts(["KI","ya","RI","SE","NN","NI","I","KO","U"], 8*3, 8*12)
            pyxel.text(40, 8*14, "Continue...", 7)
        else:
            if self.talking == False and self.answered == False and self.switched == False:
                self.ReverseMap()
        if self.talking == True:
            self.paused = True
            self.Draw_fonts(["KI","ya","RI","SE","NN","HE","YO","U","KO","SO"], 8*3, 8*16+8*11)
            pyxel.text(40, 8*16+8*14, "Continue...", 7)
        if self.answered == True:
            self.Erase_fonts(["KI","ya","RI","SE","NN","HE","YO","U","KO","SO"], 8*3, 8*16+8*11)
            self.Erase_fonts(["KI","ya","RI","SE","NN","HE","YO","U","KO","SO"], 8*5, 8*16+8*14)
            self.Draw_fonts(["KO","TA","E","HA","NA","I","SI","yo","DA","YO"], 8*3, 8*16+8*11)
            self.Draw_fonts(["KI","ya","RI","SE","NN","NI","KI","TE","NE"], 8*3, 8*16+8*12)
            self.finished_flag = True
            pyxel.text(40, 8*16+8*14, "Continue...", 7)

        if self.quit_flag == True:
            pyxel.cls(0)
            #self.Draw_textbox(0)
            self.Draw_fonts(["A","KI","RA","ME","TI","ya","DA","ME","DA","YO"], 8*3, 8*12)
            pyxel.text(40, 8*14, "Restart...", 7)

    def Draw_fonts(self,txt,x,y):  
        txt_count = len(txt)      
        for i in range(txt_count):
            #Key check
            font_xy = self.font_list[txt[i]]
        
            fontx = font_xy[0]
            fonty = font_xy[1]
            pyxel.blt(x + 8 * i,y,1,fontx,fonty,8,8,14)

    def Erase_fonts(self,txt,x,y):  
        txt_count = len(txt)      
        for i in range(txt_count):
            pyxel.blt(x + 8 * i,y,1,0,32,8,8,14)

    def Draw_textbox(self,k):
        pyxel.tilemaps[0].pset(0, 16*(k+1)-6, (0, 8))
        pyxel.tilemaps[0].pset(0, 16*(k+1)-1, (0, 9))
        pyxel.tilemaps[0].pset(16-1, 16*(k+1)-6, (2, 8))
        pyxel.tilemaps[0].pset(16-1, 16*(k+1)-1, (2, 9))
        for i in range(1, 15):
            pyxel.tilemaps[0].pset(i, 16*(k+1)-6, (1, 8))
            pyxel.tilemaps[0].pset(i, 16*(k+1)-1, (1, 9))
            for j in range(2, 6):
                pyxel.tilemaps[0].pset(i, 16*(k+1)-j, (5, 0))
        for i in range(2, 6):
            pyxel.tilemaps[0].pset(0, 16*(k+1)-i, (3, 9))
            pyxel.tilemaps[0].pset(16-1, 16*(k+1)-i, (3, 8))
        

    def ReverseMap(self):
        for i in range(1, 7):
            for j in range(0, 16):
                pyxel.tilemaps[0].pset(j, 16*1-i, (0, 1))
        for i in range(2, 7):
            for j in range(1, 10):
                pyxel.tilemaps[0].pset(j, 16*1-i, (0, 0))
        pyxel.tilemaps[0].pset(8, 13, (0, 4))

        pyxel.tilemaps[0].pset(1, 11, (1, 0))
        pyxel.tilemaps[0].pset(2, 11, (1, 0))
        pyxel.tilemaps[0].pset(3, 11, (1, 0))
        pyxel.tilemaps[0].pset(2, 12, (1, 0))
        pyxel.tilemaps[0].pset(3, 12, (1, 0))
        pyxel.tilemaps[0].pset(3, 13, (1, 0))
        pyxel.tilemaps[0].pset(8, 12, (1, 0))
        pyxel.tilemaps[0].pset(9, 12, (1, 0))
        pyxel.tilemaps[0].pset(9, 13, (1, 0))
        pyxel.tilemaps[0].pset(9, 14, (1, 0))
        pyxel.tilemaps[0].pset(8, 14, (1, 0))
        pyxel.tilemaps[0].pset(7, 14, (1, 0))
        pyxel.tilemaps[0].pset(6, 14, (1, 0))

        pyxel.tilemaps[0].pset(12, 10, (0, 6))
        pyxel.tilemaps[0].pset(13, 10, (1, 6))
        pyxel.tilemaps[0].pset(12, 11, (0, 7))
        pyxel.tilemaps[0].pset(13, 11, (1, 7))

        pyxel.tilemaps[0].pset(12, 14, (2, 6))
        pyxel.tilemaps[0].pset(13, 14, (3, 6))
        pyxel.tilemaps[0].pset(12, 15, (2, 7))
        pyxel.tilemaps[0].pset(13, 15, (3, 7))

        pyxel.tilemaps[0].pset(14, 12, (4, 6))
        pyxel.tilemaps[0].pset(15, 12, (5, 6))
        pyxel.tilemaps[0].pset(14, 13, (4, 7))
        pyxel.tilemaps[0].pset(15, 13, (5, 7))

        pyxel.tilemaps[0].pset(10, 12, (6, 6))
        pyxel.tilemaps[0].pset(11, 12, (7, 6))
        pyxel.tilemaps[0].pset(10, 13, (6, 7))
        pyxel.tilemaps[0].pset(11, 13, (7, 7))

        pyxel.tilemaps[0].pset(12, 12, (8, 6))
        pyxel.tilemaps[0].pset(13, 12, (9, 6))
        pyxel.tilemaps[0].pset(12, 13, (8, 7))
        pyxel.tilemaps[0].pset(13, 13, (9, 7))

        for i in range(1, 7):
            for j in range(0, 16):
                pyxel.tilemaps[0].pset(j, 16*2-i, (5, 0))

        pyxel.tilemaps[0].pset(12, 16+10, (0, 6))
        pyxel.tilemaps[0].pset(13, 16+10, (1, 6))
        pyxel.tilemaps[0].pset(12, 16+11, (0, 7))
        pyxel.tilemaps[0].pset(13, 16+11, (1, 7))

        pyxel.tilemaps[0].pset(12, 16+14, (2, 6))
        pyxel.tilemaps[0].pset(13, 16+14, (3, 6))
        pyxel.tilemaps[0].pset(12, 16+15, (2, 7))
        pyxel.tilemaps[0].pset(13, 16+15, (3, 7))

        pyxel.tilemaps[0].pset(14, 16+12, (4, 6))
        pyxel.tilemaps[0].pset(15, 16+12, (5, 6))
        pyxel.tilemaps[0].pset(14, 16+13, (4, 7))
        pyxel.tilemaps[0].pset(15, 16+13, (5, 7))

        pyxel.tilemaps[0].pset(10, 16+12, (6, 6))
        pyxel.tilemaps[0].pset(11, 16+12, (7, 6))
        pyxel.tilemaps[0].pset(10, 16+13, (6, 7))
        pyxel.tilemaps[0].pset(11, 16+13, (7, 7))

        pyxel.tilemaps[0].pset(12, 16+12, (8, 6))
        pyxel.tilemaps[0].pset(13, 16+12, (9, 6))
        pyxel.tilemaps[0].pset(12, 16+13, (8, 7))
        pyxel.tilemaps[0].pset(13, 16+13, (9, 7))
App()