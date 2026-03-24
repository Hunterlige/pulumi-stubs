import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AiRagEngineConfigArgs", "AiRagEngineConfig"]

@pulumi.input_type
class AiRagEngineConfigArgs:
    def __init__(
        __self__,
        *,
        rag_managed_db_config: pulumi.Input[AiRagEngineConfigRagManagedDbConfigArgs],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ragManagedDbConfig")
    def rag_managed_db_config(
        self,
    ) -> pulumi.Input[AiRagEngineConfigRagManagedDbConfigArgs]: ...
    @rag_managed_db_config.setter
    def rag_managed_db_config(
        self, value: pulumi.Input[AiRagEngineConfigRagManagedDbConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AiRagEngineConfigState:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rag_managed_db_config: Optional[
            pulumi.Input[AiRagEngineConfigRagManagedDbConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="ragManagedDbConfig")
    def rag_managed_db_config(
        self,
    ) -> Optional[pulumi.Input[AiRagEngineConfigRagManagedDbConfigArgs]]: ...
    @rag_managed_db_config.setter
    def rag_managed_db_config(
        self, value: Optional[pulumi.Input[AiRagEngineConfigRagManagedDbConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:vertex/aiRagEngineConfig:AiRagEngineConfig")
class AiRagEngineConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rag_managed_db_config: Optional[
            pulumi.Input[
                Union[
                    AiRagEngineConfigRagManagedDbConfigArgs,
                    AiRagEngineConfigRagManagedDbConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AiRagEngineConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rag_managed_db_config: Optional[
            pulumi.Input[
                Union[
                    AiRagEngineConfigRagManagedDbConfigArgs,
                    AiRagEngineConfigRagManagedDbConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AiRagEngineConfig: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ragManagedDbConfig")
    def rag_managed_db_config(
        self,
    ) -> pulumi.Output[outputs.AiRagEngineConfigRagManagedDbConfig]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
