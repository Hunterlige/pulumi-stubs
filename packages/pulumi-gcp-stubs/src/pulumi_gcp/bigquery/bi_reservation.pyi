import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BiReservationArgs", "BiReservation"]

@pulumi.input_type
class BiReservationArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        preferred_tables: Optional[
            pulumi.Input[Sequence[pulumi.Input[BiReservationPreferredTableArgs]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        size: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="preferredTables")
    def preferred_tables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BiReservationPreferredTableArgs]]]
    ]: ...
    @preferred_tables.setter
    def preferred_tables(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BiReservationPreferredTableArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _BiReservationState:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_tables: Optional[
            pulumi.Input[Sequence[pulumi.Input[BiReservationPreferredTableArgs]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        size: Optional[pulumi.Input[_builtins.int]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredTables")
    def preferred_tables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BiReservationPreferredTableArgs]]]
    ]: ...
    @preferred_tables.setter
    def preferred_tables(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BiReservationPreferredTableArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:bigquery/biReservation:BiReservation")
class BiReservation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BiReservationPreferredTableArgs,
                            BiReservationPreferredTableArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        size: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BiReservationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BiReservationPreferredTableArgs,
                            BiReservationPreferredTableArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        size: Optional[pulumi.Input[_builtins.int]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> BiReservation: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredTables")
    def preferred_tables(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.BiReservationPreferredTable]]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
