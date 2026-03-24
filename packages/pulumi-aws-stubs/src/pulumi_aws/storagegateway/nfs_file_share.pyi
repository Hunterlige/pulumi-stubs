import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NfsFileShareArgs", "NfsFileShare"]

@pulumi.input_type
class NfsFileShareArgs:
    def __init__(
        __self__,
        *,
        client_lists: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        gateway_arn: pulumi.Input[_builtins.str],
        location_arn: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[pulumi.Input[NfsFileShareCacheAttributesArgs]] = ...,
        default_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        guess_mime_type_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        nfs_file_share_defaults: Optional[
            pulumi.Input[NfsFileShareNfsFileShareDefaultsArgs]
        ] = ...,
        notification_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        object_acl: Optional[pulumi.Input[_builtins.str]] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester_pays: Optional[pulumi.Input[_builtins.bool]] = ...,
        squash: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_endpoint_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientLists")
    def client_lists(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @client_lists.setter
    def client_lists(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Input[_builtins.str]: ...
    @gateway_arn.setter
    def gateway_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> pulumi.Input[_builtins.str]: ...
    @location_arn.setter
    def location_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="auditDestinationArn")
    def audit_destination_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audit_destination_arn.setter
    def audit_destination_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_region.setter
    def bucket_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> Optional[pulumi.Input[NfsFileShareCacheAttributesArgs]]: ...
    @cache_attributes.setter
    def cache_attributes(
        self, value: Optional[pulumi.Input[NfsFileShareCacheAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultStorageClass")
    def default_storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_storage_class.setter
    def default_storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_share_name.setter
    def file_share_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="guessMimeTypeEnabled")
    def guess_mime_type_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @guess_mime_type_enabled.setter
    def guess_mime_type_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsEncrypted")
    def kms_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @kms_encrypted.setter
    def kms_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nfsFileShareDefaults")
    def nfs_file_share_defaults(
        self,
    ) -> Optional[pulumi.Input[NfsFileShareNfsFileShareDefaultsArgs]]: ...
    @nfs_file_share_defaults.setter
    def nfs_file_share_defaults(
        self, value: Optional[pulumi.Input[NfsFileShareNfsFileShareDefaultsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationPolicy")
    def notification_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_policy.setter
    def notification_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectAcl")
    def object_acl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_acl.setter
    def object_acl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requesterPays")
    def requester_pays(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @requester_pays.setter
    def requester_pays(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def squash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @squash.setter
    def squash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="vpcEndpointDnsName")
    def vpc_endpoint_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_dns_name.setter
    def vpc_endpoint_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NfsFileShareState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[pulumi.Input[NfsFileShareCacheAttributesArgs]] = ...,
        client_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        fileshare_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        guess_mime_type_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        location_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        nfs_file_share_defaults: Optional[
            pulumi.Input[NfsFileShareNfsFileShareDefaultsArgs]
        ] = ...,
        notification_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        object_acl: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester_pays: Optional[pulumi.Input[_builtins.bool]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        squash: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_endpoint_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="auditDestinationArn")
    def audit_destination_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audit_destination_arn.setter
    def audit_destination_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_region.setter
    def bucket_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> Optional[pulumi.Input[NfsFileShareCacheAttributesArgs]]: ...
    @cache_attributes.setter
    def cache_attributes(
        self, value: Optional[pulumi.Input[NfsFileShareCacheAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientLists")
    def client_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @client_lists.setter
    def client_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultStorageClass")
    def default_storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_storage_class.setter
    def default_storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_share_name.setter
    def file_share_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileshareId")
    def fileshare_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fileshare_id.setter
    def fileshare_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_arn.setter
    def gateway_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="guessMimeTypeEnabled")
    def guess_mime_type_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @guess_mime_type_enabled.setter
    def guess_mime_type_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsEncrypted")
    def kms_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @kms_encrypted.setter
    def kms_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_arn.setter
    def location_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nfsFileShareDefaults")
    def nfs_file_share_defaults(
        self,
    ) -> Optional[pulumi.Input[NfsFileShareNfsFileShareDefaultsArgs]]: ...
    @nfs_file_share_defaults.setter
    def nfs_file_share_defaults(
        self, value: Optional[pulumi.Input[NfsFileShareNfsFileShareDefaultsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationPolicy")
    def notification_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_policy.setter
    def notification_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectAcl")
    def object_acl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_acl.setter
    def object_acl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requesterPays")
    def requester_pays(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @requester_pays.setter
    def requester_pays(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def squash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @squash.setter
    def squash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="vpcEndpointDnsName")
    def vpc_endpoint_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_dns_name.setter
    def vpc_endpoint_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:storagegateway/nfsFileShare:NfsFileShare")
class NfsFileShare(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[
            pulumi.Input[
                Union[
                    NfsFileShareCacheAttributesArgs, NfsFileShareCacheAttributesArgsDict
                ]
            ]
        ] = ...,
        client_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        guess_mime_type_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        location_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        nfs_file_share_defaults: Optional[
            pulumi.Input[
                Union[
                    NfsFileShareNfsFileShareDefaultsArgs,
                    NfsFileShareNfsFileShareDefaultsArgsDict,
                ]
            ]
        ] = ...,
        notification_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        object_acl: Optional[pulumi.Input[_builtins.str]] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester_pays: Optional[pulumi.Input[_builtins.bool]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        squash: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_endpoint_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NfsFileShareArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[
            pulumi.Input[
                Union[
                    NfsFileShareCacheAttributesArgs, NfsFileShareCacheAttributesArgsDict
                ]
            ]
        ] = ...,
        client_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        fileshare_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        guess_mime_type_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        location_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        nfs_file_share_defaults: Optional[
            pulumi.Input[
                Union[
                    NfsFileShareNfsFileShareDefaultsArgs,
                    NfsFileShareNfsFileShareDefaultsArgsDict,
                ]
            ]
        ] = ...,
        notification_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        object_acl: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester_pays: Optional[pulumi.Input[_builtins.bool]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        squash: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_endpoint_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NfsFileShare: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="auditDestinationArn")
    def audit_destination_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> pulumi.Output[Optional[outputs.NfsFileShareCacheAttributes]]: ...
    @_builtins.property
    @pulumi.getter(name="clientLists")
    def client_lists(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultStorageClass")
    def default_storage_class(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileshareId")
    def fileshare_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="guessMimeTypeEnabled")
    def guess_mime_type_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsEncrypted")
    def kms_encrypted(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nfsFileShareDefaults")
    def nfs_file_share_defaults(
        self,
    ) -> pulumi.Output[Optional[outputs.NfsFileShareNfsFileShareDefaults]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationPolicy")
    def notification_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="objectAcl")
    def object_acl(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requesterPays")
    def requester_pays(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def squash(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointDnsName")
    def vpc_endpoint_dns_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
