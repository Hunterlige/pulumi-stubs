import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BackendEnvironmentArgs", "BackendEnvironment"]

@pulumi.input_type
class BackendEnvironmentArgs:
    def __init__(
        __self__,
        *,
        app_id: pulumi.Input[_builtins.str],
        environment_name: pulumi.Input[_builtins.str],
        deployment_artifacts: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[_builtins.str]: ...
    @app_id.setter
    def app_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[_builtins.str]: ...
    @environment_name.setter
    def environment_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentArtifacts")
    def deployment_artifacts(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_artifacts.setter
    def deployment_artifacts(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stackName")
    def stack_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stack_name.setter
    def stack_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _BackendEnvironmentState:
    def __init__(
        __self__,
        *,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_artifacts: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentArtifacts")
    def deployment_artifacts(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_artifacts.setter
    def deployment_artifacts(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stackName")
    def stack_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stack_name.setter
    def stack_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:amplify/backendEnvironment:BackendEnvironment")
class BackendEnvironment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_artifacts: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BackendEnvironmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_artifacts: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> BackendEnvironment: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentArtifacts")
    def deployment_artifacts(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stackName")
    def stack_name(self) -> pulumi.Output[_builtins.str]: ...
