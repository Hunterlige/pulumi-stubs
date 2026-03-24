

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PrivateStoreCollectionArgs', 'PrivateStoreCollection']
@pulumi.input_type
class PrivateStoreCollectionArgs:
    def __init__(__self__, *, private_store_id: pulumi.Input[_builtins.str], all_subscriptions: Optional[pulumi.Input[_builtins.bool]] = ..., claim: Optional[pulumi.Input[_builtins.str]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., collection_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., subscriptions_list: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateStoreId")
    def private_store_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @private_store_id.setter
    def private_store_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allSubscriptions")
    def all_subscriptions(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @all_subscriptions.setter
    def all_subscriptions(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def claim(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @claim.setter
    def claim(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collection_id.setter
    def collection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collection_name.setter
    def collection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionsList")
    def subscriptions_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subscriptions_list.setter
    def subscriptions_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:marketplace:PrivateStoreCollection")
class PrivateStoreCollection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., all_subscriptions: Optional[pulumi.Input[_builtins.bool]] = ..., claim: Optional[pulumi.Input[_builtins.str]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., collection_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., private_store_id: Optional[pulumi.Input[_builtins.str]] = ..., subscriptions_list: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PrivateStoreCollectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> PrivateStoreCollection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allSubscriptions")
    def all_subscriptions(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedRules")
    def applied_rules(self) -> pulumi.Output[Sequence[outputs.RuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approveAllItems")
    def approve_all_items(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approveAllItemsModifiedAt")
    def approve_all_items_modified_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def claim(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfOffers")
    def number_of_offers(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionsList")
    def subscriptions_list(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


