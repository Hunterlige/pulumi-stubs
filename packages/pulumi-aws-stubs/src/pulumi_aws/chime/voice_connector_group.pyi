

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
__all__ = ['VoiceConnectorGroupArgs', 'VoiceConnectorGroup']
@pulumi.input_type
class VoiceConnectorGroupArgs:
    def __init__(__self__, *, connectors: Optional[pulumi.Input[Sequence[pulumi.Input[VoiceConnectorGroupConnectorArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VoiceConnectorGroupConnectorArgs]]]]:
        
        ...
    
    @connectors.setter
    def connectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VoiceConnectorGroupConnectorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _VoiceConnectorGroupState:
    def __init__(__self__, *, connectors: Optional[pulumi.Input[Sequence[pulumi.Input[VoiceConnectorGroupConnectorArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VoiceConnectorGroupConnectorArgs]]]]:
        
        ...
    
    @connectors.setter
    def connectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VoiceConnectorGroupConnectorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:chime/voiceConnectorGroup:VoiceConnectorGroup")
class VoiceConnectorGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connectors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VoiceConnectorGroupConnectorArgs, VoiceConnectorGroupConnectorArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[VoiceConnectorGroupArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., connectors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VoiceConnectorGroupConnectorArgs, VoiceConnectorGroupConnectorArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> VoiceConnectorGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connectors(self) -> pulumi.Output[Optional[Sequence[outputs.VoiceConnectorGroupConnector]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


