

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DeploymentArgs', 'Deployment']
@pulumi.input_type
class DeploymentArgs:
    def __init__(__self__, *, target: pulumi.Input[DeploymentTargetArgs], create_policy: Optional[pulumi.Input[_builtins.str]] = ..., delete_policy: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentLabelArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preview: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[DeploymentTargetArgs]:
        
        ...
    
    @target.setter
    def target(self, value: pulumi.Input[DeploymentTargetArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createPolicy")
    def create_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_policy.setter
    def create_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletePolicy")
    def delete_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_policy.setter
    def delete_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentLabelArgs]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @preview.setter
    def preview(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DeploymentState:
    def __init__(__self__, *, create_policy: Optional[pulumi.Input[_builtins.str]] = ..., delete_policy: Optional[pulumi.Input[_builtins.str]] = ..., deployment_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentLabelArgs]]]] = ..., manifest: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preview: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[DeploymentTargetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createPolicy")
    def create_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_policy.setter
    def create_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletePolicy")
    def delete_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_policy.setter
    def delete_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentLabelArgs]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def manifest(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @manifest.setter
    def manifest(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @preview.setter
    def preview(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[DeploymentTargetArgs]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[DeploymentTargetArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:deploymentmanager/deployment:Deployment")
class Deployment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., create_policy: Optional[pulumi.Input[_builtins.str]] = ..., delete_policy: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentLabelArgs, DeploymentLabelArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preview: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[Union[DeploymentTargetArgs, DeploymentTargetArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeploymentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_policy: Optional[pulumi.Input[_builtins.str]] = ..., delete_policy: Optional[pulumi.Input[_builtins.str]] = ..., deployment_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentLabelArgs, DeploymentLabelArgsDict]]]]] = ..., manifest: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., preview: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[Union[DeploymentTargetArgs, DeploymentTargetArgsDict]]] = ...) -> Deployment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createPolicy")
    def create_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletePolicy")
    def delete_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[outputs.DeploymentLabel]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def manifest(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preview(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[outputs.DeploymentTarget]:
        
        ...
    


