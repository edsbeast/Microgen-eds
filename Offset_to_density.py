from pathlib import Path

import cadquery as cq

from microgen import Tpms, surface_functions

###Parameters
Offset = 0.7 #offset parameter used

    ###Calculate the density from the given offset
density = Tpms.density_from_offset(
     surface_function=surface_functions.schwarz_p, #select which morphology to use
     offset=Offset,
     part_type = 'sheet', #State the part type, 'sheet', 'lower skeletal', or 'upper skeletal'
     resolution = 15,  #keep resolution consistent between conversion
    )

print(f"The density for the given offset is: {density}")
    ###Combine and export file

'''
0.8schwarzD COMSOL = 0.34575185
0.8schwarzD microgen = 0.3408794

0.6gyroid COMSOL = 0.07217407
0.6gyroid microgen = 0.1993156

0.4gyroid COMSOL = 0.1969037
0.4gyroid microgen = 0.131774

0.7schwarzP COMSOL = 0.15198889
0.7schwarzP microgen = 0.2033903

0.7 DENSITY gyroid on COMSOL = 0.3662

'''

