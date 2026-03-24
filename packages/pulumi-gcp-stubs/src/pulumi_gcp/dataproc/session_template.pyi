import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SessionTemplateArgs", "SessionTemplate"]

@pulumi.input_type
class SessionTemplateArgs:
    def __init__(
        __self__,
        *,
        environment_config: Optional[
            pulumi.Input[SessionTemplateEnvironmentConfigArgs]
        ] = ...,
        jupyter_session: Optional[
            pulumi.Input[SessionTemplateJupyterSessionArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_config: Optional[pulumi.Input[SessionTemplateRuntimeConfigArgs]] = ...,
        spark_connect_session: Optional[
            pulumi.Input[SessionTemplateSparkConnectSessionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="environmentConfig")
    def environment_config(
        self,
    ) -> Optional[pulumi.Input[SessionTemplateEnvironmentConfigArgs]]: ...
    @environment_config.setter
    def environment_config(
        self, value: Optional[pulumi.Input[SessionTemplateEnvironmentConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jupyterSession")
    def jupyter_session(
        self,
    ) -> Optional[pulumi.Input[SessionTemplateJupyterSessionArgs]]: ...
    @jupyter_session.setter
    def jupyter_session(
        self, value: Optional[pulumi.Input[SessionTemplateJupyterSessionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfig")
    def runtime_config(
        self,
    ) -> Optional[pulumi.Input[SessionTemplateRuntimeConfigArgs]]: ...
    @runtime_config.setter
    def runtime_config(
        self, value: Optional[pulumi.Input[SessionTemplateRuntimeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkConnectSession")
    def spark_connect_session(
        self,
    ) -> Optional[pulumi.Input[SessionTemplateSparkConnectSessionArgs]]: ...
    @spark_connect_session.setter
    def spark_connect_session(
        self, value: Optional[pulumi.Input[SessionTemplateSparkConnectSessionArgs]]
    ): ...

@pulumi.input_type
class _SessionTemplateState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        environment_config: Optional[
            pulumi.Input[SessionTemplateEnvironmentConfigArgs]
        ] = ...,
        jupyter_session: Optional[
            pulumi.Input[SessionTemplateJupyterSessionArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        runtime_config: Optional[pulumi.Input[SessionTemplateRuntimeConfigArgs]] = ...,
        spark_connect_session: Optional[
            pulumi.Input[SessionTemplateSparkConnectSessionArgs]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        uuid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def creator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creator.setter
    def creator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentConfig")
    def environment_config(
        self,
    ) -> Optional[pulumi.Input[SessionTemplateEnvironmentConfigArgs]]: ...
    @environment_config.setter
    def environment_config(
        self, value: Optional[pulumi.Input[SessionTemplateEnvironmentConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jupyterSession")
    def jupyter_session(
        self,
    ) -> Optional[pulumi.Input[SessionTemplateJupyterSessionArgs]]: ...
    @jupyter_session.setter
    def jupyter_session(
        self, value: Optional[pulumi.Input[SessionTemplateJupyterSessionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfig")
    def runtime_config(
        self,
    ) -> Optional[pulumi.Input[SessionTemplateRuntimeConfigArgs]]: ...
    @runtime_config.setter
    def runtime_config(
        self, value: Optional[pulumi.Input[SessionTemplateRuntimeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkConnectSession")
    def spark_connect_session(
        self,
    ) -> Optional[pulumi.Input[SessionTemplateSparkConnectSessionArgs]]: ...
    @spark_connect_session.setter
    def spark_connect_session(
        self, value: Optional[pulumi.Input[SessionTemplateSparkConnectSessionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:dataproc/sessionTemplate:SessionTemplate")
class SessionTemplate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        environment_config: Optional[
            pulumi.Input[
                Union[
                    SessionTemplateEnvironmentConfigArgs,
                    SessionTemplateEnvironmentConfigArgsDict,
                ]
            ]
        ] = ...,
        jupyter_session: Optional[
            pulumi.Input[
                Union[
                    SessionTemplateJupyterSessionArgs,
                    SessionTemplateJupyterSessionArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_config: Optional[
            pulumi.Input[
                Union[
                    SessionTemplateRuntimeConfigArgs,
                    SessionTemplateRuntimeConfigArgsDict,
                ]
            ]
        ] = ...,
        spark_connect_session: Optional[
            pulumi.Input[
                Union[
                    SessionTemplateSparkConnectSessionArgs,
                    SessionTemplateSparkConnectSessionArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[SessionTemplateArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        environment_config: Optional[
            pulumi.Input[
                Union[
                    SessionTemplateEnvironmentConfigArgs,
                    SessionTemplateEnvironmentConfigArgsDict,
                ]
            ]
        ] = ...,
        jupyter_session: Optional[
            pulumi.Input[
                Union[
                    SessionTemplateJupyterSessionArgs,
                    SessionTemplateJupyterSessionArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        runtime_config: Optional[
            pulumi.Input[
                Union[
                    SessionTemplateRuntimeConfigArgs,
                    SessionTemplateRuntimeConfigArgsDict,
                ]
            ]
        ] = ...,
        spark_connect_session: Optional[
            pulumi.Input[
                Union[
                    SessionTemplateSparkConnectSessionArgs,
                    SessionTemplateSparkConnectSessionArgsDict,
                ]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        uuid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SessionTemplate: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def creator(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="environmentConfig")
    def environment_config(
        self,
    ) -> pulumi.Output[Optional[outputs.SessionTemplateEnvironmentConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="jupyterSession")
    def jupyter_session(
        self,
    ) -> pulumi.Output[Optional[outputs.SessionTemplateJupyterSession]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeConfig")
    def runtime_config(
        self,
    ) -> pulumi.Output[Optional[outputs.SessionTemplateRuntimeConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="sparkConnectSession")
    def spark_connect_session(
        self,
    ) -> pulumi.Output[Optional[outputs.SessionTemplateSparkConnectSession]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[_builtins.str]: ...
