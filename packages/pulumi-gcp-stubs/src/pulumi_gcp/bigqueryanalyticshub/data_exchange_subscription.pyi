

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
__all__ = ['DataExchangeSubscriptionArgs', 'DataExchangeSubscription']
@pulumi.input_type
class DataExchangeSubscriptionArgs:
    def __init__(__self__, *, data_exchange_id: pulumi.Input[_builtins.str], data_exchange_location: pulumi.Input[_builtins.str], data_exchange_project: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], subscription_id: pulumi.Input[_builtins.str], destination_dataset: Optional[pulumi.Input[DataExchangeSubscriptionDestinationDatasetArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., refresh_policy: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_contact: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_exchange_id.setter
    def data_exchange_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeLocation")
    def data_exchange_location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_exchange_location.setter
    def data_exchange_location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeProject")
    def data_exchange_project(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_exchange_project.setter
    def data_exchange_project(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationDataset")
    def destination_dataset(self) -> Optional[pulumi.Input[DataExchangeSubscriptionDestinationDatasetArgs]]:
        
        ...
    
    @destination_dataset.setter
    def destination_dataset(self, value: Optional[pulumi.Input[DataExchangeSubscriptionDestinationDatasetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshPolicy")
    def refresh_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @refresh_policy.setter
    def refresh_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberContact")
    def subscriber_contact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscriber_contact.setter
    def subscriber_contact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DataExchangeSubscriptionState:
    def __init__(__self__, *, creation_time: Optional[pulumi.Input[_builtins.str]] = ..., data_exchange: Optional[pulumi.Input[_builtins.str]] = ..., data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ..., data_exchange_location: Optional[pulumi.Input[_builtins.str]] = ..., data_exchange_project: Optional[pulumi.Input[_builtins.str]] = ..., destination_dataset: Optional[pulumi.Input[DataExchangeSubscriptionDestinationDatasetArgs]] = ..., last_modify_time: Optional[pulumi.Input[_builtins.str]] = ..., linked_dataset_maps: Optional[pulumi.Input[Sequence[pulumi.Input[DataExchangeSubscriptionLinkedDatasetMapArgs]]]] = ..., linked_resources: Optional[pulumi.Input[Sequence[pulumi.Input[DataExchangeSubscriptionLinkedResourceArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., log_linked_dataset_query_user_email: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., organization_display_name: Optional[pulumi.Input[_builtins.str]] = ..., organization_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., refresh_policy: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_contact: Optional[pulumi.Input[_builtins.str]] = ..., subscription_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchange")
    def data_exchange(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_exchange.setter
    def data_exchange(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_exchange_id.setter
    def data_exchange_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeLocation")
    def data_exchange_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_exchange_location.setter
    def data_exchange_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeProject")
    def data_exchange_project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_exchange_project.setter
    def data_exchange_project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationDataset")
    def destination_dataset(self) -> Optional[pulumi.Input[DataExchangeSubscriptionDestinationDatasetArgs]]:
        
        ...
    
    @destination_dataset.setter
    def destination_dataset(self, value: Optional[pulumi.Input[DataExchangeSubscriptionDestinationDatasetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifyTime")
    def last_modify_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modify_time.setter
    def last_modify_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedDatasetMaps")
    def linked_dataset_maps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataExchangeSubscriptionLinkedDatasetMapArgs]]]]:
        
        ...
    
    @linked_dataset_maps.setter
    def linked_dataset_maps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataExchangeSubscriptionLinkedDatasetMapArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedResources")
    def linked_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataExchangeSubscriptionLinkedResourceArgs]]]]:
        
        ...
    
    @linked_resources.setter
    def linked_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataExchangeSubscriptionLinkedResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLinkedDatasetQueryUserEmail")
    def log_linked_dataset_query_user_email(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @log_linked_dataset_query_user_email.setter
    def log_linked_dataset_query_user_email(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationDisplayName")
    def organization_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_display_name.setter
    def organization_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshPolicy")
    def refresh_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @refresh_policy.setter
    def refresh_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberContact")
    def subscriber_contact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscriber_contact.setter
    def subscriber_contact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DataExchangeSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ..., data_exchange_location: Optional[pulumi.Input[_builtins.str]] = ..., data_exchange_project: Optional[pulumi.Input[_builtins.str]] = ..., destination_dataset: Optional[pulumi.Input[Union[DataExchangeSubscriptionDestinationDatasetArgs, DataExchangeSubscriptionDestinationDatasetArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., refresh_policy: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_contact: Optional[pulumi.Input[_builtins.str]] = ..., subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataExchangeSubscriptionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., data_exchange: Optional[pulumi.Input[_builtins.str]] = ..., data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ..., data_exchange_location: Optional[pulumi.Input[_builtins.str]] = ..., data_exchange_project: Optional[pulumi.Input[_builtins.str]] = ..., destination_dataset: Optional[pulumi.Input[Union[DataExchangeSubscriptionDestinationDatasetArgs, DataExchangeSubscriptionDestinationDatasetArgsDict]]] = ..., last_modify_time: Optional[pulumi.Input[_builtins.str]] = ..., linked_dataset_maps: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataExchangeSubscriptionLinkedDatasetMapArgs, DataExchangeSubscriptionLinkedDatasetMapArgsDict]]]]] = ..., linked_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataExchangeSubscriptionLinkedResourceArgs, DataExchangeSubscriptionLinkedResourceArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., log_linked_dataset_query_user_email: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., organization_display_name: Optional[pulumi.Input[_builtins.str]] = ..., organization_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., refresh_policy: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subscriber_contact: Optional[pulumi.Input[_builtins.str]] = ..., subscription_id: Optional[pulumi.Input[_builtins.str]] = ...) -> DataExchangeSubscription:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchange")
    def data_exchange(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeLocation")
    def data_exchange_location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeProject")
    def data_exchange_project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationDataset")
    def destination_dataset(self) -> pulumi.Output[Optional[outputs.DataExchangeSubscriptionDestinationDataset]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifyTime")
    def last_modify_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedDatasetMaps")
    def linked_dataset_maps(self) -> pulumi.Output[Sequence[outputs.DataExchangeSubscriptionLinkedDatasetMap]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedResources")
    def linked_resources(self) -> pulumi.Output[Sequence[outputs.DataExchangeSubscriptionLinkedResource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLinkedDatasetQueryUserEmail")
    def log_linked_dataset_query_user_email(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationDisplayName")
    def organization_display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshPolicy")
    def refresh_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriberContact")
    def subscriber_contact(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


