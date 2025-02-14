# VSPreview Comparison Script

## Overview
This script is designed to facilitate video quality comparisons using VapourSynth and VSPreview. It allows you to load multiple video sources, apply preprocessing such as cropping, scaling, tonemapping, and framerate adjustments, and output the results for easy evaluation.

## Prerequisites
Before using this script, ensure you have the following installed:

### Required Software
- [VapourSynth](https://vapoursynth.com/)
- [VSPreview](https://github.com/Irrational-Encoding-Wizardry/vspreview)
- Python (3.6 or later)

### Required Dependencies
To install the necessary VapourSynth plugins, run:
```sh
vsrepo.py install libp2p lsmas sub placebo vivtc
```

To install additional Python dependencies, run:
```sh
pip install git+https://github.com/OpusGang/awsmfunc.git
```

## Usage

### 1. Prepare Your Video Files
Ensure your video files are accessible and note their file paths.

### 2. Edit the Script
Modify `comp.py` to specify the correct file paths and adjust parameters as needed.

#### Set File Paths
```python
clip1 = core.lsmas.LWLibavSource(r"C:\Path\To\File1.mkv")
clip2 = core.lsmas.LWLibavSource(r"C:\Path\To\File2.mkv")
clip3 = core.lsmas.LWLibavSource(r"C:\Path\To\File3.mkv")
```

#### Adjust Frame Rate Settings (if necessary)
```python
clip1 = core.std.AssumeFPS(clip1, fpsnum=24000, fpsden=1001)
```

#### Enable Cropping (if needed)
```python
clip1 = core.std.Crop(clip1, left=240, right=240, top=0, bottom=0)
```

#### Apply Scaling (if required)
```python
clip1 = EwaLanczos.scale(clip1, 1920, 1080, sigmoid=True)
```

#### Enable Tonemapping for HDR/DV Content
```python
clip1 = core.placebo.Tonemap(clip1, **clip1args.vsplacebo_dict())
```

### 3. Run the Script
Open a terminal in the directory containing `comp.py` and execute:
```sh
vspreview comp.py
```

### 4. Navigate VSPreview
Use the following keybinds to navigate:
- **Left Arrow (`<-`)**: Move back frames
- **Right Arrow (`->`)**: Move forward frames
- **Number Keys (`1`, `2`, `3`)**: Switch between sources
- **Shift + S**: Take and save a screenshot
- **Ctrl + Space**: Mark frame number for semi-automatic comparisons

### 5. Upload to SlowPics
To upload automatically:
1. Click `Plugins` in VSPreview.
2. Select `SlowPics Comps`.
3. Fill out the form (Title, Random Frame Count, TMDB ID, etc.).
4. Click `Start Upload`.

## Troubleshooting
- Ensure `vsrepo.py` is executable.
- If `vspreview` does not start, check Python and VapourSynth installations.
- If frame sync issues occur, use `AssumeFPS` to match frame rates.
