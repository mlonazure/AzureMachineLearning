import azureml.core
from azureml.core import Workspace, Datastore, Dataset, Experiment, Run, Model
import argparse

print('Register Model file started')

parser = argparse.ArgumentParser()
parser.add_argument("--model_path")
parser.add_argument("--model_name")
parser.add_argument("--model_description")
args = parser.parse_args()

print('arguments parsed')

modelPath = args.model_path
modelName = args.model_name
modelDescription = args.model_description

print('Model Path: ', modelPath)
print('Model Name: ', modelName)
print('Model Description: ', modelDescription)

print('getting run context')
run_context = Run.get_context()
run_context.log('Author','Sam was here!')

ws = run_context.experiment.workspace

print('Model Registeration began')

Model.register(workspace = ws,
               model_path = modelPath, 
               model_name = modelName,
               tags=None,
               properties=None,
               description=modelDescription,
               datasets=None,
               model_framework=None,
               model_framework_version=None,
               child_paths=None,
               sample_input_dataset=None,
               sample_output_dataset=None,
               resource_configuration=None)


print('Model Registeration completed')