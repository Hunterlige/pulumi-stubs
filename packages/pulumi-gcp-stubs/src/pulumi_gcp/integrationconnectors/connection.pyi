import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConnectionArgs", "Connection"]

@pulumi.input_type
class ConnectionArgs:
    def __init__(
        __self__,
        *,
        connector_version: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        auth_config: Optional[pulumi.Input[ConnectionAuthConfigArgs]] = ...,
        config_variables: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionConfigVariableArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionDestinationConfigArgs]]]
        ] = ...,
        eventing_config: Optional[pulumi.Input[ConnectionEventingConfigArgs]] = ...,
        eventing_enablement_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        lock_config: Optional[pulumi.Input[ConnectionLockConfigArgs]] = ...,
        log_config: Optional[pulumi.Input[ConnectionLogConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_config: Optional[pulumi.Input[ConnectionNodeConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_config: Optional[pulumi.Input[ConnectionSslConfigArgs]] = ...,
        suspended: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorVersion")
    def connector_version(self) -> pulumi.Input[_builtins.str]: ...
    @connector_version.setter
    def connector_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(self) -> Optional[pulumi.Input[ConnectionAuthConfigArgs]]: ...
    @auth_config.setter
    def auth_config(self, value: Optional[pulumi.Input[ConnectionAuthConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="configVariables")
    def config_variables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionConfigVariableArgs]]]
    ]: ...
    @config_variables.setter
    def config_variables(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionConfigVariableArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationConfigs")
    def destination_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionDestinationConfigArgs]]]
    ]: ...
    @destination_configs.setter
    def destination_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionDestinationConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventingConfig")
    def eventing_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionEventingConfigArgs]]: ...
    @eventing_config.setter
    def eventing_config(
        self, value: Optional[pulumi.Input[ConnectionEventingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventingEnablementType")
    def eventing_enablement_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eventing_enablement_type.setter
    def eventing_enablement_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter(name="lockConfig")
    def lock_config(self) -> Optional[pulumi.Input[ConnectionLockConfigArgs]]: ...
    @lock_config.setter
    def lock_config(self, value: Optional[pulumi.Input[ConnectionLockConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[ConnectionLogConfigArgs]]: ...
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[ConnectionLogConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[ConnectionNodeConfigArgs]]: ...
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[ConnectionNodeConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(self) -> Optional[pulumi.Input[ConnectionSslConfigArgs]]: ...
    @ssl_config.setter
    def ssl_config(self, value: Optional[pulumi.Input[ConnectionSslConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def suspended(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @suspended.setter
    def suspended(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _ConnectionState:
    def __init__(
        __self__,
        *,
        auth_config: Optional[pulumi.Input[ConnectionAuthConfigArgs]] = ...,
        config_variables: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionConfigVariableArgs]]]
        ] = ...,
        connection_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        connector_version: Optional[pulumi.Input[_builtins.str]] = ...,
        connector_version_infra_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionConnectorVersionInfraConfigArgs]]
            ]
        ] = ...,
        connector_version_launch_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionDestinationConfigArgs]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        eventing_config: Optional[pulumi.Input[ConnectionEventingConfigArgs]] = ...,
        eventing_enablement_type: Optional[pulumi.Input[_builtins.str]] = ...,
        eventing_runtime_datas: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionEventingRuntimeDataArgs]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        lock_config: Optional[pulumi.Input[ConnectionLockConfigArgs]] = ...,
        log_config: Optional[pulumi.Input[ConnectionLogConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_config: Optional[pulumi.Input[ConnectionNodeConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_config: Optional[pulumi.Input[ConnectionSslConfigArgs]] = ...,
        statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionStatusArgs]]]
        ] = ...,
        subscription_type: Optional[pulumi.Input[_builtins.str]] = ...,
        suspended: Optional[pulumi.Input[_builtins.bool]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(self) -> Optional[pulumi.Input[ConnectionAuthConfigArgs]]: ...
    @auth_config.setter
    def auth_config(self, value: Optional[pulumi.Input[ConnectionAuthConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="configVariables")
    def config_variables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionConfigVariableArgs]]]
    ]: ...
    @config_variables.setter
    def config_variables(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionConfigVariableArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionRevision")
    def connection_revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_revision.setter
    def connection_revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectorVersion")
    def connector_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connector_version.setter
    def connector_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectorVersionInfraConfigs")
    def connector_version_infra_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionConnectorVersionInfraConfigArgs]]]
    ]: ...
    @connector_version_infra_configs.setter
    def connector_version_infra_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionConnectorVersionInfraConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectorVersionLaunchStage")
    def connector_version_launch_stage(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connector_version_launch_stage.setter
    def connector_version_launch_stage(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationConfigs")
    def destination_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionDestinationConfigArgs]]]
    ]: ...
    @destination_configs.setter
    def destination_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionDestinationConfigArgs]]]
        ],
    ): ...
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
    @pulumi.getter(name="eventingConfig")
    def eventing_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionEventingConfigArgs]]: ...
    @eventing_config.setter
    def eventing_config(
        self, value: Optional[pulumi.Input[ConnectionEventingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventingEnablementType")
    def eventing_enablement_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eventing_enablement_type.setter
    def eventing_enablement_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventingRuntimeDatas")
    def eventing_runtime_datas(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionEventingRuntimeDataArgs]]]
    ]: ...
    @eventing_runtime_datas.setter
    def eventing_runtime_datas(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionEventingRuntimeDataArgs]]]
        ],
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
    @pulumi.getter(name="lockConfig")
    def lock_config(self) -> Optional[pulumi.Input[ConnectionLockConfigArgs]]: ...
    @lock_config.setter
    def lock_config(self, value: Optional[pulumi.Input[ConnectionLockConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[ConnectionLogConfigArgs]]: ...
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[ConnectionLogConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[ConnectionNodeConfigArgs]]: ...
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[ConnectionNodeConfigArgs]]): ...
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
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectory")
    def service_directory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_directory.setter
    def service_directory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(self) -> Optional[pulumi.Input[ConnectionSslConfigArgs]]: ...
    @ssl_config.setter
    def ssl_config(self, value: Optional[pulumi.Input[ConnectionSslConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConnectionStatusArgs]]]]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectionStatusArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionType")
    def subscription_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_type.setter
    def subscription_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def suspended(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @suspended.setter
    def suspended(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:integrationconnectors/connection:Connection")
class Connection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auth_config: Optional[
            pulumi.Input[Union[ConnectionAuthConfigArgs, ConnectionAuthConfigArgsDict]]
        ] = ...,
        config_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ConnectionConfigVariableArgs,
                            ConnectionConfigVariableArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        connector_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ConnectionDestinationConfigArgs,
                            ConnectionDestinationConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        eventing_config: Optional[
            pulumi.Input[
                Union[ConnectionEventingConfigArgs, ConnectionEventingConfigArgsDict]
            ]
        ] = ...,
        eventing_enablement_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        lock_config: Optional[
            pulumi.Input[Union[ConnectionLockConfigArgs, ConnectionLockConfigArgsDict]]
        ] = ...,
        log_config: Optional[
            pulumi.Input[Union[ConnectionLogConfigArgs, ConnectionLogConfigArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_config: Optional[
            pulumi.Input[Union[ConnectionNodeConfigArgs, ConnectionNodeConfigArgsDict]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_config: Optional[
            pulumi.Input[Union[ConnectionSslConfigArgs, ConnectionSslConfigArgsDict]]
        ] = ...,
        suspended: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        auth_config: Optional[
            pulumi.Input[Union[ConnectionAuthConfigArgs, ConnectionAuthConfigArgsDict]]
        ] = ...,
        config_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ConnectionConfigVariableArgs,
                            ConnectionConfigVariableArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        connection_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        connector_version: Optional[pulumi.Input[_builtins.str]] = ...,
        connector_version_infra_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ConnectionConnectorVersionInfraConfigArgs,
                            ConnectionConnectorVersionInfraConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        connector_version_launch_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ConnectionDestinationConfigArgs,
                            ConnectionDestinationConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        eventing_config: Optional[
            pulumi.Input[
                Union[ConnectionEventingConfigArgs, ConnectionEventingConfigArgsDict]
            ]
        ] = ...,
        eventing_enablement_type: Optional[pulumi.Input[_builtins.str]] = ...,
        eventing_runtime_datas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ConnectionEventingRuntimeDataArgs,
                            ConnectionEventingRuntimeDataArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        lock_config: Optional[
            pulumi.Input[Union[ConnectionLockConfigArgs, ConnectionLockConfigArgsDict]]
        ] = ...,
        log_config: Optional[
            pulumi.Input[Union[ConnectionLogConfigArgs, ConnectionLogConfigArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_config: Optional[
            pulumi.Input[Union[ConnectionNodeConfigArgs, ConnectionNodeConfigArgsDict]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_config: Optional[
            pulumi.Input[Union[ConnectionSslConfigArgs, ConnectionSslConfigArgsDict]]
        ] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ConnectionStatusArgs, ConnectionStatusArgsDict]]
                ]
            ]
        ] = ...,
        subscription_type: Optional[pulumi.Input[_builtins.str]] = ...,
        suspended: Optional[pulumi.Input[_builtins.bool]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Connection: ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(self) -> pulumi.Output[Optional[outputs.ConnectionAuthConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="configVariables")
    def config_variables(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ConnectionConfigVariable]]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionRevision")
    def connection_revision(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorVersion")
    def connector_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorVersionInfraConfigs")
    def connector_version_infra_configs(
        self,
    ) -> pulumi.Output[Sequence[outputs.ConnectionConnectorVersionInfraConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="connectorVersionLaunchStage")
    def connector_version_launch_stage(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationConfigs")
    def destination_configs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ConnectionDestinationConfig]]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventingConfig")
    def eventing_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionEventingConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="eventingEnablementType")
    def eventing_enablement_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventingRuntimeDatas")
    def eventing_runtime_datas(
        self,
    ) -> pulumi.Output[Sequence[outputs.ConnectionEventingRuntimeData]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lockConfig")
    def lock_config(self) -> pulumi.Output[Optional[outputs.ConnectionLockConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[Optional[outputs.ConnectionLogConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> pulumi.Output[outputs.ConnectionNodeConfig]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectory")
    def service_directory(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(self) -> pulumi.Output[Optional[outputs.ConnectionSslConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.ConnectionStatus]]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionType")
    def subscription_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def suspended(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
