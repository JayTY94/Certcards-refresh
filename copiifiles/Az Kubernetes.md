https://learn.microsoft.com/en-us/azure/aks/what-is-aks
What is Azure Kubernetes Service (AKS)?

Azure Kubernetes Service (AKS) is a managed Kubernetes service that you can use to deploy and manage containerized applications. You need minimal container orchestration expertise to use AKS. AKS reduces the complexity and operational overhead of managing Kubernetes by offloading much of that responsibility to Azure. AKS is an ideal platform for deploying and managing containerized applications that require high availability, scalability, and portability, and for deploying applications to multiple regions, using open-source tools, and integrating with existing DevOps tools.

This article is intended for platform administrators for developers who are looking for scalable, automated, managed Kubernetes solution.

Overview of AKS

AKS reduces the complexity and opeartional overhead of managing Kubernetes by shifting that responsibilty to Azure. When you create an AKS cluster, Azure automatically creates and configures a control pane for you at no cost. The Azure platform manages the AKS control pane, which is responsible for the Kubernetes objects and worker nodes that you deploy to run your applications. Azure takes care of critical operations like health monitoring an maintenance, and you only pay for the AKS nodes that run your applications.

Note:

AKS is CNCF-certified and is compliant with SOC, ISO, PCI DSS, and HIPAA. For more information, see Microsoft Azure compliance overview.

Container solutions in Azure

Azure offers a range of container solutions designed to accommodate various workfloads, architectures, and business needs

Container solution: Resource type
Azure Kubernetes Service: Managed Kubernetes
Azure Red Hat OpenShift: Managed Kubernetes
Azure Arc-enabled Kubernetes: Unmanaged Kubernetes
Azure Container Instance: Managed Docker container instances.

...
https://learn.microsoft.com/en-us/azure/architecture/guide/choose-azure-container-service

Web App for Containers is a feature of Azure App Service, a fully managed service for hosting HTTP-based web apps with built-in infrastructure maintenance, security patching, scaling, and diagnostic tooling. For more information, see App Service documentation.

For a complete list of all Azure container services, see the container services product category page.

Service model considerations

The service model provides the broadest insight into the level of flexibility and control that any Azure container service provides, in exchange for its overall simplicity and ease of use.

For a general introduction into the terminology and concepts around service models, including infrastructure as a service (IaaS) and platform as a service (PaaS) see Shared responsibility in the cloud.

Comparing the service models of Azure Container solutions

...

Operational considerations
Although AKS offers the most customization, it demands greater operational input. In contrast, PaaS solutions like Container Apps and Web App for Containers let Azure handle tasks like OS updates. Scalability and Hardware SKU flexibility are crucial. AKS provides flexible hardware options, whereas Container Apps and Weba App for Containers provide set configurations. Application scalability in AKS is the sole responsibility of the customer. Container Apps and Web App for Containers offer more streamlined approaches.

Reliability condsiderations

Web App for Containers and Container Apps health probe configurations are more streamlined than those of AKS, given that they use the familiar Amazon Resource Manager API. AKS requires the use of the Kubernetes API. It also requires you to take on the additional responsibility of managing Kubernetes node pool scalability and availability in order to properly schedule application instances. These requirements result in additional overhead for AKS.

Moreover, SLAs for Container Apps and Web App for Containers are more straightforward than those of AKS, for which the control plane and node pools each have their own SLAs and need to be compounded accordingly. All services offer zone redundancy in datacenters that offer it.

After reviewing the preceding considerations, you still might not have found the perfect fit. That's perfectly normal.

Evaluating tradeoffs

Choosing a cloud service isn't a straightforward exercise. Given the complexity of cloud computing, the collaboration between many teams, and resource constraints involving people, budgets, and time, every solution has tradeoffs.

Be aware that, for any given workload

...

https://learn.microsoft.com/en-us/training/modules/intro-to-docker-containers/1-introduction

Introduction

Teams today must release apps quickly to attract and keep business. This requirement forces software development and support teams to always look at solutions that save time and reduce costs. An ideal solution reduces the time spent on creating and configuring deployment environments and simplifies the software deployment process.

The idea of software containerization technology as a time-saving and cost-reduction solution is popular. One of containerization's strengths is that you don't have to configure hardware and spend time installing operating systems and software to host a deployment. Containers are isolated from each other, and multiple containers can run on the same hardware. This configuration helps us to use hardware more efficiently and can help improve our applications' security.

Suppose you work for an online clothing retailer that's planning to develop several internal apps. Your team develops and tests all applications on-premises, then deploys them to Azure for pre-production testinga nd final production hosting.

...

https://learn.microsoft.com/en-us/training/modules/intro-to-docker-containers/3-how-docker-images-work

What is the host OS?

The host OS is the OS on which the Docker engine runs. Docker containers running on Linux share the host OS kernel, and don't require a container OS as long as teh binary can access the OS kernel directly. 

However, Windows containers need a container OS. The container depends on the OS kernel to manage services such as the file system, network management, process scheduling, and memory management.

What is the container OS?

The container OS is the OS that's part of the packaged image. We have the flexibility to include different versions of Linux or Windows operating systems in a container. This flexibility allows us to access specific OS features or install additional software our applications might use.

The container OS is isolated from the host OS, and it's the environment in which we deploy and run our application.

...

How to manage Docker images

Docker images are large files that are initially stored on your PC, and we need tools to manage these files.

The Docker CLI and Docker Desktop allow us to manage images created by building, listing, removing, and running them. We manage Docker images by using teh docker client. The client doesn't execute the commands directly, and sends all queries to teh dockerd daemon.

We aren't gonig to cover all the client commands and command flags here, but we'll look at some of the most used commands. The Learn more section in this module's Summary unit includes links to Docker documentation, which covers all commands and command flags in detail.

How to build an image.

We use the docker build command to build Docker images. Let's assume we use the Dockerfile definition from earler to build an image. Here's an example that shows the build command:

docker build -t temp-ubuntu

...

https://learn.microsoft.com/en-us/training/modules/intro-to-docker-containers/4-how-docker-containers-work

Earlier, you discovered the container becomes the unit you'll use to distribute your apps. You also learned the container is in a standardized format both yoru developer and operation teams use.

In this example, you're developing an order-tracking portal for your company's various outlets to use. With the Docker image built, your operations team is now responsible for deploying, rolling out updates, and managing your order tracking portal.

In the previous unit, you looked at how a Docker image is built. Here, you'll look a bit at a Docker container's lifecycle and how to manage contianers. You'll also learn about configuring data storage and the network options for your containers.

How to manage Docker containers.

A Docker container has a lifecycle that you can use to manage and track the state of a container.

To place a container in the run state, you use the run command. You can also restart a container that is already running. When restarting a container, the container receives a termination signal to enable any running processes to shut down gracefully before the container's kernel terminates.

A container is considered in a running state until it's either paused, stopped, or killed. A container, however, can also exit from the running state by itself.

...

Docker container network configuration

The default Docker network configuration allows for isolating containers on the Docker host. This feature allows you to build and configure apps that can communicate securely with each other.

Docker provides different network settings for Linux and Windows.

For linux, there are six preconfigured network options:
    Bridget
    Host
    Overlay
    IPvLan
    MACvLan
    None

For Windows, there are six preconfigured network options:
    NAT
    Transparent
    Overlay
    L2Bridge
    L2Tunnel
    None

You can choose which of these network configurations to apply to your container depending on its network requirements.

What is the bridge network?

The bridge network is the default configuration applied to containers when launched without specifying any other network configuration. This network has an internal, private network used by the container, and it isolates teh container network from the Docker host network.

Each container in the bridge network is assigned an IP address and a subnet mask, with the hostname defaulting to the container name. Containers connected to the default .

...

https://learn.microsoft.com/en-us/training/modules/intro-to-docker-containers/5-when-use-docker-containers

...

Application delivery

With Docker, the container becomes the unit we use to distribute applications. This concept ensures that we have a standardized container format both our developer and operations teams use. Our developers can focus on developing software, and the operations team can focus on deploying and managing software.

We can use the container in every step of our deployment system once our development team releases a build of our application. Containers are ideal for continuous integration, and speed up the time from build to production.

Managing hosting environments

We configure our application's environment internally to the container. This containment provides flexibility for our operations team to manage hte application's environment much closer. Our team can monitor OS updates, apply security patches once, and roll out he updated container as needed.

Our team can also manage which applications to install, update, and remove without affecting other containers. Each container is isolated and has its resource limits assinged separately from other containers.

Cloud deployments

...

https://learn.microsoft.com/en-us/training/modules/intro-to-containers/1-introduction
Introduction

Rapid deployment is the key to business agility. Modern organizations must be able to release apps quickly to attract and retain business. Containerization saves time and reduces costs. You don't have to configure hardware and spend time installing operating systems and software to host a deployment. Multiple apps can run in their isolated containers on the same hardware. You can scale out quickly by starting more instances of containers. The images that run in containers are extensible; you can start with a working base image and alyer more functionality on top to create a new image.

Suppose you work for an online clothing retailer that's planning to deploy a handful of internal apps, but it hasn't yet decided how to host them. You're looking for maximum compatibility, and the apps could be hosted on-premises, in Azure, or in another cloud provider. Some fo teh apps might share IaaS infrastructure. In these cases, the company requires the apps to be isolated from each other. Apps can share the hardware resources, but an app shouldn't be able to interfere

...

You use the docker pull command with the image name to retrieve an image. By default, Docker will download the image tagged latest from that repository on Docker Hub if you specify only the repository name. Keep in mind htat you can modify the command to pull different tags and from different repositories. This example fetches the image with the tag aspnetapp from mcr.microsoft.com/dotnet/samples:aspnetapp repository. This image contains a simple ASP.NET Core web app.

Note
The examples in this unit are intended to show the syntax of various Docker commands. You don't need to run these commands while reading this unit. The exercises that follow this unit will guide you through working with Docker Directly.

docker pull mcr.microsoft.com/dotnet/samples:aspnetapp 

When you fetch an image, Docker stores it locally and makes it available for running containers. You can view the images in your local repository with the docker image list command.

docker image list

The output looks like the following example:
REPOSITORY TAG IMAGE ID CREATED SIZE
mcr.microsoft.com/dotnet/samples   aspnetapp           6e2737d83726        6 days ago          263MB

You can use the image name ID to reference the image in many other Docker commands.

Run a Docker container

Use the docker run command to start a container. Specify the image to run with its name or ID. If you haven't run docker pull already, Docker will do it for you.

docker run mcr.microsoft.com/dotnet/samples:aspnetapp

In this example, the command responds with teh following message:
warn: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[35]
 No XML encryptor configured. Key {d8e1e1ea-126a-4383-add9-d9ab0b56520d} may be persisted to storage in unencrypted form.
Hosting environment: Production
Content root path: /app
Now listening on: http://[::]:80
Application started. Press Ctrl+C to shut down.

This image contains a web app, so it's now listening for requests to arrive on HTTP port 80. However, if you open a web browser and navigate to http://localhost:80, you won't see the app.

By default, Docker doesn't allow inbound network requests to reach your container. YOu need to tell Docker

...

https://learn.microsoft.com/en-us/training/modules/intro-to-containers/3-exercise-deploy-docker-image-locally

Exercise - Retrieve an existing Docker image and deploy it locally

https://learn.microsoft.com/en-us/training/modules/intro-to-containers/4-create-custom-docker-image

Customize a Docker image to run your own web app

Docker Hub is an excellent source of images to get you started building your own containerized apps. You can download an image that provides the basic functionality you require, then layer your own application on top of it to create a new custom image. You can automate the steps for this process by writing a Dockerfile.

In the online clothing store scenario, the company decided that Docker is the way forward. The next step is to determine the best way to containerize your web applications. The company plans to build many of the apps using ASP.NET Core. You've noticed that Docker Hub contains a base image that includes this framework. As a proof of concept, you want to start with this base image and add the code for one of the web apps to create a new custom image. yoU also want this process to be easily repeatable, so it can bea utomated whenever you release a new version of the web app.

In this unit, you'll learn how to create a custom Docker image and how you can automate the process by writing a Dockerfile.

Create a custom image with a Dockerfile

To create a Docker Image containing your application, you typically begin by identifying a base image, to which you add fiels and configuration information. The process of identifying a suitable base image usually starts with an image search on Docker Hub. You want an image that already contains an application framework and all the utilities and tools of a Linux distribution, like Ubuntu or Alpine. For rexample, 

...

Command - Action

From - Downloads the specified image and creates a new container based on this image
WORKDIR - Sets the current working directory in the contianer; used by subsequent commands 
COPY - Copies files from the host computer to the container. The first argument (myapp_code) is a file or folder on the host computer. The second argument (.) specifies the name of the file or folder to act as the destination in the container. In this case, the destination is the current working directory (/app).
RUN - Executes a command in the container. Arguments to the RUN command are command-line like commands.
EXPOSE - Creates a configuration in the new image that specifies which ports to open when the container runs. If the container is running a web ap, it's common to EXPOSE port 80
ENTRYPOINT - Specifies the operation the container should run when it starts. In this example, it runs the newly built app. You specify the command you want to run and each of its arguments as a string array.

By convention, applications meant to be packaged as Docker images typically have a Dockerfile located in teh root of their sourcecode, and it's almost always named Dockerfile.

The docker build command

...

https://learn.microsoft.com/en-us/training/modules/intro-to-containers/5-exercise-create-custom-docker-image

A Dockerfile contains the steps for building a custom Docker image.

You decide to deploy one of your organization's web apps using Docker. You select a simple web app that implements a web API for a hotel reservations website. The web API exposes HTTP POST and GET operations that create and retrieve customers' bookings.

Note In this version of the web app, the bookings aren't actually persisted, and queries return dummy data.

In this exercise, you'll create a Dockerfile for an app that doesn't have one. Then, you'll build the image and run it locally.

Create a Dockerfile for the web app

1. If it's not already running, start Docker on your computer.

2. In a command prompt window on your local computer, run the following command to download the source code for the web app.

[code]

3. Enter the following command to open the src directory 

cd mslearn-hote...

2. Run the following command to verify that the image has been created and stored in the local registry:

docker image list

The image will have the name reservationsystem. You'll also have an image named microsoft/dotnet.

Test the web app

1. Enter the following code to run a container using the reservationsystem imiage. Docker will return a lengthy string of hex digits. The container runs in the background without any UE. Port 80 in the container is mapped to port 8080 on the host machine. The container is named reservations.

2. Start a web browser and navigate to http://localhost:8080/api/reservations/1. You should see a JSON object containing the data for reservation number 1 similar to the following output:

Replace the "1" at the end of the localhost URL with a different reservation number, like 2 or 20, to view the corresponding reservation details.

3. Run the following command to view the container's status:

docker ps -a

...

https://learn.microsoft.com/en-us/training/modules/intro-to-containers/6-deploy-docker-image-to-container-instance

...

Different SKUs provide varying levels of scalability and storage

Azure Container Registry repositories are private, meaning they don't support unauthenticated access. To pull images from an Azure Container Registry repository, use the docker login command and specify the URL of the login server for the registry. The login server URL for a registry in Azure Container Registry has the form <registry_name>.azurecr.io

docker login myregistry.azurecr.io

Docker login will prompt you for a username and password. To find this information, go to the Azure portal and look up the access keys for the registry or run the following command.

az acr credential show --name myregistry --resource-group mygroup

You push an image from your local computer to a Docker registry by using the docker push command. Before you push an image, you must create an alias for the image that specifies the repository and tag that the Docker registry creates.