# Paraview-to-POVRay-Water-Render
A python script to export isosurfaces from ParaView and render a scene with natural water appeareancescene via POV-Ray

Required softwares:

ParaView (https://www.paraview.org/download/)

POV-Ray (https://www.povray.org/download/)

FFmpeg (https://www.ffmpeg.org/download.html)

GETTING STARTED:

- Clone Paraview-to-POVRay-Water-Render archives to a directory of your choice

- Open a shell prompt, seek the directory where you cloned it and run: python water_render.py

OPERATING THE SOFTWARE:

The software will ask you to input a few parameters before it starts rendering:

- Input the path to the XDMF file in your simulation database

- Input a name to create a new directory whe your visualization files will be saved

- Input the total frames number and time [seconds] of your simulation (this step requires open your XDMF file manually in ParaView and withdrawn the information from the toolbar by seting the last frame)

- Select the range of frames you want to render inputing the first and last values of it

- Select the range of isovalours you want in your isosurface inputing how many of they and the first and last values of this

RENDERING PROCESS:

After setting the parameters the software will export the isosurfaces and synthesize a picture from the last frame.

The software will ask if you want to escalete the objects in the scene. If you choose to do it, input a value to scale it and wait for the rendering process again. The software will redo this step until you are satisfied with the result and set the new scale value.

The rendering process of all frames will commence and show a mp4 video (in infinite loop) with a pattern framerate (15fps) after it finishes. The software asks if you want to set a new framerate. If yes, input another value and check the result. 

The rendering process ends when you are satisfied with the output.

