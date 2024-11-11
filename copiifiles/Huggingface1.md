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

TO use the model for inference, create teh image shape with random Gaussian noise. It should have a batch axis because the model can receive multiple random noises, a channel axis corresponsding to the number of input channels, and a sample_size axis for the height and width of the image:

For inference, pass the noisy image and a timestep to the model. The timestep indicates how noisy the input image is, with the more noise at the beginning and less at the end. This helps the model determine its position in the diffusion process, whether it is closer to the start or the end. Use teh sample method to get the model output.

Schedulers

Schedulers manage going from a noisy sample to a less noisy sample given the model output - in this case, it is the noisy_residual.

Diffusers is a toolbox for building diffusion systems. While the Diffusion Pipeline is a convenient way to get started with a pre-built diffusion system, you can also choose your own model and scheduler components separately to build a custom diffusion system.

For the quicktour, you'll instantiate the DPPMScheduler with its from_config() method:

Unlike a model, a scheduler does not have trainable weights and is parameter-free!

Some of the most important parameters are:

num_train_timestamps: the length of the denoising process or, in other words, the number of timesteps required to process random Gaussian noise into a data sample.

beta_schedule: the type of noise schedule to use for inference and training.

beta_start and beta_end: the start and end noise values for the noise schedule.

To predict a slightly less noisy image, pass the followign to the scheduler's step() method: model output, timestep, and current sample.

The less_noisy_sample can be passed to the next timestep where it'll get even less noisy! Let's bring it all together now and visualize the entire denoising process.

First, create a function that postprocesses and displays the denoised image as a PIL.Image.

To speed up the denoising process, move the input and model to a GPU: [code]

Now create a denoising loop that predicts the residual of the less noisy smaple, and computes the less noisy sample with the scheduler:

Next Steps

Hopefully, you generated some cool images with Diffusers in this quicktour! For your next steps, you can 

    Train or finetune a model to generate your own images in this training tutorial
    See official and community training or finetuning scripts for a variety of use cases.

    Learn more about loading, accessing, changing, and comparing schedulers in the Using different Schedulers guide.

    Explore prompt engineering, speed, and memory optimizations, and tips and tricks for generating higher-quality images with the Stable Diffusion guide.

    Dive deeper into speeding up Diffusers with guides on optimized PyTorch on a GPU, and inference guides for running Stable Diffusion on Apple Silicon (M1/M2) and ONNX Runtime.

https://huggingface.co/docs/diffusers/en/stable_diffusion#effective-and-efficient-diffusion:~:text=and%20efficient%20diffusion-,Effective%20and%20efficient%20diffusion,-Getting%20the%20DiffusionPipeline

Getting the DiffusionPipeline to generate images in a certain style or include what you want can be tricky. Often times, you have to run the DiffusionPipeline several times before you end up with an image you're happy with. But generating something out of nothing is a computationally intensive process, especially if you're running inference over and over again.

This is why it's important to get the most computational speed and memory (GPU vRAM) efficiency from the pipelien to reduce the time between inference cycles so you can iterate faster.

This tutorial walks you through how to generate faster and better with the DiffusionPipeline.

The example prompt you'll use is a portrait of an old warrior chief, but feel free to use your own prompt:

prompt = "portrait photo of an old warrior chief"

Speed

If you don't have access to a GPU, you can use one for free from a GPU provider like Colab!

One of the simplest ways to speed up  inference is to place the pipeline on a GPU the same way you would with any PyTorch module:

pipeline = pipeline.to("cuda")

To make sure you can use the same image and improve on it, use a Geneartor and set a speed for reproducability:

import torch

generator = torch.Generator("cuda").manual_seed(0)

Now you can generate an image:

image = pipeline(prompt, geneartor=generator).images[0]
image

This process took ~30 seconds on a T4 GPU (it might be faster if your allocated GPU is better than a T4). By Default, the DiffusionPipeline runs inference with full float32 precision for 50 inference steps. 

Let's start by loading the model in float16 and generate an image.

import torch

pipeline = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_safetensors=True)
pipeline = pipeline.to("cuda")
generator = torch.Generator("cuda").manual_seed(0)
image = pipeline(prompt, generator=generator).images[0]
image

This time, it took only ~11 seconds to generate the image, which is almost 3x faster than before!

We strongly suggest always running your pipelines in float16, and so far, we've rarely seen any degredation in ouput quality.

Another option is to reduce the number of inference steps. Choosing a more efficient scheduler could help decrease the number of steps without sacrificing output quality. You can find which schedulers are compatible with a different model in the DiffusionPipeline by calling the compatibles method:

pipeline.scheduler.compatibles

The Stable Diffusion model uses PNDMScheduler by default which usually requires ~50 inference steps, but more performant schedulers like DPMSolverMultistepScheduler require only ~20 or ~25 inference steps. Use the from_config() method to load a new scheduler:

from diffusers import DPMSolverMultistepScheduler

pipeline.scheduler = DPMSolverMultistepScheduler.from_config(pipeline.scheduler.config) 

Now set the num_inference_steps to 20:

generator = torch.Generator("cuda").manual_seed(0)
image = pipeline(prompt, generator=generator, num_inference_steps=20).images[0]
image

Great, you've managed to cut the inference time to just 4 seconds!

Memory

The other key to improving pipeline performance is consuming less memory, which indirectly implies more speed, since you're often trying to maximize the number of images generated per second. The easiest way to see how many images you can generate at once is to try different batch sizes until you get an OutOfMemoryError(OOM).

Create a function that'll generate a batch of images from a list of prompts and Generators. Make sure to assign each Generator a seed so you can reuse it if it prodcues a good result.

def get_inputs(batch_size=1):
    generator = [torch.Generator("cuda").manual_seed(i) for i in range(batch_size)]
    prompts = batch_size * [prompt]
    num_inference_steps = 20

    return {"prompt": prompts, "generator": generator, "num_inference_steps": num_inference_steps}

Start with batch_size=4 and see how much memory you've consumed:

from diffusers.utils import make_image_grid 

images = pipeline(**get_inputs(batch_size=4)).images
make_image_grid(images, 2,2)

Unelss you have a GPU with more vRAM, the code above probably returned an OOM error! Most of the memory is taken up by the cross-attention layers. Instead of running this operation in a batch, you can run it sequentially to save a significant amount of memory. All you have to do is configure the pipelient o use the enable_attention_slicing() function.

...

Better prompt engineering

The text prompt you use to generate an image is super important, so much so that it is called prompt engineering. Some considerations to keep during prompt engineering are:

    How is the image or similar images of the oen I want to generate stored on the internet?
    What additional detail can I give that steers the model towards teh style I want?

With this in mind, let's improve the prompt to include color and higher quality details:

prompt += ", tribal panther make up, blue on red, side profile, looking away, serious eyes"
prompt += " 50mm portrait photography, hard rim lighting photography--beta --ar 2:3  --beta --upbeta"

Generate a batch of images with the new prompt: images=pipeline(**getinputs(batch_size = 8)).images
make_images_grid(image, rows=2, cols=4)

Prety impressive! Let's tweak the second image - corresepondding to Geneartor with a seed of 1 - a bit more by adding some text about hte age of the subject.

prompts = [
    "portrait photo of the oldest warrior chief, tribal panther make up, blue on red, side profile, looking away, serious eyes 50mm portrait photography, hard rim lighting photography--beta --ar 2:3  --beta --upbeta",
    "portrait photo of an old warrior chief, tribal panther make up, blue on red, side profile, looking away, serious eyes 50mm portrait photography, hard rim lighting photography--beta --ar 2:3  --beta --upbeta",
    "portrait photo of a warrior chief, tribal panther make up, blue on red, side profile, looking away, serious eyes 50mm portrait photography, hard rim lighting photography--beta --ar 2:3  --beta --upbeta",
    "portrait photo of a young warrior chief, tribal panther make up, blue on red, side profile, looking away, serious eyes 50mm portrait photography, hard rim lighting photography--beta --ar 2:3  --beta --upbeta",
]

generator = [torch.Generator("cuda").manual_seed(1) for _ in range(len(prompts))]
images = pipeline(prompt=prompts, generator=generator, num_inference_steps=25).images
make_image_grid(images, 2, 2)

Next steps

In this tutorial, you learned how to optimize a DiffusionPipeline for computational and memory efficiency as well as improving the quality of generated outputs. If you're interested in making your pipeline even faster, take a look at the folowing resources: 

    Learn how PyTorch2.0 and torch.compile can yield 5-300% faster inference seped. On an A100 GPU, inference can be up to 50% faster!
    If you can't use PyTorch 2, we recommend you install xFormers. Its memory-efficient attention mechanism works great with PyTorch 1.13.1. for faster speed and reduced memroy consumption.
    Other optimization techniques, such as model offloading, are covered in this guide.

