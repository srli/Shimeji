#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sat May 24 18:48:34 2014

@author: sophie
"""

import screenlets
import cairo
from screenlets.options import BoolOption

import gettext

_ = screenlets.utils.get_translator(__file__)
#
#def tdoc(obj):
#	obj.__doc__ = _(obj.__doc__)
#	return obj
#
#@tdoc
class ShimejiScreenlet (screenlets.Screenlet):
"""Linux version of Shiemji. Added functionality as desktop assistant"""
    # default meta-info for Screenlets
    __name__	= 'Shimeji'
    __version__	= '0.1'
    __author__	= 'Sophie'
    __desc__	= __doc__
    
    show_vertical	= False

    def __init__ (self, **keyword_args):
  #call super (and not show window yet)
        screenlets.Screenlet.__init__(self, uses_theme=True, **keyword_args)
        # set theme
        self.theme_name = "default"
        # theme loaded? set window size according to theme-size
        if self.theme:
		sizes = (self.theme.width, self.theme.height)
        else:
		sizes = (500, 500)
      self.window.resize(sizes[0], sizes[1])
		self.width	= sizes[0]
		self.height	= sizes[1]
		self.update_shape()
		# finally, show window
		self.window.show()

		self.add_options_group(_('Options'), _('Options'))

		self.add_option(BoolOption(_('Options'), 'show_vertical',
			self.show_vertical, _('Vertical Ruler'), _('Show vertical instead of horizontal ...')))

	def __setattr__(self, name, value):
		# call Screenlet.__setattr__ in baseclass (ESSENTIAL!!!!)
		screenlets.Screenlet.__setattr__(self, name, value)
		if name == 'show_vertical':
			if value == True:
				self.width = 500
				self.height = 500
			else:
				self.width = 500
				self.height = 500
			self.redraw_canvas()

	def on_init (self):
		print "Screenlet has been initialized."
		# add default menuitems
		self.add_default_menuitems()
	
	def on_draw (self, ctx):
		ctx.set_operator(cairo.OPERATOR_OVER)
		ctx.scale(self.scale, self.scale)
   print "drawing"
		if self.theme:
			#self.theme['ruler-bg.svg'].render_cairo(ctx)
			if self.show_vertical:
				ctx.translate (100,0)
				#ctx.translate(self.width/2,self.height/2)
				ctx.rotate(1.57)
				#ctx.translate(-self.width/2,-self.height/2)

			self.theme.render(ctx, 'shime1')

	
	def on_draw_shape (self,ctx):
		# simply call drawing handler and pass shape-context
		self.on_draw(ctx)

	
# If the program is run directly or passed as an argument to the python
# interpreter then create a Screenlet instance and show it
if __name__ == "__main__":
	# create new session
	import screenlets.session
	screenlets.session.create_session(ShimejiScreenlet)

