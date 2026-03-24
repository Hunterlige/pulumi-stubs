

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
__all__ = ['InboundSamlConfigArgs', 'InboundSamlConfig']
@pulumi.input_type
class InboundSamlConfigArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], idp_config: pulumi.Input[InboundSamlConfigIdpConfigArgs], sp_config: pulumi.Input[InboundSamlConfigSpConfigArgs], enabled: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idpConfig")
    def idp_config(self) -> pulumi.Input[InboundSamlConfigIdpConfigArgs]:
        
        ...
    
    @idp_config.setter
    def idp_config(self, value: pulumi.Input[InboundSamlConfigIdpConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spConfig")
    def sp_config(self) -> pulumi.Input[InboundSamlConfigSpConfigArgs]:
        
        ...
    
    @sp_config.setter
    def sp_config(self, value: pulumi.Input[InboundSamlConfigSpConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InboundSamlConfigState:
    def __init__(__self__, *, display_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., idp_config: Optional[pulumi.Input[InboundSamlConfigIdpConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., sp_config: Optional[pulumi.Input[InboundSamlConfigSpConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idpConfig")
    def idp_config(self) -> Optional[pulumi.Input[InboundSamlConfigIdpConfigArgs]]:
        
        ...
    
    @idp_config.setter
    def idp_config(self, value: Optional[pulumi.Input[InboundSamlConfigIdpConfigArgs]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spConfig")
    def sp_config(self) -> Optional[pulumi.Input[InboundSamlConfigSpConfigArgs]]:
        
        ...
    
    @sp_config.setter
    def sp_config(self, value: Optional[pulumi.Input[InboundSamlConfigSpConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class InboundSamlConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., idp_config: Optional[pulumi.Input[Union[InboundSamlConfigIdpConfigArgs, InboundSamlConfigIdpConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., sp_config: Optional[pulumi.Input[Union[InboundSamlConfigSpConfigArgs, InboundSamlConfigSpConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InboundSamlConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., idp_config: Optional[pulumi.Input[Union[InboundSamlConfigIdpConfigArgs, InboundSamlConfigIdpConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., sp_config: Optional[pulumi.Input[Union[InboundSamlConfigSpConfigArgs, InboundSamlConfigSpConfigArgsDict]]] = ...) -> InboundSamlConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idpConfig")
    def idp_config(self) -> pulumi.Output[outputs.InboundSamlConfigIdpConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spConfig")
    def sp_config(self) -> pulumi.Output[outputs.InboundSamlConfigSpConfig]:
        
        ...
    


