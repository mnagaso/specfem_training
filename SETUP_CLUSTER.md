# setup scratch directory
0. ssh login
    ssh sca00000@training.hlrs.de
1. create a working directory
    `SPECFEM3D_SCRATCH=$(ws_allocate specfem3d-exercise 10)` 

2. create sub directories in the working directory
    
    `cd /shared/training/ws/$(whoami)-specfem3d-exercise/`  
    `mkdir homogeneous`  
    `mkdir marmousi_acoustic`  
    `mkdir piton`  
    
3. load the python module with `module load python`

4. install pyspecfem on cluster
    `cd /shared/cheese/specfem3d/pyspecfem`  
    `pip install --user .`  