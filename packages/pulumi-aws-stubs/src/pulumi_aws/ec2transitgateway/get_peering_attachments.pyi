

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPeeringAttachmentsResult', 'AwaitableGetPeeringAttachmentsResult', 'get_peering_attachments', 'get_peering_attachments_output']
@pulumi.output_type
class GetPeeringAttachmentsResult:
    
    def __init__(__self__, filters=..., id=..., ids=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetPeeringAttachmentsFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetPeeringAttachmentsResult(GetPeeringAttachmentsResult):
    def __await__(self): # -> Generator[Never, Any, GetPeeringAttachmentsResult]:
        ...
    


def get_peering_attachments(filters: Optional[Sequence[Union[GetPeeringAttachmentsFilterArgs, GetPeeringAttachmentsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPeeringAttachmentsResult:
    
    ...

def get_peering_attachments_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetPeeringAttachmentsFilterArgs, GetPeeringAttachmentsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPeeringAttachmentsResult]:
    
    ...

