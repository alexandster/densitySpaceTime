Space-Time Kernel Density Estimation STKDE

Required modules:
numpy, scipy

Relevant literature:
Hohl, A., Delmelle, E. M., & Tang, W. (2015). Spatiotemporal domain decomposition for massive parallel computation of space-time kernel density. ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences, 2(4), 7.
Hohl, A., Delmelle, E., Tang, W., & Casas, I. (2016). Accelerating the discovery of space-time patterns of infectious diseases using parallel computing. Spatial and spatio-temporal epidemiology, 19, 10-20.
Hohl, A., Casas, I., Delmelle, E., & Tang, W. (2016, January). Hybrid Indexing for Parallel Analysis of Spatiotemporal Point Patterns. In International Conference on GIScience Short Paper Proceedings (Vol. 1, No. 1).

Files:
main.py - reads data and parameter files, creates directories, starts STKDE
settings.py - initiates global variables
kde.py - contains kernel density function

files/data.txt - contains 100 random data points used in this example. Each point has 3 coordinates (2 spatial & 1 temporal)
files/parameterFile.txt - contains parameter values relevant for STKDE

Procedure:
Dump the entire repository in a directory, execute main.py
It creates a directory that contains files of density estimates and execution time.
