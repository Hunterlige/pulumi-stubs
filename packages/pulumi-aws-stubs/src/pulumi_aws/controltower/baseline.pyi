

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BaselineArgs', 'Baseline']
@pulumi.input_type
class BaselineArgs:
    def __init__(__self__, *, baseline_identifier: pulumi.Input[_builtins.str], baseline_version: pulumi.Input[_builtins.str], target_identifier: pulumi.Input[_builtins.str], parameters: Optional[pulumi.Input[BaselineParametersArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[BaselineTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineIdentifier")
    def baseline_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @baseline_identifier.setter
    def baseline_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineVersion")
    def baseline_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @baseline_version.setter
    def baseline_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIdentifier")
    def target_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_identifier.setter
    def target_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[BaselineParametersArgs]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[BaselineParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[BaselineTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[BaselineTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _BaselineState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., baseline_identifier: Optional[pulumi.Input[_builtins.str]] = ..., baseline_version: Optional[pulumi.Input[_builtins.str]] = ..., operation_identifier: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[BaselineParametersArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_identifier: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[BaselineTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineIdentifier")
    def baseline_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @baseline_identifier.setter
    def baseline_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineVersion")
    def baseline_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @baseline_version.setter
    def baseline_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationIdentifier")
    def operation_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @operation_identifier.setter
    def operation_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[BaselineParametersArgs]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[BaselineParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIdentifier")
    def target_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_identifier.setter
    def target_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[BaselineTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[BaselineTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:controltower/baseline:Baseline")
class Baseline(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., baseline_identifier: Optional[pulumi.Input[_builtins.str]] = ..., baseline_version: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Union[BaselineParametersArgs, BaselineParametersArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_identifier: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[BaselineTimeoutsArgs, BaselineTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BaselineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., baseline_identifier: Optional[pulumi.Input[_builtins.str]] = ..., baseline_version: Optional[pulumi.Input[_builtins.str]] = ..., operation_identifier: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Union[BaselineParametersArgs, BaselineParametersArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_identifier: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[BaselineTimeoutsArgs, BaselineTimeoutsArgsDict]]] = ...) -> Baseline:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineIdentifier")
    def baseline_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineVersion")
    def baseline_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationIdentifier")
    def operation_identifier(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[outputs.BaselineParameters]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIdentifier")
    def target_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.BaselineTimeouts]]:
        ...
    


