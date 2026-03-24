import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ClusterArgs", "Cluster"]

@pulumi.input_type
class ClusterArgs:
    def __init__(
        __self__,
        *,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_properties: Optional[
            pulumi.Input[ClusterMultiRegionPropertiesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[ClusterTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsEncryptionKey")
    def kms_encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_encryption_key.setter
    def kms_encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiRegionProperties")
    def multi_region_properties(
        self,
    ) -> Optional[pulumi.Input[ClusterMultiRegionPropertiesArgs]]: ...
    @multi_region_properties.setter
    def multi_region_properties(
        self, value: Optional[pulumi.Input[ClusterMultiRegionPropertiesArgs]]
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
    def timeouts(self) -> Optional[pulumi.Input[ClusterTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ClusterTimeoutsArgs]]): ...

@pulumi.input_type
class _ClusterState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterEncryptionDetailArgs]]]
        ] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_properties: Optional[
            pulumi.Input[ClusterMultiRegionPropertiesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[ClusterTimeoutsArgs]] = ...,
        vpc_endpoint_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionDetails")
    def encryption_details(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterEncryptionDetailArgs]]]
    ]: ...
    @encryption_details.setter
    def encryption_details(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterEncryptionDetailArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsEncryptionKey")
    def kms_encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_encryption_key.setter
    def kms_encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiRegionProperties")
    def multi_region_properties(
        self,
    ) -> Optional[pulumi.Input[ClusterMultiRegionPropertiesArgs]]: ...
    @multi_region_properties.setter
    def multi_region_properties(
        self, value: Optional[pulumi.Input[ClusterMultiRegionPropertiesArgs]]
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
    def timeouts(self) -> Optional[pulumi.Input[ClusterTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ClusterTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceName")
    def vpc_endpoint_service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_service_name.setter
    def vpc_endpoint_service_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:dsql/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_properties: Optional[
            pulumi.Input[
                Union[
                    ClusterMultiRegionPropertiesArgs,
                    ClusterMultiRegionPropertiesArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[ClusterTimeoutsArgs, ClusterTimeoutsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ClusterArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterEncryptionDetailArgs, ClusterEncryptionDetailArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_properties: Optional[
            pulumi.Input[
                Union[
                    ClusterMultiRegionPropertiesArgs,
                    ClusterMultiRegionPropertiesArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[ClusterTimeoutsArgs, ClusterTimeoutsArgsDict]]
        ] = ...,
        vpc_endpoint_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Cluster: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionDetails")
    def encryption_details(
        self,
    ) -> pulumi.Output[Sequence[outputs.ClusterEncryptionDetail]]: ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsEncryptionKey")
    def kms_encryption_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multiRegionProperties")
    def multi_region_properties(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterMultiRegionProperties]]: ...
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
    def timeouts(self) -> pulumi.Output[Optional[outputs.ClusterTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceName")
    def vpc_endpoint_service_name(self) -> pulumi.Output[_builtins.str]: ...
