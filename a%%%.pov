
#include "./a%%%.inc"   // match %%% for the correspondent mesh a%03d
#include "math.inc"
#include "finish.inc"
#include "transforms.inc"
#include "colors.inc"
#include "textures.inc"
#include "stones.inc"    
#include "glass.inc"

#declare AreaLight=on;
#declare Radiosity=on;
#declare Photons=on;
#declare TestLight=off;

global_settings{
  max_trace_level 15
  assumed_gamma 1
    
  #if (Radiosity=on)
    radiosity{
      pretrace_start 0.08
      pretrace_end   0.01
      count 130
      nearest_count 5
      error_bound 0.3

      recursion_limit 1
      low_error_factor 0.5
      gray_threshold 0.0
      minimum_reuse 0.015
      brightness 1.0
      adc_bailout 0.01/2
      normal on
    }
  #end

  #if (Photons=on)
    photons {
      spacing 0.003
      save_file "photons.ph" //*****save photon calculating for later rendering, use load_file "photons.ph"

    }
  #end

}

// camera // location on the x axis 
#declare Cam0 = camera {/*ultra_wide_angle*/ angle 45 
                        location  <16.864 , 5.0 ,-7.5> 
                        look_at   <16.564 , 1 , 0.0>
                        rotate  <-5, -50, 0>
                        translate < 8, 2, -15>
                        }
camera{Cam0}


// OBJECT--------------------------------------------------------------------------

#declare Min = min_extent(a%%%);   // match %%% for the correspondent a%03d.inc 
#declare Max = max_extent(a%%%);   // match %%% for the correspondent a%03d.inc 
#declare bottom_diag = sqrt(pow(Max.y - Min.y, 2) + pow(Max.x - Min.x, 2));
#debug concat("bottom_diag:", str(bottom_diag, 5, 0))
#declare box_diag = sqrt(pow(bottom_diag, 2) + pow(Max.z - Min.z, 2));
#debug concat("box_diag:", str(box_diag, 5, 0))
#declare look_angle = degrees(tanh((Max.z - Min.z) / (bottom_diag / 2)));
#declare look_at_z = (Max.z - Min.z) / 2;
#debug concat("look_at:", str(look_at_z, 5, 0))


object {
  a%%%
 // match % for the correspondent a%03d.inc 
  texture{ pigment { Col_Glass_Old } 
                normal { ripples 0.7 scale 1.25
                          translate< 1.5,0,2>}
                finish { ambient 0.05 diffuse 0.55 
                         brilliance 3.0 specular 0.8 roughness 0.0025
                         reflection 0.0 }
              }
      interior{ ior 1.33 }
}

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

// stone plane --------------------------------------------------------------------

plane{ <0,1,0>, 0 
       texture { T_Stone1 	scale 4}
       photons {collect off}      
     }
//---------------------------------------------------------

