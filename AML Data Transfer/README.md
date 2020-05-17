## Azure Machine Learning service - Transfer Data withing a Pipeline using DataTransferStep

![TransferDataStepImage](https://mlonazure.com/wp-content/uploads/2020/05/AML-Transfer-Data-1.jpg)

A sample for moving data from Azure Blob Storage to Azure SQL Database using an Existing Azure Data Factory. For a general walkthrough, see: [AML Product Team GitHub - MachineLearningNotebooks/aml-pipelines-data-transfer](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/intro-to-pipelines/aml-pipelines-data-transfer.ipynb)

### Data transfer currently supports following storage types:

| Data store | Supported as a source | Supported as a sink |
| --- | --- | --- |
| Azure Blob Storage | Yes | Yes |
| Azure Data Lake Storage Gen 1 | Yes | Yes |
| Azure Data Lake Storage Gen 2 | Yes | Yes |
| Azure SQL Database | Yes | Yes |
| Azure Database for PostgreSQL | Yes | Yes |
| Azure Database for MySQL | Yes | Yes |

## Major Steps

**Step 1** [01. Transfer Data Configuration.ipynb](http://www.microsoft.com) Cofigure necessary components to perform a Data Transfer in the next notebook

**Step 2** [02. Transfer Data.ipynb](http://www.microsoft.com) Transfer Data from Blob Storage to Azure SQL Database using an existing Azure Data Factory

### References Section

[Workspace](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace%28class%29?view=azure-ml-py)
Connect to your Azure Machine Learning service Workspace. Note that if you are using a Compute Instance the config file is already there for the Workspace you're within, otherwise you will need to create it.

[Datastore class](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.datastore%28class%29?view=azure-ml-py) Used to **register the blob storage and Azure SQL Database**. <br> In this example, the default blob storage that is provisioned when an Azure Learning service is provisioned. Note that the best practice is to keep your data in your own Azure Blob Storage or Azure Data Lake Gen2.

This classe allows you to register a number of Azure services to be used in your Pipelines including,

- Azure Blob Container
- Azure File Share
- Azure Data Lake
- Azure Data Lake Gen2
- Azure SQL Database
- Azure Database for PostgreSQL
- Databricks File System
- Azure Database for MySQL

[Experiment Class](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment%28class%29?view=azure-ml-py) Experimenation Tracking: Creates an Experiment which has Runs underneath it.

[DataFactoryCompute.attach_configuration](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.datafactory.datafactorycompute?view=azure-ml-py#attach-configuration-resource-group-none--factory-name-none--resource-id-none-) Provides configuration for an existing Azrue Data Factory

[ComputeTarget.attach](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.computetarget?view=azure-ml-py#attach-workspace--name--attach-configuration-) Attaches the existing Azure Data Factory as an "Attached Compute" under "Compute" in Studio

[DataReference Class](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.data_reference.datareference?view=azure-ml-py) Create a reference to the blob storage. 

[SqlDataReference Class](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.sql_data_reference.sqldatareference?view=azure-ml-py) Create a reference to a registered SQL Datastore

[datafactory module](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.datafactory?view=azure-ml-py) Datafactory module providing various Azure Data Factory operations.

[DataFactoryCompute Class](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.datafactory.datafactorycompute?view=azure-ml-py) Connect to an attached Azure  Data Factory that

[Pipeline Class](https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.pipeline.pipeline?view=azure-ml-py#publish-name-none--description-none--version-none--continue-on-step-failure-none-)

[DataTransferStep class](https://docs.microsoft.com/en-us/python/api/azureml-pipeline-steps/azureml.pipeline.steps.datatransferstep?view=azure-ml-py) Creates a DataTransferStep providing source and destination

### Further Explanation

Coming soon on [www.mlonazure.com](http://www.mlonazure.com)
