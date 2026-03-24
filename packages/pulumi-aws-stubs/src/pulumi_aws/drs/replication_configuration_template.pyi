import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReplicationConfigurationTemplateArgs", "ReplicationConfigurationTemplate"]

@pulumi.input_type
class ReplicationConfigurationTemplateArgs:
    def __init__(
        __self__,
        *,
        associate_default_security_group: pulumi.Input[_builtins.bool],
        bandwidth_throttling: pulumi.Input[_builtins.int],
        create_public_ip: pulumi.Input[_builtins.bool],
        data_plane_routing: pulumi.Input[_builtins.str],
        default_large_staging_disk_type: pulumi.Input[_builtins.str],
        ebs_encryption: pulumi.Input[_builtins.str],
        replication_server_instance_type: pulumi.Input[_builtins.str],
        replication_servers_security_groups_ids: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
        staging_area_subnet_id: pulumi.Input[_builtins.str],
        staging_area_tags: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        use_dedicated_replication_server: pulumi.Input[_builtins.bool],
        auto_replicate_new_disks: Optional[pulumi.Input[_builtins.bool]] = ...,
        ebs_encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        pit_policies: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationConfigurationTemplatePitPolicyArgs]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[ReplicationConfigurationTemplateTimeoutsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associateDefaultSecurityGroup")
    def associate_default_security_group(self) -> pulumi.Input[_builtins.bool]: ...
    @associate_default_security_group.setter
    def associate_default_security_group(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="bandwidthThrottling")
    def bandwidth_throttling(self) -> pulumi.Input[_builtins.int]: ...
    @bandwidth_throttling.setter
    def bandwidth_throttling(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="createPublicIp")
    def create_public_ip(self) -> pulumi.Input[_builtins.bool]: ...
    @create_public_ip.setter
    def create_public_ip(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="dataPlaneRouting")
    def data_plane_routing(self) -> pulumi.Input[_builtins.str]: ...
    @data_plane_routing.setter
    def data_plane_routing(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultLargeStagingDiskType")
    def default_large_staging_disk_type(self) -> pulumi.Input[_builtins.str]: ...
    @default_large_staging_disk_type.setter
    def default_large_staging_disk_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ebsEncryption")
    def ebs_encryption(self) -> pulumi.Input[_builtins.str]: ...
    @ebs_encryption.setter
    def ebs_encryption(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="replicationServerInstanceType")
    def replication_server_instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @replication_server_instance_type.setter
    def replication_server_instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="replicationServersSecurityGroupsIds")
    def replication_servers_security_groups_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @replication_servers_security_groups_ids.setter
    def replication_servers_security_groups_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stagingAreaSubnetId")
    def staging_area_subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @staging_area_subnet_id.setter
    def staging_area_subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stagingAreaTags")
    def staging_area_tags(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @staging_area_tags.setter
    def staging_area_tags(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useDedicatedReplicationServer")
    def use_dedicated_replication_server(self) -> pulumi.Input[_builtins.bool]: ...
    @use_dedicated_replication_server.setter
    def use_dedicated_replication_server(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="autoReplicateNewDisks")
    def auto_replicate_new_disks(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_replicate_new_disks.setter
    def auto_replicate_new_disks(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ebsEncryptionKeyArn")
    def ebs_encryption_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ebs_encryption_key_arn.setter
    def ebs_encryption_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pitPolicies")
    def pit_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ReplicationConfigurationTemplatePitPolicyArgs]]
        ]
    ]: ...
    @pit_policies.setter
    def pit_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationConfigurationTemplatePitPolicyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[ReplicationConfigurationTemplateTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[pulumi.Input[ReplicationConfigurationTemplateTimeoutsArgs]],
    ): ...

@pulumi.input_type
class _ReplicationConfigurationTemplateState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        associate_default_security_group: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_replicate_new_disks: Optional[pulumi.Input[_builtins.bool]] = ...,
        bandwidth_throttling: Optional[pulumi.Input[_builtins.int]] = ...,
        create_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_plane_routing: Optional[pulumi.Input[_builtins.str]] = ...,
        default_large_staging_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        pit_policies: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationConfigurationTemplatePitPolicyArgs]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_server_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_servers_security_groups_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        staging_area_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        staging_area_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[ReplicationConfigurationTemplateTimeoutsArgs]
        ] = ...,
        use_dedicated_replication_server: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="associateDefaultSecurityGroup")
    def associate_default_security_group(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @associate_default_security_group.setter
    def associate_default_security_group(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoReplicateNewDisks")
    def auto_replicate_new_disks(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_replicate_new_disks.setter
    def auto_replicate_new_disks(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bandwidthThrottling")
    def bandwidth_throttling(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bandwidth_throttling.setter
    def bandwidth_throttling(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="createPublicIp")
    def create_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_public_ip.setter
    def create_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dataPlaneRouting")
    def data_plane_routing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_plane_routing.setter
    def data_plane_routing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultLargeStagingDiskType")
    def default_large_staging_disk_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_large_staging_disk_type.setter
    def default_large_staging_disk_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ebsEncryption")
    def ebs_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ebs_encryption.setter
    def ebs_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebsEncryptionKeyArn")
    def ebs_encryption_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ebs_encryption_key_arn.setter
    def ebs_encryption_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pitPolicies")
    def pit_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ReplicationConfigurationTemplatePitPolicyArgs]]
        ]
    ]: ...
    @pit_policies.setter
    def pit_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationConfigurationTemplatePitPolicyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationServerInstanceType")
    def replication_server_instance_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_server_instance_type.setter
    def replication_server_instance_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationServersSecurityGroupsIds")
    def replication_servers_security_groups_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @replication_servers_security_groups_ids.setter
    def replication_servers_security_groups_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stagingAreaSubnetId")
    def staging_area_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @staging_area_subnet_id.setter
    def staging_area_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stagingAreaTags")
    def staging_area_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @staging_area_tags.setter
    def staging_area_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[ReplicationConfigurationTemplateTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[pulumi.Input[ReplicationConfigurationTemplateTimeoutsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="useDedicatedReplicationServer")
    def use_dedicated_replication_server(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_dedicated_replication_server.setter
    def use_dedicated_replication_server(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.type_token(...)
class ReplicationConfigurationTemplate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        associate_default_security_group: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_replicate_new_disks: Optional[pulumi.Input[_builtins.bool]] = ...,
        bandwidth_throttling: Optional[pulumi.Input[_builtins.int]] = ...,
        create_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_plane_routing: Optional[pulumi.Input[_builtins.str]] = ...,
        default_large_staging_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        pit_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReplicationConfigurationTemplatePitPolicyArgs,
                            ReplicationConfigurationTemplatePitPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_server_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_servers_security_groups_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        staging_area_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        staging_area_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ReplicationConfigurationTemplateTimeoutsArgs,
                    ReplicationConfigurationTemplateTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        use_dedicated_replication_server: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReplicationConfigurationTemplateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        associate_default_security_group: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_replicate_new_disks: Optional[pulumi.Input[_builtins.bool]] = ...,
        bandwidth_throttling: Optional[pulumi.Input[_builtins.int]] = ...,
        create_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_plane_routing: Optional[pulumi.Input[_builtins.str]] = ...,
        default_large_staging_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        pit_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReplicationConfigurationTemplatePitPolicyArgs,
                            ReplicationConfigurationTemplatePitPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_server_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_servers_security_groups_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        staging_area_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        staging_area_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ReplicationConfigurationTemplateTimeoutsArgs,
                    ReplicationConfigurationTemplateTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        use_dedicated_replication_server: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> ReplicationConfigurationTemplate: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associateDefaultSecurityGroup")
    def associate_default_security_group(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="autoReplicateNewDisks")
    def auto_replicate_new_disks(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="bandwidthThrottling")
    def bandwidth_throttling(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="createPublicIp")
    def create_public_ip(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dataPlaneRouting")
    def data_plane_routing(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultLargeStagingDiskType")
    def default_large_staging_disk_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ebsEncryption")
    def ebs_encryption(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ebsEncryptionKeyArn")
    def ebs_encryption_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pitPolicies")
    def pit_policies(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ReplicationConfigurationTemplatePitPolicy]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationServerInstanceType")
    def replication_server_instance_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationServersSecurityGroupsIds")
    def replication_servers_security_groups_ids(
        self,
    ) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="stagingAreaSubnetId")
    def staging_area_subnet_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stagingAreaTags")
    def staging_area_tags(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.ReplicationConfigurationTemplateTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="useDedicatedReplicationServer")
    def use_dedicated_replication_server(self) -> pulumi.Output[_builtins.bool]: ...
