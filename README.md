# VSPreview Comparison Script

This script is designed for advanced video quality comparisons using VapourSynth and VSPreview. It enables users to load multiple video sources, apply preprocessing techniques such as cropping, scaling, tonemapping, and frame rate adjustments, and analyze the output efficiently.

## Prerequisites

Before executing the script, ensure that the necessary software and dependencies are installed.

### Required Software

- [VapourSynth](https://github.com/vapoursynth/vapoursynth)
- [VSPreview](https://github.com/Irrational-Encoding-Wizardry/vs-preview)
- Python (3.12 or later)

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

### Step 1: Prepare Video Files

Ensure the video files are accessible and note their file paths.

### Step 2: Configure the Script

Modify `comp.py` to specify file paths and adjust processing parameters as needed.

#### **Defining File Paths**

Replace placeholders with actual file locations:

```python
clip1 = core.lsmas.LWLibavSource(r"C:\Path\To\File1.mkv")
clip2 = core.lsmas.LWLibavSource(r"C:\Path\To\File2.mkv")
clip3 = core.lsmas.LWLibavSource(r"C:\Path\To\File3.mkv")
```

#### **Adjusting the Number of Clips**

To add a fourth clip:

```python
clip4 = core.lsmas.LWLibavSource(r"C:\Path\To\File4.mkv")
```

Modify processing steps accordingly. To remove a clip, comment out or delete its corresponding lines.

#### **Modifying Frame Rate**

To specify a frame rate conversion, adjust the `AssumeFPS` values:

```python
clip1 = core.std.AssumeFPS(clip1, fpsnum=24000, fpsden=1001)
clip2 = core.std.AssumeFPS(clip2, fpsnum=25000, fpsden=1000)
clip3 = core.std.AssumeFPS(clip3, fpsnum=24000, fpsden=1000)
```

### Step 3: Enabling or Disabling Processing Features

To disable a processing feature for a specific clip, comment out the corresponding line:

- **Disable interlacing fix for clip1:**

```python
# clip1 = core.std.SetFieldBased(clip1, 0)
```

- **Disable cropping for clip2:**

```python
# clip2 = core.std.Crop(clip2, left=240, right=240, top=0, bottom=0)
```

- **Disable scaling for clip3:**

```python
# clip3 = EwaLanczos.scale(clip3, 1920, 1080, sigmoid=True)
```

- **Disable tonemapping for clip1:**

```python
# clip1 = core.placebo.Tonemap(clip1, **clip1args.vsplacebo_dict())
```

### Step 4: Executing the Script

Open a terminal in the directory containing `comp.py` and run:

```sh
vspreview comp.py
```

### Step 5: Navigating VSPreview

Use the following keybindings for efficient navigation:

- **Left Arrow (<-)**: Move back frames
- **Right Arrow (->)**: Move forward frames
- **Number Keys (1, 2, 3, ...)**: Switch between sources
- **Shift + S**: Capture and save a screenshot
- **Ctrl + Space**: Mark frame number for automated comparisons

### Step 6: Uploading to SlowPics

To upload automatically:

1. Click **Plugins** in VSPreview.
2. Select **SlowPics Comps**.
3. Complete the form (Title, Random Frame Count, TMDB ID, etc.).
4. Click **Start Upload**.

For uploading to [Slowpoke Pics](https://slow.pics) under a personal account, configure authentication:

1. Navigate to **Plugins -> SlowPics Comps -> Settings**.
2. Enter the **Username** and **Password** fields.
3. Click **Login**.
4. Click **Start Upload**.

## Customization Examples

### **Example: Comparing SDR and HDR Clips**

- **Clip 1 (SDR):** No tonemapping applied.
- **Clip 2 (SDR):** No tonemapping applied.
- **Clip 3 (HDR):** Tonemapping applied using `Spline`.

```python
# clip1 = core.placebo.Tonemap(clip1, **clip1args.vsplacebo_dict())  # Tonemapping disabled for SDR
# clip2 = core.placebo.Tonemap(clip2, **clip2args.vsplacebo_dict())  # Tonemapping disabled for SDR
clip3 = core.placebo.Tonemap(clip3, **clip3args.vsplacebo_dict())  # Apply tonemapping for HDR clip
```

### **Example: Upscaling Clips to 4K**

```python
clip1 = EwaLanczos.scale(clip1, 3840, 2160, sigmoid=True)
clip2 = EwaLanczos.scale(clip2, 3840, 2160, sigmoid=True)
clip3 = EwaLanczos.scale(clip3, 3840, 2160, sigmoid=True)
```

