

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataShareConsumerAssociationArgs', 'DataShareConsumerAssociation']
@pulumi.input_type
class DataShareConsumerAssociationArgs:
    def __init__(__self__, *, data_share_arn: pulumi.Input[_builtins.str], allow_writes: Optional[pulumi.Input[_builtins.bool]] = ..., associate_entire_account: Optional[pulumi.Input[_builtins.bool]] = ..., consumer_arn: Optional[pulumi.Input[_builtins.str]] = ..., consumer_region: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataShareArn")
    def data_share_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_share_arn.setter
    def data_share_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowWrites")
    def allow_writes(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_writes.setter
    def allow_writes(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associateEntireAccount")
    def associate_entire_account(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @associate_entire_account.setter
    def associate_entire_account(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_arn.setter
    def consumer_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerRegion")
    def consumer_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_region.setter
    def consumer_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DataShareConsumerAssociationState:
    def __init__(__self__, *, allow_writes: Optional[pulumi.Input[_builtins.bool]] = ..., associate_entire_account: Optional[pulumi.Input[_builtins.bool]] = ..., consumer_arn: Optional[pulumi.Input[_builtins.str]] = ..., consumer_region: Optional[pulumi.Input[_builtins.str]] = ..., data_share_arn: Optional[pulumi.Input[_builtins.str]] = ..., managed_by: Optional[pulumi.Input[_builtins.str]] = ..., producer_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowWrites")
    def allow_writes(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_writes.setter
    def allow_writes(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associateEntireAccount")
    def associate_entire_account(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @associate_entire_account.setter
    def associate_entire_account(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_arn.setter
    def consumer_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerRegion")
    def consumer_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_region.setter
    def consumer_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataShareArn")
    def data_share_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_share_arn.setter
    def data_share_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="producerArn")
    def producer_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @producer_arn.setter
    def producer_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DataShareConsumerAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_writes: Optional[pulumi.Input[_builtins.bool]] = ..., associate_entire_account: Optional[pulumi.Input[_builtins.bool]] = ..., consumer_arn: Optional[pulumi.Input[_builtins.str]] = ..., consumer_region: Optional[pulumi.Input[_builtins.str]] = ..., data_share_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataShareConsumerAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allow_writes: Optional[pulumi.Input[_builtins.bool]] = ..., associate_entire_account: Optional[pulumi.Input[_builtins.bool]] = ..., consumer_arn: Optional[pulumi.Input[_builtins.str]] = ..., consumer_region: Optional[pulumi.Input[_builtins.str]] = ..., data_share_arn: Optional[pulumi.Input[_builtins.str]] = ..., managed_by: Optional[pulumi.Input[_builtins.str]] = ..., producer_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> DataShareConsumerAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowWrites")
    def allow_writes(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associateEntireAccount")
    def associate_entire_account(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerRegion")
    def consumer_region(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataShareArn")
    def data_share_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="producerArn")
    def producer_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


