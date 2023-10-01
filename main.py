from PIL import Image, ImageFont, ImageDraw
import textwrap

FRAME_DIMENSIONS = (1280, 720)

FONT_SIZE = 100
TEXT_SPACING = 66
LINE_MAX_CHARS = 14
LOGO_LOC = (50, 50)

KDLP_YELLOW = (255, 255, 209)
KDLP_RED = (214, 76, 55)

def wrap_join(wrap):
    ret = ""
    num_lines = 0
    for string in wrap:
        ret += string + "\n"
    return ret

def find_longest_line(wrap):
    longest = -1
    for string in wrap:
        if len(string) > longest:
            longest = len(string)
    return longest

img = Image.new(mode="RGB", size=FRAME_DIMENSIONS, color=(255,255,255))
logo = Image.open("kdlp_logo.png")
LOGO_WIDTH = logo.getbbox()[2]
img.paste(logo, LOGO_LOC)
draw = ImageDraw.Draw(img)

courier = None
try:
    courier = ImageFont.truetype("Courier.ttc",FONT_SIZE)
except:
    try:
        courier = ImageFont.truetype("courier.ttf", FONT_SIZE)
    except:
        print("COULD NOT LOCATE COURIER FONT. EXITING...")
        exit(1)


text = "Bash Tips and Tricks"
wrap = textwrap.wrap(text, width=LINE_MAX_CHARS)
print(wrap)
print(find_longest_line(wrap))
wraplen = len(wrap)


TEXTBOX_HEIGHT = (wraplen * (FONT_SIZE * .75)) + ((wraplen - 1) * TEXT_SPACING)
TEXTBOX_WIDTH = find_longest_line(wrap) * (FONT_SIZE * .6)

LOGO_OFFSET = LOGO_LOC[0] + LOGO_WIDTH
TEXT_TOPLEFT = (((FRAME_DIMENSIONS[0] - LOGO_OFFSET)/2) + LOGO_OFFSET - (TEXTBOX_WIDTH/2), FRAME_DIMENSIONS[1]/2 - TEXTBOX_HEIGHT/2 - 50)

bg_x1 = TEXT_TOPLEFT[0] - (FONT_SIZE * .1)
bg_y1 = TEXT_TOPLEFT[1] # There is already a bit of padding on the top of the text box
bg_x2 = TEXT_TOPLEFT[0] + TEXTBOX_WIDTH + (FONT_SIZE * .1)
bg_y2 = TEXT_TOPLEFT[1] +  TEXTBOX_HEIGHT + (FONT_SIZE * .25) # 2.5x padding to mirror default upper padding

acc_x1 = bg_x1
acc_y1 = bg_y2
acc_x2 = bg_x2
acc_y2 = acc_y1 + 5

draw.rectangle((bg_x1, bg_y1, bg_x2, bg_y2), fill=KDLP_YELLOW)
draw.rectangle((acc_x1, acc_y1, acc_x2, acc_y2), fill=KDLP_RED)
draw.multiline_text(TEXT_TOPLEFT, wrap_join(wrap), font=courier, fill=(0,0,0), spacing=TEXT_SPACING, align='center')
img.show()