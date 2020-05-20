---
layout     : default
---

# XN Industry Projects:

The MRI Segmentation Project and Surgery Planning project are XN projects sponsored by [Z-Imaging](http://zimaging.io/), a Harvard Innovation Labs sponsored startup. Below is our student at the Harvard Innovation Labs with CTO Raahil Sha.

<div><img class="XNImage" src="https://raw.githubusercontent.com/tipthederiver/Math-7243-2020/master/Projects/Z-Imaging%20Meeting.jpg"></div>
<div><img class="XNImage" src="https://raw.githubusercontent.com/tipthederiver/Math-7243-2020/master/Projects/Z-Imaging%20Meeting2.jpg"></div>

![Image](https://raw.githubusercontent.com/tipthederiver/Math-7243-2020/master/Projects/Z-Imaging%20Meeting.jpg)
![Image](https://raw.githubusercontent.com/tipthederiver/Math-7243-2020/master/Projects/Z-Imaging%20Meeting2.jpg)

## MRI Segmentation:

This project used the [OASIS1](https://www.oasis-brains.org/) dataset to perform automatic segmentation of the ventricles. Students used 3D slicer to construct a large dataset of 3D ventricular segmentations from volumetric MRI data. The group then constructed a 3D UNET that takes in a piece of MRI data and returns a 3D segmented volume. The main issues with this project were in data handling, as the data set has few members (100) but each data point (MRI) is 12 MB. Down-sampling, memory handling and a carefully constructed network were required to train a network capable of proper segmentation. 

This project is on going and the current source code can be found here on [the github page](https://github.com/tipthederiver/Math-7243-2020/tree/master/Segmentation).

## Surgery Planing for External Ventricular Drain:

In this project, students took a series of MRI's, segmented the skull and the ventricles, and simulated various kinds of obstructions. The students then constructed a stochastic sampling function that evaluated many possible surgery paths, picked the best of the sampled and paths, and then further optimized the path to construct a surgery path for EVD that minimally intersected with obstructions. 


## Getting Started Resource:

As stated before, we will all start by segmenting some MRI images. We will be using 3d Slicer and possibly Nvidia’s product. To get an idea of the flavor of this, take a look at the short tutorials here:
Information on Segmentation:
A reasonable first article on segmentation to skim:
https://www.hindawi.com/journals/cmmm/2015/450341/

Ventricular Segmentation Using 3D Slicer: [Demo 1](https://www.youtube.com/watch?v=cIpPSo9Y0Yo&t=92s
), [Demo 2](https://www.youtube.com/watch?v=cIpPSo9Y0Yo&t=92s), [Converting STL Files to Numpy Arrays](https://www.youtube.com/watch?v=ggPed6RvQno). 

Automatic Segmentation using Neural Networks: [U-Net Paper](https://arxiv.org/abs/1505.04597), [No New U-Net Paper](https://arxiv.org/abs/1809.10486).


A couple of articles on Surgery Planning:
[A pretty good overview of the general problem of surgery planing](https://www.ncbi.nlm.nih.gov/pubmed/17487658).
[A pretty good visual description of the issues around brain surgery](https://kclpure.kcl.ac.uk/portal/en/publications/stereoelectroencephalography-electrode-placement(8dc02cb6-4f2a-489a-9796-ffb6f592fbc7).html).

Both of these papers can be access through Northeastern’s Library.
