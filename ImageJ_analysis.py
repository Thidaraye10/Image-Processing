
import imagej
import os 
from scyjava import jimport
import scyjava as sj
ij = imagej.init('sc.fiji:fiji')
import numpy as np
from PIL import Image
import tifffile

print(f"ImageJ2 version: {ij.getVersion()}")
print(ij.getApp().getInfo(True))

Runtime = jimport('java.lang.Runtime')
def java_mem():
    rt = Runtime.getRuntime()
    mem_max = rt.maxMemory()
    mem_used = rt.totalMemory() - rt.freeMemory()
    return '{} of {} MB ({}%)'.format(int(mem_used)/2**20, int(mem_max/2**20), int(100*mem_used/mem_max))

print(java_mem())


BF = sj.jimport('loci.plugins.BF')# needed for importing ND2 files 
options = sj.jimport('loci.plugins.in.ImporterOptions')() # import and initialize ImporterOptions
options.setOpenAllSeries(True)
options.setVirtual(True)
options.setId(r"/*PATH TO IMAGE*/")
imps = BF.openImagePlus(options)

# print(imps[0].shape)
# print(imps[0].dims)

ZProjector = sj.jimport("ij.plugin.ZProjector")()
test = (ZProjector.run(imps[0],'max'))
# print(test.dims)
# print(test.shape)

ChannelSplitter = sj.jimport("ij.plugin.ChannelSplitter")()
test2 = ChannelSplitter.split(test)


print(test2)
print(test2.length)


############# TESTING AREA FOR COLOR INCLUSION #######################
rgbtest = ij.py.to_xarray(test).values 
uint8rgbtest = rgbtest.astype(np.uint8) #casting to different type did not result in total fix here...
# "raise ValueError('ImageJ hyperstack is not a RGB image')"
# w/o casting it I get this: "ValueError: the ImageJ format does not support data type dtype('<u2') for RGB"

test12 = ij.py.to_xarray(test2[0]).values
test13 = ij.py.to_xarray(test2[1]).values
# imsave('my_image.tif', test13)
image = Image.fromarray(test12)
image.save("output.tif", "TIFF") #still greyscale here!
tifffile.imwrite("output2.tif", test12) #, photometric='rgb') # Photometric DOES NOT WORK 

####################################################################

print(dir(test2[0]))
print((test2[0].getID))
print((test2[0].getTitle()))
print((test2[1].getTitle()))

RGBStackMerge = sj.jimport("ij.plugin.RGBStackMerge")()
test3 = RGBStackMerge.mergeChannels([test2[0],test2[1]], True)
# test3 = RGBStackMerge.mergeChannels([test2[0].__getstate__, test[1].__getstate__] ,True)
print(test3)

save = sj.jimport("ij.IJ")()
save.saveAsTiff(test2[1], r"/*OUTPUT PATH FOR TIF FILE*/.tif") #greyscale image output here


# import ZProjector
# ZProjector = sj.jimport("ij.plugin.ZProjector")()
# impz = ij.py.to_imageplus(imps[0])
# z_project_result = ZProjector(impz, "avg")







# print(imps.shape())
# print(f"imp type: {type(imps)}") #imp type: <java class 'ij.ImagePlus[]'>
# # ij.py.show(imps)
# print(imps) #[<java object 'ij.CompositeImage$Anonymous'>]
# xarr = ij.py.from_java(imps)
# print(xarr)
# xarr2 = ij.py.to_dataset(imps)
# print(xarr2)

# imps_arr = []
# for imp in imps:
#     imps_arr.append(imp)
#     # imp.show()

# def dump_info(image):
#     """A handy function to print details of an image object."""
#     name = image.name if hasattr(image, 'name') else None # xarray
#     if name is None and hasattr(image, 'getName'): name = image.getName() # Dataset
#     if name is None and hasattr(image, 'getTitle'): name = image.getTitle() # ImagePlus
#     print(f" name: {name or 'N/A'}")
#     print(f" type: {type(image)}")
#     print(f"dtype: {image.dtype if hasattr(image, 'dtype') else 'N/A'}")
#     print(f"shape: {image.shape}")
#     print(f" dims: {image.dims if hasattr(image, 'dims') else 'N/A'}")

# # xarr = ij.py.from_java(imps)
# dump_info(xarr)
# dump_info(xarr2)
# # dump_info(imps)



# ij.ui().show(imps)
# load test image
# dataset = ij.io().open("/Volumes/All_Staff/People/Thidar/Microscopy/1182024_fancd2_mcherry_IR/1182024_facd2_mcherry_IR_1.nd2")

# display test image (see the Working with Images for more info)
# ij.py.show(dataset)






# # Load individual channel images
# red_channel = ij.io().open(os.path.abspath("RNAi_egl2_1_gfp"))
# green_channel = ij.io().open(os.path.abspath("RNAi_egl2_1_mcherry"))
# #blue_channel = ij.io().open(os.path.abspath("blue_channel.tif"))

# # Create a composite image
# composite_image = ij.op().run("Merge Channels...", {
#     "c1": red_channel,
#     "c2": green_channel,
#     #"c3": blue_channel,
#     "red": "c1",
#     "green": "c2",
#     #"blue": "c3",
#     "create": True
# })

# # Save the composite image
# ij.io().save(composite_image, "merged_image.tif")