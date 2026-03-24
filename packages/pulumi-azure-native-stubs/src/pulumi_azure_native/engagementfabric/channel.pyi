

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ChannelArgs', 'Channel']
@pulumi.input_type
class ChannelArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], channel_type: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], channel_functions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., channel_name: Optional[pulumi.Input[_builtins.str]] = ..., credentials: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @channel_type.setter
    def channel_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelFunctions")
    def channel_functions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @channel_functions.setter
    def channel_functions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:engagementfabric:Channel")
class Channel(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., channel_functions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., channel_name: Optional[pulumi.Input[_builtins.str]] = ..., channel_type: Optional[pulumi.Input[_builtins.str]] = ..., credentials: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ChannelArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Channel:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelFunctions")
    def channel_functions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


