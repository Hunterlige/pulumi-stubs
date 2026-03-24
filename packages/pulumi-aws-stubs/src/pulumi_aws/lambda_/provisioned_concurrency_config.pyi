import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProvisionedConcurrencyConfigArgs", "ProvisionedConcurrencyConfig"]

@pulumi.input_type
class ProvisionedConcurrencyConfigArgs:
    def __init__(
        __self__,
        *,
        function_name: pulumi.Input[_builtins.str],
        provisioned_concurrent_executions: pulumi.Input[_builtins.int],
        qualifier: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[_builtins.str]: ...
    @function_name.setter
    def function_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedConcurrentExecutions")
    def provisioned_concurrent_executions(self) -> pulumi.Input[_builtins.int]: ...
    @provisioned_concurrent_executions.setter
    def provisioned_concurrent_executions(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> pulumi.Input[_builtins.str]: ...
    @qualifier.setter
    def qualifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _ProvisionedConcurrencyConfigState:
    def __init__(
        __self__,
        *,
        function_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_concurrent_executions: Optional[pulumi.Input[_builtins.int]] = ...,
        qualifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @function_name.setter
    def function_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedConcurrentExecutions")
    def provisioned_concurrent_executions(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_concurrent_executions.setter
    def provisioned_concurrent_executions(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @qualifier.setter
    def qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token(...)
class ProvisionedConcurrencyConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        function_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_concurrent_executions: Optional[pulumi.Input[_builtins.int]] = ...,
        qualifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProvisionedConcurrencyConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        function_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_concurrent_executions: Optional[pulumi.Input[_builtins.int]] = ...,
        qualifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> ProvisionedConcurrencyConfig: ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedConcurrentExecutions")
    def provisioned_concurrent_executions(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
