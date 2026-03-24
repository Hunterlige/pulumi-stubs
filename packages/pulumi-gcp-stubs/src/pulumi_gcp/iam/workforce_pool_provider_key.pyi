import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkforcePoolProviderKeyArgs", "WorkforcePoolProviderKey"]

@pulumi.input_type
class WorkforcePoolProviderKeyArgs:
    def __init__(
        __self__,
        *,
        key_data: pulumi.Input[WorkforcePoolProviderKeyKeyDataArgs],
        key_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        provider_id: pulumi.Input[_builtins.str],
        use: pulumi.Input[_builtins.str],
        workforce_pool_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(self) -> pulumi.Input[WorkforcePoolProviderKeyKeyDataArgs]: ...
    @key_data.setter
    def key_data(self, value: pulumi.Input[WorkforcePoolProviderKeyKeyDataArgs]): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]: ...
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Input[_builtins.str]: ...
    @provider_id.setter
    def provider_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def use(self) -> pulumi.Input[_builtins.str]: ...
    @use.setter
    def use(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @workforce_pool_id.setter
    def workforce_pool_id(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _WorkforcePoolProviderKeyState:
    def __init__(
        __self__,
        *,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        key_data: Optional[pulumi.Input[WorkforcePoolProviderKeyKeyDataArgs]] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        use: Optional[pulumi.Input[_builtins.str]] = ...,
        workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(
        self,
    ) -> Optional[pulumi.Input[WorkforcePoolProviderKeyKeyDataArgs]]: ...
    @key_data.setter
    def key_data(
        self, value: Optional[pulumi.Input[WorkforcePoolProviderKeyKeyDataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="providerId")
    def provider_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider_id.setter
    def provider_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def use(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @use.setter
    def use(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workforce_pool_id.setter
    def workforce_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class WorkforcePoolProviderKey(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        key_data: Optional[
            pulumi.Input[
                Union[
                    WorkforcePoolProviderKeyKeyDataArgs,
                    WorkforcePoolProviderKeyKeyDataArgsDict,
                ]
            ]
        ] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
        use: Optional[pulumi.Input[_builtins.str]] = ...,
        workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkforcePoolProviderKeyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        key_data: Optional[
            pulumi.Input[
                Union[
                    WorkforcePoolProviderKeyKeyDataArgs,
                    WorkforcePoolProviderKeyKeyDataArgsDict,
                ]
            ]
        ] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        use: Optional[pulumi.Input[_builtins.str]] = ...,
        workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> WorkforcePoolProviderKey: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyData")
    def key_data(self) -> pulumi.Output[outputs.WorkforcePoolProviderKeyKeyData]: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def use(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Output[_builtins.str]: ...
