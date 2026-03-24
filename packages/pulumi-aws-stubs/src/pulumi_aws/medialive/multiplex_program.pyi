

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MultiplexProgramArgs', 'MultiplexProgram']
@pulumi.input_type
class MultiplexProgramArgs:
    def __init__(__self__, *, multiplex_id: pulumi.Input[_builtins.str], program_name: pulumi.Input[_builtins.str], multiplex_program_settings: Optional[pulumi.Input[MultiplexProgramMultiplexProgramSettingsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[MultiplexProgramTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiplexId")
    def multiplex_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @multiplex_id.setter
    def multiplex_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="programName")
    def program_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @program_name.setter
    def program_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiplexProgramSettings")
    def multiplex_program_settings(self) -> Optional[pulumi.Input[MultiplexProgramMultiplexProgramSettingsArgs]]:
        
        ...
    
    @multiplex_program_settings.setter
    def multiplex_program_settings(self, value: Optional[pulumi.Input[MultiplexProgramMultiplexProgramSettingsArgs]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[MultiplexProgramTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[MultiplexProgramTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _MultiplexProgramState:
    def __init__(__self__, *, multiplex_id: Optional[pulumi.Input[_builtins.str]] = ..., multiplex_program_settings: Optional[pulumi.Input[MultiplexProgramMultiplexProgramSettingsArgs]] = ..., program_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[MultiplexProgramTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiplexId")
    def multiplex_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @multiplex_id.setter
    def multiplex_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiplexProgramSettings")
    def multiplex_program_settings(self) -> Optional[pulumi.Input[MultiplexProgramMultiplexProgramSettingsArgs]]:
        
        ...
    
    @multiplex_program_settings.setter
    def multiplex_program_settings(self, value: Optional[pulumi.Input[MultiplexProgramMultiplexProgramSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="programName")
    def program_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @program_name.setter
    def program_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[MultiplexProgramTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[MultiplexProgramTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:medialive/multiplexProgram:MultiplexProgram")
class MultiplexProgram(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., multiplex_id: Optional[pulumi.Input[_builtins.str]] = ..., multiplex_program_settings: Optional[pulumi.Input[Union[MultiplexProgramMultiplexProgramSettingsArgs, MultiplexProgramMultiplexProgramSettingsArgsDict]]] = ..., program_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[MultiplexProgramTimeoutsArgs, MultiplexProgramTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MultiplexProgramArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., multiplex_id: Optional[pulumi.Input[_builtins.str]] = ..., multiplex_program_settings: Optional[pulumi.Input[Union[MultiplexProgramMultiplexProgramSettingsArgs, MultiplexProgramMultiplexProgramSettingsArgsDict]]] = ..., program_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[MultiplexProgramTimeoutsArgs, MultiplexProgramTimeoutsArgsDict]]] = ...) -> MultiplexProgram:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiplexId")
    def multiplex_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiplexProgramSettings")
    def multiplex_program_settings(self) -> pulumi.Output[Optional[outputs.MultiplexProgramMultiplexProgramSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="programName")
    def program_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.MultiplexProgramTimeouts]]:
        ...
    


