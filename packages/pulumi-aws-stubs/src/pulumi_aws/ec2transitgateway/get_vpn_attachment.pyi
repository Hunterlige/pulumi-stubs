

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVpnAttachmentResult', 'AwaitableGetVpnAttachmentResult', 'get_vpn_attachment', 'get_vpn_attachment_output']
@pulumi.output_type
class GetVpnAttachmentResult:
    
    def __init__(__self__, filters=..., id=..., region=..., tags=..., transit_gateway_id=..., vpn_connection_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpnAttachmentFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnConnectionId")
    def vpn_connection_id(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetVpnAttachmentResult(GetVpnAttachmentResult):
    def __await__(self): # -> Generator[Never, Any, GetVpnAttachmentResult]:
        ...
    


def get_vpn_attachment(filters: Optional[Sequence[Union[GetVpnAttachmentFilterArgs, GetVpnAttachmentFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., transit_gateway_id: Optional[_builtins.str] = ..., vpn_connection_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpnAttachmentResult:
    
    ...

def get_vpn_attachment_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetVpnAttachmentFilterArgs, GetVpnAttachmentFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., transit_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., vpn_connection_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpnAttachmentResult]:
    
    ...

