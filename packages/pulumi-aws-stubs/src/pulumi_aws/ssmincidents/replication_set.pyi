import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReplicationSetArgs", "ReplicationSet"]

@pulumi.input_type
class ReplicationSetArgs:
    def __init__(
        __self__,
        *,
        region: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]
        ] = ...,
        regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""region is deprecated. Use regions instead.""")
    def region(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]]: ...
    @region.setter
    def region(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]]: ...
    @regions.setter
    def regions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]],
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

@pulumi.input_type
class _ReplicationSetState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protected: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_modified_by: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]
        ] = ...,
        regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtected")
    def deletion_protected(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protected.setter
    def deletion_protected(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modified_by.setter
    def last_modified_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""region is deprecated. Use regions instead.""")
    def region(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]]: ...
    @region.setter
    def region(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]]: ...
    @regions.setter
    def regions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReplicationSetRegionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:ssmincidents/replicationSet:ReplicationSet")
class ReplicationSet(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReplicationSetRegionArgs, ReplicationSetRegionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        regions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReplicationSetRegionArgs, ReplicationSetRegionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ReplicationSetArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protected: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_modified_by: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReplicationSetRegionArgs, ReplicationSetRegionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        regions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReplicationSetRegionArgs, ReplicationSetRegionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> ReplicationSet: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtected")
    def deletion_protected(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""region is deprecated. Use regions instead.""")
    def region(self) -> pulumi.Output[Sequence[outputs.ReplicationSetRegion]]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence[outputs.ReplicationSetRegion]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
