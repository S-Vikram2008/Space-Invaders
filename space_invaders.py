#------ Importing necessary modules ------------
import pyray as pr
import random

#------- Initialising screen height and screen width for creating a game window --------------
screen_height=750
screen_width=750

#------- Creating a window of width=screen_width and height=screen_height and game window title as "Space Invaders"       
pr.init_window(screen_width,screen_height,"Space Invaders")

#------ Setting a target frames per second to control the number of times the gap loop should execute (Here 20 frames per second means the game loop will execute 20 times every second )
pr.set_target_fps(20)

# ------- Loading some image textures ---------
alien_img=pr.load_texture('alien.png')
player_img=pr.load_texture('player.png')
ufo_img=pr.load_texture('ufo.png')

#-------- Function to display final game score --------------
def game_over(score):   
    while (not pr.window_should_close()):
        if pr.is_key_pressed(pr.KEY_R):
            return
        
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        pr.draw_text("GAME OVER",280,305,30,pr.WHITE)
        pr.draw_text("SCORE : {}".format(score),300,335,25,pr.WHITE)
        pr.draw_text("Press R to Restart ",280,650,25,pr.WHITE)
        pr.draw_text("PRESS ESC TO QUIT ",280,700,25,pr.WHITE)
        pr.end_drawing()
        
    
#--------- Main game loop function -----------------    
def game():

    # These values denote the position of space shuttle at the start of the game 
    shuttle_x=screen_width//2
    shuttle_y=screen_height-50

    # For creating alien grid , we create a grid of aliens with rows and cols. Here alien grid starts at start_x and start_y
    rows = 4
    cols = 8
    start_x = 80
    start_y = 50

    # For ensuring even spacing between any two aliens , we use gap_x and gap_y
    gap_x = 70
    gap_y = 60

    # aliens list stores all the aliens present in the window
    aliens=[]
    
    # alien_ufo list stores all ufo present in the window
    alien_ufo=[]
    
    # Bullets list stores the bullets present in screen . When the bullets reach the end of screen ie) when y coordinate of a bullet reaches the end it is removed from the bullets list 
    bullets=[]

    # This variable keeps track of the scores / number of bullets which hits the alien.
    score=0

    # This variable keeps track of the lifes that are present for the player 
    life=3

    # This stores the enemy bullets 
    enemy_bullets=[]

    # Creating a grid of aliens.
    for i in range(rows):
        for j in range(cols):
            aliens.append({
                "x": start_x + j * gap_x,
                "y": start_y + i * gap_y
            })

    # Creating a row of alien UFO
    for x in [100, screen_width//2 - 25, screen_width - 150]:
        alien_ufo.append({
            "x": x,
            "y": 20,
            "health": 5
        })
    
    #Here we choose a random enemy from aliens list and then create a enemy bullet from that enemy's x and y coordinate so it appears like the bullet is shooted by the enemy alien 
    enemy = random.choice(aliens)
    enemy_bullets.append({
        "x": enemy["x"],
        "y": enemy["y"]
    })

    
    while (not pr.window_should_close()):
        # If Space key is pressed we append a bullet into the bullets list and afterwards we draw that bullet on screen 
        if pr.is_key_pressed(pr.KEY_SPACE):
            bullets.append({'x':shuttle_x,'y':screen_height-100})
        # If Left key is pressed we decrease the space shuttle's x coordinate by 10 so afterwards when we draw the space shuttle it appears it has moves left by 10 units 
        if pr.is_key_down(pr.KEY_LEFT):
            shuttle_x-=10
            
        # If Right key is pressed we increase the space shuttle's x coordinate by 10 so afterwards when we draw the space shuttle it appears it has moves right by 10 units 
        elif pr.is_key_down(pr.KEY_RIGHT):
            shuttle_x+=10

        # Boundary conditions : This ensures that the space shuttle does not leave the window . So if shuttle_x becomes less than 10 we make the shuttle_x value as 10 similarly when shuttle_x becomes greater than 740 we make shuttle_x as 740   
        if shuttle_x<10:
            shuttle_x=10
        if shuttle_x>740:
            shuttle_x=740
            
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        # Drawing the space shuttle 
        pr.draw_texture(player_img,shuttle_x,shuttle_y,pr.WHITE)

        # Drawing each alien present in aliens list 
        for alien in aliens:
            pr.draw_texture(alien_img,alien['x'],int(alien['y']),pr.WHITE)
            alien['y']+=0.5 # This makes the alien to move by 0.5 units each time the while loop executes 

        # Drawing every UFO present in alien_ufo list 
        for ufo in alien_ufo:
            pr.draw_texture(ufo_img,ufo['x'],int(ufo['y']),pr.WHITE)
            ufo['y']+=0.5

        # Drawing every bullet present in bullets list    
        for i in bullets:
            pr.draw_rectangle(i['x'],i['y'],5,5,pr.GREEN)
            i['y']-=5

        # Checking whether the bullet has already left the game window , if so we remove it .
        ''' Here we iterate the bullets 's copy and not orginal bullets list ,
            This is because removing an element from iterating a list is not allowed '''
        for i in bullets[:]:
            if i['y']<10:
                bullets.remove(i)

        # Drawing bullets and making them move by 5 units every time the while loop executes .
        for i in enemy_bullets:
            pr.draw_rectangle(i['x'],int(i['y']),5,5,pr.RED)
            i['y']+=5

        for i in enemy_bullets[:]:
            if i['y']>shuttle_y:
                enemy_bullets.remove(i)
                
        # If there is no enemy bullet on screen , we create another bullet 
        if not enemy_bullets:
            if aliens:
                enemy = random.choice(aliens)
                enemy_bullets.append({
                    "x": enemy["x"],
                    "y": enemy["y"]
                })
        
        # If any alien goes off the screen , it means we lost the game and we return the score 
        for alien in aliens:
            if alien['y']>750:
                return score
        # If an UFO  goes off the screen , it means we lost the game and we return the score 
        for ufo in alien_ufo:
            if ufo['y']>750:
                return score

        # Checking collision between bullets shot by the player and the alien.    
        for b in bullets[:]:
            bullet_rec=pr.Rectangle(b['x'],b['y'],5,5)
            for alien in aliens[:]:
                alien_rec=pr.Rectangle(alien['x'],int(alien['y']),16,16)

                if pr.check_collision_recs(bullet_rec,alien_rec):
                    score+=1
                    aliens.remove(alien)
                    bullets.remove(b)
                    break

        # Checking collision between bullets shot by the player and the UFO .    
        for b in bullets[:]:
            bullet_rec=pr.Rectangle(b['x'],b['y'],5,5)
            for ufo in alien_ufo[:]:
                ufo_rec=pr.Rectangle(ufo['x'],int(ufo['y']),48,21)

                if pr.check_collision_recs(bullet_rec,ufo_rec):
                    
                    if ufo['health']==0:
                        alien_ufo.remove(ufo)
                        bullets.remove(b)
                        score+=5
                        break
                    else:
                        ufo['health']-=1
                        bullets.remove(b)
                        break

        player_rec=pr.Rectangle(shuttle_x,shuttle_y,26,16)

        # Checking collision between enemey bullets shot by the alien and the player.    
        for b in enemy_bullets[:]:
            enemy_bullet_rec=pr.Rectangle(b['x'],b['y'],5,5)
            if pr.check_collision_recs(player_rec,enemy_bullet_rec):
                life-=1
                enemy_bullets.remove(b)

            if life==0:
                return score

        # Checking collision between bullets shot by the player and the enemey bullets shot by the alien.       
        for bullet in bullets[:]:
            bullet_rec=pr.Rectangle(bullet['x'],bullet['y'],10,10)

            for enemy_bullet in enemy_bullets[:]:
                enemy_bullet_rec=pr.Rectangle(enemy_bullet['x'],enemy_bullet['y'],5,5)

                if pr.check_collision_recs(bullet_rec,enemy_bullet_rec):
                    bullets.remove(bullet)
                    enemy_bullets.remove(enemy_bullet)
                    break
                    

        # If all aliens and all the UFO are shot by the player then we create a new wave of aliens and UFO           
        if aliens==[] and alien_ufo==[]:
            for i in range(rows):
                for j in range(cols):
                    aliens.append({
                        "x": start_x + j * gap_x,
                        "y": start_y + i * gap_y
                    })
            
            for x in [100, screen_width//2 - 25, screen_width - 150]:
                alien_ufo.append({
                    "x": x,
                    "y": 20,
                    "health": 5
                })
                
                
            
        # Drawing the Score fetched by the player         
        pr.draw_text("Score : {}".format(score),10,20,24,pr.WHITE)
        # Drawing the lifes fetched by the player
        pr.draw_text("LIFE : {}".format(life),650,20,24,pr.WHITE)
        pr.end_drawing()
        
    return score
    

while not pr.window_should_close():
    score = game()
    game_over(score)

# ----------- Finally unloading all textures to free up disk space -----------------
pr.unload_texture(alien_img)
pr.unload_texture(player_img)
pr.unload_texture(ufo_img)

#---------- Finally closeing the game window -----------------
pr.close_window()
    
