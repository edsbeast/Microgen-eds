from pathlib import Path

import cadquery as cq

from microgen import Tpms, surface_functions

###Parameters
plt_thick = 0.3 #thickness of plate
size = 3 #int, size of lattice
comb = plt_thick + size
thickness = 0.8 #offset parameter
while thickness <= 1.5:

    ###Create the plates
    box = cq.Workplane().box(comb,comb,size)
    shell = cq.Workplane("front").box(comb,comb,comb)
    shell = shell.cut(box)
    shell = shell.val()

    ###Create the lattice structure
    geometry = Tpms(
        surface_function=surface_functions.schwarz_d,
        offset=thickness,
        repeat_cell=size,
        resolution = 15,
    )
    shape = geometry.generate(type_part="sheet", smoothing=0)

    ###Combine and export file
    compound = cq.Compound.makeCompound([shell, shape])
    stl_file = str(Path(__file__).parent / "SchwarzD" / f"{thickness}tpms_schwarzd.stl")
    cq.exporters.export(compound, stl_file)
    thickness += 0.05