from psychopy import visual

class Mask():

    def __init__(self, win, width=0.5, height=0.5, autoLog=None, units='pix', lineWidth=1.5, lineColor='white', 
        lineColorSpace='rgb', fillColor='white', fillColorSpace='rgb', pos=(0, 0), size=[50, 50], ori=0.0, 
        opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoDraw=False, target_height=50):

        # make the squares that form the mask, shifted from the given position by target_height
        self.up_rect = visual.Rect(win=win, width=width, height=height, autoLog=autoLog, units=units, 
        lineWidth=lineWidth, lineColor=lineColor, lineColorSpace=lineColorSpace, fillColor=fillColor, 
        fillColorSpace=fillColorSpace, pos=(pos[0], pos[1]+target_height), size=size, ori=ori, opacity=opacity, contrast=contrast, 
        depth=depth, interpolate=interpolate, name=name, autoDraw=autoDraw)

        self.down_rect = visual.Rect(win=win, width=width, height=height, autoLog=autoLog, units=units, 
        lineWidth=lineWidth, lineColor=lineColor, lineColorSpace=lineColorSpace, fillColor=fillColor, 
        fillColorSpace=fillColorSpace, pos=(pos[0], pos[1]-target_height), size=size, ori=ori, opacity=opacity, contrast=contrast, 
        depth=depth, interpolate=interpolate, name=name, autoDraw=autoDraw)

        self.left_rect = visual.Rect(win=win, width=width, height=height, autoLog=autoLog, units=units, 
        lineWidth=lineWidth, lineColor=lineColor, lineColorSpace=lineColorSpace, fillColor=fillColor, 
        fillColorSpace=fillColorSpace, pos=(pos[0]-target_height, pos[1]), size=size, ori=ori, opacity=opacity, contrast=contrast, 
        depth=depth, interpolate=interpolate, name=name, autoDraw=autoDraw)

        self.right_rect = visual.Rect(win=win, width=width, height=height, autoLog=autoLog, units=units, 
        lineWidth=lineWidth, lineColor=lineColor, lineColorSpace=lineColorSpace, fillColor=fillColor, 
        fillColorSpace=fillColorSpace, pos=(pos[0]+target_height, pos[1]), size=size, ori=ori, opacity=opacity, contrast=contrast, 
        depth=depth, interpolate=interpolate, name=name, autoDraw=autoDraw)


    def draw(self):
        self.up_rect.draw()
        self.down_rect.draw()
        self.left_rect.draw()
        self.right_rect.draw()

    def set_pos(self, pos):
        self.up_rect.pos = (pos[0], pos[1]+self.target_height)
        self.down_rect.pos = (pos[0], pos[1]-self.target_height)
        self.left_rect.pos = (pos[0]-self.target_height, pos[1])
        self.right_rect.pos = (pos[0]+self.target_height, pos[1])
