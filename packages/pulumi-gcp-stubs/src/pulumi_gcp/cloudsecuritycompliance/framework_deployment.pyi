

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
__all__ = ['FrameworkDeploymentArgs', 'FrameworkDeployment']
@pulumi.input_type
class FrameworkDeploymentArgs:
    def __init__(__self__, *, cloud_control_metadatas: pulumi.Input[Sequence[pulumi.Input[FrameworkDeploymentCloudControlMetadataArgs]]], framework: pulumi.Input[FrameworkDeploymentFrameworkArgs], framework_deployment_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], organization: pulumi.Input[_builtins.str], target_resource_config: pulumi.Input[FrameworkDeploymentTargetResourceConfigArgs], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudControlMetadatas")
    def cloud_control_metadatas(self) -> pulumi.Input[Sequence[pulumi.Input[FrameworkDeploymentCloudControlMetadataArgs]]]:
        
        ...
    
    @cloud_control_metadatas.setter
    def cloud_control_metadatas(self, value: pulumi.Input[Sequence[pulumi.Input[FrameworkDeploymentCloudControlMetadataArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def framework(self) -> pulumi.Input[FrameworkDeploymentFrameworkArgs]:
        
        ...
    
    @framework.setter
    def framework(self, value: pulumi.Input[FrameworkDeploymentFrameworkArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="frameworkDeploymentId")
    def framework_deployment_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @framework_deployment_id.setter
    def framework_deployment_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @organization.setter
    def organization(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceConfig")
    def target_resource_config(self) -> pulumi.Input[FrameworkDeploymentTargetResourceConfigArgs]:
        
        ...
    
    @target_resource_config.setter
    def target_resource_config(self, value: pulumi.Input[FrameworkDeploymentTargetResourceConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FrameworkDeploymentState:
    def __init__(__self__, *, cloud_control_deployment_references: Optional[pulumi.Input[Sequence[pulumi.Input[FrameworkDeploymentCloudControlDeploymentReferenceArgs]]]] = ..., cloud_control_metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[FrameworkDeploymentCloudControlMetadataArgs]]]] = ..., computed_target_resource: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deployment_state: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., framework: Optional[pulumi.Input[FrameworkDeploymentFrameworkArgs]] = ..., framework_deployment_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., target_resource_config: Optional[pulumi.Input[FrameworkDeploymentTargetResourceConfigArgs]] = ..., target_resource_display_name: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudControlDeploymentReferences")
    def cloud_control_deployment_references(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FrameworkDeploymentCloudControlDeploymentReferenceArgs]]]]:
        
        ...
    
    @cloud_control_deployment_references.setter
    def cloud_control_deployment_references(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FrameworkDeploymentCloudControlDeploymentReferenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudControlMetadatas")
    def cloud_control_metadatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FrameworkDeploymentCloudControlMetadataArgs]]]]:
        
        ...
    
    @cloud_control_metadatas.setter
    def cloud_control_metadatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FrameworkDeploymentCloudControlMetadataArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computedTargetResource")
    def computed_target_resource(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @computed_target_resource.setter
    def computed_target_resource(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentState")
    def deployment_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_state.setter
    def deployment_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def framework(self) -> Optional[pulumi.Input[FrameworkDeploymentFrameworkArgs]]:
        
        ...
    
    @framework.setter
    def framework(self, value: Optional[pulumi.Input[FrameworkDeploymentFrameworkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="frameworkDeploymentId")
    def framework_deployment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @framework_deployment_id.setter
    def framework_deployment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceConfig")
    def target_resource_config(self) -> Optional[pulumi.Input[FrameworkDeploymentTargetResourceConfigArgs]]:
        
        ...
    
    @target_resource_config.setter
    def target_resource_config(self, value: Optional[pulumi.Input[FrameworkDeploymentTargetResourceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceDisplayName")
    def target_resource_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_resource_display_name.setter
    def target_resource_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class FrameworkDeployment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cloud_control_metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FrameworkDeploymentCloudControlMetadataArgs, FrameworkDeploymentCloudControlMetadataArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., framework: Optional[pulumi.Input[Union[FrameworkDeploymentFrameworkArgs, FrameworkDeploymentFrameworkArgsDict]]] = ..., framework_deployment_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., target_resource_config: Optional[pulumi.Input[Union[FrameworkDeploymentTargetResourceConfigArgs, FrameworkDeploymentTargetResourceConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FrameworkDeploymentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cloud_control_deployment_references: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FrameworkDeploymentCloudControlDeploymentReferenceArgs, FrameworkDeploymentCloudControlDeploymentReferenceArgsDict]]]]] = ..., cloud_control_metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FrameworkDeploymentCloudControlMetadataArgs, FrameworkDeploymentCloudControlMetadataArgsDict]]]]] = ..., computed_target_resource: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deployment_state: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., framework: Optional[pulumi.Input[Union[FrameworkDeploymentFrameworkArgs, FrameworkDeploymentFrameworkArgsDict]]] = ..., framework_deployment_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., target_resource_config: Optional[pulumi.Input[Union[FrameworkDeploymentTargetResourceConfigArgs, FrameworkDeploymentTargetResourceConfigArgsDict]]] = ..., target_resource_display_name: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> FrameworkDeployment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudControlDeploymentReferences")
    def cloud_control_deployment_references(self) -> pulumi.Output[Sequence[outputs.FrameworkDeploymentCloudControlDeploymentReference]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudControlMetadatas")
    def cloud_control_metadatas(self) -> pulumi.Output[Sequence[outputs.FrameworkDeploymentCloudControlMetadata]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computedTargetResource")
    def computed_target_resource(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentState")
    def deployment_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def framework(self) -> pulumi.Output[outputs.FrameworkDeploymentFramework]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frameworkDeploymentId")
    def framework_deployment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceConfig")
    def target_resource_config(self) -> pulumi.Output[outputs.FrameworkDeploymentTargetResourceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceDisplayName")
    def target_resource_display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


