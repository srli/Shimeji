#! usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat May 24 21:39:41 2014

@author: sophie
"""

import screenlets
import cairo
from screenlets.options import BoolOption
from time import sleep
from random import randint
import gettext

_ = screenlets.utils.get_translator(__file__)

class ShimejiScreenlet (screenlets.Screenlet):
    """Linux version of Shimeji. Added functionality as desktop assistant."""
    __name__ = "Shimeji"
    __version__ = "0.1"
    __author__ = "Sophie"
    __desc__ = __doc__
    
    def __init__ (self, **keyword_args):
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
        
        self.add_options_group(_('Options'), _('Options'))
    
    def __setattr__(self, name, value):
        #call Screenlet.__setattr___ in baseclass (Important!)
        screenlets.Screenlet.__setattr__(self, name, value)
        self.redraw_canvas()
    
    def on_init(self):
        print "Screenlet has been initialized."
        self.add_default_menuitems()

    
    def on_draw(self, ctx):
        list_possible = ["shime1", "shime1a", "shime1b", "shime7", "shime9", "shime20", "shime30", "shime11"]
        ctx.set_operator(cairo.OPERATOR_CLEAR)
        ctx.fill()
        ctx.set_operator(cairo.OPERATOR_OVER)
        ctx.scale(self.scale, self.scale)
        if self.theme:
            random_number = randint(0,7)
            print "random number is ", random_number
            self.theme.render(ctx, list_possible[random_number])
            print "drawing now"
    
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
        
    
    def idle(self):
        idle_list_forwards = ["shime1", "shime1a", "shime1b", "shime2", "shime3"]
        idle_list_backwards = idle_list_forwards[::-1]
        idle = idle_list_forwards + idle_list_backwards
        for i in idle:
            self.draw_idle(i)
            sleep(1)
            
    def on_unfocus (self, event):
        """Called when the Screenlet's window loses focus."""
        self.idle()


        
if __name__ == "__main__":
    #creates new session
    import screenlets.session
    screenlets.session.create_session(ShimejiScreenlet)
