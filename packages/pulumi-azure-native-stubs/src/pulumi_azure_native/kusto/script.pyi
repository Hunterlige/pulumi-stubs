import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ScriptArgs", "Script"]

@pulumi.input_type
class ScriptArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        database_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        continue_on_errors: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_permissions_action: Optional[
            pulumi.Input[Union[_builtins.str, PrincipalPermissionsAction]]
        ] = ...,
        script_content: Optional[pulumi.Input[_builtins.str]] = ...,
        script_level: Optional[pulumi.Input[Union[_builtins.str, ScriptLevel]]] = ...,
        script_name: Optional[pulumi.Input[_builtins.str]] = ...,
        script_url: Optional[pulumi.Input[_builtins.str]] = ...,
        script_url_sas_token: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="continueOnErrors")
    def continue_on_errors(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continue_on_errors.setter
    def continue_on_errors(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalPermissionsAction")
    def principal_permissions_action(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrincipalPermissionsAction]]]: ...
    @principal_permissions_action.setter
    def principal_permissions_action(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PrincipalPermissionsAction]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptContent")
    def script_content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_content.setter
    def script_content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptLevel")
    def script_level(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ScriptLevel]]]: ...
    @script_level.setter
    def script_level(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ScriptLevel]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptName")
    def script_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_name.setter
    def script_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptUrl")
    def script_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_url.setter
    def script_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptUrlSasToken")
    def script_url_sas_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_url_sas_token.setter
    def script_url_sas_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:kusto:Script")
class Script(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        continue_on_errors: Optional[pulumi.Input[_builtins.bool]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_permissions_action: Optional[
            pulumi.Input[Union[_builtins.str, PrincipalPermissionsAction]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        script_content: Optional[pulumi.Input[_builtins.str]] = ...,
        script_level: Optional[pulumi.Input[Union[_builtins.str, ScriptLevel]]] = ...,
        script_name: Optional[pulumi.Input[_builtins.str]] = ...,
        script_url: Optional[pulumi.Input[_builtins.str]] = ...,
        script_url_sas_token: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ScriptArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Script: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="continueOnErrors")
    def continue_on_errors(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalPermissionsAction")
    def principal_permissions_action(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scriptLevel")
    def script_level(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scriptUrl")
    def script_url(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
