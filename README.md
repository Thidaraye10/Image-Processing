# Image Processing 
## Confocal microscopy images of Drosophila Melanogaster brain lobes instar larvae 3 stage.
Trangenic flies contain ubiquitin promoter to drive the expression of gene fused to GFP. Brains are also stained with nuclei marker, DAPI. Images were taken on nikon confocal microscope with Z-stacks (nd2). This code contains the following image processing fucntions:
- Z projection of all Z stacks to project maximum intensity 
- Spliting the channels after max-intensity
- Mergeing the channels after max-intensity 
- Saving the processed images after converting from nd2 files to tiffs 

This was performed using the following enviroment: 
- Apple M1 Macbook Air
- MacOS: Sonoma 14.4
- ImageJ2 2.16.0
- Java 11.0.23

More to-dos include but are not limited to: 
- Bugfix for greyscale images at the end result
- Batch file inclusion for analyzing whole folders of ND2 images 
- Re-configuration of code to be object oriented 
- Potential for further analysis steps using NumPy
