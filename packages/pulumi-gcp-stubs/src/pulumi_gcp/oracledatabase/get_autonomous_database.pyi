

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAutonomousDatabaseResult', 'AwaitableGetAutonomousDatabaseResult', 'get_autonomous_database', 'get_autonomous_database_output']
@pulumi.output_type
class GetAutonomousDatabaseResult:
    
    def __init__(__self__, admin_password=..., autonomous_database_id=..., cidr=..., create_time=..., database=..., deletion_protection=..., disaster_recovery_supported_locations=..., display_name=..., effective_labels=..., entitlement_id=..., id=..., labels=..., location=..., name=..., network=..., odb_network=..., odb_subnet=..., peer_autonomous_databases=..., project=..., properties=..., pulumi_labels=..., source_configs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autonomousDatabaseId")
    def autonomous_database_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disasterRecoverySupportedLocations")
    def disaster_recovery_supported_locations(self) -> Sequence[_builtins.str]:
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
    @pulumi.getter(name="odbNetwork")
    def odb_network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbSubnet")
    def odb_subnet(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAutonomousDatabases")
    def peer_autonomous_databases(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Sequence[outputs.GetAutonomousDatabasePropertyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConfigs")
    def source_configs(self) -> Sequence[outputs.GetAutonomousDatabaseSourceConfigResult]:
        ...
    


class AwaitableGetAutonomousDatabaseResult(GetAutonomousDatabaseResult):
    def __await__(self): # -> Generator[Never, Any, GetAutonomousDatabaseResult]:
        ...
    


def get_autonomous_database(autonomous_database_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAutonomousDatabaseResult:
    
    ...

def get_autonomous_database_output(autonomous_database_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAutonomousDatabaseResult]:
    
    ...

