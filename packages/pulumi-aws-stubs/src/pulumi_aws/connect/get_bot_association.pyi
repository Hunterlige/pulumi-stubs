

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBotAssociationResult', 'AwaitableGetBotAssociationResult', 'get_bot_association', 'get_bot_association_output']
@pulumi.output_type
class GetBotAssociationResult:
    
    def __init__(__self__, id=..., instance_id=..., lex_bot=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lexBot")
    def lex_bot(self) -> outputs.GetBotAssociationLexBotResult:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetBotAssociationResult(GetBotAssociationResult):
    def __await__(self): # -> Generator[Never, Any, GetBotAssociationResult]:
        ...
    


def get_bot_association(instance_id: Optional[_builtins.str] = ..., lex_bot: Optional[Union[GetBotAssociationLexBotArgs, GetBotAssociationLexBotArgsDict]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBotAssociationResult:
    
    ...

def get_bot_association_output(instance_id: Optional[pulumi.Input[_builtins.str]] = ..., lex_bot: Optional[pulumi.Input[Union[GetBotAssociationLexBotArgs, GetBotAssociationLexBotArgsDict]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBotAssociationResult]:
    
    ...

