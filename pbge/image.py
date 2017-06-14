# Load one image file, use it for multiple images.

import pygame
import weakref
import util
from . import my_state

# Keep a list of already-loaded images, to save memory when multiple objects
# need to use the same image file.
pre_loaded_images = weakref.WeakValueDictionary()

class Image( object ):
    def __init__(self,fname=None,frame_width=0,frame_height=0):
        """Load image file, or create blank image, at frame size"""
        if fname:
            if fname in pre_loaded_images:
                self.bitmap = pre_loaded_images[fname]
            else:
                self.bitmap = pygame.image.load( util.image_dir( fname ) ).convert()
                self.bitmap.set_colorkey((0,0,255),pygame.RLEACCEL)
                pre_loaded_images[fname] = self.bitmap
        else:
            self.bitmap = pygame.Surface( (frame_width , frame_height) )
            self.bitmap.fill((0,0,255))
            self.bitmap.set_colorkey((0,0,255),pygame.RLEACCEL)

        if frame_width == 0:
            frame_width = self.bitmap.get_width()
        if frame_height == 0:
            frame_height = self.bitmap.get_height()

        if frame_width > self.bitmap.get_width():
            frame_width = self.bitmap.get_width()
        self.fname = fname
        self.frame_width = frame_width
        self.frame_height = frame_height

    def render( self , dest = (0,0) , frame=0, dest_surface=None ):
        # Render this Image onto the provided surface.
        # Start by determining the correct sub-area of the image.
        frames_per_row = self.bitmap.get_width() / self.frame_width
        area_x = ( frame % frames_per_row ) * self.frame_width
        area_y = ( frame / frames_per_row ) * self.frame_height
        area = pygame.Rect( area_x , area_y , self.frame_width , self.frame_height )
        dest_surface = dest_surface or my_state.screen
        dest_surface.blit(self.bitmap , dest , area )

    def num_frames( self ):
        frames_per_row = self.bitmap.get_width() / self.frame_width
        frames_per_column = self.bitmap.get_height() / self.frame_height
        return frames_per_row * frames_per_column


    def __reduce__( self ):
        # Rather than trying to save the bitmap image, just save the filename.
        return Image, ( self.fname , self.frame_width , self.frame_height )

    def tile( self , dest , frame = 0, dest_surface=None ):
        dest_surface = dest_surface or my_state.screen
        grid_w = dest.w / self.frame_width + 2
        grid_h = dest.h / self.frame_height + 2
        dest_surface.set_clip( dest )
        my_rect = pygame.Rect(0,0,0,0)

        for x in range(0,grid_w):
            my_rect.x = dest.x + x * self.frame_width
            for y in range(0,grid_h):
                my_rect.y = dest.y + y*self.frame_height
                self.render(my_rect,frame,dest_surface)

        dest_surface.set_clip( None )



