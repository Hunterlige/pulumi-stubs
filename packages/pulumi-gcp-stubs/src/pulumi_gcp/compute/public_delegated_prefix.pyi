import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PublicDelegatedPrefixArgs", "PublicDelegatedPrefix"]

@pulumi.input_type
class PublicDelegatedPrefixArgs:
    def __init__(
        __self__,
        *,
        ip_cidr_range: pulumi.Input[_builtins.str],
        parent_prefix: pulumi.Input[_builtins.str],
        region: pulumi.Input[_builtins.str],
        allocatable_prefix_length: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_live_migration: Optional[pulumi.Input[_builtins.bool]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Input[_builtins.str]: ...
    @ip_cidr_range.setter
    def ip_cidr_range(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="parentPrefix")
    def parent_prefix(self) -> pulumi.Input[_builtins.str]: ...
    @parent_prefix.setter
    def parent_prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allocatablePrefixLength")
    def allocatable_prefix_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocatable_prefix_length.setter
    def allocatable_prefix_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isLiveMigration")
    def is_live_migration(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_live_migration.setter
    def is_live_migration(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PublicDelegatedPrefixState:
    def __init__(
        __self__,
        *,
        allocatable_prefix_length: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_enhanced_ipv4_allocation: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        is_live_migration: Optional[pulumi.Input[_builtins.bool]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        public_delegated_sub_prefixs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PublicDelegatedPrefixPublicDelegatedSubPrefixArgs]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatablePrefixLength")
    def allocatable_prefix_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @allocatable_prefix_length.setter
    def allocatable_prefix_length(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableEnhancedIpv4Allocation")
    def enable_enhanced_ipv4_allocation(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_enhanced_ipv4_allocation.setter
    def enable_enhanced_ipv4_allocation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_cidr_range.setter
    def ip_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_access_type.setter
    def ipv6_access_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isLiveMigration")
    def is_live_migration(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_live_migration.setter
    def is_live_migration(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentPrefix")
    def parent_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_prefix.setter
    def parent_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicDelegatedSubPrefixs")
    def public_delegated_sub_prefixs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PublicDelegatedPrefixPublicDelegatedSubPrefixArgs]]
        ]
    ]: ...
    @public_delegated_sub_prefixs.setter
    def public_delegated_sub_prefixs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PublicDelegatedPrefixPublicDelegatedSubPrefixArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class PublicDelegatedPrefix(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allocatable_prefix_length: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ...,
        is_live_migration: Optional[pulumi.Input[_builtins.bool]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PublicDelegatedPrefixArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allocatable_prefix_length: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_enhanced_ipv4_allocation: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        is_live_migration: Optional[pulumi.Input[_builtins.bool]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        public_delegated_sub_prefixs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PublicDelegatedPrefixPublicDelegatedSubPrefixArgs,
                            PublicDelegatedPrefixPublicDelegatedSubPrefixArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PublicDelegatedPrefix: ...
    @_builtins.property
    @pulumi.getter(name="allocatablePrefixLength")
    def allocatable_prefix_length(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableEnhancedIpv4Allocation")
    def enable_enhanced_ipv4_allocation(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isLiveMigration")
    def is_live_migration(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parentPrefix")
    def parent_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicDelegatedSubPrefixs")
    def public_delegated_sub_prefixs(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.PublicDelegatedPrefixPublicDelegatedSubPrefix]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
