## Workflow

- preprocess on local computer usisng notbook
- upload configuration files to training cluster
- run specfem on training cluster
- download results in local computer 
- post-process results 

## Local computer

### Material for training 
https://github.com/mnagaso/specfem_training
notebooks are also on training cluster 
/shared/cheese/specfem3d/notebook
follow the instruction to setup docker image in your local computer.

## Training cluster 

Specfem executable are in : 
`/shared/cheese/specfem3d/specfem_fwi/bin`  
compiled with the following modules  
`module load compiler/intel/19.1.3`  
`module load mpi/impi/19.1.3`  
create scractch disk space  
`specfem3d_SCRATCH=$(ws_allocate specfem3d_scratch 10)`  
go inside this directory  
`cd $specfem3d_SCRATCH/`  
for an exercise create a directory  
`mkdir name_of_directory_for_exercice`  
For the exercice the setup files will be uploaded in this directory, specfem will be launch inside  

### setup python tools 
```
cd /shared/cheese/specfem3d/pyspecfem/
module load python/3.9
pip install .
```
### Launching pbs script with qsub
`qsub -q pbs_script.pbs`