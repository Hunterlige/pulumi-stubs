import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSAPDiskConfigurationsResult",
    "AwaitableGetSAPDiskConfigurationsResult",
    "get_sap_disk_configurations",
    "get_sap_disk_configurations_output",
]

@pulumi.output_type
class GetSAPDiskConfigurationsResult:
    def __init__(__self__, volume_configurations=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="volumeConfigurations")
    def volume_configurations(
        self,
    ) -> Optional[Mapping[str, outputs.SAPDiskConfigurationResponse]]: ...

class AwaitableGetSAPDiskConfigurationsResult(GetSAPDiskConfigurationsResult):
    def __await__(self): ...

def get_sap_disk_configurations(
    app_location: Optional[_builtins.str] = ...,
    database_type: Optional[Union[_builtins.str, SAPDatabaseType]] = ...,
    db_vm_sku: Optional[_builtins.str] = ...,
    deployment_type: Optional[Union[_builtins.str, SAPDeploymentType]] = ...,
    environment: Optional[Union[_builtins.str, SAPEnvironmentType]] = ...,
    location: Optional[_builtins.str] = ...,
    sap_product: Optional[Union[_builtins.str, SAPProductType]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSAPDiskConfigurationsResult: ...
def get_sap_disk_configurations_output(
    app_location: Optional[pulumi.Input[_builtins.str]] = ...,
    database_type: Optional[pulumi.Input[Union[_builtins.str, SAPDatabaseType]]] = ...,
    db_vm_sku: Optional[pulumi.Input[_builtins.str]] = ...,
    deployment_type: Optional[
        pulumi.Input[Union[_builtins.str, SAPDeploymentType]]
    ] = ...,
    environment: Optional[pulumi.Input[Union[_builtins.str, SAPEnvironmentType]]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    sap_product: Optional[pulumi.Input[Union[_builtins.str, SAPProductType]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSAPDiskConfigurationsResult]: ...
