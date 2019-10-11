from compas.datastructures import mesh_weld
from compas_assembly.datastructures import Assembly
from compas_assembly.datastructures import Block
from compas_rhino.utilities import get_meshes

# get support meshes and block meshes from Rhino
rhino_supports = get_meshes("Supports")
rhino_blocks = get_meshes("Blocks")

#  create and weld compas meshes
supports = []
for i in rhino_supports:
    support = Block.from_rhinomesh(i)
    support = mesh_weld(support)
    supports.append(support)

blocks = []
for i in rhino_blocks:
    block = Block.from_rhinomesh(i)
    block = mesh_weld(block)
    blocks.append(block)

# create an assembly
assembly = Assembly()

for i in supports:
    assembly.add_block(i, is_support = True)
for i in blocks:
    assembly.add_block(i, is_support = False)

# export the assembly in a .json file

assembly.to_json('assembly_taubman.json')