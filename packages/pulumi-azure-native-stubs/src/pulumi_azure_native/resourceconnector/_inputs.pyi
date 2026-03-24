

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppliancePropertiesInfrastructureConfigArgs', 'AppliancePropertiesInfrastructureConfigArgsDict', 'IdentityArgs', 'IdentityArgsDict']
class AppliancePropertiesInfrastructureConfigArgsDict(TypedDict):
    
    provider: NotRequired[pulumi.Input[Union[_builtins.str, Provider]]]


@pulumi.input_type
class AppliancePropertiesInfrastructureConfigArgs:
    def __init__(__self__, *, provider: Optional[pulumi.Input[Union[_builtins.str, Provider]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> Optional[pulumi.Input[Union[_builtins.str, Provider]]]:
        
        ...
    
    @provider.setter
    def provider(self, value: Optional[pulumi.Input[Union[_builtins.str, Provider]]]): # -> None:
        ...
    


class IdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]]


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceIdentityType]]]): # -> None:
        ...
    


