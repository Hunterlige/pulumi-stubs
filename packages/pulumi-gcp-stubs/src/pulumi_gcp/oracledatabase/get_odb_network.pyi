

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOdbNetworkResult', 'AwaitableGetOdbNetworkResult', 'get_odb_network', 'get_odb_network_output']
@pulumi.output_type
class GetOdbNetworkResult:
    
    def __init__(__self__, create_time=..., deletion_protection=..., effective_labels=..., entitlement_id=..., gcp_oracle_zone=..., id=..., labels=..., location=..., name=..., network=..., odb_network_id=..., project=..., pulumi_labels=..., state=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entitlementId")
    def entitlement_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpOracleZone")
    def gcp_oracle_zone(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbNetworkId")
    def odb_network_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    


class AwaitableGetOdbNetworkResult(GetOdbNetworkResult):
    def __await__(self): # -> Generator[Never, Any, GetOdbNetworkResult]:
        ...
    


def get_odb_network(location: Optional[_builtins.str] = ..., odb_network_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOdbNetworkResult:
    
    ...

def get_odb_network_output(location: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOdbNetworkResult]:
    
    ...

