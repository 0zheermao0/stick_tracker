
stick_track - v1 2024-04-10 10:38am
==============================

This dataset was exported via roboflow.com on April 10, 2024 at 2:39 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 91 images.
Stick are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random rotation of between -15 and +15 degrees

The following transformations were applied to the bounding boxes of each image:
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise


