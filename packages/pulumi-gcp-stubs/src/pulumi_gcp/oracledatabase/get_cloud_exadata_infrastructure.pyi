

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCloudExadataInfrastructureResult', 'AwaitableGetCloudExadataInfrastructureResult', 'get_cloud_exadata_infrastructure', 'get_cloud_exadata_infrastructure_output']
@pulumi.output_type
class GetCloudExadataInfrastructureResult:
    
    def __init__(__self__, cloud_exadata_infrastructure_id=..., create_time=..., deletion_protection=..., display_name=..., effective_labels=..., entitlement_id=..., gcp_oracle_zone=..., id=..., labels=..., location=..., name=..., project=..., properties=..., pulumi_labels=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> _builtins.str:
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
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
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
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Sequence[outputs.GetCloudExadataInfrastructurePropertyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetCloudExadataInfrastructureResult(GetCloudExadataInfrastructureResult):
    def __await__(self): # -> Generator[Never, Any, GetCloudExadataInfrastructureResult]:
        ...
    


def get_cloud_exadata_infrastructure(cloud_exadata_infrastructure_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCloudExadataInfrastructureResult:
    
    ...

def get_cloud_exadata_infrastructure_output(cloud_exadata_infrastructure_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCloudExadataInfrastructureResult]:
    
    ...

