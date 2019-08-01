Notes to fix gpu driver problem on ubuntu titanX

ImportError: libcublas.so.10.0: cannot open shared object file: No such file or directory
ImportError: libcusolver.so.10.0: cannot open shared object file: No such file or directory

create symlink like:





This means tensorflow-gpu cant find the right CUDA version which is 10.0 for tensorflow 13.1.1 w/Python 3.7
Some versions of tf require Cuda10.1

Install instructions after you download the deb local file from NVIDIA: 
`sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb`
`sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub`
`sudo apt-get update`
`sudo apt-get install cuda`
