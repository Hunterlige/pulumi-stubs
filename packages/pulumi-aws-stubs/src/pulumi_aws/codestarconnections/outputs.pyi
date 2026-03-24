

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HostVpcConfiguration']
@pulumi.output_type
class HostVpcConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, security_group_ids: Sequence[_builtins.str], subnet_ids: Sequence[_builtins.str], vpc_id: _builtins.str, tls_certificate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsCertificate")
    def tls_certificate(self) -> Optional[_builtins.str]:
        
        ...
    


