from __future__ import annotations
import cPy.CoreAPI
#PrimAPI
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class SpiralProfile(Enum):
	'''
			
		The profile type of the spiral.
		
	'''
	CIRCLE = Coat_CPP.SpiralProfile.CIRCLE.value
	RECTANGLE = Coat_CPP.SpiralProfile.RECTANGLE.value


class FontStyle(Enum):
	'''
			
		Enumeration of the string drawing styles.
		
	'''
	Regular = Coat_CPP.FontStyle.Regular.value
	Italic = Coat_CPP.FontStyle.Italic.value
	Underline = Coat_CPP.FontStyle.Underline.value
	StrikeThrough = Coat_CPP.FontStyle.StrikeThrough.value


class FontWeight(Enum):
	
	Dont = Coat_CPP.FontWeight.Dont.value
	Thin = Coat_CPP.FontWeight.Thin.value
	ExtraLight = Coat_CPP.FontWeight.ExtraLight.value
	Light = Coat_CPP.FontWeight.Light.value
	Normal = Coat_CPP.FontWeight.Normal.value
	Medium = Coat_CPP.FontWeight.Medium.value
	DemiBold = Coat_CPP.FontWeight.DemiBold.value
	Bold = Coat_CPP.FontWeight.Bold.value
	ExtraBold = Coat_CPP.FontWeight.ExtraBold.value
	Black = Coat_CPP.FontWeight.Black.value


class ThreadProfile(Enum):
	'''
			
		thread profile types
		
	'''
	ThreadNone = Coat_CPP.ThreadProfile.ThreadNone.value
	ThreadTriangle = Coat_CPP.ThreadProfile.ThreadTriangle.value
	ThreadTrapeze = Coat_CPP.ThreadProfile.ThreadTrapeze.value
	ThreadRectangular = Coat_CPP.ThreadProfile.ThreadRectangular.value
	ThreadRound = Coat_CPP.ThreadProfile.ThreadRound.value
	ThreadPersistent = Coat_CPP.ThreadProfile.ThreadPersistent.value


class ThreadStudBodyType(Enum):
	'''
			
		thread body type
		
	'''
	StudCylinder = Coat_CPP.ThreadStudBodyType.StudCylinder.value
	StudCone = Coat_CPP.ThreadStudBodyType.StudCone.value


class SlitType(Enum):
	'''
			
		enumeration the slit types
		
	'''
	none = Coat_CPP.SlitType.none.value
	Slot = Coat_CPP.SlitType.Slot.value
	Phillipse = Coat_CPP.SlitType.Phillipse.value
	Pozidriv = Coat_CPP.SlitType.Pozidriv.value
	Robertson = Coat_CPP.SlitType.Robertson.value
	HexSocket = Coat_CPP.SlitType.HexSocket.value
	SecurityHexSocket = Coat_CPP.SlitType.SecurityHexSocket.value
	Torx = Coat_CPP.SlitType.Torx.value
	SecurityTorx = Coat_CPP.SlitType.SecurityTorx.value
	TriWing = Coat_CPP.SlitType.TriWing.value
	TorqSet = Coat_CPP.SlitType.TorqSet.value
	TripleSquare = Coat_CPP.SlitType.TripleSquare.value
	Polydrive = Coat_CPP.SlitType.Polydrive.value
	DoubleSquare = Coat_CPP.SlitType.DoubleSquare.value
	SplineDrive = Coat_CPP.SlitType.SplineDrive.value
	DoubleHex = Coat_CPP.SlitType.DoubleHex.value
	Bristol = Coat_CPP.SlitType.Bristol.value
	Pentalobular = Coat_CPP.SlitType.Pentalobular.value
	Frearson = Coat_CPP.SlitType.Frearson.value
	SnakeEyes = Coat_CPP.SlitType.SnakeEyes.value
	TA = Coat_CPP.SlitType.TA.value
	TP3 = Coat_CPP.SlitType.TP3.value
	MorTorq = Coat_CPP.SlitType.MorTorq.value
	ClutCHG = Coat_CPP.SlitType.ClutCHG.value
	ClutCHA = Coat_CPP.SlitType.ClutCHA.value
	GroupEyes = Coat_CPP.SlitType.GroupEyes.value


class BoltHeadType(Enum):
	'''
			
		enumeration the types of the bolt head
		
	'''
	BoltNone = Coat_CPP.BoltHeadType.BoltNone.value
	BoltHexa = Coat_CPP.BoltHeadType.BoltHexa.value
	Countersunk = Coat_CPP.BoltHeadType.Countersunk.value
	BoltRound = Coat_CPP.BoltHeadType.BoltRound.value
	Pan = Coat_CPP.BoltHeadType.Pan.value
	Dome = Coat_CPP.BoltHeadType.Dome.value
	Oval = Coat_CPP.BoltHeadType.Oval.value
	Square = Coat_CPP.BoltHeadType.Square.value
	TShaped = Coat_CPP.BoltHeadType.TShaped.value
	Cylinder = Coat_CPP.BoltHeadType.Cylinder.value
	Lamb = Coat_CPP.BoltHeadType.Lamb.value
	Rim = Coat_CPP.BoltHeadType.Rim.value
	Eye = Coat_CPP.BoltHeadType.Eye.value
	Bugle = Coat_CPP.BoltHeadType.Bugle.value
	Clop = Coat_CPP.BoltHeadType.Clop.value


class NutType(Enum):
	'''
			
		enumeration the types of the nut
		
	'''
	NutNone = Coat_CPP.NutType.NutNone.value
	NutHexa = Coat_CPP.NutType.NutHexa.value
	Quard = Coat_CPP.NutType.Quard.value
	Acorn = Coat_CPP.NutType.Acorn.value
	Lowacorn = Coat_CPP.NutType.Lowacorn.value
	NutFlange = Coat_CPP.NutType.NutFlange.value
	Slits = Coat_CPP.NutType.Slits.value
	Radial = Coat_CPP.NutType.Radial.value
	NutLamb = Coat_CPP.NutType.NutLamb.value
	NutRim = Coat_CPP.NutType.NutRim.value
	Selflock = Coat_CPP.NutType.Selflock.value
	NutTShaped = Coat_CPP.NutType.NutTShaped.value
	Clamplever = Coat_CPP.NutType.Clamplever.value
	NtCount = Coat_CPP.NutType.NtCount.value


class ThreadSurface(Enum):
	
	ThreadCylinder = Coat_CPP.ThreadSurface.ThreadCylinder.value
	ThreadCone = Coat_CPP.ThreadSurface.ThreadCone.value
	ThreadEdge = Coat_CPP.ThreadSurface.ThreadEdge.value


class prim():
	'''
			
		The abstract prim class.
		
	'''

	def __init__(self):
		pass # CPP source

	def class_name(self) -> any:
		'''
			
		get the primitive class name.
		
		'''
		pass # cpp source

	def name(self, s: str) -> prim:
		'''
			
		set the primitive object name.

		Args:
			s (str): the object name

		Returns:
			prim: the prim object reference
		
		'''
		pass # cpp source

	def name(self) -> any:
		'''
			
		get the primitive object name.
		
		'''
		pass # cpp source

	def add(self, v: cPy.CoreAPI.Volume):
		'''
			
		add the prim into scene

		Args:
			v (Volume): the scene volume reference
		
		'''
		pass # cpp source

	def subtract(self, v: cPy.CoreAPI.Volume):
		'''
			
		subtract the prim from scene

		Args:
			v (Volume): the scene volume reference
		
		'''
		pass # cpp source

	def intersect(self, v: cPy.CoreAPI.Volume):
		'''
			
		intersect the prim into scene

		Args:
			v (Volume): the scene volume reference
		
		'''
		pass # cpp source

	def merge(self, v: cPy.CoreAPI.Volume, op: cPy.CoreAPI.BoolOpType):
		'''
			
		merge the prim into scene

		Args:
			v (Volume): the scene volume reference
			op (BoolOpType): the type of the merge
		
		'''
		pass # cpp source

	def mesh(self) -> cPy.CoreAPI.Mesh:
		'''
			
		get the mesh prim

		Returns:
			cPy.CoreAPI.Mesh: mesh object
		
		'''
		pass # cpp source

	def color(self, CL: int) -> prim:
		'''
			
		assign the color to the primitive (in voxels)

		Args:
			CL (int): color in hexadecimal form 0xAARRGGBB

		Returns:
			prim: the reference
		
		'''
		pass # cpp source

	def color(self, r: float, g: float, b: float, a: float) -> prim:
		'''
			
		assign the color to the primitive (in voxels)

		Args:
			r (float): red value 0..255
			g (float): green value 0..255
			b (float): blue value 0..255
			a (float): alpha value 0..255

		Returns:
			prim: the reference
		
		'''
		pass # cpp source

	def color(self, r: float, g: float, b: float) -> prim:
		'''
			
		assign the color to the primitive (in voxels)

		Args:
			r (float): red value 0..255
			g (float): green value 0..255
			b (float): blue value 0..255

		Returns:
			prim: the reference
		
		'''
		pass # cpp source

	def color(self, colorid: str) -> prim:
		'''
			
		assign the color to the primitive (in voxels)

		Args:
			colorid (str): the color in any suitable form: "RGB", "ARGB", "RRGGBB", "AARRGGBB", "#RGB", "#ARGB", "#RRGGBB", "#AARRGGBB",
		any web-color common name as "red", "green", "purple", google "webcolors"

		Returns:
			prim: the reference
		
		'''
		pass # cpp source

	def gloss(self, value: float) -> prim:
		'''
			
		assign the gloss for the voxel primitive, it will work only if the color already assigned

		Args:
			value (float): the [0..1] value of the gloss

		Returns:
			prim: the reference
		
		'''
		pass # cpp source

	def roughness(self, value: float) -> prim:
		'''
			
		assign the roughness for the voxel primitive, it will work only if the color already assigned

		Args:
			value (float): the [0..1] value of the roughness

		Returns:
			prim: the reference
		
		'''
		pass # cpp source

	def metal(self, value: float) -> prim:
		'''
			
		the metalliclty value for the voxel primitive, it will work only if the color already assigned

		Args:
			value (float): the [0..1] metal value

		Returns:
			prim: the reference
		
		'''
		pass # cpp source

	def opacity(self, value: float) -> prim:
		'''
			
		assign the opacity of the color over the voxel primitive. The color should be assigned before you assign the opacity,
		for example p.color("red").opacity(0.5)

		Args:
			value (float): the opacity value [0..1]

		Returns:
			prim: the reference
		
		'''
		pass # cpp source

	def details(self, det_level: float) -> prim:
		'''
			
		set the detail level

		Returns:
			prim: prim reference
		
		'''
		pass # cpp source

	def details(self) -> float:
		'''
			
		get the detail level

		Returns:
			float: detail level
		
		'''
		pass # cpp source

	def transform(self, t: any) -> prim:
		'''
			
		set the transform matrix

		Args:
			t : the matrix

		Returns:
			prim: prim reference
		
		'''
		pass # cpp source

	def transform(self) -> any:
		'''
			
		get the transform matrix

		Returns:
			any: matrix
		
		'''
		pass # cpp source

	def scale(self, scale: float) -> prim:
		'''
			
		set the scale

		Args:
			scale (float): the scale factor

		Returns:
			prim: prim reference
		
		'''
		pass # cpp source

	def scale(self, v: any) -> prim:
		'''
			
		set the scale

		Args:
			v : the scale vector

		Returns:
			prim: this primitive reference
		
		'''
		pass # cpp source

	def scale(self) -> any:
		'''
			
		get the scale

		Returns:
			any: the scale 3d vector
		
		'''
		pass # cpp source

	def translate(self, _0: any) -> prim:
		'''
			
		Set the primitive translation

		Args:
			_pos : the new primitive position

		Returns:
			prim: this primitive reference
		
		'''
		pass # cpp source

	def translate(self) -> any:
		'''
			
		get the primitive translation

		Returns:
			any: primitive translation
		
		'''
		pass # cpp source

	def translate(self, x: float, y: float, z: float) -> prim:
		'''
			
		Set the primitive translation

		Args:
			x (float): the new x primitive position
			y (float): the new y primitive position
			z (float): the new z primitive position

		Returns:
			prim: this primitive reference
		
		'''
		pass # cpp source

	def x(self, x: float) -> prim:
		'''
			
		shift the primitive along the x - axis

		Args:
			x (float): the x value

		Returns:
			prim: this primitive reference
		
		'''
		pass # cpp source

	def y(self, y: float) -> prim:
		'''
			
		shift the primitive along the y - axis

		Args:
			y (float): the y value

		Returns:
			prim: this primitive reference
		
		'''
		pass # cpp source

	def z(self, z: float) -> prim:
		'''
			
		shift the primitive along the z - axis

		Args:
			z (float): the z value

		Returns:
			prim: this primitive reference
		
		'''
		pass # cpp source

	def auto_divide(self, average_div: float) -> prim:
		'''
			
		set the auto devide

		Args:
			average_div (float): the average divide factor

		Returns:
			prim: this prim reference
		
		'''
		pass # cpp source

	def step_divide(self, step: float) -> prim:
		'''
			
		set the step devide

		Args:
			step (float): the step divide factor

		Returns:
			prim: primitive reference
		
		'''
		pass # cpp source

	def fillet(self, radius: float) -> prim:
		'''
			
		set the fillet

		Args:
			radius (float): the fillet radius

		Returns:
			prim: this primitive reference
		
		'''
		pass # cpp source

	@staticmethod
	def debug_on(isOn: bool = True):
		'''
			
		indicates whether to turn on or off the debug mode.

		Args:
			isOn (bool): if this parameter is true, the debug mode is on, otherwise the debug mode is off.
		
		'''
		pass # cpp source

	@staticmethod
	def debug_clear():
		'''
			
		clear the debug info for primitive operations
		
		'''
		pass # cpp source

	@staticmethod
	def push_transform(t: any):
		'''
			
		set the global transform matrix to all primitives

		Args:
			t : the matrix
		
		'''
		pass # cpp source

	@staticmethod
	def push_translate(d: any):
		'''
			
		Set the translation to all primitives
		
		Not implemented yet

		Args:
			d : the new position of the primitives
		
		'''
		pass # cpp source

	@staticmethod
	def push_scale(scale: float):
		'''
			
		Set the scale to all primitives
		
		Not implemented yet

		Args:
			scale (float): the new scale factor
		
		'''
		pass # cpp source

	@staticmethod
	def push_scale(s: any):
		'''
			
		Set the scale to all primitives
		
		Not implemented yet
		
		'''
		pass # cpp source

	@staticmethod
	def push_details(details_modulator: float):
		'''
			
		set the detail level to all primitives
		
		Not implemented yet

		Args:
			details_modulator (float): datail level
		
		'''
		pass # cpp source

	@staticmethod
	def reset_transform():
		'''
			
		reset the global transform matrix
		
		Not implemented yet
		
		'''
		pass # cpp source

	def fillet_relative(self) -> float:
		'''
			
		calculates a fillet relative value (0..1).

		Returns:
			float: fillet relative value
		
		'''
		pass # cpp source



class box(prim):
	'''
			
		The box.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->box:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a box class or its descendant, and if so, returns the specified object, but of the box type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, sizeX: float, sizeY: float, sizeZ: float):
		pass # CPP source

	def __init__(self, size: any):
		pass # CPP source

	def __init__(self, pos: any, size: any):
		pass # CPP source

	def __init__(self, pos: any, size: any, fillet: float):
		pass # CPP source

	def axis(self, directionX: any) -> box:
		'''
			
		set the x-direction

		Args:
			directionX : the x-direction

		Returns:
			box: box reference
		
		'''
		pass # cpp source

	def axis(self, directionX: any, directionY: any) -> box:
		'''
			
		set the x and y direction

		Args:
			directionX : the x-direction
			directionY : the y-direction

		Returns:
			box: box reference
		
		'''
		pass # cpp source

	def axis(self, directionX: any, directionY: any, directionZ: any) -> box:
		'''
			
		set the x, y and z direction

		Args:
			directionX : the x-direction
			directionY : the y-direction
			directionZ : the z-direction

		Returns:
			box: box reference
		
		'''
		pass # cpp source

	def reset_axis(self) -> box:
		'''
			
		reset the x, y and z direction

		Returns:
			box: box reference
		
		'''
		pass # cpp source

	def axis_x(self) -> any:
		'''
			
		get the x-axis

		Returns:
			any: vec3 axis
		
		'''
		pass # cpp source

	def axis_y(self) -> any:
		'''
			
		get the y-axis

		Returns:
			any: vec3 axis
		
		'''
		pass # cpp source

	def axis_z(self) -> any:
		'''
			
		get the z-axis

		Returns:
			any: vec3 axis
		
		'''
		pass # cpp source

	def divide(self, nx: int, ny: int, nz: int) -> box:
		'''
			
		set the number deviding

		Args:
			nx (int): number deviding along the x-axis
			ny (int): number deviding along the y-axis
			nz (int): number deviding along the z-axis

		Returns:
			box: box reference
		
		'''
		pass # cpp source

	def size(self, _0: any) -> box:
		'''
			
		set the box size

		Args:
			_size : size

		Returns:
			box: box reference
		
		'''
		pass # cpp source

	def size(self, x: float, y: float, z: float) -> box:
		'''
			
		set the box size

		Args:
			x (float): size x
			y (float): size y
			z (float): size z

		Returns:
			box: box reference
		
		'''
		pass # cpp source

	def size(self) -> any:
		'''
			
		get the box size.

		Returns:
			any: size
		
		'''
		pass # cpp source

	def fillet_relative(self) -> float:
		'''
			
		calculates a fillet relative value (0..1).

		Returns:
			float: fillet relative value
		
		'''
		pass # cpp source



class torus(box):
	'''
			
		The torus.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->torus:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a torus class or its descendant, and if so, returns the specified object, but of the torus type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, ringRadius: float, crossSectionRadius: float):
		pass # CPP source

	def __init__(self, pos: any, ringRadius: float, crossSectionRadius: float):
		pass # CPP source

	def slices(self, _0: int) -> torus:
		'''
			
		set the number of slices in the mesh.

		Args:
			_slices (int): number of slices.

		Returns:
			torus: torus reference
		
		'''
		pass # cpp source

	def slices(self) -> int:
		'''
			
		get the number of slices in the mesh.

		Returns:
			int: number of slices
		
		'''
		pass # cpp source

	def rings(self, _0: int) -> torus:
		'''
			
		set the number of rings in the mesh.

		Args:
			_rings (int): number of rings.

		Returns:
			torus: torus reference
		
		'''
		pass # cpp source

	def rings(self) -> int:
		'''
			
		get the number of rings in the mesh.

		Returns:
			int: number of rings
		
		'''
		pass # cpp source

	def radius(self, r: float) -> torus:
		'''
			
		set the ring radius.

		Args:
			r (float): ring radius

		Returns:
			torus: torus reference
		
		'''
		pass # cpp source

	def radius(self) -> float:
		'''
			
		get the ring radius.

		Returns:
			float: ring radius
		
		'''
		pass # cpp source

	def section_radius(self, section_r: float) -> torus:
		'''
			
		set the cross section radius.

		Args:
			section_r (float): cross section radius

		Returns:
			torus: torus reference
		
		'''
		pass # cpp source

	def section_radius(self) -> float:
		'''
			
		get the cross section radius.

		Returns:
			float: cross section radius
		
		'''
		pass # cpp source

	def diameter(self, d: float) -> torus:
		'''
			
		set the ring diameter.

		Args:
			d (float): ring diameter

		Returns:
			torus: torus reference
		
		'''
		pass # cpp source

	def diameter(self) -> float:
		'''
			
		get the ring diameter.

		Returns:
			float: ring diameter
		
		'''
		pass # cpp source

	def section_diameter(self, section_d: float) -> torus:
		'''
			
		set the cross section diameter.

		Args:
			section_d (float): cross section diameter

		Returns:
			torus: torus reference
		
		'''
		pass # cpp source

	def section_diameter(self) -> float:
		'''
			
		get the cross section diameter.

		Returns:
			float: cross section diameter
		
		'''
		pass # cpp source

	def sector_on(self, _0: bool) -> torus:
		'''
			
		set the flag to create a portion of torus.

		Args:
			_switch (bool): the boolean true/false value

		Returns:
			torus: torus reference
		
		'''
		pass # cpp source

	def sector_on(self) -> bool:
		'''
			
		get the flag of creating a portion of torus. Default = false.

		Returns:
			bool: the sector switch
		
		'''
		pass # cpp source

	def slices_angle(self, angle: float) -> torus:
		'''
			
		When sector is on, specifies the angle for torus slices. Default = 360 degrees.

		Args:
			angle (float): the angle for torus slices

		Returns:
			torus: torus reference
		
		'''
		pass # cpp source

	def slices_angle(self) -> float:
		'''
			
		get the angle for torus slices

		Returns:
			float: the slices angle
		
		'''
		pass # cpp source

	def rings_angle(self, angle: float) -> torus:
		'''
			
		When sector is on, specifies the angle for torus rings. Default = 360 degrees.

		Args:
			angle (float): the angle for torus rings

		Returns:
			torus: torus reference
		
		'''
		pass # cpp source

	def rings_angle(self) -> float:
		'''
			
		get the angle for torus rings

		Returns:
			float: the rings angle
		
		'''
		pass # cpp source



class sphere(prim):
	'''
			
		The sphere.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->sphere:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a sphere class or its descendant, and if so, returns the specified object, but of the sphere type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, radius: float):
		pass # CPP source

	def __init__(self, pos: any, radius: float):
		pass # CPP source

	def radius(self, r: float) -> sphere:
		'''
			
		set the radius of the sphere.

		Args:
			r (float): radius.

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def radius(self) -> float:
		'''
			
		get the radius of the sphere.

		Returns:
			float: radius value
		
		'''
		pass # cpp source

	def diameter(self, d: float) -> sphere:
		'''
			
		set the diameter of the sphere.

		Args:
			d (float): diameter.

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def diameter(self) -> float:
		'''
			
		get the diameter of the sphere.

		Returns:
			float: diameter value
		
		'''
		pass # cpp source

	def sub_division(self, subdiv: int) -> sphere:
		'''
			
		set the degree for subdivision in the mesh.

		Args:
			subdiv (int): subdivision.

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def sub_division(self) -> int:
		'''
			
		get the degree of subdivision triangular or cubic division of the sphere.

		Returns:
			int: subdivision degree.
		
		'''
		pass # cpp source

	def sub_div_mode(self, divmode: any) -> sphere:
		'''
			
		set the division mode for the mesh.

		Args:
			divmode : mode of the mesh division.

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def sub_div_mode(self) -> any:
		'''
			
		get the division mode for the mesh.

		Returns:
			any: mode of the mesh division
		
		'''
		pass # cpp source

	def rings(self, _0: int) -> sphere:
		'''
			
		set the number of rings in the mesh.

		Args:
			_rings (int): number of rings.

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def rings(self) -> int:
		'''
			
		get the number of rings in the mesh.

		Returns:
			int: number of rings
		
		'''
		pass # cpp source

	def slices(self, _0: int) -> sphere:
		'''
			
		set the number of slices in the mesh.

		Args:
			_slices (int): number of slices.

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def slices(self) -> int:
		'''
			
		get the number of slices in the mesh.

		Returns:
			int: number of slices
		
		'''
		pass # cpp source

	def sector_on(self, _0: bool) -> sphere:
		'''
			
		set the flag to create a portion of sphere.

		Args:
			_switch (bool): the boolean true/false value

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def sector_on(self) -> bool:
		'''
			
		get the flag of creating a portion of sphere. Default = false.

		Returns:
			bool: the sector switch
		
		'''
		pass # cpp source

	def slice_from(self, angle: float) -> sphere:
		'''
			
		When sector is on, specifies the angle where the sphere slice begins.

		Args:
			angle (float): the angle for sphere slice begin

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def slice_from(self) -> float:
		'''
			
		get the angle where the sphere slice begins.

		Returns:
			float: the slice begin angle
		
		'''
		pass # cpp source

	def slice_to(self, angle: float) -> sphere:
		'''
			
		When sector is on, specifies the angle where the sphere slice ends.

		Args:
			angle (float): the angle for sphere slice end

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def slice_to(self) -> float:
		'''
			
		get the angle where the sphere slice ends.

		Returns:
			float: the slice end angle
		
		'''
		pass # cpp source

	def ring_from(self, angle: float) -> sphere:
		'''
			
		When sector is on, specifies the angle where the sphere ring begins.

		Args:
			angle (float): the angle for sphere ring begin

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def ring_from(self) -> float:
		'''
			
		get the angle where the sphere ring begins.

		Returns:
			float: the ring begin angle
		
		'''
		pass # cpp source

	def ring_to(self, angle: float) -> sphere:
		'''
			
		When sector is on, specifies the angle where the sphere ring ends.

		Args:
			angle (float): the angle for sphere ring end

		Returns:
			sphere: sphere reference
		
		'''
		pass # cpp source

	def ring_to(self) -> float:
		'''
			
		get the angle where the sphere ring ends.

		Returns:
			float: the ring end angle
		
		'''
		pass # cpp source



class ellipse(sphere):
	'''
			
		The ellipse.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->ellipse:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a ellipse class or its descendant, and if so, returns the specified object, but of the ellipse type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, pos: any, rx: float, ry: float, rz: float):
		pass # CPP source

	def __init__(self, pos: any, size: any):
		pass # CPP source

	def __init__(self, size: any):
		pass # CPP source

	def axis(self, directionX: any, directionY: any = 3, directionZ: any = 3) -> ellipse:
		'''
			
		set the axis x, y and z direction

		Args:
			directionX : the x-direction
			directionY : the y-direction
			directionZ : the z-direction

		Returns:
			ellipse: ellipse reference
		
		'''
		pass # cpp source

	def reset_axis(self) -> ellipse:
		'''
			
		reset the x, y and z directions

		Returns:
			ellipse: ellipse reference
		
		'''
		pass # cpp source

	def size(self, _0: any) -> ellipse:
		'''
			
		set the size of the ellipse.

		Args:
			_size : size

		Returns:
			ellipse: ellipse reference
		
		'''
		pass # cpp source

	def size(self) -> any:
		'''
			
		get the size of the ellipse.

		Returns:
			any: ellipse size
		
		'''
		pass # cpp source



class cylinder(prim):
	'''
			
		The cylinder.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->cylinder:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a cylinder class or its descendant, and if so, returns the specified object, but of the cylinder type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, height: float, radiusTop: float, radiusBottom: float, fillet: float = 0.0):
		pass # CPP source

	def __init__(self, posTop: any, posBottom: any, radiusTop: float, radiusBottom: float, fillet: float = 0.0):
		pass # CPP source

	def positionTop(self, pos: any) -> cylinder:
		'''
			
		set the top position.

		Args:
			pos : position

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def positionTop(self) -> any:
		'''
			
		get the top position.

		Returns:
			any: position
		
		'''
		pass # cpp source

	def positionBottom(self, pos: any) -> cylinder:
		'''
			
		set the bottom position.

		Args:
			pos : position

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def positionBottom(self) -> any:
		'''
			
		get the bottom position.

		Returns:
			any: position
		
		'''
		pass # cpp source

	def radiusTop(self, r: float) -> cylinder:
		'''
			
		set the top radius.

		Args:
			r (float): radius

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def radiusTop(self) -> float:
		'''
			
		get the top radius.

		Returns:
			float: radius value
		
		'''
		pass # cpp source

	def radiusBottom(self, r: float) -> cylinder:
		'''
			
		set the bottom radius.

		Args:
			r (float): radius

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def radiusBottom(self) -> float:
		'''
			
		get the bottom radius.

		Returns:
			float: radius value
		
		'''
		pass # cpp source

	def radius(self, r: float) -> cylinder:
		'''
			
		set the radius.

		Args:
			r (float): radius

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def radius(self) -> float:
		'''
			
		get the radius.

		Returns:
			float: radius value
		
		'''
		pass # cpp source

	def diameterTop(self, d: float) -> cylinder:
		'''
			
		set the top diameter.

		Args:
			d (float): diameter

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def diameterTop(self) -> float:
		'''
			
		get the top diameter.

		Returns:
			float: diameter value
		
		'''
		pass # cpp source

	def diameterBottom(self, r: float) -> cylinder:
		'''
			
		set the bottom diameter.

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def diameterBottom(self) -> float:
		'''
			
		get the bottom diameter.

		Returns:
			float: diameter value
		
		'''
		pass # cpp source

	def diameter(self, d: float) -> cylinder:
		'''
			
		set the diameter.

		Args:
			d (float): diameter

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def diameter(self) -> float:
		'''
			
		get the diameter.

		Returns:
			float: diameter value
		
		'''
		pass # cpp source

	def height(self, _0: float) -> cylinder:
		'''
			
		set the height in the z-axis.

		Args:
			_height (float): height

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def height(self) -> float:
		'''
			
		get the height.

		Returns:
			float: height value
		
		'''
		pass # cpp source

	def sectorAngle(self, angle: float) -> cylinder:
		'''
			
		set the angle for cylinder with sector.

		Args:
			angle (float): the sector angle

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def sectorAngle(self) -> float:
		'''
			
		get the sector angle.

		Returns:
			float: angle value
		
		'''
		pass # cpp source

	def topCapScale(self, scale: float) -> cylinder:
		'''
			
		set the top cap scale.

		Args:
			scale (float): the scale value

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def topCapScale(self) -> float:
		'''
			
		get the top cap scale.

		Returns:
			float: the scale value
		
		'''
		pass # cpp source

	def bottomCapScale(self, scale: float) -> cylinder:
		'''
			
		set the bottom cap scale.

		Args:
			scale (float): the scale value

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def bottomCapScale(self) -> float:
		'''
			
		get the bottom cap scale.

		Returns:
			float: the scale value
		
		'''
		pass # cpp source

	def slices(self, nslices: int) -> cylinder:
		'''
			
		set the number of slices in the mesh.

		Args:
			nslices (int): number of slices.

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def slices(self) -> int:
		'''
			
		get the number of slices in the mesh.

		Returns:
			int: number of slices.
		
		'''
		pass # cpp source

	def rings(self, nrings: int) -> cylinder:
		'''
			
		set the number of rings in the mesh.

		Args:
			nrings (int): number of rings.

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def rings(self) -> int:
		'''
			
		get the number of rings in the mesh.

		Returns:
			int: number of rings.
		
		'''
		pass # cpp source

	def caps(self, ncaps: int) -> cylinder:
		'''
			
		set the number of caps in the mesh.

		Args:
			ncaps (int): number of caps.

		Returns:
			cylinder: cylinder reference
		
		'''
		pass # cpp source

	def caps(self) -> int:
		'''
			
		get the number of caps in the mesh.

		Returns:
			int: number of caps.
		
		'''
		pass # cpp source

	def fillet_relative(self) -> float:
		'''
			
		calculates a fillet relative value (0..1).

		Returns:
			float: fillet relative value
		
		'''
		pass # cpp source



class cone(cylinder):
	'''
			
		The cone.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->cone:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a cone class or its descendant, and if so, returns the specified object, but of the cone type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, height: float, radiusBottom: float, fillet: float = 0.0):
		pass # CPP source

	def __init__(self, posTop: any, posBottom: any, radiusBottom: float, fillet: float = 0.0):
		pass # CPP source

	def radius(self, r: float) -> cone:
		'''
			
		set the value of radius.

		Args:
			r (float): radius

		Returns:
			cone: cone reference
		
		'''
		pass # cpp source

	def radius(self) -> float:
		'''
			
		get the value of radius.

		Returns:
			float: radius value
		
		'''
		pass # cpp source

	def diameter(self, d: float) -> cone:
		'''
			
		set the value of diameter.

		Args:
			d (float): diameter

		Returns:
			cone: cone reference
		
		'''
		pass # cpp source

	def diameter(self) -> float:
		'''
			
		get the value of diameter.

		Returns:
			float: diameter value
		
		'''
		pass # cpp source

	def fillet_relative(self) -> float:
		'''
			
		calculates a fillet relative value (0..1).

		Returns:
			float: fillet relative value
		
		'''
		pass # cpp source



class tube(cylinder):
	'''
			
		The tube.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->tube:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a tube class or its descendant, and if so, returns the specified object, but of the tube type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, height: float, radiusTop: float, radiusBottom: float):
		pass # CPP source

	def __init__(self, height: float, radiusTop: float, radiusBottom: float, fillet: float):
		pass # CPP source

	def __init__(self, height: float, radiusTop: float, radiusBottom: float, relativeHoleRadius: float, fillet: float):
		pass # CPP source

	def __init__(self, posTop: any, posBottom: any, radiusTop: float, radiusBottom: float, relativeHoleRadius: float):
		pass # CPP source

	def __init__(self, posTop: any, posBottom: any, radiusTop: float, radiusBottom: float, relativeHoleRadius: float, fillet: float):
		pass # CPP source

	def relativeHoleRadius(self, r: float) -> tube:
		'''
			
		set the relative value of the hole radius.

		Args:
			r (float): relative value

		Returns:
			tube: tube reference
		
		'''
		pass # cpp source

	def relativeHoleRadius(self) -> float:
		'''
			
		get the relative value of the hole radius.

		Returns:
			float: relative value (0..1)
		
		'''
		pass # cpp source

	def thickness(self, w: float) -> tube:
		'''
			
		set the wall thickness value.

		Args:
			w (float): thickness value

		Returns:
			tube: tube reference
		
		'''
		pass # cpp source

	def thickness(self) -> float:
		'''
			
		get the relative value of the hole radius.

		Returns:
			float: relative value (0..1)
		
		'''
		pass # cpp source

	def fillet_relative(self) -> float:
		'''
			
		calculates a fillet relative value (0..1).

		Returns:
			float: fillet relative value
		
		'''
		pass # cpp source



class gear(tube):
	'''
			
		The gear.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->gear:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a gear class or its descendant, and if so, returns the specified object, but of the gear type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, height: float, radiusTop: float, radiusBottom: float):
		pass # CPP source

	def __init__(self, height: float, radiusTop: float, radiusBottom: float, depth: float, sharpness: float = 0.5, order: int = 16):
		pass # CPP source

	def __init__(self, posTop: any, posBottom: any, radiusTop: float, radiusBottom: float, depth: float = 0.1, sharpness: float = 0.5, order: int = 16):
		pass # CPP source

	def depth(self, _0: float) -> gear:
		'''
			
		set the depth value.

		Args:
			__depth (float): depth value

		Returns:
			gear: gear reference
		
		'''
		pass # cpp source

	def depth(self) -> float:
		'''
			
		get the depth value.

		Returns:
			float: depth value
		
		'''
		pass # cpp source

	def sharpness(self, sharp: float) -> gear:
		'''
			
		set the sharpness value.

		Args:
			sharp (float): sharpness value

		Returns:
			gear: gear reference
		
		'''
		pass # cpp source

	def sharpness(self) -> float:
		'''
			
		get the depth value.

		Returns:
			float: depth value
		
		'''
		pass # cpp source

	def order(self, nteeth: int) -> gear:
		'''
			
		set the number of teeth in gear.

		Args:
			nteeth (int): number of teeth

		Returns:
			gear: gear reference
		
		'''
		pass # cpp source

	def order(self) -> int:
		'''
			
		get the number of teeth in gear.

		Returns:
			int: the number of teeth
		
		'''
		pass # cpp source



class ngon(gear):
	'''
			
		The ngon.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->ngon:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a ngon class or its descendant, and if so, returns the specified object, but of the ngon type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, height: float, radiusTop: float, radiusBottom: float, order: int):
		pass # CPP source

	def __init__(self, height: float, radiusTop: float, radiusBottom: float, fillet: float, order: int):
		pass # CPP source

	def __init__(self, posTop: any, posBottom: any, radiusTop: float, radiusBottom: float, order: int):
		pass # CPP source

	def fillet_relative(self) -> float:
		'''
			
		calculates a fillet relative value (0..1).

		Returns:
			float: fillet relative value
		
		'''
		pass # cpp source



class capsule(cylinder):
	'''
			
		The capsule.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->capsule:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a capsule class or its descendant, and if so, returns the specified object, but of the capsule type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, height: float, radiusTop: float, radiusBottom: float):
		pass # CPP source

	def __init__(self, posTop: any, posBottom: any, radiusTop: float, radiusBottom: float):
		pass # CPP source



class spiral(prim):
	'''
			
		The spiral.
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->spiral:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a spiral class or its descendant, and if so, returns the specified object, but of the spiral type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, out_radius: float, in_radius: float, _2: float, nturns: float):
		pass # CPP source

	def radius(self, r: float) -> spiral:
		'''
			
		set the outer radius of the spiral.

		Args:
			r (float): radius value

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def radius(self) -> float:
		'''
			
		get the outer radius.

		Returns:
			float: outer radius
		
		'''
		pass # cpp source

	def profile_radius(self, r: float) -> spiral:
		'''
			
		set the profile radius.

		Args:
			r (float): radius value

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def profile_radius(self) -> float:
		'''
			
		get the profile radius.

		Returns:
			float: profile radius
		
		'''
		pass # cpp source

	def diameter(self, d: float) -> spiral:
		'''
			
		set the outer diameter of the spiral.

		Args:
			d (float): diameter value

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def diameter(self) -> float:
		'''
			
		get the outer diameter.

		Returns:
			float: outer diameter
		
		'''
		pass # cpp source

	def profile_diameter(self, d: float) -> spiral:
		'''
			
		set the profile diameter.

		Args:
			d (float): diameter value

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def profile_diameter(self) -> float:
		'''
			
		get the profile diameter.

		Returns:
			float: profile diameter
		
		'''
		pass # cpp source

	def turns(self, nturns: int) -> spiral:
		'''
			
		set the number of turns.

		Args:
			nturns (int): turns count

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def turns(self) -> int:
		'''
			
		get the number of turns.

		Returns:
			int: turns count
		
		'''
		pass # cpp source

	def step(self, vstep: float) -> spiral:
		'''
			
		set the spiral step.

		Args:
			vstep (float): step value

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def step(self) -> float:
		'''
			
		get the spiral step.

		Returns:
			float: step value
		
		'''
		pass # cpp source

	def profile_type(self, type: SpiralProfile) -> spiral:
		'''
			
		set the type of profile (circle or rectangle).

		Args:
			type (SpiralProfile): profile type

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def profile_rect(self, width: float, height: float) -> spiral:
		'''
			
		set the dimensions for the rectangle profile.

		Args:
			width (float): the width value
			height (float): the height value

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def clock_wise(self, clockWise: bool) -> spiral:
		'''
			
		set the clockwise direction of the spiral.

		Args:
			clockWise (bool): the indicator of the clockwise direction

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def clock_wise(self) -> bool:
		'''
			
		get the clokwise direction of the spiral.

		Returns:
			bool: the clokwise direction( true or false)
		
		'''
		pass # cpp source

	def profile_height(self) -> float:
		'''
			
		get the profile height for rectangle profile.

		Returns:
			float: the profile height
		
		'''
		pass # cpp source

	def profile_width(self) -> float:
		'''
			
		get the profile width for rectangle profile.

		Returns:
			float: the profile width
		
		'''
		pass # cpp source

	def slices(self, nslices: int) -> spiral:
		'''
			
		set the number of slices in the mesh.

		Args:
			nslices (int): number of slices.

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def slices(self) -> int:
		'''
			
		get the number of slices in the mesh.

		Returns:
			int: number of slices
		
		'''
		pass # cpp source

	def rings(self, nrings: int) -> spiral:
		'''
			
		set the number of rings in the mesh.

		Args:
			nrings (int): number of rings.

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def rings(self) -> int:
		'''
			
		get the number of rings in the mesh.

		Returns:
			int: number of rings
		
		'''
		pass # cpp source

	def caps(self, ncaps: int) -> spiral:
		'''
			
		set the number of caps in the mesh.

		Args:
			ncaps (int): number of caps.

		Returns:
			spiral: spiral reference
		
		'''
		pass # cpp source

	def caps(self) -> int:
		'''
			
		get the number of caps in the mesh.

		Returns:
			int: number of caps
		
		'''
		pass # cpp source



class FontInfo():
	'''
			
		Holds the general information about font
		
	'''

	size: int #: int (T)  
	weight: int #: int (T)  
	style: int #: int (T)  
	fname: str #: std :: string (T)  


class Font():
	def __init__(self):
		pass # CPP source

	def __init__(self, _0: FontInfo):
		pass # CPP source

	def __init__(self, _0: str):
		pass # CPP source

	def __init__(self, _0: str, _1: int):
		pass # CPP source

	def size(self, _0: int) -> Font:
		'''
			
		set the font size

		Args:
			_size (int): font size property

		Returns:
			Font: font reference
		
		'''
		pass # cpp source

	def size(self) -> int:
		'''
			
		get the font size

		Returns:
			int: font size
		
		'''
		pass # cpp source

	def weight(self, weight: int) -> Font:
		'''
			
		set the font weight

		Args:
			weight (int): font weight property

		Returns:
			Font: font reference
		
		'''
		pass # cpp source

	def weight(self) -> int:
		'''
			
		get the font weight

		Returns:
			int: font weight
		
		'''
		pass # cpp source

	def style(self, st: int) -> Font:
		'''
			
		set the style of the font

		Args:
			st (int): the new font style

		Returns:
			Font: font reference
		
		'''
		pass # cpp source

	def style(self) -> int:
		'''
			
		get the font style

		Returns:
			int: the font style
		
		'''
		pass # cpp source

	def name(self, _0: str) -> Font:
		'''
			
		set the font name

		Args:
			_fname (str): the font name

		Returns:
			Font: font reference
		
		'''
		pass # cpp source

	def name(self) -> str:
		'''
			
		get the font name

		Returns:
			str: the font name
		
		'''
		pass # cpp source

	def select(self):
		'''
			
		selects a font object into the viewport
		
		'''
		pass # cpp source



class text(prim):
	'''
			
		text primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->text:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a text class or its descendant, and if so, returns the specified object, but of the text type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, s: str):
		pass # CPP source

	def string(self, s: str) -> text:
		'''
			
		set the text's string.

		Args:
			s (str): the string
		
		'''
		pass # cpp source

	def string(self) -> any:
		'''
			
		get the text's string.

		Returns:
			any: the string
		
		'''
		pass # cpp source

	def font(self, f: Font) -> text:
		'''
			
		set the text font

		Args:
			f (Font): font object

		Returns:
			text: the text reference
		
		'''
		pass # cpp source

	def font(self) -> Font:
		'''
			
		get the font object

		Returns:
			Font: font object
		
		'''
		pass # cpp source

	def width(self, w: float) -> text:
		'''
			
		set the text width in the pixels

		Args:
			w (float): width

		Returns:
			text: the text reference
		
		'''
		pass # cpp source

	def width(self) -> float:
		'''
			
		get the text width

		Returns:
			float: the width value
		
		'''
		pass # cpp source

	def depth(self, d: float) -> text:
		'''
			
		set the text depth in the pixels

		Args:
			d (float): depth

		Returns:
			text: the text reference
		
		'''
		pass # cpp source

	def depth(self) -> float:
		'''
			
		get the text depth

		Returns:
			float: the depth value
		
		'''
		pass # cpp source

	def bendRadius(self, radius: float) -> text:
		'''
			
		set the bend radius.

		Args:
			radius (float): bend radius of the text

		Returns:
			text: the text reference
		
		'''
		pass # cpp source

	def bendRadius(self) -> float:
		'''
			
		get the bend radius.

		Returns:
			float: the bend radius of the text
		
		'''
		pass # cpp source

	def extraRotation(self, rotation: float) -> text:
		'''
			
		set the rotate angle around the x-axis.

		Returns:
			text: the text reference
		
		'''
		pass # cpp source

	def extraRotation(self) -> float:
		'''
			
		get the rotate angle around the x-axis.

		Returns:
			float: the rotate angle
		
		'''
		pass # cpp source

	def invertBending(self, _0: bool) -> text:
		'''
			
		set the invert of the text bending.

		Returns:
			text: the text reference
		
		'''
		pass # cpp source

	def invertBending(self) -> float:
		'''
			
		get the invert of the text bending.

		Returns:
			float: the invert bending
		
		'''
		pass # cpp source



class lathe(box):
	'''
			
		lathe primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->lathe:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a lathe class or its descendant, and if so, returns the specified object, but of the lathe type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def type(self, t: any) -> lathe:
		'''
			
		set the lathe type

		Args:
			t : type value (cylinder or rectangle)

		Returns:
			lathe: the lathe reference
		
		'''
		pass # cpp source

	def type(self) -> any:
		'''
			
		get the lathe type.

		Returns:
			any: the type value
		
		'''
		pass # cpp source

	def add_point(self, point: any, st: int) -> lathe:
		'''
			
		add the point into curve

		Args:
			point : the 2d point
			st (int): the point state

		Returns:
			lathe: lathe reference
		
		'''
		pass # cpp source

	def profile(self) -> any:
		'''
			
		get the pointer to the profile

		Returns:
			any: the profile pointer
		
		'''
		pass # cpp source

	def reset(self) -> lathe:
		'''
			
		reset the curve points
		
		'''
		pass # cpp source

	def clear(self) -> lathe:
		'''
			
		clear points of the profile
		
		'''
		pass # cpp source



class image(text):
	'''
			
		image primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->image:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a image class or its descendant, and if so, returns the specified object, but of the image type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def topTexture(self, _0: str) -> image:
		'''
			
		set the top texture

		Args:
			_texture (str): image file name

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def topTexture(self) -> any:
		'''
			
		get the top texture

		Returns:
			any: the string of the image file name
		
		'''
		pass # cpp source

	def topBumpTexture(self, _0: str) -> image:
		'''
			
		set the top bump texture

		Args:
			_texture (str): image file name

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def topBumpTexture(self) -> any:
		'''
			
		get the top bump texture

		Returns:
			any: the string of the image file name
		
		'''
		pass # cpp source

	def bottomTexture(self, _0: str) -> image:
		'''
			
		set the bottom texture

		Args:
			_texture (str): image file name

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def bottomTexture(self) -> any:
		'''
			
		get the bottom texture

		Returns:
			any: the string of the image file name
		
		'''
		pass # cpp source

	def bottomBumpTexture(self, _0: str) -> image:
		'''
			
		set the bottom bump texture

		Args:
			_texture (str): image file name

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def bottomBumpTexture(self) -> any:
		'''
			
		get the bottom bump texture

		Returns:
			any: the string of the image file name
		
		'''
		pass # cpp source

	def strencilTexture(self, _0: str) -> image:
		'''
			
		set the strencil texture

		Args:
			_texture (str): image file name

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def strencilTexture(self) -> any:
		'''
			
		get the strencil texture

		Returns:
			any: the string of the image file name
		
		'''
		pass # cpp source

	def bottomStrencilTexture(self, _0: str) -> image:
		'''
			
		set the bottom strencil texture

		Args:
			_texture (str): image file name

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def bottomStrencilTexture(self) -> any:
		'''
			
		get the bottom strencil texture

		Returns:
			any: the string of the image file name
		
		'''
		pass # cpp source

	def basicThickness(self, _0: float) -> image:
		'''
			
		set the basic thickness of image

		Args:
			_thickness (float): thickness value

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def basicThickness(self) -> float:
		'''
			
		get the basic thickness of image

		Returns:
			float: the thickness value
		
		'''
		pass # cpp source

	def bumpThickness(self, _0: float) -> image:
		'''
			
		set the bump thickness of image

		Args:
			_thickness (float): thickness value

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def bumpThickness(self) -> float:
		'''
			
		get the bump thickness of image

		Returns:
			float: the thickness value
		
		'''
		pass # cpp source

	def taperAngle(self, _0: float) -> image:
		'''
			
		set the angle of tapering

		Args:
			_angle (float): taper angle value

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def taperAngle(self) -> float:
		'''
			
		get the angle of tapering of image

		Returns:
			float: the taper angle value
		
		'''
		pass # cpp source

	def topBottomWeight(self, weight: float) -> image:
		'''
			
		set the weight of the top and bottom image

		Args:
			weight (float): weight value

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def topBottomWeight(self) -> float:
		'''
			
		get the weight of the top and bottom image

		Returns:
			float: the weight value
		
		'''
		pass # cpp source

	def sizeInScene(self, _0: float) -> image:
		'''
			
		set the size of image in the scene

		Args:
			_size (float): size value

		Returns:
			image: the image reference
		
		'''
		pass # cpp source

	def sizeInScene(self) -> float:
		'''
			
		get the size of image in the scene

		Returns:
			float: the size value
		
		'''
		pass # cpp source



class thread(prim):
	'''
			
		thread primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->thread:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a thread class or its descendant, and if so, returns the specified object, but of the thread type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def diameter(self, d: float) -> thread:
		'''
			
		set the diameter of the thread.

		Args:
			d (float): diameter value

		Returns:
			thread: thread reference
		
		'''
		pass # cpp source

	def diameter(self) -> float:
		'''
			
		get the diameter of the thread.

		Returns:
			float: thread diameter
		
		'''
		pass # cpp source

	def pitch(self, p: float) -> thread:
		'''
			
		set the pitch of the thread.

		Args:
			p (float): pitch value

		Returns:
			thread: thread reference
		
		'''
		pass # cpp source

	def pitch(self) -> float:
		'''
			
		set the pitch of the thread.

		Returns:
			float: pitch value
		
		'''
		pass # cpp source

	def stub(self, l: float) -> thread:
		'''
			
		set the stub length of the thread.

		Args:
			l (float): stub length value

		Returns:
			thread: thread reference
		
		'''
		pass # cpp source

	def stub(self) -> float:
		'''
			
		get the stub length of the thread.

		Returns:
			float: stub length value
		
		'''
		pass # cpp source

	def height(self, h: float) -> thread:
		'''
			
		set the height of the thread.

		Args:
			h (float): height value

		Returns:
			thread: thread reference
		
		'''
		pass # cpp source

	def height(self) -> float:
		'''
			
		get the height of the thread.

		Returns:
			float: height value
		
		'''
		pass # cpp source

	def turns(self, n: int) -> thread:
		'''
			
		set the number of the thread turns.

		Args:
			n (int): turns count

		Returns:
			thread: thread reference
		
		'''
		pass # cpp source

	def turns(self) -> int:
		'''
			
		get the number of the thread turns.

		Returns:
			int: turns count
		
		'''
		pass # cpp source

	def clockwise(self, cw: bool) -> thread:
		'''
			
		set the clockwise flag of the thread.

		Args:
			cw (bool): if value is true then thread direction is clockwise

		Returns:
			thread: thread reference
		
		'''
		pass # cpp source

	def clockwise(self) -> bool:
		'''
			
		get the clockwise of the thread.

		Returns:
			bool: clockwise flag
		
		'''
		pass # cpp source

	def close(self, b: bool) -> thread:
		'''
			
		set the closed thread.

		Args:
			b (bool): closed value

		Returns:
			thread: thread reference
		
		'''
		pass # cpp source

	def close(self) -> bool:
		'''
			
		set the closed thread.

		Returns:
			bool: closed flag
		
		'''
		pass # cpp source

	def profile(self, prf: ThreadProfile) -> thread:
		'''
			
		set the thread profile type.

		Args:
			prf (ThreadProfile): profile type

		Returns:
			thread: thread reference
		
		'''
		pass # cpp source

	def profile(self) -> ThreadProfile:
		'''
			
		get the thread profile type.

		Returns:
			ThreadProfile: profile type
		
		'''
		pass # cpp source



class threadStud(thread):
	'''
			
		thread stud primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->threadStud:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a threadStud class or its descendant, and if so, returns the specified object, but of the threadStud type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def diameter(self, d: float) -> threadStud:
		'''
			
		set the diameter of the thread.

		Args:
			d (float): diameter value

		Returns:
			threadStud: thread stud reference
		
		'''
		pass # cpp source

	def diameter(self) -> float:
		'''
			
		get the diameter of the thread.

		Returns:
			float: diameter value
		
		'''
		pass # cpp source

	def diameterTop(self, d: float) -> threadStud:
		'''
			
		get the top diameter of the thread.

		Args:
			d (float): diameter value

		Returns:
			threadStud: thread stud reference
		
		'''
		pass # cpp source

	def diameterTop(self) -> float:
		'''
			
		get the top diameter of the thread.

		Returns:
			float: diameter value
		
		'''
		pass # cpp source

	def diameterBottom(self, d: float) -> threadStud:
		'''
			
		set the bottom diameter of the thread.

		Args:
			d (float): diameter value

		Returns:
			threadStud: thread stud reference
		
		'''
		pass # cpp source

	def diameterBottom(self) -> float:
		'''
			
		get the bottom diameter of the thread.

		Returns:
			float: diameter value
		
		'''
		pass # cpp source

	def length(self, l: float) -> threadStud:
		'''
			
		set the stud length.

		Args:
			l (float): length value

		Returns:
			threadStud: thread stud reference
		
		'''
		pass # cpp source

	def length(self) -> float:
		'''
			
		get the length of the stud.

		Returns:
			float: length value
		
		'''
		pass # cpp source

	def threadLength(self) -> float:
		'''
			
		get the length of the thread.

		Returns:
			float: length value
		
		'''
		pass # cpp source

	def enableThread(self, enable: bool) -> threadStud:
		'''
			
		enabled or disabled thread in the stud.

		Returns:
			threadStud: thread stud reference
		
		'''
		pass # cpp source

	def enableThread(self) -> bool:
		'''
			
		get the indicator of the enabled thread.

		Returns:
			bool: enabled/disabled value
		
		'''
		pass # cpp source

	def bodyType(self, bt: ThreadStudBodyType) -> threadStud:
		'''
			
		set the body type.

		Args:
			bt (ThreadStudBodyType): body type

		Returns:
			threadStud: thread stud reference
		
		'''
		pass # cpp source

	def bodyType(self) -> ThreadStudBodyType:
		'''
			
		get the body type.

		Returns:
			ThreadStudBodyType: type value
		
		'''
		pass # cpp source



class Slit():
	'''
			
		class of the slits
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, w: float, h: float, d: float, t: SlitType):
		pass # CPP source

	def type(self, _0: int) -> Slit:
		'''
			
		set the slit type.

		Args:
			_t (int): type value

		Returns:
			Slit: slit reference
		
		'''
		pass # cpp source

	def type(self) -> int:
		'''
			
		get the slit type.

		Returns:
			int: type value
		
		'''
		pass # cpp source

	def width(self, _0: float) -> Slit:
		'''
			
		set the width.

		Args:
			_w (float): width value

		Returns:
			Slit: slit reference
		
		'''
		pass # cpp source

	def width(self) -> float:
		'''
			
		get the width.

		Returns:
			float: width value
		
		'''
		pass # cpp source

	def height(self, _0: float) -> Slit:
		'''
			
		set the height.

		Args:
			_h (float): height value

		Returns:
			Slit: slit reference
		
		'''
		pass # cpp source

	def height(self) -> float:
		'''
			
		get the height.

		Returns:
			float: height value
		
		'''
		pass # cpp source

	def depth(self, _0: float) -> Slit:
		'''
			
		set the depth.

		Args:
			_d (float): depth value

		Returns:
			Slit: slit reference
		
		'''
		pass # cpp source

	def depth(self) -> float:
		'''
			
		get the depth.

		Returns:
			float: depth value
		
		'''
		pass # cpp source



class HeadParams():
	'''
			
		class HeadParams
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, _0: int, _1: any):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def setData(self, _0: int, param: any) -> HeadParams:
		'''
			
		set the parameters data with specified type.

		Args:
			_type (int): head type
		
		'''
		pass # cpp source

	def getData(self) -> any:
		'''
			
		get the head data

		Returns:
			any: pointer to the head data
		
		'''
		pass # cpp source

	def __assign__(self, h: HeadParams) -> HeadParams:
		return super().__assign__(h)

	def copy(self, h: HeadParams):
		'''
			
		copies the HeadParams object
		
		'''
		pass # cpp source

	def release(self):
		'''
			
		release the data
		
		'''
		pass # cpp source



class HeadBaseParams():
	'''
			
		HeadBaseParams struct of the head data
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, _0: float, _1: float):
		pass # CPP source

	def diameter(self, _0: float) -> HeadBaseParams:
		'''
			
		set the diameter.

		Args:
			_d (float): diameter

		Returns:
			HeadBaseParams: HeadBaseParams reference
		
		'''
		pass # cpp source

	def height(self, _0: float) -> HeadBaseParams:
		'''
			
		set the height.

		Args:
			_h (float): height

		Returns:
			HeadBaseParams: HeadBaseParams reference
		
		'''
		pass # cpp source

	_diameter: float #: float (T)  
	_height: float #: float (T)  


class TShapedParams():
	'''
			
		struct of the TShapedParams data
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, _0: float, _1: float, _2: float):
		pass # CPP source

	def diameter(self, _0: float) -> TShapedParams:
		'''
			
		set the diameter.

		Args:
			_d (float): diameter

		Returns:
			TShapedParams: TShapedParams reference
		
		'''
		pass # cpp source

	def height(self, _0: float) -> TShapedParams:
		'''
			
		set the height.

		Args:
			_h (float): height

		Returns:
			TShapedParams: TShapedParams reference
		
		'''
		pass # cpp source

	def width(self, _0: float) -> TShapedParams:
		'''
			
		set the width.

		Args:
			_w (float): width

		Returns:
			TShapedParams: TShapedParams reference
		
		'''
		pass # cpp source

	_diameter: float #: float (T)  
	_height: float #: float (T)  
	_width: float #: float (T)  


class LambParams():
	'''
			
		struct of the LambParams data
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, _0: float, _1: float, _2: float, _3: float, _4: float, _5: float):
		pass # CPP source

	def length(self, _0: float) -> LambParams:
		'''
			
		set the length.

		Args:
			_l (float): length

		Returns:
			LambParams: LambParams reference
		
		'''
		pass # cpp source

	def diameterTop(self, _0: float) -> LambParams:
		'''
			
		set the top diameter.

		Args:
			_d (float): top diameter

		Returns:
			LambParams: LambParams reference
		
		'''
		pass # cpp source

	def diameterBottom(self, _0: float) -> LambParams:
		'''
			
		set the bottom diameter.

		Args:
			_d (float): bottom diameter

		Returns:
			LambParams: LambParams reference
		
		'''
		pass # cpp source

	def height(self, _0: float) -> LambParams:
		'''
			
		set the height.

		Args:
			_h (float): height

		Returns:
			LambParams: LambParams reference
		
		'''
		pass # cpp source

	def headHeight(self, _0: float) -> LambParams:
		'''
			
		set the head height.

		Args:
			_h (float): height

		Returns:
			LambParams: LambParams reference
		
		'''
		pass # cpp source

	def thickness(self, _0: float) -> LambParams:
		'''
			
		set the thickness.

		Args:
			_t (float): thickness

		Returns:
			LambParams: LambParams reference
		
		'''
		pass # cpp source

	_length: float #: float (T)  
	_diameterTop: float #: float (T)  
	_diameterBottom: float #: float (T)  
	_headHeight: float #: float (T)  
	_height: float #: float (T)  
	_thickness: float #: float (T)  


class RimParams():
	'''
			
		struct of the RimParams data
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, _0: float, _1: float, _2: float, _3: float):
		pass # CPP source

	def shoulderDiameter(self, _0: float) -> RimParams:
		'''
			
		set the shoulder diameter.

		Args:
			_d (float): diameter

		Returns:
			RimParams: RimParams reference
		
		'''
		pass # cpp source

	def shoulderHeight(self, _0: float) -> RimParams:
		'''
			
		set the shoulder height.

		Args:
			_h (float): height

		Returns:
			RimParams: RimParams reference
		
		'''
		pass # cpp source

	def inRingDiameter(self, _0: float) -> RimParams:
		'''
			
		set the inner ring diameter.

		Args:
			_d (float): diameter

		Returns:
			RimParams: RimParams reference
		
		'''
		pass # cpp source

	def outRingDiameter(self, _0: float) -> RimParams:
		'''
			
		set the outer ring diameter.

		Args:
			_d (float): diameter

		Returns:
			RimParams: RimParams reference
		
		'''
		pass # cpp source

	_shoulderDiameter: float #: float (T)  
	_shoulderHeight: float #: float (T)  
	_inRingDiameter: float #: float (T)  
	_outRingDiameter: float #: float (T)  


class EyeParams():
	'''
			
		struct of the EyeParams data
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, _0: float, _1: float, _2: float):
		pass # CPP source

	def inRingDiameter(self, _0: float) -> EyeParams:
		'''
			
		set the inner ring diameter.

		Args:
			_d (float): diameter

		Returns:
			EyeParams: EyeParams reference
		
		'''
		pass # cpp source

	def outRingDiameter(self, _0: float) -> EyeParams:
		'''
			
		set the outer ring diameter.

		Args:
			_d (float): diameter

		Returns:
			EyeParams: EyeParams reference
		
		'''
		pass # cpp source

	def thickness(self, _0: float) -> EyeParams:
		'''
			
		set the thickness.

		Args:
			_t (float): thickness

		Returns:
			EyeParams: EyeParams reference
		
		'''
		pass # cpp source

	_thickness: float #: float (T)  
	_inRingDiameter: float #: float (T)  
	_outRingDiameter: float #: float (T)  


class boltHead(prim):
	'''
			
		bolt head primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->boltHead:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a boltHead class or its descendant, and if so, returns the specified object, but of the boltHead type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def head(self, _0: HeadParams) -> boltHead:
		'''
			
		set the head object.

		Args:
			_h (HeadParams): head obj reference

		Returns:
			boltHead: bolt head reference
		
		'''
		pass # cpp source

	def head(self) -> HeadParams:
		'''
			
		get the HeadParams object.

		Returns:
			HeadParams: HeadParams object reference
		
		'''
		pass # cpp source

	def head(self) -> HeadParams:
		'''
			
		get the const HeadParams object.

		Returns:
			HeadParams: HeadParams object reference
		
		'''
		pass # cpp source

	def head(self, _0: int, data: any) -> boltHead:
		'''
			
		set the head object with specified type and data.

		Args:
			_type (int): head type

		Returns:
			boltHead: bolt head reference
		
		'''
		pass # cpp source

	def slit(self, _0: Slit) -> boltHead:
		'''
			
		set the slit object.

		Args:
			_s (Slit): slit reference.

		Returns:
			boltHead: bolt head reference
		
		'''
		pass # cpp source

	def slit(self) -> Slit:
		'''
			
		get the slit object.

		Returns:
			Slit: slit object reference
		
		'''
		pass # cpp source

	def slit(self) -> Slit:
		'''
			
		get the const slit object.

		Returns:
			Slit: slit object reference
		
		'''
		pass # cpp source

	def __assign__(self, h: boltHead) -> boltHead:
		return super().__assign__(h)



class NutHeadBaseParams():
	def __init__(self):
		pass # CPP source

	def __init__(self, t: NutType, d: float, h: float):
		pass # CPP source

	def diameter(self, d: float) -> NutHeadBaseParams:
		'''
			
		set the diameter.

		Args:
			d (float): diameter

		Returns:
			NutHeadBaseParams: NutRadialParams reference
		
		'''
		pass # cpp source

	def diameter(self) -> float:
		'''
			
		get the diameter.

		Returns:
			float: diameter
		
		'''
		pass # cpp source

	def height(self, h: float) -> NutHeadBaseParams:
		'''
			
		set the height.

		Args:
			h (float): height value.

		Returns:
			NutHeadBaseParams: NutHeadBaseParams reference
		
		'''
		pass # cpp source

	def height(self) -> float:
		'''
			
		get the height.

		Returns:
			float: height value
		
		'''
		pass # cpp source

	def type(self, t: int) -> NutHeadBaseParams:
		'''
			
		set the nut type.

		Args:
			t (int): type value.

		Returns:
			NutHeadBaseParams: NutHeadBaseParams reference
		
		'''
		pass # cpp source

	def type(self) -> int:
		'''
			
		set the nut type.

		Returns:
			int: type value.
		
		'''
		pass # cpp source

	def copy(self, p: NutHeadBaseParams = None) -> NutHeadBaseParams:
		'''
			
		copies the object.

		Args:
			p (NutHeadBaseParams): pointer to the object to copy. If the pointer equals to null then the object is duplicated

		Returns:
			NutHeadBaseParams: the pointer to a copy of an object.
		
		'''
		pass # cpp source



class NutHexaParams(NutHeadBaseParams):
	'''
			
		 NutHexaParams
		
	'''


	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutHexaParams:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutHexaParams class or its descendant, and if so, returns the specified object, but of the NutHexaParams type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float):
		pass # CPP source



class NutAcornParams(NutHeadBaseParams):

	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutAcornParams:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutAcornParams class or its descendant, and if so, returns the specified object, but of the NutAcornParams type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float, h1: float):
		pass # CPP source

	def facetHeight(self, _0: float) -> NutAcornParams:
		'''
			
		set the facet height.

		Args:
			_h (float): height value.

		Returns:
			NutAcornParams: NutAcornParams reference
		
		'''
		pass # cpp source

	def facetHeight(self) -> float:
		'''
			
		get the facet height.

		Returns:
			float: facet height value.
		
		'''
		pass # cpp source

	def copy(self, p: NutHeadBaseParams = None) -> NutHeadBaseParams:
		'''
			
		copies the NutAcornParams object.

		Args:
			p (NutHeadBaseParams): pointer to the NutAcornParams object to copy. If the pointer equals to null then the object is duplicated

		Returns:
			NutHeadBaseParams: the pointer to a copy of an NutAcornParams object.
		
		'''
		pass # cpp source



class NutLowAcornParams(NutAcornParams):

	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutLowAcornParams:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutLowAcornParams class or its descendant, and if so, returns the specified object, but of the NutLowAcornParams type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float, h1: float):
		pass # CPP source



class NutSelfLockParams(NutAcornParams):

	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutSelfLockParams:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutSelfLockParams class or its descendant, and if so, returns the specified object, but of the NutSelfLockParams type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float, h1: float):
		pass # CPP source



class NutTShapedParams(NutAcornParams):

	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutTShapedParams:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutTShapedParams class or its descendant, and if so, returns the specified object, but of the NutTShapedParams type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float, h1: float):
		pass # CPP source



class NutFlangeParams(NutHeadBaseParams):

	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutFlangeParams:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutFlangeParams class or its descendant, and if so, returns the specified object, but of the NutFlangeParams type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float):
		pass # CPP source

	def __init__(self, d: float, h: float, fw: float, fh: float):
		pass # CPP source

	def facetWidth(self, w: float) -> NutFlangeParams:
		'''
			
		set the width.

		Args:
			w (float): width value.

		Returns:
			NutFlangeParams: NutFlangeParams reference
		
		'''
		pass # cpp source

	def facetHeight(self, h: float) -> NutFlangeParams:
		'''
			
		set the facet height.

		Args:
			h (float): height value.

		Returns:
			NutFlangeParams: NutFlangeParams reference
		
		'''
		pass # cpp source

	def facetWidth(self) -> float:
		'''
			
		get the width.

		Returns:
			float: width value.
		
		'''
		pass # cpp source

	def facetHeight(self) -> float:
		'''
			
		get the height.

		Returns:
			float: height value.
		
		'''
		pass # cpp source

	def copy(self, p: NutHeadBaseParams = None) -> NutHeadBaseParams:
		'''
			
		copies the NutFlangeParams object.

		Args:
			p (NutHeadBaseParams): pointer to the NutFlangeParams object to copy. If the pointer equals to null then the object is duplicated

		Returns:
			NutHeadBaseParams: the pointer to a copy of an NutFlangeParams object.
		
		'''
		pass # cpp source



class NutRadialParams(NutHeadBaseParams):

	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutRadialParams:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutRadialParams class or its descendant, and if so, returns the specified object, but of the NutRadialParams type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float):
		pass # CPP source

	def __init__(self, d: float, h: float, d1: float, d2: float):
		pass # CPP source

	def holeDiameter(self, d: float) -> NutRadialParams:
		'''
			
		set the hole diameter.

		Args:
			d (float): diameter

		Returns:
			NutRadialParams: NutRadialParams reference
		
		'''
		pass # cpp source

	def holeDepth(self, d: float) -> NutRadialParams:
		'''
			
		set the hole depth.

		Args:
			d (float): depth

		Returns:
			NutRadialParams: NutRadialParams reference
		
		'''
		pass # cpp source

	def holeDiameter(self) -> float:
		'''
			
		set the hole diameter.

		Returns:
			float: hole diameter
		
		'''
		pass # cpp source

	def holeDepth(self) -> float:
		'''
			
		get the hole depth.

		Returns:
			float: NutRadialParams hole depth
		
		'''
		pass # cpp source

	def holePlace(self, place: int) -> NutRadialParams:
		'''
			
		set the hole place (0 - face, 1 - side).

		Args:
			place (int): place flag

		Returns:
			NutRadialParams: NutRadialParams reference
		
		'''
		pass # cpp source

	def holePlace(self) -> int:
		'''
			
		get the hole place.

		Returns:
			int: place flag 0 - face, 1 - side
		
		'''
		pass # cpp source

	def copy(self, p: NutHeadBaseParams = None) -> NutHeadBaseParams:
		'''
			
		copies the radial object.

		Args:
			p (NutHeadBaseParams): pointer to the radial object to copy. If the pointer equals to null then the object is duplicated

		Returns:
			NutHeadBaseParams: the pointer to a copy of an radial object.
		
		'''
		pass # cpp source



class NutLambParams(NutHeadBaseParams):

	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutLambParams:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutLambParams class or its descendant, and if so, returns the specified object, but of the NutLambParams type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float):
		pass # CPP source

	def length(self, _0: float) -> NutLambParams:
		'''
			
		set the length.

		Args:
			_l (float): length

		Returns:
			NutLambParams: NutLambParams reference
		
		'''
		pass # cpp source

	def diameterBottom(self, _0: float) -> NutLambParams:
		'''
			
		set the bottom diameter.

		Args:
			_d (float): bottom diameter

		Returns:
			NutLambParams: NutLambParams reference
		
		'''
		pass # cpp source

	def diameterTop(self, _0: float) -> NutLambParams:
		'''
			
		set the top diameter.

		Args:
			_d (float): top diameter

		Returns:
			NutLambParams: NutLambParams reference
		
		'''
		pass # cpp source

	def headHeight(self, _0: float) -> NutLambParams:
		'''
			
		set the head height.

		Args:
			_h (float): height

		Returns:
			NutLambParams: NutLambParams reference
		
		'''
		pass # cpp source

	def thickness(self, _0: float) -> NutLambParams:
		'''
			
		set the thickness.

		Args:
			_t (float): thickness

		Returns:
			NutLambParams: NutLambParams reference
		
		'''
		pass # cpp source

	def length(self) -> float:
		'''
			
		get the length.

		Returns:
			float: length value
		
		'''
		pass # cpp source

	def diameterBottom(self) -> float:
		'''
			
		get the bottom diameter.

		Returns:
			float: bottom diameter
		
		'''
		pass # cpp source

	def diameterTop(self) -> float:
		'''
			
		get the top diameter.

		Returns:
			float: top diameter
		
		'''
		pass # cpp source

	def headHeight(self) -> float:
		'''
			
		get the head height.

		Returns:
			float: height value
		
		'''
		pass # cpp source

	def thickness(self) -> float:
		'''
			
		get the thickness.

		Returns:
			float: thickness value
		
		'''
		pass # cpp source

	def copy(self, p: NutHeadBaseParams = None) -> NutHeadBaseParams:
		'''
			
		copies the NutLambParams object.

		Args:
			p (NutHeadBaseParams): pointer to the NutLambParams object to copy. If the pointer equals to null then the object is duplicated

		Returns:
			NutHeadBaseParams: the pointer to a copy of an NutLambParams object.
		
		'''
		pass # cpp source



class NutSlitsParams(NutHeadBaseParams):

	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutSlitsParams:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutSlitsParams class or its descendant, and if so, returns the specified object, but of the NutSlitsParams type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float):
		pass # CPP source

	def width(self, w: float) -> NutSlitsParams:
		'''
			
		set the width.

		Args:
			w (float): width value.

		Returns:
			NutSlitsParams: NutSlitsParams reference
		
		'''
		pass # cpp source

	def length(self, l: float) -> NutSlitsParams:
		'''
			
		set the length.

		Args:
			l (float): length value.

		Returns:
			NutSlitsParams: NutSlitsParams reference
		
		'''
		pass # cpp source

	def count(self, n: int) -> NutSlitsParams:
		'''
			
		set the count of NutSlitsParams.

		Args:
			n (int): count value.

		Returns:
			NutSlitsParams: NutSlitsParams reference
		
		'''
		pass # cpp source

	def width(self) -> float:
		'''
			
		get the width.

		Returns:
			float: width value.
		
		'''
		pass # cpp source

	def length(self) -> float:
		'''
			
		get the length.

		Returns:
			float: length value.
		
		'''
		pass # cpp source

	def count(self) -> int:
		'''
			
		get the count of NutSlitsParams.

		Returns:
			int: count value.
		
		'''
		pass # cpp source

	def copy(self, p: NutHeadBaseParams = None) -> NutHeadBaseParams:
		'''
			
		copies the NutSlitsParams object.

		Args:
			p (NutHeadBaseParams): pointer to the NutSlitsParams object to copy. If the pointer equals to null then the object is duplicated

		Returns:
			NutHeadBaseParams: the pointer to a copy of an NutSlitsParams object.
		
		'''
		pass # cpp source



class NutRimParams(NutHeadBaseParams):

	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutRimParams:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutRimParams class or its descendant, and if so, returns the specified object, but of the NutRimParams type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float):
		pass # CPP source

	def inRingDiameter(self, _0: float) -> NutRimParams:
		'''
			
		set the inner ring diameter.

		Args:
			_d (float): diameter

		Returns:
			NutRimParams: NutRimParams reference
		
		'''
		pass # cpp source

	def outRingDiameter(self, _0: float) -> NutRimParams:
		'''
			
		set the outer ring diameter.

		Args:
			_d (float): diameter

		Returns:
			NutRimParams: NutRimParams reference
		
		'''
		pass # cpp source

	def inRingDiameter(self) -> float:
		'''
			
		get the inner ring diameter.

		Returns:
			float: inner diameter
		
		'''
		pass # cpp source

	def outRingDiameter(self) -> float:
		'''
			
		get the outer ring diameter.

		Returns:
			float: outer diameter
		
		'''
		pass # cpp source

	def copy(self, p: NutHeadBaseParams = None) -> NutHeadBaseParams:
		'''
			
		copies the NutRimParams object.

		Args:
			p (NutHeadBaseParams): pointer to the NutRimParams object to copy. If the pointer equals to null then the object is duplicated

		Returns:
			NutHeadBaseParams: the pointer to a copy of an NutRimParams object.
		
		'''
		pass # cpp source



class NutClampLever(NutHeadBaseParams):

	@staticmethod
	def dynamic_cast(pObject : NutHeadBaseParams)->NutClampLever:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a NutClampLever class or its descendant, and if so, returns the specified object, but of the NutClampLever type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, d: float, h: float):
		pass # CPP source

	def holderDiameter(self, _0: float) -> NutClampLever:
		'''
			
		set the diameter of the holder.

		Args:
			_d (float): diameter

		Returns:
			NutClampLever: NutClampLever reference
		
		'''
		pass # cpp source

	def length(self, _0: float) -> NutClampLever:
		'''
			
		set the length.

		Args:
			_l (float): length

		Returns:
			NutClampLever: NutClampLever reference
		
		'''
		pass # cpp source

	def holderDiameter(self) -> float:
		'''
			
		get the diameter of the holder.

		Returns:
			float: holder diameter
		
		'''
		pass # cpp source

	def length(self) -> float:
		'''
			
		get the length.

		Returns:
			float: length value
		
		'''
		pass # cpp source

	def copy(self, p: NutHeadBaseParams = None) -> NutHeadBaseParams:
		'''
			
		copies the NutClampLever object.

		Args:
			p (NutHeadBaseParams): pointer to the NutClampLever object to copy. If the pointer equals to null then the object is duplicated

		Returns:
			NutHeadBaseParams: the pointer to a copy of an NutClampLever object.
		
		'''
		pass # cpp source



class nut(prim):
	'''
			
		nut primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->nut:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a nut class or its descendant, and if so, returns the specified object, but of the nut type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def setTypeData(self, data: any) -> nut:
		'''
			
		set the typed data.

		Args:
			data : pointer to the data

		Returns:
			nut: nut reference
		
		'''
		pass # cpp source

	def getTypeData(self) -> any:
		'''
			
		get the typed data.

		Returns:
			any: pointer to the data
		
		'''
		pass # cpp source

	def threadDiameter(self, d: float) -> nut:
		'''
			
		set the hole thread diameter.

		Returns:
			nut: nut reference
		
		'''
		pass # cpp source

	def threadDiameter(self) -> float:
		'''
			
		get the hole thread diameter.

		Returns:
			float: diameter
		
		'''
		pass # cpp source

	def pitch(self, p: float) -> nut:
		'''
			
		set the thread pitch.

		Returns:
			nut: nut reference
		
		'''
		pass # cpp source

	def pitch(self) -> float:
		'''
			
		get the thread pitch.

		Returns:
			float: pitch
		
		'''
		pass # cpp source

	def enableThread(self, f: bool) -> nut:
		'''
			
		set the enabled thread.

		Returns:
			nut: nut reference
		
		'''
		pass # cpp source

	def enableThread(self) -> bool:
		'''
			
		get the enabled thread.

		Returns:
			bool: enabled flag
		
		'''
		pass # cpp source

	def threadType(self, _0: int) -> nut:
		'''
			
		set the nut thread profile.

		Args:
			_t (int): profile type value (triangle,trapeze,rectangular,round,persistent)

		Returns:
			nut: nut reference
		
		'''
		pass # cpp source

	def threadType(self) -> int:
		'''
			
		get the nut thread profile.

		Returns:
			int: thread type value.
		
		'''
		pass # cpp source



class bolt(prim):
	'''
			
		bolt primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->bolt:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a bolt class or its descendant, and if so, returns the specified object, but of the bolt type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def head(self, _0: boltHead) -> bolt:
		'''
			
		set the head object.

		Args:
			_h (boltHead): head obj reference

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def head(self) -> boltHead:
		'''
			
		get the head object.

		Returns:
			boltHead: head obj reference
		
		'''
		pass # cpp source

	def diameter(self, _0: float) -> bolt:
		'''
			
		set the bolt diameter.

		Args:
			_d (float): diameter

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def diameter(self) -> float:
		'''
			
		get the bolt diameter.

		Returns:
			float: diameter
		
		'''
		pass # cpp source

	def pitch(self, _0: float) -> bolt:
		'''
			
		set the thread pitch.

		Args:
			_p (float): pitch

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def pitch(self) -> float:
		'''
			
		get the thread pitch.

		Returns:
			float: pitch
		
		'''
		pass # cpp source

	def threadHeight(self, _0: float) -> bolt:
		'''
			
		set the thread height.

		Args:
			_h (float): height

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def threadHeight(self) -> float:
		'''
			
		get the thread height.

		Returns:
			float: height value
		
		'''
		pass # cpp source

	def length(self, _0: float) -> bolt:
		'''
			
		set the bolt length.

		Args:
			_l (float): length

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def length(self) -> float:
		'''
			
		get the bolt length.
		
		'''
		pass # cpp source

	def threadLength(self, _0: float) -> bolt:
		'''
			
		set the thread length.

		Args:
			_l (float): length

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def threadLength(self) -> float:
		'''
			
		get the thread length.

		Returns:
			float: length
		
		'''
		pass # cpp source

	def threadType(self, _0: int) -> bolt:
		'''
			
		set the screw thread profile.

		Args:
			_t (int): profile type value (triangle,trapeze,rectangular,round,persistent)

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def threadType(self) -> int:
		'''
			
		get the screw thread profile.

		Returns:
			int: thread type value.
		
		'''
		pass # cpp source

	def underhead(self, _0: int) -> bolt:
		'''
			
		set the under head type.

		Args:
			_uh (int): type value (0-cylinder,1-rect)

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def underhead(self) -> int:
		'''
			
		get the under head type.

		Returns:
			int: under head type value
		
		'''
		pass # cpp source

	def uwidth(self, _0: int) -> bolt:
		'''
			
		set the underhead width.

		Args:
			_uw (int): width

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def uwidth(self) -> float:
		'''
			
		get the underhead width.

		Returns:
			float: width value
		
		'''
		pass # cpp source

	def uheight(self, _0: int) -> bolt:
		'''
			
		set the underhead height.

		Args:
			_uh (int): height

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def uheight(self) -> float:
		'''
			
		get the underhead height.

		Returns:
			float: height value
		
		'''
		pass # cpp source

	def nutType(self, _0: int) -> bolt:
		'''
			
		set the nut type.

		Args:
			_t (int): type value (see nut::Type enumarate)

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def nutType(self) -> int:
		'''
			
		get the nut type.

		Returns:
			int: type value
		
		'''
		pass # cpp source

	def nutLocation(self, _0: float) -> bolt:
		'''
			
		set the nut location on the bolt.

		Args:
			_loc (float): location value

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def nutLocation(self) -> float:
		'''
			
		get the nut location on the bolt.

		Returns:
			float: location value
		
		'''
		pass # cpp source

	def nutHeight(self, _0: float) -> bolt:
		'''
			
		set the nut height on the bolt.

		Args:
			_h (float): height value

		Returns:
			bolt: bolt reference
		
		'''
		pass # cpp source

	def nutHeight(self) -> float:
		'''
			
		get the nut height on the bolt.

		Returns:
			float: location value
		
		'''
		pass # cpp source



class screw(prim):
	'''
			
		screw primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->screw:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a screw class or its descendant, and if so, returns the specified object, but of the screw type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def head(self, _0: boltHead) -> screw:
		'''
			
		set the bolt head object.

		Args:
			_h (boltHead): bolt head obj reference

		Returns:
			screw: screw reference
		
		'''
		pass # cpp source

	def head(self) -> boltHead:
		'''
			
		get the bolt head object.

		Returns:
			boltHead: bolt head obj reference
		
		'''
		pass # cpp source

	def diameter(self, _0: float) -> screw:
		'''
			
		set the screw diameter.

		Args:
			_d (float): diameter

		Returns:
			screw: screw reference
		
		'''
		pass # cpp source

	def diameter(self) -> float:
		'''
			
		get the screw diameter.

		Returns:
			float: diameter
		
		'''
		pass # cpp source

	def pitch(self, _0: float) -> screw:
		'''
			
		set the screw thread step(pitch).

		Args:
			_p (float): step

		Returns:
			screw: screw reference
		
		'''
		pass # cpp source

	def pitch(self) -> float:
		'''
			
		get the screw thread step(pitch).

		Returns:
			float: step value
		
		'''
		pass # cpp source

	def threadDiameter(self, _0: float) -> screw:
		'''
			
		set the thread diameter.

		Args:
			_d (float): diameter

		Returns:
			screw: screw reference
		
		'''
		pass # cpp source

	def threadDiameter(self) -> float:
		'''
			
		get the thread diameter.

		Returns:
			float: diameter
		
		'''
		pass # cpp source

	def threadHeight(self, _0: float) -> screw:
		'''
			
		set the screw thread height.

		Args:
			_h (float): height

		Returns:
			screw: screw reference
		
		'''
		pass # cpp source

	def threadHeight(self) -> float:
		'''
			
		get the screw thread height.

		Returns:
			float: thread height value
		
		'''
		pass # cpp source

	def threadLength(self, _0: float) -> screw:
		'''
			
		set the screw thread length.

		Args:
			_l (float): length

		Returns:
			screw: screw reference
		
		'''
		pass # cpp source

	def threadLength(self) -> float:
		'''
			
		get the screw thread length.

		Returns:
			float: length value
		
		'''
		pass # cpp source

	def length(self, _0: float) -> screw:
		'''
			
		set the screw length.

		Args:
			_l (float): length

		Returns:
			screw: screw reference
		
		'''
		pass # cpp source

	def length(self) -> float:
		'''
			
		get the screw length.

		Returns:
			float: length
		
		'''
		pass # cpp source

	def underhead(self, _0: int) -> screw:
		'''
			
		set the underhead type.

		Args:
			_uh (int): type (0-cylinder,1-rect)

		Returns:
			screw: screw reference
		
		'''
		pass # cpp source

	def underhead(self) -> int:
		'''
			
		get the underhead type.

		Returns:
			int: type value
		
		'''
		pass # cpp source

	def uwidth(self, _0: int) -> screw:
		'''
			
		set the underhead width.

		Args:
			_uw (int): width

		Returns:
			screw: screw reference
		
		'''
		pass # cpp source

	def uwidth(self) -> float:
		'''
			
		get the underhead width.

		Returns:
			float: width value
		
		'''
		pass # cpp source

	def uheight(self, _0: int) -> screw:
		'''
			
		set the underhead height.

		Args:
			_uh (int): height

		Returns:
			screw: screw reference
		
		'''
		pass # cpp source

	def uheight(self) -> float:
		'''
			
		get the underhead height.

		Returns:
			float: height value
		
		'''
		pass # cpp source



class washer(prim):
	'''
			
		washer primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->washer:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a washer class or its descendant, and if so, returns the specified object, but of the washer type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def innerDiameter(self, _0: float) -> washer:
		'''
			
		set the inner diameter.

		Args:
			_d (float): diameter

		Returns:
			washer: washer reference
		
		'''
		pass # cpp source

	def innerDiameter(self) -> float:
		'''
			
		get the inner diameter.

		Returns:
			float: diameter
		
		'''
		pass # cpp source

	def outerDiameter(self, _0: float) -> washer:
		'''
			
		set the outer diameter.

		Args:
			_d (float): diameter

		Returns:
			washer: washer reference
		
		'''
		pass # cpp source

	def outerDiameter(self) -> float:
		'''
			
		get the outer diameter.

		Returns:
			float: diameter
		
		'''
		pass # cpp source

	def conusDiameter(self, _0: float) -> washer:
		'''
			
		set the diameter of the conus washer.

		Args:
			_d (float): diameter

		Returns:
			washer: washer reference
		
		'''
		pass # cpp source

	def conusDiameter(self) -> float:
		'''
			
		get the diameter of the conus washer.

		Returns:
			float: diameter
		
		'''
		pass # cpp source

	def thickness(self, _0: float) -> washer:
		'''
			
		set the washer thickness.

		Args:
			_s (float): thickness value

		Returns:
			washer: washer reference
		
		'''
		pass # cpp source

	def thickness(self) -> float:
		'''
			
		get the washer thickness.

		Returns:
			float: thickness value
		
		'''
		pass # cpp source

	def height(self, _0: float) -> washer:
		'''
			
		set the washer height.

		Args:
			_h (float): height value

		Returns:
			washer: washer reference
		
		'''
		pass # cpp source

	def height(self) -> float:
		'''
			
		get the washer height.

		Returns:
			float: height value
		
		'''
		pass # cpp source

	def facet(self, _0: bool) -> washer:
		'''
			
		indicates the facet usage.

		Args:
			_f (bool): facet flag

		Returns:
			washer: washer reference
		
		'''
		pass # cpp source

	def facet(self) -> bool:
		'''
			
		get the facet flag.

		Returns:
			bool: facet flag value
		
		'''
		pass # cpp source

	def type(self, _0: any) -> washer:
		'''
			
		set the washer type.

		Args:
			_t : type value

		Returns:
			washer: washer reference
		
		'''
		pass # cpp source

	def type(self) -> any:
		'''
			
		get the washer type.

		Returns:
			any: type value
		
		'''
		pass # cpp source



class freeform(prim):
	'''
			
		freeform primitive
		
	'''


	@staticmethod
	def dynamic_cast(pObject : prim)->freeform:
		'''
		An analogue of the dynamic_cast function from C++, it checks whether the object pObject is a freeform class or its descendant, and if so, returns the specified object, but of the freeform type.
		'''
		pass # cpp source

	def __init__(self):
		pass # CPP source

	def __init__(self, _0: str, _1: str):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def symx(self, x: bool) -> freeform:
		'''
			
		Enable the XYZ-mirror symmetry

		Args:
			x (bool): true to enable x-symmetry, false to disable

		Returns:
			freeform: freeform reference
		
		'''
		pass # cpp source

	def symy(self, y: bool) -> freeform:
		'''
			
		Enable the XYZ-mirror symmetry

		Args:
			y (bool): true to enable y-symmetry, false to disable

		Returns:
			freeform: freeform reference
		
		'''
		pass # cpp source

	def symz(self, z: bool) -> freeform:
		'''
			
		Enable the XYZ-mirror symmetry

		Args:
			z (bool): true to enable z-symmetry, false to disable

		Returns:
			freeform: freeform reference
		
		'''
		pass # cpp source

	def size(self, x: float, y: float, z: float) -> freeform:
		'''
			
		set the free form size

		Args:
			x (float): size in the x - axis
			y (float): size in the y - axis
			z (float): size in the z - axis

		Returns:
			freeform: freeform reference
		
		'''
		pass # cpp source

	def size(self, v: any) -> freeform:
		'''
			
		set the free form size

		Args:
			v : vector size

		Returns:
			freeform: freeform reference
		
		'''
		pass # cpp source

	def ffname(self, name: str) -> freeform:
		'''
			
		set the free form name.
		
		set of names {"Cube","Patch,"Blob","Round","Ring",Torus","Tube2","Tube3","Disc","Cylinder"}

		Args:
			name (str): the name string

		Returns:
			freeform: the freeform reference
		
		'''
		pass # cpp source

	def ffname(self) -> str:
		'''
			
		get the free form name.

		Returns:
			str: the name
		
		'''
		pass # cpp source

	def ffsubname(self, name: str) -> freeform:
		'''
			
		set the free form sub name.

		Args:
			name (str): the name string

		Returns:
			freeform: the freeform reference
		
		'''
		pass # cpp source

	def ffsubname(self) -> str:
		'''
			
		get the free form sub name.

		Returns:
			str: the name
		
		'''
		pass # cpp source

	def SetPoint(self, i: int, point: any) -> freeform:
		'''
			
		set the knot point of the primitive.

		Args:
			i (int): point index
			point : the coordinates of the point

		Returns:
			freeform: the freeform reference
		
		'''
		pass # cpp source

	def CountPoints(self) -> int:
		'''
			
		get the account of the knot points

		Returns:
			int: count of points
		
		'''
		pass # cpp source

	def ResetPoints(self):
		'''
			
		reset the knot points
		
		'''
		pass # cpp source

	def objsList(self) -> any:
		'''
			
		gets the object's list.

		Returns:
			any: objs list reference
		
		'''
		pass # cpp source

	def ffControlPoints(self) -> any:
		'''
			
		get the knot(control) points of the primitive.

		Returns:
			any: the points reference
		
		'''
		pass # cpp source

