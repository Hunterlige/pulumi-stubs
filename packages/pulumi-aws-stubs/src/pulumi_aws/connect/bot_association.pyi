

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
__all__ = ['BotAssociationArgs', 'BotAssociation']
@pulumi.input_type
class BotAssociationArgs:
    def __init__(__self__, *, instance_id: pulumi.Input[_builtins.str], lex_bot: pulumi.Input[BotAssociationLexBotArgs], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lexBot")
    def lex_bot(self) -> pulumi.Input[BotAssociationLexBotArgs]:
        
        ...
    
    @lex_bot.setter
    def lex_bot(self, value: pulumi.Input[BotAssociationLexBotArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BotAssociationState:
    def __init__(__self__, *, instance_id: Optional[pulumi.Input[_builtins.str]] = ..., lex_bot: Optional[pulumi.Input[BotAssociationLexBotArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lexBot")
    def lex_bot(self) -> Optional[pulumi.Input[BotAssociationLexBotArgs]]:
        
        ...
    
    @lex_bot.setter
    def lex_bot(self, value: Optional[pulumi.Input[BotAssociationLexBotArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:connect/botAssociation:BotAssociation")
class BotAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., lex_bot: Optional[pulumi.Input[Union[BotAssociationLexBotArgs, BotAssociationLexBotArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BotAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., lex_bot: Optional[pulumi.Input[Union[BotAssociationLexBotArgs, BotAssociationLexBotArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> BotAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lexBot")
    def lex_bot(self) -> pulumi.Output[outputs.BotAssociationLexBot]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


