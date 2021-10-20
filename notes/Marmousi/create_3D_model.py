import h5py
import argparse
import numpy as np

def write_in_bin(bin_file, array):
    f_bin_data = open(bin_file,"wb")
    array_to_write = array.astype(np.float32)
    array_to_write = array_to_write.copy(order='C')
    f_bin_data.write(array_to_write)

parser = argparse.ArgumentParser(description=
                                 'create model in 3D fd grid from 2d slices in hdf5 file')


parser.add_argument('--ny',
                    help='number of point in y direction [1]',
                    default=1, type=int)


parser.add_argument('--dy',
                    help='step  in y direction [1]',
                    default=1, type=float)


parser.add_argument('--oy',
                    help=' origin in y direction [1]',
                    default=1, type=float)

parser.add_argument('--f',
                    help=' hdf5 file with 2d slices of model  [input_2d_model.h5]',
                    default='input_2d_model.h5')


args = parser.parse_args()


with h5py.File(args.f, "r") as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]
    print("Attribues: %s" % f['/'].attrs.keys())

    print(f['/'].attrs['description'])

    dx = f['/'].attrs["dx"][0]
    dz = f['/'].attrs["dz"][0]
    dy = args.dy
    
    nx = int(f['/'].attrs["nx"][0])
    nz = int(f['/'].attrs["nz"][0])
    ny = args.ny
    
    ox = f['/'].attrs["ox"][0]
    oz = f['/'].attrs["oz"][0]
    oy = args.oy
    
    rh2d = f.get('RHO')
    vp2d = f.get('VP')
    vs2d = f.get('VS')

    print(vp2d.shape)

    # write model in hdf5 file in single precision
    rh3d = np.zeros((vp2d.shape[1],args.ny,vp2d.shape[0])) 
    vp3d = np.zeros((vp2d.shape[1],args.ny,vp2d.shape[0]))
    vs3d = np.zeros((vp2d.shape[1],args.ny,vp2d.shape[0]))
    for i in range(0,args.ny):
        rh3d[:,i,:]=np.transpose(rh2d)
        vp3d[:,i,:]=np.transpose(vp2d)
        vs3d[:,i,:]=np.transpose(vs2d)
        
    print(vp3d.shape)
   
    hf = h5py.File('fd_grid.h5','w-')
    hf.create_dataset("rho",data=rh3d, dtype = np.float32)
    hf.create_dataset("vp",data=vp3d, dtype = np.float32)
    hf.create_dataset("vs",data=vs3d, dtype = np.float32)

    
    # write grid properties in ascii file
    fid = open("fd_grid.txt","w")
    fid.write(" {} {} {} \n".format(ox, oy, oz))
    fid.write(" {} {} {} \n".format(nx, ny, nz))
    fid.write(" {} {} {} \n".format(dx, dy, dz))
    fid.write("rho.bin \n")
    fid.write("vp.bin \n")
    fid.write("vs.bin \n")
    fid.close()
    
    # write in raw binary file also
    write_in_bin("rho.bin", rh3d)
    write_in_bin("vp.bin", vp3d)
    write_in_bin("vs.bin", vs3d)
