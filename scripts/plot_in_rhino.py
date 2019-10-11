from compas_assembly.datastructures import Assembly
import rhinoscriptsyntax as rs

# load assembly
assembly = Assembly.from_json('equilibrium_taubman.json')



# plot assembly in Rhino
assembly.draw({
    'layer': 'Assembly',
    'show.vertices': True,
    'show.edges':True,
    'show.forces': True,
    'show.forces_as_vectors': True,
    'show.interfaces': True,
    'mode.interface': 0,
    'mode.force':0,
    'show.selfweight':True,
    'scale.force': 1.0
})


rs.CurrentLayer('Assembly')
rs.LayerVisible('Blocks', False)
rs.LayerVisible('Supports', False)

