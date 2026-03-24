

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
__all__ = ['AiIndexEndpointDeployedIndexArgs', 'AiIndexEndpointDeployedIndex']
@pulumi.input_type
class AiIndexEndpointDeployedIndexArgs:
    def __init__(__self__, *, deployed_index_id: pulumi.Input[_builtins.str], index: pulumi.Input[_builtins.str], index_endpoint: pulumi.Input[_builtins.str], automatic_resources: Optional[pulumi.Input[AiIndexEndpointDeployedIndexAutomaticResourcesArgs]] = ..., dedicated_resources: Optional[pulumi.Input[AiIndexEndpointDeployedIndexDedicatedResourcesArgs]] = ..., deployed_index_auth_config: Optional[pulumi.Input[AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgs]] = ..., deployment_group: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_access_logging: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedIndexId")
    def deployed_index_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @deployed_index_id.setter
    def deployed_index_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def index(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @index.setter
    def index(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexEndpoint")
    def index_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @index_endpoint.setter
    def index_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticResources")
    def automatic_resources(self) -> Optional[pulumi.Input[AiIndexEndpointDeployedIndexAutomaticResourcesArgs]]:
        
        ...
    
    @automatic_resources.setter
    def automatic_resources(self, value: Optional[pulumi.Input[AiIndexEndpointDeployedIndexAutomaticResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedResources")
    def dedicated_resources(self) -> Optional[pulumi.Input[AiIndexEndpointDeployedIndexDedicatedResourcesArgs]]:
        
        ...
    
    @dedicated_resources.setter
    def dedicated_resources(self, value: Optional[pulumi.Input[AiIndexEndpointDeployedIndexDedicatedResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedIndexAuthConfig")
    def deployed_index_auth_config(self) -> Optional[pulumi.Input[AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgs]]:
        
        ...
    
    @deployed_index_auth_config.setter
    def deployed_index_auth_config(self, value: Optional[pulumi.Input[AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentGroup")
    def deployment_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_group.setter
    def deployment_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAccessLogging")
    def enable_access_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_access_logging.setter
    def enable_access_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedIpRanges")
    def reserved_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @reserved_ip_ranges.setter
    def reserved_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _AiIndexEndpointDeployedIndexState:
    def __init__(__self__, *, automatic_resources: Optional[pulumi.Input[AiIndexEndpointDeployedIndexAutomaticResourcesArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dedicated_resources: Optional[pulumi.Input[AiIndexEndpointDeployedIndexDedicatedResourcesArgs]] = ..., deployed_index_auth_config: Optional[pulumi.Input[AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgs]] = ..., deployed_index_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment_group: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_access_logging: Optional[pulumi.Input[_builtins.bool]] = ..., index: Optional[pulumi.Input[_builtins.str]] = ..., index_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., index_sync_time: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[AiIndexEndpointDeployedIndexPrivateEndpointArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticResources")
    def automatic_resources(self) -> Optional[pulumi.Input[AiIndexEndpointDeployedIndexAutomaticResourcesArgs]]:
        
        ...
    
    @automatic_resources.setter
    def automatic_resources(self, value: Optional[pulumi.Input[AiIndexEndpointDeployedIndexAutomaticResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedResources")
    def dedicated_resources(self) -> Optional[pulumi.Input[AiIndexEndpointDeployedIndexDedicatedResourcesArgs]]:
        
        ...
    
    @dedicated_resources.setter
    def dedicated_resources(self, value: Optional[pulumi.Input[AiIndexEndpointDeployedIndexDedicatedResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedIndexAuthConfig")
    def deployed_index_auth_config(self) -> Optional[pulumi.Input[AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgs]]:
        
        ...
    
    @deployed_index_auth_config.setter
    def deployed_index_auth_config(self, value: Optional[pulumi.Input[AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedIndexId")
    def deployed_index_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployed_index_id.setter
    def deployed_index_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentGroup")
    def deployment_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_group.setter
    def deployment_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAccessLogging")
    def enable_access_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_access_logging.setter
    def enable_access_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def index(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index.setter
    def index(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexEndpoint")
    def index_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index_endpoint.setter
    def index_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexSyncTime")
    def index_sync_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index_sync_time.setter
    def index_sync_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AiIndexEndpointDeployedIndexPrivateEndpointArgs]]]]:
        
        ...
    
    @private_endpoints.setter
    def private_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AiIndexEndpointDeployedIndexPrivateEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedIpRanges")
    def reserved_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @reserved_ip_ranges.setter
    def reserved_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AiIndexEndpointDeployedIndex(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., automatic_resources: Optional[pulumi.Input[Union[AiIndexEndpointDeployedIndexAutomaticResourcesArgs, AiIndexEndpointDeployedIndexAutomaticResourcesArgsDict]]] = ..., dedicated_resources: Optional[pulumi.Input[Union[AiIndexEndpointDeployedIndexDedicatedResourcesArgs, AiIndexEndpointDeployedIndexDedicatedResourcesArgsDict]]] = ..., deployed_index_auth_config: Optional[pulumi.Input[Union[AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgs, AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgsDict]]] = ..., deployed_index_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment_group: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_access_logging: Optional[pulumi.Input[_builtins.bool]] = ..., index: Optional[pulumi.Input[_builtins.str]] = ..., index_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AiIndexEndpointDeployedIndexArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., automatic_resources: Optional[pulumi.Input[Union[AiIndexEndpointDeployedIndexAutomaticResourcesArgs, AiIndexEndpointDeployedIndexAutomaticResourcesArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dedicated_resources: Optional[pulumi.Input[Union[AiIndexEndpointDeployedIndexDedicatedResourcesArgs, AiIndexEndpointDeployedIndexDedicatedResourcesArgsDict]]] = ..., deployed_index_auth_config: Optional[pulumi.Input[Union[AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgs, AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgsDict]]] = ..., deployed_index_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment_group: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_access_logging: Optional[pulumi.Input[_builtins.bool]] = ..., index: Optional[pulumi.Input[_builtins.str]] = ..., index_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., index_sync_time: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AiIndexEndpointDeployedIndexPrivateEndpointArgs, AiIndexEndpointDeployedIndexPrivateEndpointArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> AiIndexEndpointDeployedIndex:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticResources")
    def automatic_resources(self) -> pulumi.Output[outputs.AiIndexEndpointDeployedIndexAutomaticResources]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dedicatedResources")
    def dedicated_resources(self) -> pulumi.Output[Optional[outputs.AiIndexEndpointDeployedIndexDedicatedResources]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedIndexAuthConfig")
    def deployed_index_auth_config(self) -> pulumi.Output[Optional[outputs.AiIndexEndpointDeployedIndexDeployedIndexAuthConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deployedIndexId")
    def deployed_index_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentGroup")
    def deployment_group(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAccessLogging")
    def enable_access_logging(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def index(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexEndpoint")
    def index_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexSyncTime")
    def index_sync_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(self) -> pulumi.Output[Sequence[outputs.AiIndexEndpointDeployedIndexPrivateEndpoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedIpRanges")
    def reserved_ip_ranges(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


