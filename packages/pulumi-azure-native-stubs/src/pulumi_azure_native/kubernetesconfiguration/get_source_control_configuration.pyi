import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSourceControlConfigurationResult",
    "AwaitableGetSourceControlConfigurationResult",
    "get_source_control_configuration",
    "get_source_control_configuration_output",
]

@pulumi.output_type
class GetSourceControlConfigurationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        compliance_status=...,
        configuration_protected_settings=...,
        enable_helm_operator=...,
        helm_operator_properties=...,
        id=...,
        name=...,
        operator_instance_name=...,
        operator_namespace=...,
        operator_params=...,
        operator_scope=...,
        operator_type=...,
        provisioning_state=...,
        repository_public_key=...,
        repository_url=...,
        ssh_known_hosts_contents=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> outputs.ComplianceStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="configurationProtectedSettings")
    def configuration_protected_settings(
        self,
    ) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableHelmOperator")
    def enable_helm_operator(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="helmOperatorProperties")
    def helm_operator_properties(
        self,
    ) -> Optional[outputs.HelmOperatorPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="operatorInstanceName")
    def operator_instance_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operatorNamespace")
    def operator_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operatorParams")
    def operator_params(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operatorScope")
    def operator_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryPublicKey")
    def repository_public_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sshKnownHostsContents")
    def ssh_known_hosts_contents(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSourceControlConfigurationResult(GetSourceControlConfigurationResult):
    def __await__(self): ...

def get_source_control_configuration(
    cluster_name: Optional[_builtins.str] = ...,
    cluster_resource_name: Optional[_builtins.str] = ...,
    cluster_rp: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    source_control_configuration_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSourceControlConfigurationResult: ...
def get_source_control_configuration_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    cluster_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    cluster_rp: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    source_control_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSourceControlConfigurationResult]: ...
