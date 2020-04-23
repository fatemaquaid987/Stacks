import pyglet                                               # imports pyglets library
from pyglet.window import Window, mouse, gl, key
 
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()
 
mygame = pyglet.window.Window(800, 710,                     # setting window
              resizable=False,  
              caption="STACKS",  
              config=pyglet.gl.Config(double_buffer=True),  # Avoids flickers
              vsync=False                                   # For flicker-free animation
              )                                             # Calling base class constructor
mygame.set_location(screen.width // 2 - 200,screen.height//2 - 350)
 
               
bgimage = pyglet.resource.image('images/background.png')           # Background image use for game

bimage = pyglet.resource.image('images/brick.jpg')                 # Image for brick
bpart=bimage.get_region(0,8,200,35)
bpart2=bimage.get_region(0,8,200,35)

inst=pyglet.resource.image('images/instructions.png')
instsprite=pyglet.sprite.Sprite(inst, 0, 0)                 # sprite for help an instructions
instsprite.visible=False

back=pyglet.resource.image('images/back.jpg')
backsprite=pyglet.sprite.Sprite(back,667,5)                 # sprite for going back
backsprite.visible=False

menuimage = pyglet.resource.image('images/menu.png')
menusprite = pyglet.sprite.Sprite(menuimage, 0, 0)          # sprite for menu
menusprite.visible= True

easyimage = pyglet.resource.image('images/easy.png')
easysprite = pyglet.sprite.Sprite(easyimage, 247, 448)      # level sprites
easysprite.visible= False

easypressimage = pyglet.resource.image('images/easypress.png')
epsprite = pyglet.sprite.Sprite(easypressimage, 247, 448)
epsprite.visible= False

hardimage = pyglet.resource.image('images/hard.png')
hardsprite = pyglet.sprite.Sprite(hardimage, 247, 216)
hardsprite.visible= False

hardpressimage = pyglet.resource.image('images/hardpress.png')
hpsprite = pyglet.sprite.Sprite(hardpressimage, 247, 216)
hpsprite.visible= False

medimage = pyglet.resource.image('images/medium.png')
medsprite = pyglet.sprite.Sprite(medimage, 247, 329)
medsprite.visible= False

medpressimage = pyglet.resource.image('images/mediumpress.png')
medpsprite = pyglet.sprite.Sprite(medpressimage, 247, 329)
medpsprite.visible= False
 
lis= [pyglet.sprite.Sprite(bpart, 300, 0),pyglet.sprite.Sprite(bpart, 20, 690)] # list that stores all the bricks
i=1                                                                             # couter
countx=[0,0]                                                                    # counter for changing x position
county=[0,0]                                                                    # counter for changing y position
tmp=2
score=0
speedx=6
speedy=4
j=0
 
overlabel = pyglet.text.Label("",
                             font_name='Comic Sans MS',
                             font_size=48,
                             x=400, y=400,
                             anchor_x='center', anchor_y='center', color=(247, 211, 26, 255))
scorelabel=pyglet.text.Label("",
                             font_name='Comic Sans MS',
                             font_size=48,
                             x=400, y=300,
                             anchor_x='center', anchor_y='center', color=(247, 211, 26, 255))
 
 
 
def check():                                                                    # checks if game is over
    global tmp
    global i
    global lis
    if tmp < 2 or lis[i].x<0 or lis[i].x>800 or lis[i].y<0:                     
        s=str(score)
        overlabel.text="Game over"
        scorelabel.text=s
    
 
@mygame.event
def on_draw():                                                                   # draws all the sprites
     
    mygame.clear()
    bgimage.blit(0,0)
    menusprite.draw()
    instsprite.draw()
    backsprite.draw()
    easysprite.draw()
    epsprite.draw()
    hardsprite.draw()
    hpsprite.draw()
    medsprite.draw()
    medpsprite.draw()
    overlabel.draw()
    scorelabel.draw()
    if menusprite.visible== False and instsprite.visible==False and backsprite.visible==True:
        for j in lis:
            j.draw()
     
@mygame.event
def on_mouse_release(x, y, button, modifiers):                                    # takes users mouse input
    
    global speedx
    global speedy
    global countx
    global county
    global score
    global lis
    global tmp
    global i
    global j
    
    if menusprite.visible== True :                                              # menu selection
        if button==mouse.LEFT: 
            if (255 <= x <= 510) and (349 <= y <= 411):                         # if play selected
                menusprite.visible= False
                backsprite.visible=True
            elif(255 <= x <= 510) and (250 <= y <= 314):                        # if levels selected
                menusprite.visible= False
                epsprite.visible= True
                hardsprite.visible= True
                medsprite.visible= True
            elif (255 <= x <= 510) and (163 <= y <= 226):                       # if help selected
                instsprite.visible=True
                menusprite.visible= False
            elif (255 <= x <= 510) and (70 <= y <= 134):                        # if quit selected
                mygame.close()
            
    elif menusprite.visible== False and instsprite.visible== True:              # help instructions
        if button==mouse.LEFT:
            if( 667 <= x <= 793) and ( 5 <= y <= 50):                           # if back is pressed
                instsprite.visible=False
                menusprite.visible=True

    elif menusprite.visible==False and instsprite.visible== False and backsprite.visible== False: # if levels selected
        if button==mouse.LEFT:
            if ( 247 <= x <= 513) and (448 <= y <= 512):                        # if level is easy
                easysprite.visible = False
                hpsprite.visible= False
                medpsprite.visible = False
                epsprite.visible= True
                hardsprite.visible= True
                medsprite.visible = True
                speedx=5
                speedy=3
            elif (247 <= x <= 513) and (216<= y <= 282):                        # if level is hard
                hardsprite.visible= False
                medpsprite.visible = False
                epsprite.visible= False
                hpsprite.visible= True
                medsprite.visible = True
                easysprite.visible= True
                speedx=13
                speedy=11
            elif (247 <= x <= 513) and (329 <= y <= 401):                       # if level is medium
                medsprite.visible = False
                epsprite.visible= False
                hpsprite.visible= False
                medpsprite.visible = True
                easysprite.visible= True
                hardsprite.visible= True
                speedx=10
                speedy=8
            elif ( 667<= x <=793 ) and ( 5 <= y <= 50 ):                        # if back is pressed
                easysprite.visible = False
                epsprite.visible= False
                hardsprite.visible= False
                hpsprite.visible= False
                medsprite.visible = False
                medpsprite.visible = False
                menusprite.visible = True
                
    elif menusprite.visible== False  and instsprite.visible==False and backsprite.visible==True: # if back is pressed during game
        if button==mouse.LEFT:
            
            
            if ( 694<=x <= 792) and ( 7<= y <= 51):
                if tmp < 2 or lis[i].x<0 or lis[i].x>800 or lis[i].y<0:     # to start a new game all the variables are initialized again
                    backsprite.visible= False
                    menusprite.visible = True
                    overlabel.text = ""
                    scorelabel.text= ""
                    lis= [pyglet.sprite.Sprite(bpart, 300, 0),pyglet.sprite.Sprite(bpart, 20, 690)] 
                    countx=[0,0]                                                                    
                    county=[0,0]                                                                
                    score=0
                    speedx=6
                    speedy=4
                    i=1
                    j=0
                else:
                    backsprite.visible= False
                    menusprite.visible = True
                    


                    
@mygame.event

def on_key_press(symbol, modifiers):                                          # takes users keyboard input

    global i
    global countx
    global county
    global bpart2
    global score
    global tmp
    global j
    
    
    if menusprite.visible== False  and instsprite.visible==False and backsprite.visible==True:
        if symbol== key.SPACE:
            if lis[i].x >(lis[i-1].x +lis[i-1].width) or (lis[i].x +lis[i].width)<lis[i-1].x: # if brick is not in the range of stack
                countx[i]=230
                county[i]=0
 
            else:
                countx[i]=230
                county[i]=230
                lis[i].y = lis[i-1].y+lis[i-1].height
                    

                if lis[i].x <= lis[i-1].x:                                 # if brick overlaps from the right 

                    tmp = (lis[i].x + lis[i].width) - lis[i-1].x
                    bpart2=bimage.get_region(0,8,tmp,35)

                    lis[i]= pyglet.sprite.Sprite(bpart2, lis[i-1].x, lis[i-1].y + lis[i-1].height)
                    if i%2==0 and tmp>1:
                        lis.append(pyglet.sprite.Sprite(bpart2, 20, 690)) # appends a new brick into the list
                        i+=1
                    elif i%2!=0 and tmp>1:
                        lis.append(pyglet.sprite.Sprite(bpart2, 780, 690))# appends a new brick into the list
                        i+=1

                    countx.append(0)
                    county.append(0)
                    score+=1
                    
                    

                elif lis[i].x > lis[i-1].x:                              # if brick overlaps rom the left
                    a=lis[i].x
                    tmp = lis[i].width-(lis[i].x - lis[i-1].x)

                    bpart2=bimage.get_region(0,8,tmp,35)
                    lis[i]= pyglet.sprite.Sprite(bpart2, a,lis[i-1].y + lis[i-1].height )
                    if i%2==0 and tmp>1:
                        lis.append(pyglet.sprite.Sprite(bpart2, 20, 690))# appends a new brick into the list
                        i+=1
                    elif i%2!=0 and tmp>1:
                        lis.append(pyglet.sprite.Sprite(bpart2, 780, 690))# appends a new brick into the list
                        i+=1
                    
                    countx.append(0)
                    county.append(0)
                    score+=1
                               
    if i>8:                                                             # The stack can have no more than 9 bricks on the screen
        lis[j].visible=False
        j+=1
        for v in range(1,len(lis)):
            lis[v].y-=35
         

    check()
 
def update(dt):                                                         # updates position of brick, moves it on the screen
    
    global county
    global countx
    global i
    global speedx
    global speedy
    if menusprite.visible== False and instsprite.visible==False and backsprite.visible== True:
 
        if i%2==0 and countx[i]!= 230:                                  # when the brick comes from left
            lis[i].x-=speedx
            countx[i]+=1
        elif i%2!=0 and countx[i]!=230:                                 # when the brick comes from right
            lis[i].x+=speedx
            countx[i]+=1
             
        if county[i]< 230:                                              # brick falls 
            lis[i].y-=speedy
            county[i]+=1
            
    check()
 
pyglet.clock.schedule_interval(update, 1/60.)                           # calls update function 60 times a second
 
pyglet.app.run()
