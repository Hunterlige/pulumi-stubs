import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserDefinedFunctionArgs", "UserDefinedFunction"]

@pulumi.input_type
class UserDefinedFunctionArgs:
    def __init__(
        __self__,
        *,
        class_name: pulumi.Input[_builtins.str],
        database_name: pulumi.Input[_builtins.str],
        owner_name: pulumi.Input[_builtins.str],
        owner_type: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserDefinedFunctionResourceUriArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="className")
    def class_name(self) -> pulumi.Input[_builtins.str]: ...
    @class_name.setter
    def class_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ownerName")
    def owner_name(self) -> pulumi.Input[_builtins.str]: ...
    @owner_name.setter
    def owner_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ownerType")
    def owner_type(self) -> pulumi.Input[_builtins.str]: ...
    @owner_type.setter
    def owner_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="resourceUris")
    def resource_uris(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[UserDefinedFunctionResourceUriArgs]]]
    ]: ...
    @resource_uris.setter
    def resource_uris(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserDefinedFunctionResourceUriArgs]]]
        ],
    ): ...

@pulumi.input_type
class _UserDefinedFunctionState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        class_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserDefinedFunctionResourceUriArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="className")
    def class_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @class_name.setter
    def class_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerName")
    def owner_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_name.setter
    def owner_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerType")
    def owner_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_type.setter
    def owner_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceUris")
    def resource_uris(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[UserDefinedFunctionResourceUriArgs]]]
    ]: ...
    @resource_uris.setter
    def resource_uris(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserDefinedFunctionResourceUriArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:glue/userDefinedFunction:UserDefinedFunction")
class UserDefinedFunction(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        class_name: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uris: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            UserDefinedFunctionResourceUriArgs,
                            UserDefinedFunctionResourceUriArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UserDefinedFunctionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        class_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uris: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            UserDefinedFunctionResourceUriArgs,
                            UserDefinedFunctionResourceUriArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> UserDefinedFunction: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="className")
    def class_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerName")
    def owner_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerType")
    def owner_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceUris")
    def resource_uris(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.UserDefinedFunctionResourceUri]]]: ...
