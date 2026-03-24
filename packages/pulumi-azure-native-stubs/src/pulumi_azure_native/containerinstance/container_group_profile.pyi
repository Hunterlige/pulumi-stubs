

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ContainerGroupProfileArgs', 'ContainerGroupProfile']
@pulumi.input_type
class ContainerGroupProfileArgs:
    def __init__(__self__, *, containers: pulumi.Input[Sequence[pulumi.Input[ContainerArgs]]], os_type: pulumi.Input[Union[_builtins.str, OperatingSystemTypes]], resource_group_name: pulumi.Input[_builtins.str], confidential_compute_properties: Optional[pulumi.Input[ConfidentialComputePropertiesArgs]] = ..., container_group_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., diagnostics: Optional[pulumi.Input[ContainerGroupDiagnosticsArgs]] = ..., encryption_properties: Optional[pulumi.Input[EncryptionPropertiesArgs]] = ..., extensions: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentExtensionSpecArgs]]]] = ..., image_registry_credentials: Optional[pulumi.Input[Sequence[pulumi.Input[ImageRegistryCredentialArgs]]]] = ..., init_containers: Optional[pulumi.Input[Sequence[pulumi.Input[InitContainerDefinitionArgs]]]] = ..., ip_address: Optional[pulumi.Input[IpAddressArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[Union[_builtins.str, ContainerGroupPriority]]] = ..., restart_policy: Optional[pulumi.Input[Union[_builtins.str, ContainerGroupRestartPolicy]]] = ..., sku: Optional[pulumi.Input[Union[_builtins.str, ContainerGroupSku]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., volumes: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeArgs]]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> pulumi.Input[Sequence[pulumi.Input[ContainerArgs]]]:
        
        ...
    
    @containers.setter
    def containers(self, value: pulumi.Input[Sequence[pulumi.Input[ContainerArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]:
        
        ...
    
    @os_type.setter
    def os_type(self, value: pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialComputeProperties")
    def confidential_compute_properties(self) -> Optional[pulumi.Input[ConfidentialComputePropertiesArgs]]:
        
        ...
    
    @confidential_compute_properties.setter
    def confidential_compute_properties(self, value: Optional[pulumi.Input[ConfidentialComputePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerGroupProfileName")
    def container_group_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_group_profile_name.setter
    def container_group_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Optional[pulumi.Input[ContainerGroupDiagnosticsArgs]]:
        
        ...
    
    @diagnostics.setter
    def diagnostics(self, value: Optional[pulumi.Input[ContainerGroupDiagnosticsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionProperties")
    def encryption_properties(self) -> Optional[pulumi.Input[EncryptionPropertiesArgs]]:
        
        ...
    
    @encryption_properties.setter
    def encryption_properties(self, value: Optional[pulumi.Input[EncryptionPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentExtensionSpecArgs]]]]:
        
        ...
    
    @extensions.setter
    def extensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentExtensionSpecArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageRegistryCredentials")
    def image_registry_credentials(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageRegistryCredentialArgs]]]]:
        
        ...
    
    @image_registry_credentials.setter
    def image_registry_credentials(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageRegistryCredentialArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initContainers")
    def init_containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InitContainerDefinitionArgs]]]]:
        
        ...
    
    @init_containers.setter
    def init_containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InitContainerDefinitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[IpAddressArgs]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[IpAddressArgs]]): # -> None:
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
    def priority(self) -> Optional[pulumi.Input[Union[_builtins.str, ContainerGroupPriority]]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[Union[_builtins.str, ContainerGroupPriority]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restartPolicy")
    def restart_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, ContainerGroupRestartPolicy]]]:
        
        ...
    
    @restart_policy.setter
    def restart_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, ContainerGroupRestartPolicy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[Union[_builtins.str, ContainerGroupSku]]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[Union[_builtins.str, ContainerGroupSku]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeArgs]]]]:
        
        ...
    
    @volumes.setter
    def volumes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ContainerGroupProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., confidential_compute_properties: Optional[pulumi.Input[Union[ConfidentialComputePropertiesArgs, ConfidentialComputePropertiesArgsDict]]] = ..., container_group_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., containers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ContainerArgs, ContainerArgsDict]]]]] = ..., diagnostics: Optional[pulumi.Input[Union[ContainerGroupDiagnosticsArgs, ContainerGroupDiagnosticsArgsDict]]] = ..., encryption_properties: Optional[pulumi.Input[Union[EncryptionPropertiesArgs, EncryptionPropertiesArgsDict]]] = ..., extensions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeploymentExtensionSpecArgs, DeploymentExtensionSpecArgsDict]]]]] = ..., image_registry_credentials: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ImageRegistryCredentialArgs, ImageRegistryCredentialArgsDict]]]]] = ..., init_containers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InitContainerDefinitionArgs, InitContainerDefinitionArgsDict]]]]] = ..., ip_address: Optional[pulumi.Input[Union[IpAddressArgs, IpAddressArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., os_type: Optional[pulumi.Input[Union[_builtins.str, OperatingSystemTypes]]] = ..., priority: Optional[pulumi.Input[Union[_builtins.str, ContainerGroupPriority]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., restart_policy: Optional[pulumi.Input[Union[_builtins.str, ContainerGroupRestartPolicy]]] = ..., sku: Optional[pulumi.Input[Union[_builtins.str, ContainerGroupSku]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., volumes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VolumeArgs, VolumeArgsDict]]]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ContainerGroupProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ContainerGroupProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialComputeProperties")
    def confidential_compute_properties(self) -> pulumi.Output[Optional[outputs.ConfidentialComputePropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> pulumi.Output[Sequence[outputs.ContainerResponseV2]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> pulumi.Output[Optional[outputs.ContainerGroupDiagnosticsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionProperties")
    def encryption_properties(self) -> pulumi.Output[Optional[outputs.EncryptionPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> pulumi.Output[Optional[Sequence[outputs.DeploymentExtensionSpecResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageRegistryCredentials")
    def image_registry_credentials(self) -> pulumi.Output[Optional[Sequence[outputs.ImageRegistryCredentialResponseV2]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initContainers")
    def init_containers(self) -> pulumi.Output[Optional[Sequence[outputs.InitContainerDefinitionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[Optional[outputs.IpAddressResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restartPolicy")
    def restart_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> pulumi.Output[Optional[Sequence[outputs.VolumeResponseV2]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


