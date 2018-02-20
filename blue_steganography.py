import pygame

pygame.init()

# config
stop_flag = "[[:stop:]]"

def text_to_binary(text):
  '''
  Converts ASCII text to a string binary digits. Each character will be
  represented as 8 bits.
  '''

  binary_str = ""
  
  for c in text:
    d = ord(c)
    b = bin(d)
    b = b[2:]

    while len(b) < 8:
      b = "0" + b
    
    binary_str += b
    
  return binary_str

def binary_to_text(binary_str):
  '''
  Converts a string binary digits to ASCII text. Each character will be
  represented as 8 bits.
  '''

  result = ""

  # separate binary string into 8 bit chunks
  chunks = [binary_str[i: i+8] for i in range(0, len(binary_str), 8)]

  for c in chunks:
    d = int(c, 2)
    if 32 <= d <= 126:
      result += str(chr(d))

  return result

def hide_message(message_file_path, original_image_path, encoded_image_path):
  # read message from text file and append stop flag
  with open(message_file_path, 'r') as f:
    message = f.read()
  message += stop_flag

  # convert message to binary
  binary_digits = text_to_binary(message)
    
  # load the original image file as a surface
  surf = pygame.image.load(original_image_path)
  width = surf.get_width()
  height = surf.get_height()

  # loop through surface and adjust pixels
  digit_index = 0
  result = ""
  for x in range(width):
    for y in range(height):
      loc = [x, y]
      
      if digit_index < len(binary_digits):
        color = surf.get_at(loc)

        blue = color.b
        bit = int(binary_digits[digit_index])
        even = blue % 2 == 0
        
        if (even and bit == 1) or (not even and bit == 0):
          blue += 1

          if blue > 255:
            blue -= 2
            
        color.b = blue
        result += str(color.b % 2)
        
        surf.set_at(loc, color)
        digit_index += 1

  # save the new image
  pygame.image.save(surf, encoded_image_path)

  print("Success! Your secret message was hidden in '" + encoded_image_path + "'.")


def extract_message(encoded_image_path, extracted_message_path):
  # load image as surface
  surf = pygame.image.load(encoded_image_path)
  width = surf.get_width()
  height = surf.get_height()

  # build binary digit string from image
  binary_str = ""
  
  for x in range(width):
    for y in range(height):
      loc = [x, y]
      color = surf.get_at(loc)
      blue = color.b
      binary_str += str(blue % 2)

  # convert binary string to text
  result = binary_to_text(binary_str)
  
  # truncate any characters after stop flag
  end = result.find(stop_flag)
  result = result[:end]
  
  # write extracted message to file
  with open(extracted_message_path, 'w') as f:
    f.write(result)
        
  print("Success! Your secret message was extracted to '" + extracted_message_path + "'.")

