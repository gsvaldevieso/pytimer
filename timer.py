import pygame
from pygame.locals import *

class Timer:
  DELAY_TIME = 1000
  WIDTH   = 640
  HEIGHT  = 480
  hours   = 0
  minutes = 0
  seconds = 0
  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN, 32)
    self.running = True
    self.paused = False
    
  def reset_values(self):
    self.hours = 0
    self.minutes = 0
    self.seconds = 0

  def start(self):
    while self.running:
      events = pygame.event.get()
      self.event_worker(events)
      
      if self.paused: continue

      self.draw()
      self.inc_timer()
      pygame.time.delay(self.DELAY_TIME)
    
    pygame.quit()

  def event_worker(self, events):
    for event in events:
      if event.type == pygame.KEYUP:
          if event.key == pygame.K_r:
            self.reset_values()
            self.paused = False
          if event.key == pygame.K_p:
            self.paused = not self.paused
          if event.key == pygame.K_q:
            self.running = False
            
  def draw(self):
    self.screen.fill((120, 120, 120))
    self.print_main_clock(str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + ":" + str(self.seconds).zfill(2))
    self.print_instructions()
    pygame.display.flip()

  def inc_timer(self):
    self.seconds += 1
    
    if self.seconds >= 60:
      self.minutes += 1
      self.seconds = 0
    
    if self.minutes >= 60:
      self.hours += 1
      self.minutes = 0

  def print_instructions(self):
    myfont = pygame.font.SysFont("consolas", 30)
    text = myfont.render("R - Restart or Start / P - Pause or Continue / Q - Quit", 1, (0,255,0))
    text_rect = text.get_rect(center=(self.WIDTH/2, self.HEIGHT/6))
    self.screen.blit(text, text_rect)
    
  def print_main_clock(self, text):
    myfont = pygame.font.SysFont("consolas", 200)
    text = myfont.render(text, 1, (255,0,0))
    text_rect = text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
    self.screen.blit(text, text_rect)
    
timer = Timer()
timer.start()
