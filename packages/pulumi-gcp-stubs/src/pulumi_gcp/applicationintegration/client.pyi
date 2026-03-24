

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClientArgs', 'Client']
@pulumi.input_type
class ClientArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], cloud_kms_config: Optional[pulumi.Input[ClientCloudKmsConfigArgs]] = ..., create_sample_integrations: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., run_as_service_account: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudKmsConfig")
    def cloud_kms_config(self) -> Optional[pulumi.Input[ClientCloudKmsConfigArgs]]:
        
        ...
    
    @cloud_kms_config.setter
    def cloud_kms_config(self, value: Optional[pulumi.Input[ClientCloudKmsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSampleIntegrations")
    def create_sample_integrations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_sample_integrations.setter
    def create_sample_integrations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsServiceAccount")
    @_utilities.deprecated(...)
    def run_as_service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @run_as_service_account.setter
    def run_as_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ClientState:
    def __init__(__self__, *, cloud_kms_config: Optional[pulumi.Input[ClientCloudKmsConfigArgs]] = ..., create_sample_integrations: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., run_as_service_account: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudKmsConfig")
    def cloud_kms_config(self) -> Optional[pulumi.Input[ClientCloudKmsConfigArgs]]:
        
        ...
    
    @cloud_kms_config.setter
    def cloud_kms_config(self, value: Optional[pulumi.Input[ClientCloudKmsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSampleIntegrations")
    def create_sample_integrations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_sample_integrations.setter
    def create_sample_integrations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsServiceAccount")
    @_utilities.deprecated(...)
    def run_as_service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @run_as_service_account.setter
    def run_as_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:applicationintegration/client:Client")
class Client(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cloud_kms_config: Optional[pulumi.Input[Union[ClientCloudKmsConfigArgs, ClientCloudKmsConfigArgsDict]]] = ..., create_sample_integrations: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., run_as_service_account: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClientArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cloud_kms_config: Optional[pulumi.Input[Union[ClientCloudKmsConfigArgs, ClientCloudKmsConfigArgsDict]]] = ..., create_sample_integrations: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., run_as_service_account: Optional[pulumi.Input[_builtins.str]] = ...) -> Client:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudKmsConfig")
    def cloud_kms_config(self) -> pulumi.Output[Optional[outputs.ClientCloudKmsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSampleIntegrations")
    def create_sample_integrations(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsServiceAccount")
    @_utilities.deprecated(...)
    def run_as_service_account(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


