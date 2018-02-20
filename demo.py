import blue_steganography

# first let's hide a message
message_file = "path/to/secret.txt"
original_image = "path/to/image1.png"
encoded_image =  "path/to/image2.png"
extracted_message = "path/to/decrypted.txt"

blue_steganography.hide_message(message_file, original_image, encoded_image)


# now let's get the message back out
encoded_image =  "path/to/image2.png"
extracted_message = "path/to/decrypted.txt"
blue_steganography.extract_message(encoded_image, extracted_message)
