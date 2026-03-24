

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
__all__ = ['GetVpcAttachmentsResult', 'AwaitableGetVpcAttachmentsResult', 'get_vpc_attachments', 'get_vpc_attachments_output']
@pulumi.output_type
class GetVpcAttachmentsResult:
    
    def __init__(__self__, filters=..., id=..., ids=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpcAttachmentsFilterResult]]:
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
    


class AwaitableGetVpcAttachmentsResult(GetVpcAttachmentsResult):
    def __await__(self): # -> Generator[Never, Any, GetVpcAttachmentsResult]:
        ...
    


def get_vpc_attachments(filters: Optional[Sequence[Union[GetVpcAttachmentsFilterArgs, GetVpcAttachmentsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpcAttachmentsResult:
    
    ...

def get_vpc_attachments_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetVpcAttachmentsFilterArgs, GetVpcAttachmentsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpcAttachmentsResult]:
    
    ...

