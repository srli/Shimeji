#! usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat May 24 21:39:41 2014

@author: sophie
"""

import screenlets
import cairo
from screenlets.options import BoolOption
from time import time
from random import randint
import gettext

i = 0

_ = screenlets.utils.get_translator(__file__)

class ShimejiScreenlet (screenlets.Screenlet):
    """Linux version of Shimeji. Added functionality as desktop assistant."""
    __name__ = "Shimeji"
    __version__ = "0.1"
    __author__ = "Sophie"
    __desc__ = __doc__
    
    def __init__ (self, **keyword_args):
#        self.last_draw_time = time()
        #calls super, doesn't show window yet
        screenlets.Screenlet.__init__(self, uses_theme=True, **keyword_args)
        # sets theme
        self.theme_name = "default"
        #theme loaded? sets window size according to theme-size
        if self.theme:
            sizes = (self.theme.width, self.theme.height)
        else:
            sizes = (500, 500)
        self.window.resize(sizes[0], sizes[1])
        self.width = sizes[0]
        self.height = sizes[1]
        self.update_shape()
        #show window
        self.window.show()
#        self.last_draw_time = self.last_draw_time
        self.add_options_group(_('Options'), _('Options'))       
    
    def __setattr__(self, name, value):
        #call Screenlet.__setattr___ in baseclass (Important!)
        screenlets.Screenlet.__setattr__(self, name, value)
        self.redraw_canvas()
    
    def on_init(self):
        print "Screenlet has been initialized."
        self.add_default_menuitems()

    
    def on_draw(self, ctx):
        global i
#        list_possible = ["shime1", "shime1a", "shime1b", "shime7", "shime9", "shime20", "shime30", "shime11"]
        idle_list_forwards = ["shime1", "shime1a", "shime1b", "shime2", "shime3"]
        idle_list_backwards = idle_list_forwards[::-1]
        idle_positions = idle_list_forwards + idle_list_backwards        
        ctx.set_operator(cairo.OPERATOR_CLEAR)
        ctx.fill()
        ctx.set_operator(cairo.OPERATOR_OVER)
        ctx.scale(self.scale, self.scale)
        if i == 9:
            i = 0
        if self.theme: #or (self.last_draw_time - time() > 0.5):
            print "idle_position ", i
            self.theme.render(ctx, idle_positions[i])
            print "drawing now"
            i += 1
                
    def on_draw_shape(self, ctx):
        #simple call drawing handler and pass shape-context
        self.on_draw(ctx)
        
    def draw_idle(self, ctx, image):
        ctx.set_operator(cairo.OPERATOR_CLEAR)
        ctx.fill()
        ctx.set_operator(cairo.OPERATOR_OVER)
        ctx.scale(self.scale, self.scale)
        self.theme.render(ctx, image)
        print "drawed"
        
    
#    def idle(self):
#        idle_list_forwards = ["shime1", "shime1a", "shime1b", "shime2", "shime3"]
#        idle_list_backwards = idle_list_forwards[::-1]
#        self.idle_positions = idle_list_forwards + idle_list_backwards
#        return self.idle_positions
#            
#    def on_unfocus (self, event):
#        """Called when the Screenlet's window loses focus."""
#        self.idle()


        
if __name__ == "__main__":
    #creates new session
    import screenlets.session
    screenlets.session.create_session(ShimejiScreenlet)
