

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class GetP2sVpnGatewayP2sVpnConnectionHealthDetailedResult:
    
    def __init__(__self__, sas_url=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasUrl")
    def sas_url(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetP2sVpnGatewayP2sVpnConnectionHealthDetailedResult(GetP2sVpnGatewayP2sVpnConnectionHealthDetailedResult):
    def __await__(self): # -> Generator[Never, Any, GetP2sVpnGatewayP2sVpnConnectionHealthDetailedResult]:
        ...
    


def get_p2s_vpn_gateway_p2s_vpn_connection_health_detailed(gateway_name: Optional[_builtins.str] = ..., output_blob_sas_url: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., vpn_user_names_filter: Optional[Sequence[_builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetP2sVpnGatewayP2sVpnConnectionHealthDetailedResult:
    
    ...

def get_p2s_vpn_gateway_p2s_vpn_connection_health_detailed_output(gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., output_blob_sas_url: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., vpn_user_names_filter: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetP2sVpnGatewayP2sVpnConnectionHealthDetailedResult]:
    
    ...

