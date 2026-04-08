import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSqlVirtualMachineGroupResult",
    "AwaitableGetSqlVirtualMachineGroupResult",
    "get_sql_virtual_machine_group",
    "get_sql_virtual_machine_group_output",
]

@pulumi.output_type
class GetSqlVirtualMachineGroupResult:
    def __init__(
        __self__,
        azure_api_version=...,
        cluster_configuration=...,
        cluster_manager_type=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        scale_type=...,
        sql_image_offer=...,
        sql_image_sku=...,
        system_data=...,
        tags=...,
        type=...,
        wsfc_domain_profile=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterConfiguration")
    def cluster_configuration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterManagerType")
    def cluster_manager_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="wsfcDomainProfile")
    def wsfc_domain_profile(self) -> Optional[outputs.WsfcDomainProfileResponse]: ...

class AwaitableGetSqlVirtualMachineGroupResult(GetSqlVirtualMachineGroupResult):
    def __await__(self): ...

def get_sql_virtual_machine_group(
    resource_group_name: Optional[_builtins.str] = ...,
    sql_virtual_machine_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSqlVirtualMachineGroupResult: ...
def get_sql_virtual_machine_group_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    sql_virtual_machine_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSqlVirtualMachineGroupResult]: ...
