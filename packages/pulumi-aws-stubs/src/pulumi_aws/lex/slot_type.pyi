import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SlotTypeArgs", "SlotType"]

@pulumi.input_type
class SlotTypeArgs:
    def __init__(
        __self__,
        *,
        enumeration_values: pulumi.Input[
            Sequence[pulumi.Input[SlotTypeEnumerationValueArgs]]
        ],
        create_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        value_selection_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enumerationValues")
    def enumeration_values(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[SlotTypeEnumerationValueArgs]]]: ...
    @enumeration_values.setter
    def enumeration_values(
        self, value: pulumi.Input[Sequence[pulumi.Input[SlotTypeEnumerationValueArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createVersion")
    def create_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_version.setter
    def create_version(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valueSelectionStrategy")
    def value_selection_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value_selection_strategy.setter
    def value_selection_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _SlotTypeState:
    def __init__(
        __self__,
        *,
        checksum: Optional[pulumi.Input[_builtins.str]] = ...,
        create_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enumeration_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[SlotTypeEnumerationValueArgs]]]
        ] = ...,
        last_updated_date: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        value_selection_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checksum.setter
    def checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createVersion")
    def create_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_version.setter
    def create_version(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enumerationValues")
    def enumeration_values(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SlotTypeEnumerationValueArgs]]]
    ]: ...
    @enumeration_values.setter
    def enumeration_values(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SlotTypeEnumerationValueArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_date.setter
    def last_updated_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valueSelectionStrategy")
    def value_selection_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value_selection_strategy.setter
    def value_selection_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:lex/slotType:SlotType")
class SlotType(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enumeration_values: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SlotTypeEnumerationValueArgs,
                            SlotTypeEnumerationValueArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        value_selection_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SlotTypeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        checksum: Optional[pulumi.Input[_builtins.str]] = ...,
        create_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enumeration_values: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SlotTypeEnumerationValueArgs,
                            SlotTypeEnumerationValueArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        last_updated_date: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        value_selection_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SlotType: ...
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createVersion")
    def create_version(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enumerationValues")
    def enumeration_values(
        self,
    ) -> pulumi.Output[Sequence[outputs.SlotTypeEnumerationValue]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueSelectionStrategy")
    def value_selection_strategy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
