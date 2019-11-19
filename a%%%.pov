#include "./char_.pov"   // match %%% for the correspondent mesh a%03d

#include "math.inc"
#include "finish.inc"
#include "transforms.inc"
#include "colors.inc"
#include "textures.inc"    
#include "glass.inc"

#declare AreaLight=on;
#declare Radiosity=on;
#declare Photons=on;
#declare TestLight=off;

#local p_start		=	64/image_width;
#local p_end_tune	=	8/image_width;
#local p_end_final	=	4/image_width;

global_settings{
  max_trace_level 15
  assumed_gamma 1
    
  #if (Radiosity=on)
    radiosity{
      pretrace_end   0.005
      count 130
      nearest_count 5
      error_bound 0.4

      recursion_limit 2
      minimum_reuse 0.015
      brightness 1.0
      adc_bailout 0.01/2
    }
  #end

  #if (Photons=on)
    photons {
      spacing 0.003

    }
  #end

}

// camera // location on the x axis 
#declare Cam0 = camera {/*ultra_wide_angle*/ angle 45 
                        location  <18 , 5.2 ,-8> 
                        look_at   <10, 0.5 , 2>
                        }
camera{Cam0}






//--------------------------------------------------------------------------


// light source ---------------------------------------------------------------
#if (TestLight=on)
  light_source {
    <2, 2, 2>
    color rgb 0.7
  }
#end


light_source {
  <1500,2500,-2500> color White
  #if (AreaLight=on)
    area_light 400*x 400*y  4,4
    jitter
    circular
    orient
  #end

  photons {
    reflection off
    refraction on
  }
}




// sky ---------------------------------------------------------------------
plane{<0,1,0>,1 hollow  
       texture{ pigment{ bozo turbulence 0.76
                         color_map { [0.5 rgb <0.20, 0.20, 0.9>]
                                     [0.6 rgb <1,1,1>]
                                     [1.0 rgb <0.1,0.1,0.1>]}
                         scale 3.5 translate<8,0,11>
                       }
                finish {ambient 1 diffuse 0} }      
       scale 10000}
//--------------------------------------------------------------------------
   
// fog ---------------------------------------------------------------
fog{fog_type   2   distance 85  color rgb<1,0.99,0.9>
    fog_offset 0.1 fog_alt  2 turbulence 0.2}

// grid plane --------------------------------------------------------------------

plane{ <0,1,0>, 0 
        pigment {
      Tiles_Ptrn()
      color_map{
         [0.0 color rgb <0,0,0>]   // black stanchions
         [0.04 color rgb <1,1,1>]  // white spaces
      }
     scale <0.5, 0.8, 0.5>    // Here yo can set the size and ratio of the grid
      rotate x*90  // rotates the pattern onto the "upper side" of the plane
   }     
     }
//---------------------------------------------------------


// OBJECT--------------------------------------------------------------------------

#declare Min = min_extent(char_);   // match %%% for the correspondent a%03d.inc 
#declare Max = max_extent(char_);   // match %%% for the correspondent a%03d.inc 
#declare bottom_diag = sqrt(pow(Max.y - Min.y, 2) + pow(Max.x - Min.x, 2));
#debug concat("bottom_diag:", str(bottom_diag, 5, 0))
#declare box_diag = sqrt(pow(bottom_diag, 2) + pow(Max.z - Min.z, 2));
#debug concat("box_diag:", str(box_diag, 5, 0))
#declare look_angle = degrees(tanh((Max.z - Min.z) / (bottom_diag / 2)));
#declare look_at_z = (Max.z - Min.z) / 2;
#debug concat("look_at:", str(look_at_z, 5, 0))

object {
  char_
//scale
 // match % for the correspondent a%03d.inc 
  texture{ pigment { Col_Glass_Old } 
                finish { ambient 0.0 diffuse 0.55 
                         brilliance 3.0 specular 0.8 roughness 0.0025
                         reflection 0.0 }
              }
      interior{ ior 1.33 }
}




//----------------------------------------- flow box --------------------------------------------------

//--left box
box{ <-200/2,0,-80/2>,<0,2.5/2,0.05/2> 
//scale
    texture { New_Brass 	scale 1}
                finish { ambient 0.0 diffuse 0.0
                         reflection 0.0 }   
 }

//--water flow box
box{ <-200/2,0,0.05/2>,<0,2.0/2,4/2>
//scale
    texture{ pigment { Col_Glass_Old } 
                finish { ambient 0.05 diffuse 0.55 
                         brilliance 3.0 specular 0.8 roughness 0.0025
                         reflection 0.0 }
              }
      interior{ ior 1.33 }
}
//--right box
box{ <-200/2,0,2.0/2>,<0,2.5/2,400/2> 
//scale
    texture { 	New_Brass 	scale 1 }   
                finish { ambient 0.0 diffuse 0.0
                         reflection 0.0 }  
}
//-----------------------------------------------------------------
//-----------------------------------------------------------------
