import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FileSystemAssociationArgs", "FileSystemAssociation"]

@pulumi.input_type
class FileSystemAssociationArgs:
    def __init__(
        __self__,
        *,
        gateway_arn: pulumi.Input[_builtins.str],
        location_arn: pulumi.Input[_builtins.str],
        password: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[
            pulumi.Input[FileSystemAssociationCacheAttributesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
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
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]: ...
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="auditDestinationArn")
    def audit_destination_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audit_destination_arn.setter
    def audit_destination_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> Optional[pulumi.Input[FileSystemAssociationCacheAttributesArgs]]: ...
    @cache_attributes.setter
    def cache_attributes(
        self, value: Optional[pulumi.Input[FileSystemAssociationCacheAttributesArgs]]
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

@pulumi.input_type
class _FileSystemAssociationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[
            pulumi.Input[FileSystemAssociationCacheAttributesArgs]
        ] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        location_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> Optional[pulumi.Input[FileSystemAssociationCacheAttributesArgs]]: ...
    @cache_attributes.setter
    def cache_attributes(
        self, value: Optional[pulumi.Input[FileSystemAssociationCacheAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_arn.setter
    def gateway_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_arn.setter
    def location_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class FileSystemAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        audit_destination_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_attributes: Optional[
            pulumi.Input[
                Union[
                    FileSystemAssociationCacheAttributesArgs,
                    FileSystemAssociationCacheAttributesArgsDict,
                ]
            ]
        ] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        location_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FileSystemAssociationArgs,
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
        cache_attributes: Optional[
            pulumi.Input[
                Union[
                    FileSystemAssociationCacheAttributesArgs,
                    FileSystemAssociationCacheAttributesArgsDict,
                ]
            ]
        ] = ...,
        gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        location_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> FileSystemAssociation: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="auditDestinationArn")
    def audit_destination_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cacheAttributes")
    def cache_attributes(
        self,
    ) -> pulumi.Output[Optional[outputs.FileSystemAssociationCacheAttributes]]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Output[_builtins.str]: ...
