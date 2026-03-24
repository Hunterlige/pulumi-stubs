import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceResult",
    "AwaitableGetInstanceResult",
    "get_instance",
    "get_instance_output",
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(
        __self__,
        ami=...,
        arn=...,
        associate_public_ip_address=...,
        availability_zone=...,
        credit_specifications=...,
        disable_api_stop=...,
        disable_api_termination=...,
        ebs_block_devices=...,
        ebs_optimized=...,
        enclave_options=...,
        ephemeral_block_devices=...,
        filters=...,
        get_password_data=...,
        get_user_data=...,
        host_id=...,
        host_resource_group_arn=...,
        iam_instance_profile=...,
        id=...,
        instance_id=...,
        instance_state=...,
        instance_tags=...,
        instance_type=...,
        ipv6_addresses=...,
        key_name=...,
        launch_time=...,
        maintenance_options=...,
        metadata_options=...,
        monitoring=...,
        network_interface_id=...,
        outpost_arn=...,
        password_data=...,
        placement_group=...,
        placement_group_id=...,
        placement_partition_number=...,
        private_dns=...,
        private_dns_name_options=...,
        private_ip=...,
        public_dns=...,
        public_ip=...,
        region=...,
        root_block_devices=...,
        secondary_private_ips=...,
        security_groups=...,
        source_dest_check=...,
        subnet_id=...,
        tags=...,
        tenancy=...,
        user_data=...,
        user_data_base64=...,
        vpc_security_group_ids=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ami(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creditSpecifications")
    def credit_specifications(
        self,
    ) -> Sequence[outputs.GetInstanceCreditSpecificationResult]: ...
    @_builtins.property
    @pulumi.getter(name="disableApiStop")
    def disable_api_stop(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="disableApiTermination")
    def disable_api_termination(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(
        self,
    ) -> Sequence[outputs.GetInstanceEbsBlockDeviceResult]: ...
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enclaveOptions")
    def enclave_options(self) -> Sequence[outputs.GetInstanceEnclaveOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(
        self,
    ) -> Sequence[outputs.GetInstanceEphemeralBlockDeviceResult]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetInstanceFilterResult]]: ...
    @_builtins.property
    @pulumi.getter(name="getPasswordData")
    def get_password_data(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="getUserData")
    def get_user_data(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceState")
    def instance_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceTags")
    def instance_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="launchTime")
    def launch_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceOptions")
    def maintenance_options(
        self,
    ) -> Sequence[outputs.GetInstanceMaintenanceOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Sequence[outputs.GetInstanceMetadataOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordData")
    def password_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="placementPartitionNumber")
    def placement_partition_number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="privateDns")
    def private_dns(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateDnsNameOptions")
    def private_dns_name_options(
        self,
    ) -> Sequence[outputs.GetInstancePrivateDnsNameOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicDns")
    def public_dns(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootBlockDevices")
    def root_block_devices(
        self,
    ) -> Sequence[outputs.GetInstanceRootBlockDeviceResult]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIps")
    def secondary_private_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Sequence[_builtins.str]: ...

class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): ...

def get_instance(
    filters: Optional[
        Sequence[Union[GetInstanceFilterArgs, GetInstanceFilterArgsDict]]
    ] = ...,
    get_password_data: Optional[_builtins.bool] = ...,
    get_user_data: Optional[_builtins.bool] = ...,
    instance_id: Optional[_builtins.str] = ...,
    instance_tags: Optional[Mapping[str, _builtins.str]] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceResult: ...
def get_instance_output(
    filters: Optional[
        pulumi.Input[
            Optional[Sequence[Union[GetInstanceFilterArgs, GetInstanceFilterArgsDict]]]
        ]
    ] = ...,
    get_password_data: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    get_user_data: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    instance_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    instance_tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceResult]: ...
