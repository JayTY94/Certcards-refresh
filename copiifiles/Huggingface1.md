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

Start by creating an instance of a DiffusionPipeline and specify which pipeline checkpoint you would like to download. You can use the DiffusionPipeline for any checkpoint stored on the HuggingFace Face Hub. In this quicktour, you'll load the stable-diffusion-v1-5 checkpoint for text-to-image generation.

For Stable Diffusion models, please carefully read the license first before running the model. Diffusers implements a safety_checker to prevent offensive or harmful content, but the model's improved image generation capabilities can still produce potentially harmful content.

Load the model with the from_pretrained() method:

from diffusers import DiffusionPipeline

pipeline = Diffusion Pipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", use_safetensors=True)

The DiffusionPipeline downloads and caches all modeling, tokenization, and scheduling components. You'll see that the Stable Diffusion pipeline is composed of UNet2DConditionModel and PNDMScheduler among other things:

(code)

We strongly recommend running the pipeline on a GPU because the mdoel consists of roughly 1.4 billion parameters. YOu can move the generator object to a GPU, just like you would in PyTorch:

(code), failed on my codespace, not going to worry about it for the moment.

Now you can pass a text prompt ot the pipeline to generate an image, and then acces the denoised image. By default, the imaege output is wrapped in a PIL.Image object.

```image = pipeline("An image of a squrrel in Picasso style").images[0]
image```

Save the image by calling save:

```image.save("image_of_squirrel_painting.png")```

Local pipeline

You can also use the pipeline locally. The only difference is you need to download the weights first:

```!git lfs install
!git clone https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5```

Then load the saved weights in to the pipeline: 

```pipeline = DiffusionPipeline.from_pretrained("./stable-diffusion-v1-5", use_safetensors=True)```

Swapping schedulers

Different schedulers come with different denoising speeds and quality trade-offs. The best way to find out which one works best for you is to try them out! One of the main features of Diffusers is to allow you to easily switch between schedulers. For example, to replace the default PNDMScheduler with the EulerDiscreteScheduler, load it with the from_config() method:

```from diffusers import EulerDiscreteScheduler

pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", use_safetensors=True)
pipeline.scheduler = EulerDiscreteScheduler.from_config(pipeline.scheduler.config)```

Try generating an image with the new scheduler and see if you notice a difference!

In the next section, you'll take a closer look at the components - the model and the scheduler - that make up the DiffusionPipeline and learn how to use these components to generate an image of a cat.

Models 
Most models take a noisy sample, and each timestep it predicts the noise residual (other models elarn to predict the previous sample directly or hte velcity or v-prediction), the difference between a less noisy image and the input image. You can mix and match models to create other diffusion systems.

Models are initiated with the from_pretrained() method which also locally caches the model weights so it is faster the next time you load the model. For the quicktour, you'll load the UNet2dModel, a basic and unconditional image generationmodel with a checkpoint trained on cat images:

```from diffusers import UNet2DModel

repo_id = "google/ddpm-cat-256"
model = UNet2DModel.from_pretrained(repo_id, use_safetensors=True)```

To access the model parameters, call model.config:

```model.config```

The model configuration is a frozen dictionary, which means those parameters can't be changed after the model is created. This is intentional and ensures that the parameters used to define the model architecture at the start remain the same, while other paramters can still be adjusted during inference.

Some of the most important parameters are:

sample_size the height and width dimension of the input sample.
in_channels: the number of input channels of the input sample.
down_block_types and up_block_types: the type of down- and upsampling blocks used to create teh UNet architecture.

block_out_channels: the number of output channels of the downsampling blocks; also used in reverse order for the number of input channels of hte upsampling blocks.

layers_per_block: the number of ResNet blocks present in each UNet block.

TO use the model for inference, create teh image shape with random Gaussian noise. It should have a batch axis because the model can receive multiple random noises, a channel axis corresponsding to the number of input channels