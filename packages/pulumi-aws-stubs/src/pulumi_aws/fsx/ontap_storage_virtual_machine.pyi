

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['OntapStorageVirtualMachineArgs', 'OntapStorageVirtualMachine']
@pulumi.input_type
class OntapStorageVirtualMachineArgs:
    def __init__(__self__, *, file_system_id: pulumi.Input[_builtins.str], active_directory_configuration: Optional[pulumi.Input[OntapStorageVirtualMachineActiveDirectoryConfigurationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_volume_security_style: Optional[pulumi.Input[_builtins.str]] = ..., svm_admin_password: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfiguration")
    def active_directory_configuration(self) -> Optional[pulumi.Input[OntapStorageVirtualMachineActiveDirectoryConfigurationArgs]]:
        
        ...
    
    @active_directory_configuration.setter
    def active_directory_configuration(self, value: Optional[pulumi.Input[OntapStorageVirtualMachineActiveDirectoryConfigurationArgs]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootVolumeSecurityStyle")
    def root_volume_security_style(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_volume_security_style.setter
    def root_volume_security_style(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="svmAdminPassword")
    def svm_admin_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @svm_admin_password.setter
    def svm_admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _OntapStorageVirtualMachineState:
    def __init__(__self__, *, active_directory_configuration: Optional[pulumi.Input[OntapStorageVirtualMachineActiveDirectoryConfigurationArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointArgs]]]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_volume_security_style: Optional[pulumi.Input[_builtins.str]] = ..., subtype: Optional[pulumi.Input[_builtins.str]] = ..., svm_admin_password: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., uuid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfiguration")
    def active_directory_configuration(self) -> Optional[pulumi.Input[OntapStorageVirtualMachineActiveDirectoryConfigurationArgs]]:
        
        ...
    
    @active_directory_configuration.setter
    def active_directory_configuration(self, value: Optional[pulumi.Input[OntapStorageVirtualMachineActiveDirectoryConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointArgs]]]]:
        
        ...
    
    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootVolumeSecurityStyle")
    def root_volume_security_style(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_volume_security_style.setter
    def root_volume_security_style(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtype(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subtype.setter
    def subtype(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="svmAdminPassword")
    def svm_admin_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @svm_admin_password.setter
    def svm_admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class OntapStorageVirtualMachine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., active_directory_configuration: Optional[pulumi.Input[Union[OntapStorageVirtualMachineActiveDirectoryConfigurationArgs, OntapStorageVirtualMachineActiveDirectoryConfigurationArgsDict]]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_volume_security_style: Optional[pulumi.Input[_builtins.str]] = ..., svm_admin_password: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OntapStorageVirtualMachineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., active_directory_configuration: Optional[pulumi.Input[Union[OntapStorageVirtualMachineActiveDirectoryConfigurationArgs, OntapStorageVirtualMachineActiveDirectoryConfigurationArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OntapStorageVirtualMachineEndpointArgs, OntapStorageVirtualMachineEndpointArgsDict]]]]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_volume_security_style: Optional[pulumi.Input[_builtins.str]] = ..., subtype: Optional[pulumi.Input[_builtins.str]] = ..., svm_admin_password: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., uuid: Optional[pulumi.Input[_builtins.str]] = ...) -> OntapStorageVirtualMachine:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfiguration")
    def active_directory_configuration(self) -> pulumi.Output[Optional[outputs.OntapStorageVirtualMachineActiveDirectoryConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Sequence[outputs.OntapStorageVirtualMachineEndpoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootVolumeSecurityStyle")
    def root_volume_security_style(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtype(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="svmAdminPassword")
    def svm_admin_password(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


