# Blue Steganography

## About

## Hiding messages

To embed a message,

  1) Import blue_steganography.
  2) Type a message in a plain text file.
  3) Assign the path to the message file.
  4) Assign the path to original image in which message will be hidden.
     The file type must be a PNG or Bitmap image. This image will not
     be changed.
  5) Assign the path to new image in which message will be hidden.
     The file type must be a PNG or Bitmap image. This image will be
     created when the message is hidden.
  6) Call hide_message()

Example usage:

```
message_file = "path/to/secret.txt"
original_image = "path/to/image1.png"
encoded_image =  "path/to/image2.png"
blue_steganography.hide_message(message_file, original_image, encoded_image)
```

## Extracting messages

To extract a message,

  1) Import blue_steganography.
  2) Assign the path to image in which message is hidden.
  3) Assign the path to the text file in which the extracted message will
     be saved.
  4) Call extract_message()
  5) Open the newly created text file to read the message.

Example Usage:

```
encoded_image =  "path/to/image2.png"
blue_steganography.extract_message(encoded_image, extracted_message_path)
```
