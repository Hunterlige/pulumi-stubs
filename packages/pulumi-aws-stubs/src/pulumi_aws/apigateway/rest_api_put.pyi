import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RestApiPutArgs", "RestApiPut"]

@pulumi.input_type
class RestApiPutArgs:
    def __init__(
        __self__,
        *,
        body: pulumi.Input[_builtins.str],
        rest_api_id: pulumi.Input[_builtins.str],
        fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[RestApiPutTimeoutsArgs]] = ...,
        triggers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> pulumi.Input[_builtins.str]: ...
    @body.setter
    def body(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Input[_builtins.str]: ...
    @rest_api_id.setter
    def rest_api_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_on_warnings.setter
    def fail_on_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[RestApiPutTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[RestApiPutTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @triggers.setter
    def triggers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _RestApiPutState:
    def __init__(
        __self__,
        *,
        body: Optional[pulumi.Input[_builtins.str]] = ...,
        fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[RestApiPutTimeoutsArgs]] = ...,
        triggers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_on_warnings.setter
    def fail_on_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rest_api_id.setter
    def rest_api_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[RestApiPutTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[RestApiPutTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @triggers.setter
    def triggers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:apigateway/restApiPut:RestApiPut")
class RestApiPut(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        body: Optional[pulumi.Input[_builtins.str]] = ...,
        fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[RestApiPutTimeoutsArgs, RestApiPutTimeoutsArgsDict]]
        ] = ...,
        triggers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RestApiPutArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        body: Optional[pulumi.Input[_builtins.str]] = ...,
        fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[RestApiPutTimeoutsArgs, RestApiPutTimeoutsArgsDict]]
        ] = ...,
        triggers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> RestApiPut: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.RestApiPutTimeouts]]: ...
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
