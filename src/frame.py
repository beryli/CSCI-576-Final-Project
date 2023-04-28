# Use bitwise OR to determine the frame type
# For example, if (val & Frametype.SCENE) is true, then `val` has a SCENE property.
# A single frame can have multiple properties at the same time.
# Take val = 7 for example, this frame is a SCENE, a SHOT, and a SUBSHOT at the same time,
# because (7 & Frametype.SCENE), (7 & Frametype.SHOT), and (7 & Frametype.SUBSHOT) are all true.
class Frametype:
    SCENE = 4
    SHOT = 2
    SUBSHOT = 1
