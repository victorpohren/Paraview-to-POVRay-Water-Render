tstp = input("How many timesteps to render? (type a number from 0 to 400) ") 
print('rendering '+str(tstp)+' timesteps') 


#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XDMF Reader'
snapshotsxdmf = XDMFReader(FileNames=['/home/laset/filipi/data_channel/snapshots.xdmf']) #SNAPSHOTS PATH
snapshotsxdmf.PointArrayStatus = ['phi1', 'pre', 'q-criterion', 'ux', 'uy', 'uz']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on snapshotsxdmf
snapshotsxdmf.PointArrayStatus = ['phi1']
snapshotsxdmf.GridStatus = ['0000', '0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0010', '0011', '0012', '0013', '0014', '0015', '0016', '0017', '0018', '0019', '0020', '0021', '0022', '0023', '0024', '0025', '0026', '0027', '0028', '0029', '0030', '0031', '0032', '0033', '0034', '0035', '0036', '0037', '0038', '0039', '0040', '0041', '0042', '0043', '0044', '0045', '0046', '0047', '0048', '0049', '0050', '0051', '0052', '0053', '0054', '0055', '0056', '0057', '0058', '0059', '0060', '0061', '0062', '0063', '0064', '0065', '0066', '0067', '0068', '0069', '0070', '0071', '0072', '0073', '0074', '0075', '0076', '0077', '0078', '0079', '0080', '0081', '0082', '0083', '0084', '0085', '0086', '0087', '0088', '0089', '0090', '0091', '0092', '0093', '0094', '0095', '0096', '0097', '0098', '0099', '0100', '0101', '0102', '0103', '0104', '0105', '0106', '0107', '0108', '0109', '0110', '0111', '0112', '0113', '0114', '0115', '0116', '0117', '0118', '0119', '0120', '0121', '0122', '0123', '0124', '0125', '0126', '0127', '0128', '0129', '0130', '0131', '0132', '0133', '0134', '0135', '0136', '0137', '0138', '0139', '0140', '0141', '0142', '0143', '0144', '0145', '0146', '0147', '0148', '0149', '0150', '0151', '0152', '0153', '0154', '0155', '0156', '0157', '0158', '0159', '0160', '0161', '0162', '0163', '0164', '0165', '0166', '0167', '0168', '0169', '0170', '0171', '0172', '0173', '0174', '0175', '0176', '0177', '0178', '0179', '0180', '0181', '0182', '0183', '0184', '0185', '0186', '0187', '0188', '0189', '0190', '0191', '0192', '0193', '0194', '0195', '0196', '0197', '0198', '0199', '0200', '0201', '0202', '0203', '0204', '0205', '0206', '0207', '0208', '0209', '0210', '0211', '0212', '0213', '0214', '0215', '0216', '0217', '0218', '0219', '0220', '0221', '0222', '0223', '0224', '0225', '0226', '0227', '0228', '0229', '0230', '0231', '0232', '0233', '0234', '0235', '0236', '0237', '0238', '0239', '0240', '0241', '0242', '0243', '0244', '0245', '0246', '0247', '0248', '0249', '0250', '0251', '0252', '0253', '0254', '0255', '0256', '0257', '0258', '0259', '0260', '0261', '0262', '0263', '0264', '0265', '0266', '0267', '0268', '0269', '0270', '0271', '0272', '0273', '0274', '0275', '0276', '0277', '0278', '0279', '0280', '0281', '0282', '0283', '0284', '0285', '0286', '0287', '0288', '0289', '0290', '0291', '0292', '0293', '0294', '0295', '0296', '0297', '0298', '0299', '0300', '0301', '0302', '0303', '0304', '0305', '0306', '0307', '0308', '0309', '0310', '0311', '0312', '0313', '0314', '0315', '0316', '0317', '0318', '0319', '0320', '0321', '0322', '0323', '0324', '0325', '0326', '0327', '0328', '0329', '0330', '0331', '0332', '0333', '0334', '0335', '0336', '0337', '0338', '0339', '0340', '0341', '0342', '0343', '0344', '0345', '0346', '0347', '0348', '0349', '0350', '0351', '0352', '0353', '0354', '0355', '0356', '0357', '0358', '0359', '0360', '0361', '0362', '0363', '0364', '0365', '0366', '0367', '0368', '0369', '0370', '0371', '0372', '0373', '0374', '0375', '0376', '0377', '0378', '0379', '0380', '0381', '0382', '0383', '0384', '0385', '0386', '0387', '0388', '0389', '0390', '0391', '0392', '0393', '0394', '0395', '0396', '0397', '0398', '0399', '0400']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1544, 800]

# show data in view
snapshotsxdmfDisplay = Show(snapshotsxdmf, renderView1)
# trace defaults for the display properties.
snapshotsxdmfDisplay.Representation = 'Outline'
snapshotsxdmfDisplay.ColorArrayName = ['POINTS', '']
snapshotsxdmfDisplay.OSPRayScaleArray = 'phi1'
snapshotsxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
snapshotsxdmfDisplay.SelectOrientationVectors = 'None'
snapshotsxdmfDisplay.ScaleFactor = 2.0000000596046448
snapshotsxdmfDisplay.SelectScaleArray = 'phi1'
snapshotsxdmfDisplay.GlyphType = 'Arrow'
snapshotsxdmfDisplay.GlyphTableIndexArray = 'phi1'
snapshotsxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
snapshotsxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
snapshotsxdmfDisplay.ScalarOpacityUnitDistance = 0.07777749412071798
snapshotsxdmfDisplay.Slice = 47

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract Time Steps'
extractTimeSteps1 = ExtractTimeSteps(Input=snapshotsxdmf)
extractTimeSteps1.TimeStepIndices = [0]
extractTimeSteps1.TimeStepRange = [0, 400]

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on extractTimeSteps1
extractTimeSteps1.Mode = 'Select Time Range'
extractTimeSteps1.TimeStepRange = [0, tstp] #SELECT RANGE OF TIME STEPS

# show data in view
extractTimeSteps1Display = Show(extractTimeSteps1, renderView1)
# trace defaults for the display properties.
extractTimeSteps1Display.Representation = 'Outline'
extractTimeSteps1Display.ColorArrayName = ['POINTS', '']
extractTimeSteps1Display.OSPRayScaleArray = 'phi1'
extractTimeSteps1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractTimeSteps1Display.SelectOrientationVectors = 'None'
extractTimeSteps1Display.ScaleFactor = 2.0000000596046448
extractTimeSteps1Display.SelectScaleArray = 'phi1'
extractTimeSteps1Display.GlyphType = 'Arrow'
extractTimeSteps1Display.GlyphTableIndexArray = 'phi1'
extractTimeSteps1Display.DataAxesGrid = 'GridAxesRepresentation'
extractTimeSteps1Display.PolarAxes = 'PolarAxesRepresentation'
extractTimeSteps1Display.ScalarOpacityUnitDistance = 0.07777749412071798
extractTimeSteps1Display.Slice = 47

# hide data in view
Hide(snapshotsxdmf, renderView1)

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Contour'
contour1 = Contour(Input=extractTimeSteps1)
contour1.ContourBy = ['POINTS', 'phi1']
contour1.Isosurfaces = [0.0]
contour1.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour1
contour1.Isosurfaces = [0.1]

# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = [None, '']
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = -2.0000000000000002e+298
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData('/home/laset/stl2pov/a.stl', proxy=contour1, FileType='Binary',
    WriteAllTimeSteps=1) #PATH TO SAVE STL FILES, MUST BE THE SAME FROM STL2POV

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [10.0, 1.0, 40.00710951507274]
renderView1.CameraFocalPoint = [10.0, 1.0, 0.9895833730697632]
renderView1.CameraParallelScale = 10.09847885833585

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

#gerar arquivos pov e renderizar imagens e vide partindo dos objetos STL ----------------------

import os
import sys
import fileinput

# converte arquivos stl------------------------------------------------------------------------------------

for s in range(1, tstp+1): #SELECT RANGE OF TIMESTEPS
	stl = './stl2pov -s a.' + str(s) + '.stl > a' + str("%03d" % s) + '.inc'
	os.system(stl)




# altera nome da mesh no arquivo .inc para correspondente--------------------------------------------------

for m in range(1, tstp+1): #SELECT RANGE OF TIMESTEPS
	for line in fileinput.input('a'+ str("%03d" % m) +'.inc', inplace=True):
    		if line.strip().startswith('#declare'):
        		line = '#declare a'+ str("%03d" % m) +' = mesh {\n'
    		sys.stdout.write(line)




# altera nome da mesh no arquivo .pov para correspondente--------------------------------------------------

for x in range(1, tstp+1): #SELECT RANGE OF TIMESTEPS
# Read in the file
	with open('a%%%.pov', 'r') as file :
  		filedata = file.read()

# Replace the target string
	filedata = filedata.replace('a%%%', 'a'+ str("%03d" % x))

# Write the file out again
	with open('a'+ str("%03d" % x)+ '.pov', 'w') as file:
  		file.write(filedata)




# renderiza arquivos pov via povray-----------------------------------------------------------------------

for p in range(1, tstp+1): #SELECT RANGE OF TIMESTEPS
	pov = 'povray a' + str("%03d" % p) +'.pov -w4000 -h2000'
	os.system(pov)




# produz video--------------------------------------------------------------------------------------------

video = 'ffmpeg -framerate 14 -i a%03d.png -vf format=yuv420p video.mp4'
os.system(video)

print('\nRenderizado com sucesso.\n') 
