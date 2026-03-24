

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
__all__ = ['DaprSubscriptionArgs', 'DaprSubscription']
@pulumi.input_type
class DaprSubscriptionArgs:
    def __init__(__self__, *, environment_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], bulk_subscribe: Optional[pulumi.Input[DaprSubscriptionBulkSubscribeOptionsArgs]] = ..., dead_letter_topic: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_name: Optional[pulumi.Input[_builtins.str]] = ..., routes: Optional[pulumi.Input[DaprSubscriptionRoutesArgs]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., topic: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @environment_name.setter
    def environment_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bulkSubscribe")
    def bulk_subscribe(self) -> Optional[pulumi.Input[DaprSubscriptionBulkSubscribeOptionsArgs]]:
        
        ...
    
    @bulk_subscribe.setter
    def bulk_subscribe(self, value: Optional[pulumi.Input[DaprSubscriptionBulkSubscribeOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterTopic")
    def dead_letter_topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dead_letter_topic.setter
    def dead_letter_topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubName")
    def pubsub_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pubsub_name.setter
    def pubsub_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[pulumi.Input[DaprSubscriptionRoutesArgs]]:
        
        ...
    
    @routes.setter
    def routes(self, value: Optional[pulumi.Input[DaprSubscriptionRoutesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:app:DaprSubscription")
class DaprSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bulk_subscribe: Optional[pulumi.Input[Union[DaprSubscriptionBulkSubscribeOptionsArgs, DaprSubscriptionBulkSubscribeOptionsArgsDict]]] = ..., dead_letter_topic: Optional[pulumi.Input[_builtins.str]] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., routes: Optional[pulumi.Input[Union[DaprSubscriptionRoutesArgs, DaprSubscriptionRoutesArgsDict]]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., topic: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DaprSubscriptionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DaprSubscription:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bulkSubscribe")
    def bulk_subscribe(self) -> pulumi.Output[Optional[outputs.DaprSubscriptionBulkSubscribeOptionsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterTopic")
    def dead_letter_topic(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubName")
    def pubsub_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> pulumi.Output[Optional[outputs.DaprSubscriptionRoutesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


