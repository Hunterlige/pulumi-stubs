import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ExtensionsInstanceArgs", "ExtensionsInstance"]

@pulumi.input_type
class ExtensionsInstanceArgs:
    def __init__(
        __self__,
        *,
        config: pulumi.Input[ExtensionsInstanceConfigArgs],
        instance_id: pulumi.Input[_builtins.str],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Input[ExtensionsInstanceConfigArgs]: ...
    @config.setter
    def config(self, value: pulumi.Input[ExtensionsInstanceConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ExtensionsInstanceState:
    def __init__(
        __self__,
        *,
        config: Optional[pulumi.Input[ExtensionsInstanceConfigArgs]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        error_statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExtensionsInstanceErrorStatusArgs]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_operation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        last_operation_type: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_datas: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExtensionsInstanceRuntimeDataArgs]]]
        ] = ...,
        service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[ExtensionsInstanceConfigArgs]]: ...
    @config.setter
    def config(self, value: Optional[pulumi.Input[ExtensionsInstanceConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorStatuses")
    def error_statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExtensionsInstanceErrorStatusArgs]]]
    ]: ...
    @error_statuses.setter
    def error_statuses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExtensionsInstanceErrorStatusArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastOperationName")
    def last_operation_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_operation_name.setter
    def last_operation_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastOperationType")
    def last_operation_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_operation_type.setter
    def last_operation_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter(name="runtimeDatas")
    def runtime_datas(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExtensionsInstanceRuntimeDataArgs]]]
    ]: ...
    @runtime_datas.setter
    def runtime_datas(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExtensionsInstanceRuntimeDataArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:firebase/extensionsInstance:ExtensionsInstance")
class ExtensionsInstance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        config: Optional[
            pulumi.Input[
                Union[ExtensionsInstanceConfigArgs, ExtensionsInstanceConfigArgsDict]
            ]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ExtensionsInstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        config: Optional[
            pulumi.Input[
                Union[ExtensionsInstanceConfigArgs, ExtensionsInstanceConfigArgsDict]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        error_statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExtensionsInstanceErrorStatusArgs,
                            ExtensionsInstanceErrorStatusArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_operation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        last_operation_type: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_datas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExtensionsInstanceRuntimeDataArgs,
                            ExtensionsInstanceRuntimeDataArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ExtensionsInstance: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Output[outputs.ExtensionsInstanceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorStatuses")
    def error_statuses(
        self,
    ) -> pulumi.Output[Sequence[outputs.ExtensionsInstanceErrorStatus]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastOperationName")
    def last_operation_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastOperationType")
    def last_operation_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeDatas")
    def runtime_datas(
        self,
    ) -> pulumi.Output[Sequence[outputs.ExtensionsInstanceRuntimeData]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
