

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOutboundWebIdentityFederationResult', 'AwaitableGetOutboundWebIdentityFederationResult', 'get_outbound_web_identity_federation', 'get_outbound_web_identity_federation_output']
@pulumi.output_type
class GetOutboundWebIdentityFederationResult:
    
    def __init__(__self__, id=..., issuer_identifier=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerIdentifier")
    def issuer_identifier(self) -> _builtins.str:
        
        ...
    


class AwaitableGetOutboundWebIdentityFederationResult(GetOutboundWebIdentityFederationResult):
    def __await__(self): # -> Generator[Never, Any, GetOutboundWebIdentityFederationResult]:
        ...
    


def get_outbound_web_identity_federation(opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOutboundWebIdentityFederationResult:
    
    ...

def get_outbound_web_identity_federation_output(opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOutboundWebIdentityFederationResult]:
    
    ...

