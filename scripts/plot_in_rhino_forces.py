from compas_assembly.datastructures import Assembly
import rhinoscriptsyntax as rs
from compas.geometry import centroid_points
import math as mt

# load assembly
assembly = Assembly.from_json('equilibrium_taubman.json')


# plot assembly in Rhino
assembly.draw({
    'layer': 'Assembly',
    'show.selfweight':True,
    'show.vertices': True,
    'show.edges':True,
    'show.forces': True,
    'show.forces_as_vectors': True,
    'show.interfaces': True,
    'mode.interface': 0,
    'mode.force':0,
    'scale.force': 10.0
})

rs.CurrentLayer('Assembly')
rs.LayerVisible('Blocks', False)
rs.LayerVisible('Supports', False)

rs.AddLayer('forces')
rs.LayerColor('forces',(255,0,0))
rs.DeleteObjects(rs.ObjectsByLayer('forces'))
rs.CurrentLayer('forces')

g = 9.81 #m/s^2
d = 1000 #Kg/m^3
for a, b, attr in assembly.edges(True):
    if attr['interface_forces'] is None:
        continue
    s = attr['interface_size']
    sp = attr['interface_points']
    fff = []
    for i in range(len(attr['interface_points'])):
        t = attr['interface_forces'][i]['c_nn']
        cp = centroid_points(sp)
        if t >= 0.0001:
            fff.append(t)
    fsum = mt.fsum(fff)
    if fsum:
        force = fsum * g * d #force in N
        force = round(force, 4)
        rs.AddTextDot(str(force) + ' N',cp)






