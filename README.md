# 👾 Space Invaders using Python and Pyray

A classic **Space Invaders** game built using **Python** and the **Pyray** graphics library. This project demonstrates fundamental game development concepts such as game loops, keyboard input handling, collision detection, enemy spawning, projectile systems, score tracking, life management, wave regeneration, and game state management.

---


# ✨ Features

- Classic Space Invaders gameplay
- Player movement using keyboard controls
- Shoot bullets to destroy enemies
- Multiple Alien enemies
- UFO enemies with health points
- Random enemy bullet firing
- Collision detection using rectangles
- Score tracking system
- Player life system
- Automatic enemy wave regeneration
- Game Over screen
- Restart the game by pressing **R**
- Quit anytime using **ESC**

---

# 🛠 Technologies Used

- **Python 3**
- **Pyray** (Python bindings for raylib)
- **Random** module

---

# 📂 Project Structure

```text
Space-Invaders/
│
├── space_invaders.py
├── alien.png
├── player.png
├── ufo.png
├── README.md
├── screenshot1.png
├── screenshot2.png
└── requirements.txt
```

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/S-Vikram2008/Space-Invaders.git
```

Move into the project folder.

```bash
cd Space-Invaders
```

Install Pyray.

```bash
pip install pyray
```

Run the game.

```bash
python space_invaders.py
```

---

# 🎮 Controls

| Key | Action |
|------|--------|
| ⬅️ | Move Left |
| ➡️ | Move Right |
| SPACE | Shoot |
| **R** | Restart after Game Over |
| **ESC** | Quit the Game |

---

# 🎯 Objective

Destroy all invading enemies before they reach the bottom of the screen while avoiding enemy bullets.

### Earn Points

- 👾 Alien Destroyed → **+1 Point**
- 🛸 UFO Destroyed → **+5 Points**

### Game Ends When

- An Alien reaches the bottom of the screen.
- A UFO reaches the bottom of the screen.
- The player's lives reach **0**.

---

# 🧠 Game Logic

The project is organized into two major functions.

## 1. `game()`

This is the main gameplay loop.

It is responsible for:

- Initializing all game variables
- Player movement
- Enemy movement
- Bullet movement
- Collision detection
- Score calculation
- Life management
- Enemy bullet spawning
- Wave regeneration
- Drawing every object on the screen

The function continues executing until the player loses.

---

## 2. `game_over(score)`

This function displays the **Game Over** screen.

It shows:

- Final Score
- Restart instruction
- Exit instruction

Pressing **R** immediately starts a completely new game without restarting the application.

---

# 📋 Important Variables

## 🖥 Screen Variables

```python
screen_width
screen_height
```

These variables define the dimensions of the game window.

```python
screen_width = 750
screen_height = 750
```

---

## 🚀 Player Variables

```python
shuttle_x
shuttle_y
```

These variables store the current position of the player's spaceship.

- `shuttle_x` controls horizontal movement.
- `shuttle_y` keeps the player fixed near the bottom of the screen.

---

## 👾 Alien Formation Variables

```python
rows
cols
```

These determine the number of Alien enemies generated.

Example

```text
Rows = 4
Columns = 8
```

Result

```text
👾 👾 👾 👾 👾 👾 👾 👾

👾 👾 👾 👾 👾 👾 👾 👾

👾 👾 👾 👾 👾 👾 👾 👾

👾 👾 👾 👾 👾 👾 👾 👾
```

---

## 📍 Formation Position Variables

```python
start_x
start_y
gap_x
gap_y
```

These variables control the placement of every Alien.

- **start_x** → Starting horizontal position.
- **start_y** → Starting vertical position.
- **gap_x** → Horizontal spacing between Aliens.
- **gap_y** → Vertical spacing between Aliens.

Changing these values automatically changes the enemy formation.

---

## 📦 Game Object Lists

### 👾 `aliens`

Stores all Alien enemies.

Each Alien is represented using a Python dictionary.

```python
{
    "x": 80,
    "y": 50
}
```

Each dictionary stores the Alien's current position.

---

### 🛸 `alien_ufo`

Stores all UFO enemies.

Each UFO is represented as

```python
{
    "x": 100,
    "y": 20,
    "health": 5
}
```

Unlike normal Aliens, UFOs require multiple hits before being destroyed.

---

### 🟢 `bullets`

Stores every bullet fired by the player.

Example

```python
{
    "x": 350,
    "y": 620
}
```

Using a list allows multiple bullets to exist on the screen simultaneously.

---

### 🔴 `enemy_bullets`

Stores every bullet fired by enemy Aliens.

Example

```python
{
    "x": 210,
    "y": 80
}
```

Whenever no enemy bullet exists, a random Alien fires another bullet.

---

## 🏆 Score Variable

```python
score
```

Stores the player's current score.

Points are awarded as follows:

- 👾 Alien → **+1**
- 🛸 UFO → **+5**

The score is continuously displayed during gameplay.

---

## ❤️ Life Variable

```python
life
```

Stores the player's remaining lives.

```python
life = 3
```

Every time an enemy bullet hits the player,

```text
Life -= 1
```

When the life count reaches **0**, the game ends.
---

# 👾 Alien Generation

At the beginning of every game, a formation of Alien enemies is created automatically.

The formation is generated using two nested loops.

```python
for i in range(rows):
    for j in range(cols):
```

Each Alien is stored as a dictionary containing its position.

```python
{
    "x": start_x + j * gap_x,
    "y": start_y + i * gap_y
}
```

This approach makes it easy to change the number of enemies by modifying only the number of rows and columns.

---

# 🛸 UFO System

Along with the normal Aliens, three UFO enemies are also generated.

Each UFO contains an additional **health** variable.

```python
{
    "x": 100,
    "y": 20,
    "health": 5
}
```

Unlike normal Aliens, UFOs require multiple hits before being destroyed.

Each successful hit decreases the UFO's health by **1**.

Once the health reaches **0**, the UFO is destroyed and the player earns **5 points**.

---

# 🚀 Player Movement

The player controls a spaceship located near the bottom of the screen.

Movement is handled using the keyboard.

```text
Left Arrow  → Move Left
Right Arrow → Move Right
```

The spaceship is prevented from leaving the game window by applying boundary checks.

```python
if shuttle_x < 10:
    shuttle_x = 10

if shuttle_x > 740:
    shuttle_x = 740
```

---

# 🔫 Player Bullet System

Whenever the **SPACE** key is pressed, a new bullet is created.

```python
bullets.append({
    "x": shuttle_x,
    "y": screen_height - 100
})
```

Each bullet is stored inside the `bullets` list.

Every frame,

- Bullets move upward.
- Bullets leaving the screen are removed.
- Multiple bullets can exist at the same time.

This creates smooth continuous shooting.

---

# 🔴 Enemy Bullet System

Enemy bullets are stored inside the `enemy_bullets` list.

At the beginning of the game, a random Alien is selected.

```python
enemy = random.choice(aliens)
```

The selected Alien fires a bullet.

Whenever no enemy bullet exists,

```python
if not enemy_bullets:
```

another random Alien fires a new bullet.

Only one enemy bullet is active at a time, making the gameplay balanced and predictable.

---

# 💥 Collision Detection

The project uses **Rectangle Collision Detection** provided by Pyray.

```python
pr.check_collision_recs()
```

Every important object is represented as a rectangle.

Examples include

- Player bullets
- Enemy bullets
- Aliens
- UFOs
- Player spaceship

---

## 👾 Bullet vs Alien

Whenever a player bullet collides with an Alien,

- Alien is removed.
- Bullet is removed.
- Score increases by **1**.

---

## 🛸 Bullet vs UFO

Whenever a bullet hits a UFO,

- UFO health decreases.
- Bullet disappears.

If the UFO's health reaches **0**

- UFO is removed.
- Player earns **5 points**.

---

## ❤️ Enemy Bullet vs Player

Whenever an enemy bullet collides with the player's spaceship,

```text
Life -= 1
```

The enemy bullet is immediately removed.

If all lives are lost,

```text
Game Over
```

---

## 💥 Bullet vs Bullet

Player bullets can destroy enemy bullets.

Whenever both bullets collide,

- Player bullet disappears.
- Enemy bullet disappears.

This adds another defensive gameplay mechanic.

---

# 📈 Enemy Movement

Every frame, both Aliens and UFOs slowly move downward.

```python
alien["y"] += 0.5
```

```python
ufo["y"] += 0.5
```

If any enemy reaches the bottom of the screen, the game immediately ends.

---

# 🔄 Wave Regeneration

After all Aliens and UFOs are destroyed,

```python
if aliens == [] and alien_ufo == []:
```

a completely new wave is generated.

The game recreates

- Alien formation
- UFO enemies

This allows gameplay to continue indefinitely while increasing the player's score.

---

# 🎨 Rendering

Every frame, the game draws the following objects in order.

1. Background
2. Player spaceship
3. Alien enemies
4. UFO enemies
5. Player bullets
6. Enemy bullets
7. Score
8. Remaining Lives

This process repeats **20 times every second**.

---

# 🔁 Restart Mechanism

When the player loses, the **Game Over** screen is displayed.

Press

```text
R
```

to immediately restart the game.

The game creates

- New Alien wave
- New UFOs
- New player position
- New bullets
- Score = 0
- Lives = 3

without restarting the application.

---

# 📚 Concepts Demonstrated

This project demonstrates

- Game Loop
- Frame Rate Control
- Keyboard Input
- Collision Detection
- Lists
- Dictionaries
- Nested Loops
- Functions
- Conditional Statements
- Random Number Generation
- State Management
- Rendering Graphics
- Game Restart Logic
- Enemy AI (Random Shooting)
- Wave Generation

---

# 📈 Future Improvements

Possible enhancements include

- Start Menu
- Pause Menu
- Sound Effects
- Background Music
- Explosion Animations
- Power-ups
- Multiple Enemy Types
- Boss Battles
- Difficulty Levels
- High Score Saving
- Animated Sprites
- Different Bullet Types
- Particle Effects
- Mobile Support

---

# 🎓 What I Learned

While building this project, I learned

- How to build a complete real-time game using Pyray.
- How to organize game logic using functions.
- How to generate enemy formations using nested loops.
- How to manage multiple game objects using Python lists and dictionaries.
- How rectangle collision detection works.
- How to implement player and enemy projectile systems.
- How to create enemies with multiple health points.
- How to manage score and life systems.
- How to regenerate enemy waves after clearing a level.
- How to implement a restart mechanism without restarting the application.

---

# 📄 License

This project is open source and available under the **MIT License**.

---

# 👨‍💻 Author

**S Vikram**

GitHub: **https://github.com/S-Vikram2008**
