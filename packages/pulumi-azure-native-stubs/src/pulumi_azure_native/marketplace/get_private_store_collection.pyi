

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPrivateStoreCollectionResult', 'AwaitableGetPrivateStoreCollectionResult', 'get_private_store_collection', 'get_private_store_collection_output']
@pulumi.output_type
class GetPrivateStoreCollectionResult:
    
    def __init__(__self__, all_subscriptions=..., applied_rules=..., approve_all_items=..., approve_all_items_modified_at=..., azure_api_version=..., claim=..., collection_id=..., collection_name=..., enabled=..., id=..., name=..., number_of_offers=..., subscriptions_list=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allSubscriptions")
    def all_subscriptions(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedRules")
    def applied_rules(self) -> Sequence[outputs.RuleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approveAllItems")
    def approve_all_items(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approveAllItemsModifiedAt")
    def approve_all_items_modified_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def claim(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfOffers")
    def number_of_offers(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionsList")
    def subscriptions_list(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPrivateStoreCollectionResult(GetPrivateStoreCollectionResult):
    def __await__(self): # -> Generator[Never, Any, GetPrivateStoreCollectionResult]:
        ...
    


def get_private_store_collection(collection_id: Optional[_builtins.str] = ..., private_store_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrivateStoreCollectionResult:
    
    ...

def get_private_store_collection_output(collection_id: Optional[pulumi.Input[_builtins.str]] = ..., private_store_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrivateStoreCollectionResult]:
    
    ...

