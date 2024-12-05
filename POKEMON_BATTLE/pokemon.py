import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("pokemon battle")
font=pygame.font.SysFont("Arial",36) 
pokemon_names = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle"]

def image_load(name):
    root="C:/Users/Dell/Desktop/vs_code_programs/python_programs/POKEMON_BATTLE/sprites/"
    address=root+name+".png"
    return pygame.transform.scale(pygame.image.load(address), (200, 200))

def display_pokemon_moveset(poke):
    dialogue_box=pygame.Rect((0,430),(600,180))
    pygame.draw.rect(screen, (165,213,204),dialogue_box)
    moveset_button_hitboxes=[]
    move1=font.render(poke.moveset[0],True,(0,0,0))
    rect1=move1.get_rect(center=(150,472))
    screen.blit(move1,rect1.topleft)
    moveset_button_hitboxes.append((rect1,poke.moveset[0]))        

    move2=font.render(poke.moveset[1],True,(0,0,0))
    rect2=move2.get_rect(center=(450,472))
    screen.blit(move2,rect2.topleft)
    moveset_button_hitboxes.append((rect2,poke.moveset[1]))     

    move3=font.render(poke.moveset[2],True,(0,0,0))
    rect3=move3.get_rect(center=(150,515+41))
    screen.blit(move3,rect3.topleft)
    moveset_button_hitboxes.append((rect3,poke.moveset[2]))    

    move4=font.render(poke.moveset[3],True,(0,0,0))
    rect4=move4.get_rect(center=(450,515+41))
    screen.blit(move4,rect4.topleft)
    moveset_button_hitboxes.append((rect4,poke.moveset[3]))    

    return moveset_button_hitboxes



def display_pokemon_options():
    screen.fill((255, 255, 255)) 
    y_offset = 100  
    name_rects = []  
    
    for name in pokemon_names:
        text = font.render(name, True, (0, 0, 0))  
        text_rect = text.get_rect(center=(600 // 2, y_offset))  
        name_rects.append((text_rect, name)) 
        
        screen.blit(text, text_rect.topleft)  
        y_offset += 130  
    
    return name_rects

def submit_handle():
    submit=font.render("submit",True,(0,0,0))
    submit_rect=submit.get_rect(center=(550,580))
    screen.blit(submit,submit_rect.topleft)

    return submit_rect

types=['fire','water','grass','flying','dragon','ground','rock','poison',"none"]
class Move:
    def __init__(self,move_name,power,move_type):
        self.move_name=move_name
        self.power=power
        self.move_type=move_type
    def move_dmg(self,attacker,defender):
        if self.move_type=="phy":
            damage = ((2 * 100 / 5 + 2) * self.power * (attacker.phy_atk / defender.phy_def)) / 50 + 2

        else:
            damage = ((2 * 100 / 5 + 2) * self.power * (attacker.sp_atk / defender.sp_def)) / 50 + 2
        return damage

class Pokemon:
    def __init__(self,name,front_sprite,back_sprite,type1,type2,hp,phy_atk,sp_atk,phy_def,sp_def,spd,moveset):
        self.name=name
        self.front_sprite=front_sprite
        self.back_sprite=back_sprite
        self.type1=type1
        self.type2=type2
        self.hp=hp
        self.phy_atk=phy_atk
        self.sp_atk=sp_atk
        self.spd=spd
        self.moveset=moveset
        self.phy_def=phy_def
        self.sp_def=sp_def
    

Charizard=Pokemon('Charizard',image_load("charizard_f"),image_load("charizard_b"),types[0],types[4],1000,256,100,150,90,78,["scratch",'fireball','quick attack','flamethrower'])
Blastoise=Pokemon('Blastoise',image_load("blastoise_f"),image_load("blastoise_b"),types[1],types[-1],1200,180,100,150,284,65,['scratch','water-gun','tackle','hydro-pump'])

scratch=Move("scratch",50,types[-1])

name_to_object={Charizard.name:Charizard,Blastoise.name:Blastoise}
move_to_object={scratch.move_name:scratch}

#selection screen
running=True
name_rects = []

chosen=""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                mouse_pos = pygame.mouse.get_pos()
                for rect, name in name_rects:
                    if rect.collidepoint(mouse_pos):  
                        print(f"Clicked on {name}")  
                        chosen=name
                if submit_rect.collidepoint(mouse_pos):  
                    print("submitted")
                    running=False
                

    name_rects = display_pokemon_options()  
    submit_rect=submit_handle()
    pygame.display.update()

#battle screen
chosen=name_to_object[chosen]
enemy=name_to_object["Blastoise"]
screen.fill((255,255,255))
battle=True
turn=1
myhp=chosen.hp
enemyhp=enemy.hp
once=0
dialogue_vis=True
hitboxes_vis=False
move_selected=False
while battle:  
    myhp_sprite=font.render("HP:"+str(myhp),True,(0,0,0))
    enemyhp_sprite=font.render("HP:"+str(enemyhp),True,(0,0,0))
    blanka=myhp_sprite.get_rect(center=(100,400))
    blankb=enemyhp_sprite.get_rect(center=(500,190))
    pygame.draw.rect(screen, (255,255,255),blanka)
    pygame.draw.rect(screen, (255,255,255),blankb)

    screen.blit(enemyhp_sprite,(450,170))
    screen.blit(myhp_sprite,(50,380))
    screen.blit(chosen.back_sprite,(50,200))
    screen.blit(enemy.front_sprite,(400,20))
    turn_text=font.render("Turn:"+str(turn),True,(0,0,0))
    screen.blit(turn_text,(0,0))
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                battle=False
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN and dialogue_vis and turn%2!=0 :
                pygame.draw.rect(screen, (165,213,204),dialogue_box)
                dialogue_vis=False

            if event.type == pygame.MOUSEBUTTONDOWN and hitboxes_vis:
                if event.button == 1:  
                    mouse_pos = pygame.mouse.get_pos()
                    for rect, move_name in hitboxes:
                        if rect.collidepoint(mouse_pos):  
                            pygame.draw.rect(screen, (165,213,204),dialogue_box)
                            move_chosen=move_name
                            move_selected=True
                            print(type(move_chosen))
                            once=0

    if(turn%2!=0):
        
        text="Your Turn"
        text=font.render(text,True,(0,0,0))
        screen.blit(text,(0,40))
        turn_text_blank=text.get_rect(center=(20,40))
        
        
        #showing initial dialogue
        if once==0:
            dialogue_box=pygame.Rect((0,430),(600,180))
            pygame.draw.rect(screen, (165,213,204),dialogue_box)
            dialogue="Its "+chosen.name+"'s turn ,What will he do"
            dialogue_rendered=font.render(dialogue,True,(0,0,0))
            dialogue_rect=dialogue_rendered.get_rect(center=(300,510))
            screen.blit(dialogue_rendered,dialogue_rect) 
            dialogue_vis=True
            once=1

        if dialogue_vis==False:
            hitboxes=display_pokemon_moveset(chosen)
            hitboxes_vis=True

        if move_selected:
            move_done=move_to_object[move_chosen.strip().lower()]
            damage=move_done.move_dmg(chosen,enemy)
            enemyhp=enemyhp-damage
            turn+=1
    else:
        #reset turn text
        pygame.draw.rect(screen,(255,255,255),turn_text_blank)
        text="Enemy Turn"
        text=font.render(text,True,(0,0,0))
        screen.blit(text,(0,40))
        dialogue_box=pygame.Rect((0,430),(600,180))
        pygame.draw.rect(screen, (165,213,204),dialogue_box)
        dialogue="Its "+enemy.name+"'s turn ,What will he do"
        dialogue_rendered=font.render(dialogue,True,(0,0,0))
        dialogue_rect=dialogue_rendered.get_rect(center=(300,510))
        screen.blit(dialogue_rendered,dialogue_rect) 
        
        enemy_move="scratch"

    pygame.display.update()
pygame.quit()