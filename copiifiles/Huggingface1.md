https://huggingface.co/docs/diffusers/en/quicktour

Diffusion models are trained to denoise random Gaussian noise step-by-step to generate a sample of interest, such as an image or audio. This has sparked a tremendous amount of interested in generative AI, and you have probably seen examples of diffusion generted images on the internet. Diffusers is a library aimed at maknig diffusion models widely accessible to anyone.

Whether you're a developer or an everyday user, this quicktuor will introduce you to Diffusers and help you get up and generating quickly! There are three main components to the library to know about:

The DiffusionPipeline is a high-level end-to-end class designed to rapidly generate samples form pretrained diffusion models for inference.

Popular pretrained model architectures and models that can be used as building blocks for creating diffusion systems.

Many different schedulers - algorithms that control how noise is added for training, and how to generate denoised images during inference.

The quicktuor will show you how to use the DiffusionPipelien for inference, and then walk you through ow to combine a model and a scheduler to replicate what's happening inside the DiffusionPipeline.

The quicktuor is a simplified version of hte introductory Diffusers notebook to help you get started quickly. If you want to learn more about Diffusers' goal, design philosophy, and additional details about its core API, check out the notebook!

Before you begin, make sure you have all the necessary libraries installed:

pip install --upgrade diffusers accelerate teransformers

Accellerate speeds up model loading for inference and training.

Transformers is required to run the most popular diffusion models, such as Stable Diffusion

DiffusionPipeline

The DiffusionPipeline is the easiest way to use a pretrained diffusion system for inference. It is an end-to-end system containing the model and the scheduler. You can use the DiffusionPipeline out-of-the-box for many tasks. Take a look at the table below for some supported tasks, and for a complete list of supported tasks, check out the Diffusers summary table.

Unconditional Image Generation: Generate an image from Gaussian noise
    Pipeline: unconditional_image_generation 
Text-Guided Image Generation: Generate an image given a text prompt
    Pipeline: conditional_image_generation
Text-Guided Image-to-Image Translation: Adapt an image guided by a text prompt
    Pipeline: img2img
Text-Guided Image-Inpainting: Fill the masked part of an image given the image, the mask, and a text prompt
    Pipeline: inpaint
Text-Guided Depth-to-Image Translation: adapt parts of an image guided by a text prompt while preserving structure via depth estimation
    pipeline: depth2img

Start by creating an instance of a DiffusionPipeline and specify which pipeline checkpoint you would like to download.