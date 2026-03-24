

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVpnLinkConnectionIkeSasResult', 'AwaitableGetVpnLinkConnectionIkeSasResult', 'get_vpn_link_connection_ike_sas', 'get_vpn_link_connection_ike_sas_output']
@pulumi.output_type
class GetVpnLinkConnectionIkeSasResult:
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetVpnLinkConnectionIkeSasResult(GetVpnLinkConnectionIkeSasResult):
    def __await__(self): # -> Generator[Never, Any, GetVpnLinkConnectionIkeSasResult]:
        ...
    


def get_vpn_link_connection_ike_sas(connection_name: Optional[_builtins.str] = ..., gateway_name: Optional[_builtins.str] = ..., link_connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpnLinkConnectionIkeSasResult:
    
    ...

def get_vpn_link_connection_ike_sas_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., link_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpnLinkConnectionIkeSasResult]:
    
    ...

