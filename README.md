# Paraview-to-POVRay-Water-Render
A python script to export isosurfaces from ParaView and render a scene with natural water appeareance by using Ray Tracing technique.

![Image of Yaktocat](https://github.com/victorpohren/Paraview-to-POVRay-Water-Render/blob/master/victor_bacia2.png)

Required softwares:

ParaView (https://www.paraview.org/download/)

POV-Ray (https://www.povray.org/download/)

FFmpeg (https://www.ffmpeg.org/download.html)

## GETTING STARTED:

- Clone Paraview-to-POVRay-Water-Render archives to a directory of your choice

- Open a shell prompt, seek the directory where you cloned it and run: python water_render.py

## OPERATING THE SOFTWARE:

The software will ask you to input a few parameters before it starts rendering:

- Path to the snapshots file in your simulation database

- Name to create a new directory where your visualization files will be saved

- Range of frames you want to render (input the first and last values of it)

- Range of isovalours you want in your isosurface (input how many of they as well as the first and last values of this)

## RENDERING PROCESS:

1. After setting the parameters the software will export the isosurfaces and synthesize a picture from the last frame.

2. The software will ask if you want to scalate the objects in the scene. If you choose to do it, input a value to scale it and wait for the rendering process again. The software will redo this step until you are satisfied with the result and set the new scale value.

3. After the scale test you can choose to edit camera position and flowbox to frame the flow geometry as you wish. It must be edited manually in the pattern pov file. The software will test rendering the last frame again and ask if you are satisfied.

4. Finally the rendering process of all frames will commence and show a mp4 video (in infinite loop) with a pattern framerate (15fps) after it finishes. The software asks if you want to set a new framerate. If yes, input another value and check the result. 

5. The rendering process ends when you are satisfied with the output.









