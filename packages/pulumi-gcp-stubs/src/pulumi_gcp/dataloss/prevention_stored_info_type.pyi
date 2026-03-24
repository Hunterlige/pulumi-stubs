import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PreventionStoredInfoTypeArgs", "PreventionStoredInfoType"]

@pulumi.input_type
class PreventionStoredInfoTypeArgs:
    def __init__(
        __self__,
        *,
        parent: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dictionary: Optional[
            pulumi.Input[PreventionStoredInfoTypeDictionaryArgs]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        large_custom_dictionary: Optional[
            pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryArgs]
        ] = ...,
        regex: Optional[pulumi.Input[PreventionStoredInfoTypeRegexArgs]] = ...,
        stored_info_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dictionary(
        self,
    ) -> Optional[pulumi.Input[PreventionStoredInfoTypeDictionaryArgs]]: ...
    @dictionary.setter
    def dictionary(
        self, value: Optional[pulumi.Input[PreventionStoredInfoTypeDictionaryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="largeCustomDictionary")
    def large_custom_dictionary(
        self,
    ) -> Optional[pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryArgs]]: ...
    @large_custom_dictionary.setter
    def large_custom_dictionary(
        self,
        value: Optional[
            pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[PreventionStoredInfoTypeRegexArgs]]: ...
    @regex.setter
    def regex(
        self, value: Optional[pulumi.Input[PreventionStoredInfoTypeRegexArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storedInfoTypeId")
    def stored_info_type_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stored_info_type_id.setter
    def stored_info_type_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PreventionStoredInfoTypeState:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dictionary: Optional[
            pulumi.Input[PreventionStoredInfoTypeDictionaryArgs]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        large_custom_dictionary: Optional[
            pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[pulumi.Input[PreventionStoredInfoTypeRegexArgs]] = ...,
        stored_info_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dictionary(
        self,
    ) -> Optional[pulumi.Input[PreventionStoredInfoTypeDictionaryArgs]]: ...
    @dictionary.setter
    def dictionary(
        self, value: Optional[pulumi.Input[PreventionStoredInfoTypeDictionaryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="largeCustomDictionary")
    def large_custom_dictionary(
        self,
    ) -> Optional[pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryArgs]]: ...
    @large_custom_dictionary.setter
    def large_custom_dictionary(
        self,
        value: Optional[
            pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[PreventionStoredInfoTypeRegexArgs]]: ...
    @regex.setter
    def regex(
        self, value: Optional[pulumi.Input[PreventionStoredInfoTypeRegexArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storedInfoTypeId")
    def stored_info_type_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stored_info_type_id.setter
    def stored_info_type_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class PreventionStoredInfoType(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dictionary: Optional[
            pulumi.Input[
                Union[
                    PreventionStoredInfoTypeDictionaryArgs,
                    PreventionStoredInfoTypeDictionaryArgsDict,
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        large_custom_dictionary: Optional[
            pulumi.Input[
                Union[
                    PreventionStoredInfoTypeLargeCustomDictionaryArgs,
                    PreventionStoredInfoTypeLargeCustomDictionaryArgsDict,
                ]
            ]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[
            pulumi.Input[
                Union[
                    PreventionStoredInfoTypeRegexArgs,
                    PreventionStoredInfoTypeRegexArgsDict,
                ]
            ]
        ] = ...,
        stored_info_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PreventionStoredInfoTypeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dictionary: Optional[
            pulumi.Input[
                Union[
                    PreventionStoredInfoTypeDictionaryArgs,
                    PreventionStoredInfoTypeDictionaryArgsDict,
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        large_custom_dictionary: Optional[
            pulumi.Input[
                Union[
                    PreventionStoredInfoTypeLargeCustomDictionaryArgs,
                    PreventionStoredInfoTypeLargeCustomDictionaryArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[
            pulumi.Input[
                Union[
                    PreventionStoredInfoTypeRegexArgs,
                    PreventionStoredInfoTypeRegexArgsDict,
                ]
            ]
        ] = ...,
        stored_info_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PreventionStoredInfoType: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def dictionary(
        self,
    ) -> pulumi.Output[Optional[outputs.PreventionStoredInfoTypeDictionary]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="largeCustomDictionary")
    def large_custom_dictionary(
        self,
    ) -> pulumi.Output[
        Optional[outputs.PreventionStoredInfoTypeLargeCustomDictionary]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regex(
        self,
    ) -> pulumi.Output[Optional[outputs.PreventionStoredInfoTypeRegex]]: ...
    @_builtins.property
    @pulumi.getter(name="storedInfoTypeId")
    def stored_info_type_id(self) -> pulumi.Output[_builtins.str]: ...
