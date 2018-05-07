import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import param as p

class WhirlyBirdAnimation:

	def __init__(self):
		self.flagInit = True                  # Used to indicate initialization
		self.fig = plt.figure()
		self.ax = Axes3D(self.fig)  # Create a 3D axes in the figure

		# A list object that will contain the lists of vertices of the
		# space ships sides.
		self.verts = self.getWhirlybirdVertices()

		# A list that will contain handles to the Poly3DCollection
		# Objects so that they can be modified.
		self.PolyCollections = []

		# Set axis limits
		_axis_limit = 1
		self.ax.set_zlim3d([-_axis_limit, _axis_limit])
		self.ax.set_ylim3d([-_axis_limit, _axis_limit])
		self.ax.set_xlim3d([-_axis_limit, _axis_limit])

		# Set title and labels
		self.ax.set_title('Whirlybird')
		self.ax.set_xlabel('East')
		self.ax.set_ylabel('North')
		self.ax.set_zlabel('-Down')

		# Change viewing angle
		self.ax.view_init(self.ax.elev, self.ax.azim + 90)

	def drawWhirlybird(self, u):
		# Desired configuration
		phi = u[0]  # roll
		theta = u[1]  # pitch
		psi = u[2]  # yaw


		# Rotates, translates, and transforms the whirlybird.
		verts = []
		vertsTemp = rotate(self.verts[0].T, phi, theta, psi).T #Rotate
		vertsTemp = transformXYZtoNED(vertsTemp) #Transform!
		vertsTemp = np.asarray(vertsTemp) #Make it an array
		verts.append(vertsTemp) #Make temp verts

		#This defines the Stand. We started quite simiply
		stand_verts = [[[0, 0, 0],  # Vertex 2 (X,Y,Z)
		                [0, 0, -p.h]]]  # Vertex 1 (X,Y,Z)

		if self.flagInit == True:

			# Initialize Poly3DCollection class for each set of vertices, and
			# create an object handle to each one.
			self.PolyCollections.append(Poly3DCollection(verts, facecolor='red', edgecolor='black', lw=2)) #Whirlybird
			self.PolyCollections.append(Poly3DCollection(stand_verts, facecolor='orange', edgecolor='black', lw=2)) #Stand
			# Add each Poly3DCollection object to the axes.
			for i in range(len(self.PolyCollections)):
				self.ax.add_collection3d(self.PolyCollections[i])
			self.flagInit = False

		else:
			# Update the verts
			self.PolyCollections[0].set_verts(verts)

	def getWhirlybirdVertices(self):
		# Set up Matrices Here!!! pack them!

		whirlybird_vert = np.matrix([[0, 0, 0],
									[p.l_1, 0, 0],
									[p.l_1, -(p.d - p.r), 0],
									[ (p.l_1 - p.r),-(p.d - p.r), 0],
									[(p.l_1 - p.r), -(p.d + p.r), 0],
									[(p.l_1 + p.r), -(p.d + p.r), 0],
									[(p.l_1 + p.r), -(p.d - p.r), 0],
									[p.l_1,-(p.d - p.r), 0],
									[p.l_1, (p.d - p.r), 0],
									[(p.l_1 + p.r), (p.d - p.r), 0],
									[(p.l_1 + p.r), (p.d + p.r), 0],
									[(p.l_1 - p.r), (p.d + p.r), 0],
									[(p.l_1 - p.r),(p.d - p.r), 0],
									[p.l_1, (p.d - p.r), 0],
									[p.l_1, 0, 0],
									[-p.l_2, 0, 0],
									[0, 0, 0]])

		return [whirlybird_vert]

# This function transforms the image from XYZ frame to NED frame
def transformXYZtoNED(XYZ):
		R = np.matrix([[0, 1, 0],
		               [1, 0, 0],
		               [0, 0, -1]])
		NED = XYZ * R
		return NED

def rotate(XYZ, phi, theta, psi):

	# Define rotation matrix
	R_roll = np.matrix([[1, 0, 0],
	                    [0, np.cos(phi), -np.sin(phi)],
	                    [0, np.sin(phi), np.cos(phi)]])

	R_pitch = np.matrix([[np.cos(theta), 0, np.sin(theta)],
	                     [0, 1, 0],
	                     [-np.sin(theta), 0, np.cos(theta)]])

	R_yaw = np.matrix([[np.cos(psi), -np.sin(psi), 0],
	                   [np.sin(psi), np.cos(psi), 0],
	                   [0, 0, 1]])
	R = R_yaw * R_pitch * R_roll;

	# rotate vertices
	XYZ = R * XYZ

	return XYZ