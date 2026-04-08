import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DistributedAvailabilityGroupArgs", "DistributedAvailabilityGroup"]

@pulumi.input_type
class DistributedAvailabilityGroupArgs:
    def __init__(
        __self__,
        *,
        managed_instance_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        databases: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DistributedAvailabilityGroupDatabaseArgs]]
            ]
        ] = ...,
        distributed_availability_group_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        failover_mode: Optional[
            pulumi.Input[Union[_builtins.str, FailoverModeType]]
        ] = ...,
        instance_availability_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_link_role: Optional[
            pulumi.Input[Union[_builtins.str, LinkRole]]
        ] = ...,
        partner_availability_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_mode: Optional[
            pulumi.Input[Union[_builtins.str, ReplicationModeType]]
        ] = ...,
        seeding_mode: Optional[
            pulumi.Input[Union[_builtins.str, SeedingModeType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[_builtins.str]: ...
    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DistributedAvailabilityGroupDatabaseArgs]]]
    ]: ...
    @databases.setter
    def databases(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DistributedAvailabilityGroupDatabaseArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="distributedAvailabilityGroupName")
    def distributed_availability_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distributed_availability_group_name.setter
    def distributed_availability_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failoverMode")
    def failover_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FailoverModeType]]]: ...
    @failover_mode.setter
    def failover_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FailoverModeType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceAvailabilityGroupName")
    def instance_availability_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_availability_group_name.setter
    def instance_availability_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceLinkRole")
    def instance_link_role(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LinkRole]]]: ...
    @instance_link_role.setter
    def instance_link_role(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LinkRole]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="partnerAvailabilityGroupName")
    def partner_availability_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_availability_group_name.setter
    def partner_availability_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="partnerEndpoint")
    def partner_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_endpoint.setter
    def partner_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationMode")
    def replication_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ReplicationModeType]]]: ...
    @replication_mode.setter
    def replication_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ReplicationModeType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="seedingMode")
    def seeding_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SeedingModeType]]]: ...
    @seeding_mode.setter
    def seeding_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SeedingModeType]]]
    ): ...

@pulumi.type_token("azure-native:sql:DistributedAvailabilityGroup")
class DistributedAvailabilityGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        databases: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DistributedAvailabilityGroupDatabaseArgs,
                            DistributedAvailabilityGroupDatabaseArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        distributed_availability_group_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        failover_mode: Optional[
            pulumi.Input[Union[_builtins.str, FailoverModeType]]
        ] = ...,
        instance_availability_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_link_role: Optional[
            pulumi.Input[Union[_builtins.str, LinkRole]]
        ] = ...,
        managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_availability_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_mode: Optional[
            pulumi.Input[Union[_builtins.str, ReplicationModeType]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        seeding_mode: Optional[
            pulumi.Input[Union[_builtins.str, SeedingModeType]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DistributedAvailabilityGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DistributedAvailabilityGroup: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.DistributedAvailabilityGroupDatabaseResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="distributedAvailabilityGroupId")
    def distributed_availability_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="distributedAvailabilityGroupName")
    def distributed_availability_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failoverMode")
    def failover_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceAvailabilityGroupName")
    def instance_availability_group_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceLinkRole")
    def instance_link_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerAvailabilityGroupName")
    def partner_availability_group_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="partnerEndpoint")
    def partner_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="partnerLinkRole")
    def partner_link_role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationMode")
    def replication_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="seedingMode")
    def seeding_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
