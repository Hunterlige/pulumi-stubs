

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PrefixArgs', 'Prefix']
@pulumi.input_type
class PrefixArgs:
    def __init__(__self__, *, peering_service_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], peering_service_prefix_key: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., prefix_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringServiceName")
    def peering_service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peering_service_name.setter
    def peering_service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringServicePrefixKey")
    def peering_service_prefix_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peering_service_prefix_key.setter
    def peering_service_prefix_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixName")
    def prefix_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix_name.setter
    def prefix_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:peering:Prefix")
class Prefix(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., peering_service_name: Optional[pulumi.Input[_builtins.str]] = ..., peering_service_prefix_key: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., prefix_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PrefixArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Prefix:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> pulumi.Output[Sequence[outputs.PeeringServicePrefixEventResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="learnedType")
    def learned_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringServicePrefixKey")
    def peering_service_prefix_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixValidationState")
    def prefix_validation_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


