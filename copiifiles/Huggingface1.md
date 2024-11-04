https://huggingface.co/docs/diffusers/en/quicktour

Diffusion models are trained to denoise random Gaussian noise step-by-step to generate a sample of interest, such as an image or audio. This has sparked a tremendous amount of interested in generative AI, and you have probably seen examples of diffusion generted images on the internet. Diffusers is a library aimed at maknig diffusion models widely accessible to anyone.

Whether you're a developer or an everyday user, this quicktuor will introduce you to Diffusers and help you get up and generating quickly! There are three main components to the library to know about:

The DiffusionPipeline is a high-level end-to-end class designed to rapidly generate samples form pretrained diffusion models for inference.

Popular pretrained model architectures and models that can be used as building blocks for creating diffusion systems.

Many different schedulers - algorithms that control how noise is added for training, and how to generate denoised images during inference.