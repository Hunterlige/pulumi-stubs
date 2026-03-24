import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SmbFileShareArgs", "SmbFileShare"]

@pulumi.input_type
class SmbFileShareArgs:
    def __init__(
        __self__,
        *,
        gateway_arn: pulumi.Input[_builtins.str],
        location_arn: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        access_based_enumeration: Optional[pulumi.Input[_builtins.bool]] = ...,
        admin_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[pulumi.Input[SmbFileShareCacheAttributesArgs]] = ...,
        case_sensitivity: Optional[pulumi.Input[_builtins.str]] = ...,
        default_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        guess_mime_type_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        invalid_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        object_acl: Optional[pulumi.Input[_builtins.str]] = ...,
        oplocks_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester_pays: Optional[pulumi.Input[_builtins.bool]] = ...,
        smb_acl_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        valid_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_endpoint_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="accessBasedEnumeration")
    def access_based_enumeration(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @access_based_enumeration.setter
    def access_based_enumeration(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="adminUserLists")
    def admin_user_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @admin_user_lists.setter
    def admin_user_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="auditDestinationArn")
    def audit_destination_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audit_destination_arn.setter
    def audit_destination_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_region.setter
    def bucket_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> Optional[pulumi.Input[SmbFileShareCacheAttributesArgs]]: ...
    @cache_attributes.setter
    def cache_attributes(
        self, value: Optional[pulumi.Input[SmbFileShareCacheAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="caseSensitivity")
    def case_sensitivity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @case_sensitivity.setter
    def case_sensitivity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="invalidUserLists")
    def invalid_user_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @invalid_user_lists.setter
    def invalid_user_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    @pulumi.getter(name="oplocksEnabled")
    def oplocks_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @oplocks_enabled.setter
    def oplocks_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="smbAclEnabled")
    def smb_acl_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @smb_acl_enabled.setter
    def smb_acl_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="validUserLists")
    def valid_user_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @valid_user_lists.setter
    def valid_user_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointDnsName")
    def vpc_endpoint_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_dns_name.setter
    def vpc_endpoint_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SmbFileShareState:
    def __init__(
        __self__,
        *,
        access_based_enumeration: Optional[pulumi.Input[_builtins.bool]] = ...,
        admin_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[pulumi.Input[SmbFileShareCacheAttributesArgs]] = ...,
        case_sensitivity: Optional[pulumi.Input[_builtins.str]] = ...,
        default_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        fileshare_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        guess_mime_type_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        invalid_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        location_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        object_acl: Optional[pulumi.Input[_builtins.str]] = ...,
        oplocks_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester_pays: Optional[pulumi.Input[_builtins.bool]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        smb_acl_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        valid_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_endpoint_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessBasedEnumeration")
    def access_based_enumeration(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @access_based_enumeration.setter
    def access_based_enumeration(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="adminUserLists")
    def admin_user_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @admin_user_lists.setter
    def admin_user_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_region.setter
    def bucket_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> Optional[pulumi.Input[SmbFileShareCacheAttributesArgs]]: ...
    @cache_attributes.setter
    def cache_attributes(
        self, value: Optional[pulumi.Input[SmbFileShareCacheAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="caseSensitivity")
    def case_sensitivity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @case_sensitivity.setter
    def case_sensitivity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="invalidUserLists")
    def invalid_user_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @invalid_user_lists.setter
    def invalid_user_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    @pulumi.getter(name="oplocksEnabled")
    def oplocks_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @oplocks_enabled.setter
    def oplocks_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="smbAclEnabled")
    def smb_acl_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @smb_acl_enabled.setter
    def smb_acl_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="validUserLists")
    def valid_user_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @valid_user_lists.setter
    def valid_user_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointDnsName")
    def vpc_endpoint_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_dns_name.setter
    def vpc_endpoint_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:storagegateway/smbFileShare:SmbFileShare")
class SmbFileShare(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_based_enumeration: Optional[pulumi.Input[_builtins.bool]] = ...,
        admin_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[
            pulumi.Input[
                Union[
                    SmbFileShareCacheAttributesArgs, SmbFileShareCacheAttributesArgsDict
                ]
            ]
        ] = ...,
        case_sensitivity: Optional[pulumi.Input[_builtins.str]] = ...,
        default_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        guess_mime_type_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        invalid_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        location_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        object_acl: Optional[pulumi.Input[_builtins.str]] = ...,
        oplocks_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester_pays: Optional[pulumi.Input[_builtins.bool]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        smb_acl_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        valid_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_endpoint_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SmbFileShareArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_based_enumeration: Optional[pulumi.Input[_builtins.bool]] = ...,
        admin_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[
            pulumi.Input[
                Union[
                    SmbFileShareCacheAttributesArgs, SmbFileShareCacheAttributesArgsDict
                ]
            ]
        ] = ...,
        case_sensitivity: Optional[pulumi.Input[_builtins.str]] = ...,
        default_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        file_share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        fileshare_id: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        guess_mime_type_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        invalid_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        location_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        object_acl: Optional[pulumi.Input[_builtins.str]] = ...,
        oplocks_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester_pays: Optional[pulumi.Input[_builtins.bool]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        smb_acl_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        valid_user_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_endpoint_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SmbFileShare: ...
    @_builtins.property
    @pulumi.getter(name="accessBasedEnumeration")
    def access_based_enumeration(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="adminUserLists")
    def admin_user_lists(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="auditDestinationArn")
    def audit_destination_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> pulumi.Output[Optional[outputs.SmbFileShareCacheAttributes]]: ...
    @_builtins.property
    @pulumi.getter(name="caseSensitivity")
    def case_sensitivity(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter(name="invalidUserLists")
    def invalid_user_lists(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
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
    @pulumi.getter(name="notificationPolicy")
    def notification_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="objectAcl")
    def object_acl(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="oplocksEnabled")
    def oplocks_enabled(self) -> pulumi.Output[_builtins.bool]: ...
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
    @pulumi.getter(name="smbAclEnabled")
    def smb_acl_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="validUserLists")
    def valid_user_lists(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointDnsName")
    def vpc_endpoint_dns_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
