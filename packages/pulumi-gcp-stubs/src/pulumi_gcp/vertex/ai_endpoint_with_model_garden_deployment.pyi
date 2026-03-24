

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AiEndpointWithModelGardenDeploymentArgs', 'AiEndpointWithModelGardenDeployment']
@pulumi.input_type
class AiEndpointWithModelGardenDeploymentArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], deploy_config: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentDeployConfigArgs]] = ..., endpoint_config: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentEndpointConfigArgs]] = ..., hugging_face_model_id: Optional[pulumi.Input[_builtins.str]] = ..., model_config: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentModelConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., publisher_model_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployConfig")
    def deploy_config(self) -> Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentDeployConfigArgs]]:
        
        ...
    
    @deploy_config.setter
    def deploy_config(self, value: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentDeployConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(self) -> Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentEndpointConfigArgs]]:
        
        ...
    
    @endpoint_config.setter
    def endpoint_config(self, value: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentEndpointConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="huggingFaceModelId")
    def hugging_face_model_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hugging_face_model_id.setter
    def hugging_face_model_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelConfig")
    def model_config(self) -> Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentModelConfigArgs]]:
        
        ...
    
    @model_config.setter
    def model_config(self, value: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentModelConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherModelName")
    def publisher_model_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher_model_name.setter
    def publisher_model_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AiEndpointWithModelGardenDeploymentState:
    def __init__(__self__, *, deploy_config: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentDeployConfigArgs]] = ..., deployed_model_display_name: Optional[pulumi.Input[_builtins.str]] = ..., deployed_model_id: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_config: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentEndpointConfigArgs]] = ..., hugging_face_model_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., model_config: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentModelConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., publisher_model_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployConfig")
    def deploy_config(self) -> Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentDeployConfigArgs]]:
        
        ...
    
    @deploy_config.setter
    def deploy_config(self, value: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentDeployConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedModelDisplayName")
    def deployed_model_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployed_model_display_name.setter
    def deployed_model_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedModelId")
    def deployed_model_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployed_model_id.setter
    def deployed_model_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(self) -> Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentEndpointConfigArgs]]:
        
        ...
    
    @endpoint_config.setter
    def endpoint_config(self, value: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentEndpointConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="huggingFaceModelId")
    def hugging_face_model_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hugging_face_model_id.setter
    def hugging_face_model_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelConfig")
    def model_config(self) -> Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentModelConfigArgs]]:
        
        ...
    
    @model_config.setter
    def model_config(self, value: Optional[pulumi.Input[AiEndpointWithModelGardenDeploymentModelConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherModelName")
    def publisher_model_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher_model_name.setter
    def publisher_model_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AiEndpointWithModelGardenDeployment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., deploy_config: Optional[pulumi.Input[Union[AiEndpointWithModelGardenDeploymentDeployConfigArgs, AiEndpointWithModelGardenDeploymentDeployConfigArgsDict]]] = ..., endpoint_config: Optional[pulumi.Input[Union[AiEndpointWithModelGardenDeploymentEndpointConfigArgs, AiEndpointWithModelGardenDeploymentEndpointConfigArgsDict]]] = ..., hugging_face_model_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., model_config: Optional[pulumi.Input[Union[AiEndpointWithModelGardenDeploymentModelConfigArgs, AiEndpointWithModelGardenDeploymentModelConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., publisher_model_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AiEndpointWithModelGardenDeploymentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., deploy_config: Optional[pulumi.Input[Union[AiEndpointWithModelGardenDeploymentDeployConfigArgs, AiEndpointWithModelGardenDeploymentDeployConfigArgsDict]]] = ..., deployed_model_display_name: Optional[pulumi.Input[_builtins.str]] = ..., deployed_model_id: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_config: Optional[pulumi.Input[Union[AiEndpointWithModelGardenDeploymentEndpointConfigArgs, AiEndpointWithModelGardenDeploymentEndpointConfigArgsDict]]] = ..., hugging_face_model_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., model_config: Optional[pulumi.Input[Union[AiEndpointWithModelGardenDeploymentModelConfigArgs, AiEndpointWithModelGardenDeploymentModelConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., publisher_model_name: Optional[pulumi.Input[_builtins.str]] = ...) -> AiEndpointWithModelGardenDeployment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployConfig")
    def deploy_config(self) -> pulumi.Output[Optional[outputs.AiEndpointWithModelGardenDeploymentDeployConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedModelDisplayName")
    def deployed_model_display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedModelId")
    def deployed_model_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(self) -> pulumi.Output[Optional[outputs.AiEndpointWithModelGardenDeploymentEndpointConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="huggingFaceModelId")
    def hugging_face_model_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelConfig")
    def model_config(self) -> pulumi.Output[Optional[outputs.AiEndpointWithModelGardenDeploymentModelConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherModelName")
    def publisher_model_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


