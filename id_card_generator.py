from PIL import Image, ImageDraw, ImageFont

# Create a blank image for the ID card (Width: 400px, Height: 600px)
card_width = 400
card_height = 600
card = Image.new("RGB", (card_width, card_height), color="white")
draw = ImageDraw.Draw(card)

# Draw a header banner
draw.rectangle([(0, 0), (card_width, 120)], fill="navy")

# Load fonts (Defaults to basic PIL font if custom TTF is unavailable)
try:
  font_title = ImageFont.truetype("arial.ttf", 22)
  font_bold = ImageFont.truetype("arial.ttf", 16)
  font_regular = ImageFont.truetype("arial.ttf", 14)
except IOError:
  font_title = ImageFont.load_default()
  font_bold = ImageFont.load_default()
  font_regular = ImageFont.load_default()

# Add School/University Title
draw.text((80, 40), "GLOBAL UNIVERSITY", fill="white", font=font_title)

# Draw a placeholder box for the student photo
photo_box = [(125, 150), (275, 310)]
draw.rectangle(photo_box, outline="navy", width=3)
draw.text((145, 220), "Student Photo", fill="gray", font=font_regular)

# Student Details
student_data = {
    "Name": "Alex Johnson",
    "Student ID": "GU-2026-8941",
    "Course": "B.Sc. Computer Science",
    "Valid Upto": "June 2029",
    "Phone": "+91 98765 43210",
}

# Render text information onto the card
y_position = 350
for key, value in student_data.items():
  draw.text((40, y_position), f"{key}:", fill="navy", font=font_bold)
  draw.text((150, y_position), f"{value}", fill="black", font=font_regular)
  y_position += 35

# Save the generated ID card
card.save("student_id_card.png")
print("Student ID card generated successfully as 'student_id_card.png'!")
