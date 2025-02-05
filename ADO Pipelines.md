What keyword is used to define multiple steps that should run in parallel in Azure DevOps YAML pipelines?
Answer: matrix

How do you run a pipeline on a self-hosted agent in Azure DevOps?
Answer: pool: self-hosted

What is the purpose of the 'checkout' step in an Azure DevOps YAML pipeline?
Answer: It checks out the source code from the repository for use in the pipeline.

What does the 'variables' keyword do in a YAML pipeline?
Answer: It declares the variables that can be used throughout the pipeline.

What is the default working directory for a pipeline job in Azure DevOps?
Answer: $(Build.SourcesDirectory)

How do you add a manual approval gate before a pipeline proceeds to the next stage?
Answer: Set a ApprovalRequired flag on the pipeline's stages.

How do you specify a deployment environment like 'staging' or 'production' in a YAML pipeline?
Answer: Use the environment keyword, e.g., environment: 'staging'.

What does the 'trigger' keyword do in an Azure DevOps YAML pipeline?
Answer: Defines the branches or events that will cause the pipeline to run, such as a commit to a specific branch.

You can now use or save these flashcards in plain text format. Let me know if you need anything else!




You said:
Can you do more flashcards? I know we went over more here.
ChatGPT said:
ChatGPT
Absolutely! Here are more flashcards based on the concepts we've discussed in this conversation:

Azure DevOps Flashcards

What is the main purpose of a YAML file in Azure DevOps pipelines?
Answer: To define and configure pipeline processes, including steps, tasks, and environments.

In an Azure DevOps pipeline, which YAML syntax would you use to reference a variable?
Answer: $(variable_name)

Which of the following stages is NOT typically part of a Continuous Integration (CI) pipeline in Azure DevOps?
Answer: Deploy

What is the default trigger for a YAML-based pipeline in Azure DevOps?
Answer: A trigger based on code changes in a Git repository.

Which YAML element in an Azure DevOps pipeline defines the steps or tasks to be executed?
Answer: steps

How can you specify which agent pool should be used in a YAML pipeline file?
Answer: pool: <agent_pool_name>

What is the purpose of the dependsOn keyword in Azure DevOps YAML pipelines?
Answer: It specifies the order in which stages or jobs will execute.

In Azure DevOps, what command is used to run a pipeline manually from the Azure DevOps portal?
Answer: "Run pipeline" button in the Azure DevOps portal.

In Azure DevOps YAML pipelines, which keyword is used to define multiple steps that should run in parallel?
Answer: matrix

How do you run a pipeline on a self-hosted agent in Azure DevOps?
Answer: pool: self-hosted

What is the purpose of the checkout step in an Azure DevOps YAML pipeline?
Answer: It checks out the source code from the repository for use in the pipeline.

What does the variables keyword do in a YAML pipeline?
Answer: It declares the variables that can be used throughout the pipeline.

What is the default working directory for a pipeline job in Azure DevOps?
Answer: $(Build.SourcesDirectory)

How do you add a manual approval gate before a pipeline proceeds to the next stage in Azure DevOps?
Answer: Set a ApprovalRequired flag on the pipeline's stages.

How do you specify a deployment environment like 'staging' or 'production' in a YAML pipeline?
Answer: Use the environment keyword, e.g., environment: 'staging'.

What does the trigger keyword do in an Azure DevOps YAML pipeline?
Answer: It defines the branches or events that will cause the pipeline to run, such as a commit to a specific branch.

What does the jobs keyword in Azure DevOps YAML define?
Answer: It defines a set of jobs that run in the pipeline. Each job can contain steps, and jobs can be executed in parallel or sequentially based on dependencies.

How do you specify a condition for a job or stage to run in an Azure DevOps YAML pipeline?
Answer: You use the condition keyword, such as condition: succeeded() to define when a job should run based on the status of previous jobs.

How do you cache dependencies in Azure DevOps pipelines to speed up builds?
Answer: Use the cache task in the YAML file to store and reuse files between pipeline runs. This can help speed up build times by caching dependencies.

What is the purpose of the trigger: none keyword in an Azure DevOps YAML pipeline?
Answer: It disables automatic triggers, meaning the pipeline will not run automatically on code changes. This is useful for manual execution or scheduled runs.

In Azure DevOps, what is the use of the strategy keyword in a pipeline matrix?
Answer: The strategy keyword allows you to define different combinations of variables or configurations for matrix jobs, enabling parallel execution with different environments or settings.

What does the resources keyword define in a YAML pipeline?
Answer: The resources keyword allows you to define external resources such as repositories, containers, or pipelines that a pipeline will use or depend on.

How can you pass secrets securely in Azure DevOps YAML pipelines?
Answer: You pass secrets using pipeline variables marked as secret in Azure DevOps. They are referenced in the YAML file as $(secret_variable) but are masked and not exposed in logs.

How can you trigger a pipeline based on a Git tag in Azure DevOps?
Answer: You use the trigger keyword with the tags sub-keyword to specify that the pipeline should trigger when a Git tag is pushed.

Example:

yaml
Copy
trigger:
  tags:
    include:
      - v*
What is a Deployment Pool in Azure DevOps?
Answer: A Deployment Pool is a set of environments where deployments occur. You can configure and target specific deployment pools for releases to ensure the proper deployment environment is used.

How do you use stages with dependencies in Azure DevOps YAML pipelines?
Answer: You can define dependsOn between stages to specify the execution order. Stages will run sequentially based on the dependencies defined, ensuring that one stage only runs after another has completed.