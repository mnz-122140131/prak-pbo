import pygame
import random

# Inheritance: Kelas Snake mewarisi dari kelas pygame.Rect
class Snake(pygame.Rect):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)  # Memanggil konstruktor kelas induk
        self.color = (0, 255, 0)
        self.direction = "RIGHT"
        self.body = [(x, y)]
        self.grow_pending = False

    # Abstraction: Metode move mengabstraksi detail pergerakan ular
    def move(self, screen_width, screen_height):
        if self.direction == "UP":
            self.y -= self.size[1]
            if self.y < 0:
                self.y = screen_height - self.size[1]
        elif self.direction == "DOWN":
            self.y += self.size[1]
            if self.y >= screen_height:
                self.y = 0
        elif self.direction == "LEFT":
            self.x -= self.size[0]
            if self.x < 0:
                self.x = screen_width - self.size[0]
        elif self.direction == "RIGHT":
            self.x += self.size[0]
            if self.x >= screen_width:
                self.x = 0

        self.body.insert(0, (self.x, self.y))

        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False

    def grow(self):
        self.grow_pending = True

    # Polymorphism: Metode draw mengoverride metode draw dari kelas induk
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, self.color, (segment[0], segment[1], self.size[0], self.size[1]))

# Encapsulation: Kelas Game mengenkapsulasi detail permainan
class Game:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.block_size = 20
        self.snake = Snake(self.screen_width // 2, self.screen_height // 2, self.block_size)  # Membuat objek ular
        self.apple_pos = self.generate_apple_position()
        self.obstacles = []
        self.game_over = False
        self.score = 0

    def generate_apple_position(self):
        x = random.randint(0, (self.screen_width - self.block_size) // self.block_size) * self.block_size
        y = random.randint(0, (self.screen_height - self.block_size) // self.block_size) * self.block_size
        return x, y

    def generate_obstacles(self):
        obstacles = []
        for _ in range(10):
            x = random.randint(0, (self.screen_width - self.block_size) // self.block_size) * self.block_size
            y = random.randint(0, (self.screen_height - self.block_size) // self.block_size) * self.block_size
            obstacles.append((x, y))
        return obstacles

    def move_obstacles(self):
        for i in range(len(self.obstacles)):
            x = random.randint(0, (self.screen_width - self.block_size) // self.block_size) * self.block_size
            y = random.randint(0, (self.screen_height - self.block_size) // self.block_size) * self.block_size
            self.obstacles[i] = (x, y)

    def check_collision(self):
        head = self.snake.body[0]
        return head in self.snake.body[1:] or head in self.obstacles

    def play_game(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Salman Snake Game")
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)

        self.show_start_screen(screen, clock, font)

        while True:
            while not self.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                            self.snake.direction = "UP"
                        elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                            self.snake.direction = "DOWN"
                        elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                            self.snake.direction = "LEFT"
                        elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                            self.snake.direction = "RIGHT"

                self.snake.move(self.screen_width, self.screen_height)

                if self.snake.x == self.apple_pos[0] and self.snake.y == self.apple_pos[1]:
                    self.apple_pos = self.generate_apple_position()
                    self.snake.grow()
                    self.score += 1
                    if self.score % 5 == 0:
                        self.obstacles = self.generate_obstacles()
                    if self.score % 5 == 0 and self.score > 0:
                        self.move_obstacles()

                if self.check_collision():
                    self.game_over = True

                screen.fill((0, 0, 0))
                self.snake.draw(screen)
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.apple_pos[0], self.apple_pos[1], self.block_size, self.block_size))
                for obstacle in self.obstacles:
                    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(obstacle[0], obstacle[1], self.block_size, self.block_size))

                score_text = font.render("Score: " + str(self.score), True, (255, 255, 255))
                screen.blit(score_text, (10, 10))

                pygame.display.flip()
                clock.tick(10)

            game_over_text = font.render("Game Over! Press R to restart", True, (255, 255, 255))
            game_over_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            screen.blit(game_over_text, game_over_rect)
            pygame.display.flip()

            while self.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.snake = Snake(self.screen_width // 2, self.screen_height // 2, self.block_size)
                            self.apple_pos = self.generate_apple_position()
                            self.obstacles = []
                            self.game_over = False
                            self.score = 0
                            break

    def show_start_screen(self, screen, clock, font):
        show_instructions = True
        while show_instructions:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        show_instructions = False

            screen.fill((0, 0, 0))
            self.draw_text(screen, "Welcome to               snake Game!", font, (255, 255, 255), self.screen_width // 2, self.screen_height // 2 - 100)
            self.draw_text(screen, " Salman   ", font, (255, 0, 0), self.screen_width // 2, self.screen_height // 2 - 100)
            self.draw_text(screen, "Use arrow keys to move", font, (255, 255, 255), self.screen_width // 2, self.screen_height // 2 - 50)
            self.draw_text(screen, "Avoid colliding with yourself or obstacles", font, (255, 255, 255), self.screen_width // 2, self.screen_height // 2)
            self.draw_text(screen, "Press SPACE to start", font, (255, 0, 255), self.screen_width // 2, self.screen_height // 2 + 50)

            pygame.display.flip()
            clock.tick(10)

    def draw_text(self, surface, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)

if __name__ == "__main__":
    game = Game()  # Encapsulation: Membuat objek game
    game.play_game()  # Abstraction: Memulai permainan dengan memanggil satu metode
