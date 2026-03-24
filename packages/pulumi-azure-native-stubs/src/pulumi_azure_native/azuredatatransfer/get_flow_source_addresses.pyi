

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFlowSourceAddressesResult', 'AwaitableGetFlowSourceAddressesResult', 'get_flow_source_addresses', 'get_flow_source_addresses_output']
@pulumi.output_type
class GetFlowSourceAddressesResult:
    
    def __init__(__self__, source_addresses=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetFlowSourceAddressesResult(GetFlowSourceAddressesResult):
    def __await__(self): # -> Generator[Never, Any, GetFlowSourceAddressesResult]:
        ...
    


def get_flow_source_addresses(connection_name: Optional[_builtins.str] = ..., flow_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFlowSourceAddressesResult:
    
    ...

def get_flow_source_addresses_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., flow_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFlowSourceAddressesResult]:
    
    ...

