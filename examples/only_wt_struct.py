from acdc_nn import acdc_nn
from acdc_nn import util

profile = "tests/profiles/2ocjA.prof.gz"
pdb = "tests/structures/2ocj.pdb.gz"
chain = "A"
sub = "Q104H"

wt_prof = util.getProfile(profile)  #FIXME use Profile
wt_struct = acdc_nn.Structure(pdb, chain)
net = acdc_nn.ACDC3D()
ddg = net.predict(str(sub), wt_prof, wt_struct)
print(ddg)