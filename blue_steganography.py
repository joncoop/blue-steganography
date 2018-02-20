import pygame

pygame.init()

def read_textfile(file_name):
  with open(file_name, 'r') as f:
    message = f.read()

  return message

def write_textfile(text, file_name):
  with open(file_name, 'w') as f:
    f.write(text)

def load_image(file_name):
  return pygame.image.load(file_name)

def save_surface_as_image(surf, file_name):
  pygame.image.save(surf, file_name)

def chr_to_bin(c, num_bits):
  d = ord(c)
  b = bin(d)
  b = b[2:]
  
  while len(b) < 8:
    b = "0" + b
    
  return b

def message_to_bin(message, bits_per_char):
  binary_str = ""
  
  for character in message:
    binary_str += chr_to_bin(character, bits_per_char)

  return binary_str

def adjust_pixel(pixel, bit):
  red = pixel.r
  green = pixel.g
  blue = pixel.b
    
  even = red % 2
  bit = int(bit)
  
  if (even and bit == 1) or (not even and bit == 0):
    pixel

  return pixel

def build_image(pixels, dimensions):
  image = pygame.Surface(dimensions)

  for p in pixels:
    pass
  
  return image

def embed_message(message, image_file):
  image = load_image(image_file)
  pxarray = pygame.PixelArray(image)
  
  message_size = len(message)
  
  for i in range(message_size):
    pixels[i].b = 100
  
  return pixels         


def extract_message(image):
  pass

image = load_image("red.bmp")
image_rect = image.get_rect()
print(image_rect)

width = image.get_width()
height = image.get_height()

changed_image = pygame.Surface([width, height])

print(width, height)

pxarray = pygame.PixelArray(image)

for y in range(height):
  for x in range(width):
    pixel = pygame.Color(pxarray[x, y])
    #print(type(pixel), pixel)
    red = pixel.r
    green = pixel.g
    blue = pixel.b

    print(red, green, blue)
    
    changed_image.set_at((x, y), (0, 0, 255))

pygame.image.save(changed_image, "blue.png")


num = 10
binary = bin(num)


print(binary)
print(type(binary))

decimal = int(binary, 2)
print(decimal)

secret = "Hello!"

new_pixels = adjust_pixels(secret, pxarray)

for y in range(height):
  for x in range(width):
    pixel = pygame.Color(pxarray[x, y])
    red = pixel.r
    green = pixel.g
    blue = pixel.b

    loc = [x, y]
    new_color = [red, green, blue]
    
    changed_image.set_at(loc, new_color)
    
save_surface_as_image(changed_image, "blue.png")


for i in range(32, 127):
  c = chr(i)
  b = chr_to_bin(c, 8)
  print(b)

print(message_to_bin(secret, 8))
