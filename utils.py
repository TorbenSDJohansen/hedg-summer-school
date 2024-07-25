from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def draw_picture(results, picture_path, figsize=(12, 8), font_size=24):
    """
    Draw bounding boxes and labels on the image and display it.

    Parameters:
    - results (list): Detection results containing score, label, and bounding box coordinates.
    - picture_path (str): Path to the image file.
    - figsize (tuple): Size of the figure (width, height) in inches.
    - font_size (int): Size of the font for labels.
    """
    # Open the image
    image = Image.open(picture_path)
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        # Adjust the path to the font file as needed; here, using a default PIL font
        font = ImageFont.truetype("arial.ttf", font_size)  # You can use a different font file
    except IOError:
        # If the font file is not found, use the default PIL font
        font = ImageFont.load_default()
    
    # Draw boxes and labels
    for result in results:
        score = result['score']
        label = result['label']
        box = result['box']
        
        if score > 0.5:  # Adjust the confidence threshold as needed
            # Extract bounding box coordinates
            xmin = box['xmin']
            ymin = box['ymin']
            xmax = box['xmax']
            ymax = box['ymax']
            
            # Draw the bounding box
            draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=3)
            
            # Draw the label
            text = f"{label} ({score:.2f})"
            draw.text((xmin, ymin), text, font=font, fill="blue")

    # Display the image with bounding boxes and labels
    plt.figure(figsize=figsize)  # Set the figure size
    plt.imshow(image)
    plt.axis('off')  # Turn off axis
    plt.show()