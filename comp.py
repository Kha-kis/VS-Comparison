from vstools import vs, core, set_output, depth
from awsmfunc import FrameInfo
from awsmfunc.types.placebo import PlaceboColorSpace as ColorSpace
from awsmfunc.types.placebo import PlaceboTonemapFunction as Tonemap
from awsmfunc.types.placebo import PlaceboGamutMapping as Gamut
from awsmfunc.types.placebo import PlaceboTonemapOpts
from vskernels import EwaLanczos, Hermite

# File paths
clip1 = core.lsmas.LWLibavSource(r"C:\Path\To\File1.mkv")
clip2 = core.lsmas.LWLibavSource(r"C:\Path\To\File2.mkv")
clip3 = core.lsmas.LWLibavSource(r"C:\Path\To\File3.mkv")

# Source names
source1 = "FirstSourceName"
source2 = "SecondSourceName"
source3 = "ThirdSourceName"

# Display frame info
clip1 = FrameInfo(clip1, source1)
clip2 = FrameInfo(clip2, source2)
clip3 = FrameInfo(clip3, source3)

# Frame rate adjustments (if necessary)
clip1 = core.std.AssumeFPS(clip1, fpsnum=24000, fpsden=1001)
clip2 = core.std.AssumeFPS(clip2, fpsnum=25000, fpsden=1000)
clip3 = core.std.AssumeFPS(clip3, fpsnum=24000, fpsden=1000)

# Interlacing fix
clip1 = core.std.SetFieldBased(clip1, 0)
clip2 = core.std.SetFieldBased(clip2, 0)
clip3 = core.std.SetFieldBased(clip3, 0)

# Cropping (adjust values as needed)
clip1 = core.std.Crop(clip1, left=0, right=0, top=0, bottom=0)
clip2 = core.std.Crop(clip2, left=0, right=0, top=0, bottom=0)
clip3 = core.std.Crop(clip3, left=0, right=0, top=0, bottom=0)

# Scaling (use either upscaling or downscaling as necessary)
clip1 = EwaLanczos.scale(clip1, 1920, 1080, sigmoid=True)
clip2 = EwaLanczos.scale(clip2, 1920, 1080, sigmoid=True)
clip3 = EwaLanczos.scale(clip3, 3840, 2160, sigmoid=True)

# Convert depth for tonemapping and cropping
clip1 = core.resize.Lanczos(clip1, format=vs.YUV444P16)
clip2 = core.resize.Lanczos(clip2, format=vs.YUV444P16)
clip3 = core.resize.Lanczos(clip3, format=vs.YUV444P16)

# Tonemapping (if needed)
clip1args = PlaceboTonemapOpts(source_colorspace=ColorSpace.DOVI, target_colorspace=ColorSpace.SDR, 
                               tone_map_function=Tonemap.ST2094_40, gamut_mapping=Gamut.Clip, 
                               peak_detect=True, use_dovi=True, contrast_recovery=0.3)
clip2args = PlaceboTonemapOpts(source_colorspace=ColorSpace.HDR10, target_colorspace=ColorSpace.SDR, 
                               tone_map_function=Tonemap.ST2094_40, gamut_mapping=Gamut.Clip, 
                               peak_detect=True, use_dovi=False, contrast_recovery=0.3)
clip3args = PlaceboTonemapOpts(source_colorspace=ColorSpace.HDR10, target_colorspace=ColorSpace.SDR, 
                               tone_map_function=Tonemap.Spline, gamut_mapping=Gamut.Darken, 
                               peak_detect=True, use_dovi=False, contrast_recovery=0.3, dst_max=120)

clip1 = core.placebo.Tonemap(clip1, **clip1args.vsplacebo_dict())
clip2 = core.placebo.Tonemap(clip2, **clip2args.vsplacebo_dict())
clip3 = core.placebo.Tonemap(clip3, **clip3args.vsplacebo_dict())

# Retagging video to BT.709 after tonemapping
clip1 = core.std.SetFrameProps(clip1, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)
clip2 = core.std.SetFrameProps(clip2, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)
clip3 = core.std.SetFrameProps(clip3, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)

# Set color range (if needed)
clip1 = core.resize.Lanczos(clip1, format=vs.YUV444P16, range=0)
clip2 = core.resize.Lanczos(clip2, format=vs.YUV444P16, range=0)
clip3 = core.resize.Lanczos(clip3, format=vs.YUV444P16, range=1)

# Output clips for VSPreview
set_output(clip1, name=source1)
set_output(clip2, name=source2)
set_output(clip3, name=source3)
