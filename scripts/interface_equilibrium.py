from compas_assembly.datastructures import Assembly
from compas_assembly.datastructures import assembly_interfaces_numpy
from compas_rbe.equilibrium import compute_interface_forces_cvx

# load assembly
assembly = Assembly.from_json('assembly_taubman.json')
# identify_interfaces
assembly_interfaces_numpy(assembly, nmax=10, amin=0.0001)
# compute equilibrium
compute_interface_forces_cvx(assembly, solver='CPLEX', verbose=True)
# export to json
assembly.to_json('equilibrium_taubman.json') 