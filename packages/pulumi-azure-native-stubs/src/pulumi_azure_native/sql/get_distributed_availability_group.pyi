import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDistributedAvailabilityGroupResult",
    "AwaitableGetDistributedAvailabilityGroupResult",
    "get_distributed_availability_group",
    "get_distributed_availability_group_output",
]

@pulumi.output_type
class GetDistributedAvailabilityGroupResult:
    def __init__(
        __self__,
        azure_api_version=...,
        databases=...,
        distributed_availability_group_id=...,
        distributed_availability_group_name=...,
        failover_mode=...,
        id=...,
        instance_availability_group_name=...,
        instance_link_role=...,
        name=...,
        partner_availability_group_name=...,
        partner_endpoint=...,
        partner_link_role=...,
        replication_mode=...,
        seeding_mode=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> Optional[Sequence[outputs.DistributedAvailabilityGroupDatabaseResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="distributedAvailabilityGroupId")
    def distributed_availability_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="distributedAvailabilityGroupName")
    def distributed_availability_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="failoverMode")
    def failover_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceAvailabilityGroupName")
    def instance_availability_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceLinkRole")
    def instance_link_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnerAvailabilityGroupName")
    def partner_availability_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerEndpoint")
    def partner_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerLinkRole")
    def partner_link_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationMode")
    def replication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="seedingMode")
    def seeding_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDistributedAvailabilityGroupResult(
    GetDistributedAvailabilityGroupResult
):
    def __await__(self): ...

def get_distributed_availability_group(
    distributed_availability_group_name: Optional[_builtins.str] = ...,
    managed_instance_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDistributedAvailabilityGroupResult: ...
def get_distributed_availability_group_output(
    distributed_availability_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDistributedAvailabilityGroupResult]: ...
