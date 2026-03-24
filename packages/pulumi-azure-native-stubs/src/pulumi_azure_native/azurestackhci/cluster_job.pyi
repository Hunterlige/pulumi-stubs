

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterJobArgs', 'ClusterJob']
@pulumi.input_type
class ClusterJobArgs:
    def __init__(__self__, *, cluster_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], jobs_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[HciConfigureCvmJobPropertiesArgs, HciConfigureSdnIntegrationJobPropertiesArgs]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobsName")
    def jobs_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @jobs_name.setter
    def jobs_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Union[HciConfigureCvmJobPropertiesArgs, HciConfigureSdnIntegrationJobPropertiesArgs]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Union[HciConfigureCvmJobPropertiesArgs, HciConfigureSdnIntegrationJobPropertiesArgs]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:azurestackhci:ClusterJob")
class ClusterJob(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., jobs_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[Union[HciConfigureCvmJobPropertiesArgs, HciConfigureCvmJobPropertiesArgsDict], Union[HciConfigureSdnIntegrationJobPropertiesArgs, HciConfigureSdnIntegrationJobPropertiesArgsDict]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterJobArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ClusterJob:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


