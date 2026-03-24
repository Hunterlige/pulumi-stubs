

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
__all__ = ['SourceApiAssociationArgs', 'SourceApiAssociation']
@pulumi.input_type
class SourceApiAssociationArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., merged_api_arn: Optional[pulumi.Input[_builtins.str]] = ..., merged_api_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_api_arn: Optional[pulumi.Input[_builtins.str]] = ..., source_api_association_configs: Optional[pulumi.Input[Sequence[pulumi.Input[SourceApiAssociationSourceApiAssociationConfigArgs]]]] = ..., source_api_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[SourceApiAssociationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mergedApiArn")
    def merged_api_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @merged_api_arn.setter
    def merged_api_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mergedApiId")
    def merged_api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @merged_api_id.setter
    def merged_api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApiArn")
    def source_api_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_api_arn.setter
    def source_api_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApiAssociationConfigs")
    def source_api_association_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SourceApiAssociationSourceApiAssociationConfigArgs]]]]:
        ...
    
    @source_api_association_configs.setter
    def source_api_association_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SourceApiAssociationSourceApiAssociationConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApiId")
    def source_api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_api_id.setter
    def source_api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[SourceApiAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[SourceApiAssociationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _SourceApiAssociationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., association_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., merged_api_arn: Optional[pulumi.Input[_builtins.str]] = ..., merged_api_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_api_arn: Optional[pulumi.Input[_builtins.str]] = ..., source_api_association_configs: Optional[pulumi.Input[Sequence[pulumi.Input[SourceApiAssociationSourceApiAssociationConfigArgs]]]] = ..., source_api_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[SourceApiAssociationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @association_id.setter
    def association_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mergedApiArn")
    def merged_api_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @merged_api_arn.setter
    def merged_api_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mergedApiId")
    def merged_api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @merged_api_id.setter
    def merged_api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApiArn")
    def source_api_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_api_arn.setter
    def source_api_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApiAssociationConfigs")
    def source_api_association_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SourceApiAssociationSourceApiAssociationConfigArgs]]]]:
        ...
    
    @source_api_association_configs.setter
    def source_api_association_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SourceApiAssociationSourceApiAssociationConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApiId")
    def source_api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_api_id.setter
    def source_api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[SourceApiAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[SourceApiAssociationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SourceApiAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., merged_api_arn: Optional[pulumi.Input[_builtins.str]] = ..., merged_api_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_api_arn: Optional[pulumi.Input[_builtins.str]] = ..., source_api_association_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SourceApiAssociationSourceApiAssociationConfigArgs, SourceApiAssociationSourceApiAssociationConfigArgsDict]]]]] = ..., source_api_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[SourceApiAssociationTimeoutsArgs, SourceApiAssociationTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[SourceApiAssociationArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., association_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., merged_api_arn: Optional[pulumi.Input[_builtins.str]] = ..., merged_api_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_api_arn: Optional[pulumi.Input[_builtins.str]] = ..., source_api_association_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SourceApiAssociationSourceApiAssociationConfigArgs, SourceApiAssociationSourceApiAssociationConfigArgsDict]]]]] = ..., source_api_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[SourceApiAssociationTimeoutsArgs, SourceApiAssociationTimeoutsArgsDict]]] = ...) -> SourceApiAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mergedApiArn")
    def merged_api_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mergedApiId")
    def merged_api_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApiArn")
    def source_api_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApiAssociationConfigs")
    def source_api_association_configs(self) -> pulumi.Output[Sequence[outputs.SourceApiAssociationSourceApiAssociationConfig]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApiId")
    def source_api_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.SourceApiAssociationTimeouts]]:
        ...
    


