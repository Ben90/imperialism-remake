#!/usr/bin/python3
# Imperialism remake
# Copyright (C) 2015 Spitaels <spitaelsantoine@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from PyQt5.QtGui.QPolygon import QPolygon
import math

class QHexagon(QPolygon):
    """Class QHexagon
    """
    # Attributes:
    center = None  # (int,int) 
    size = 0  # (int) 
    rotation = 0  # (int 0 to 360) 
    
    def __init__(self, center, size, rotation):
	


    # Operations
    def width(self):
        """function width
        
        returns int
        """
	return size * math.sqrt(3)/2; 
    
    
    def draw(self, scene, color, texture):
        """function draw
        
        scene: QGraphicsScene
        color: QColor
        texture: QPixmap
        
        returns 
        """
        return None # should raise NotImplementedError()
