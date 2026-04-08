import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AzurePowerShellScriptArgs", "AzurePowerShellScript"]

@pulumi.input_type
class AzurePowerShellScriptArgs:
    def __init__(
        __self__,
        *,
        az_power_shell_version: pulumi.Input[_builtins.str],
        kind: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        retention_interval: pulumi.Input[_builtins.str],
        arguments: Optional[pulumi.Input[_builtins.str]] = ...,
        cleanup_preference: Optional[
            pulumi.Input[Union[_builtins.str, CleanupOptions]]
        ] = ...,
        container_settings: Optional[pulumi.Input[ContainerConfigurationArgs]] = ...,
        environment_variables: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]
        ] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_script_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        script_content: Optional[pulumi.Input[_builtins.str]] = ...,
        script_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_settings: Optional[
            pulumi.Input[StorageAccountConfigurationArgs]
        ] = ...,
        supporting_script_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azPowerShellVersion")
    def az_power_shell_version(self) -> pulumi.Input[_builtins.str]: ...
    @az_power_shell_version.setter
    def az_power_shell_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> pulumi.Input[_builtins.str]: ...
    @retention_interval.setter
    def retention_interval(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arguments.setter
    def arguments(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cleanupPreference")
    def cleanup_preference(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CleanupOptions]]]: ...
    @cleanup_preference.setter
    def cleanup_preference(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CleanupOptions]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerSettings")
    def container_settings(
        self,
    ) -> Optional[pulumi.Input[ContainerConfigurationArgs]]: ...
    @container_settings.setter
    def container_settings(
        self, value: Optional[pulumi.Input[ContainerConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryScriptUri")
    def primary_script_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_script_uri.setter
    def primary_script_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptContent")
    def script_content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_content.setter
    def script_content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptName")
    def script_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_name.setter
    def script_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountSettings")
    def storage_account_settings(
        self,
    ) -> Optional[pulumi.Input[StorageAccountConfigurationArgs]]: ...
    @storage_account_settings.setter
    def storage_account_settings(
        self, value: Optional[pulumi.Input[StorageAccountConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportingScriptUris")
    def supporting_script_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supporting_script_uris.setter
    def supporting_script_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:resources:AzurePowerShellScript")
class AzurePowerShellScript(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        arguments: Optional[pulumi.Input[_builtins.str]] = ...,
        az_power_shell_version: Optional[pulumi.Input[_builtins.str]] = ...,
        cleanup_preference: Optional[
            pulumi.Input[Union[_builtins.str, CleanupOptions]]
        ] = ...,
        container_settings: Optional[
            pulumi.Input[
                Union[ContainerConfigurationArgs, ContainerConfigurationArgsDict]
            ]
        ] = ...,
        environment_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[EnvironmentVariableArgs, EnvironmentVariableArgsDict]
                    ]
                ]
            ]
        ] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_script_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        script_content: Optional[pulumi.Input[_builtins.str]] = ...,
        script_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_settings: Optional[
            pulumi.Input[
                Union[
                    StorageAccountConfigurationArgs, StorageAccountConfigurationArgsDict
                ]
            ]
        ] = ...,
        supporting_script_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AzurePowerShellScriptArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AzurePowerShellScript: ...
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azPowerShellVersion")
    def az_power_shell_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cleanupPreference")
    def cleanup_preference(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerSettings")
    def container_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.ContainerConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.EnvironmentVariableResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Mapping[str, Any]]: ...
    @_builtins.property
    @pulumi.getter(name="primaryScriptUri")
    def primary_script_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scriptContent")
    def script_content(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.ScriptStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountSettings")
    def storage_account_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.StorageAccountConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="supportingScriptUris")
    def supporting_script_uris(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
