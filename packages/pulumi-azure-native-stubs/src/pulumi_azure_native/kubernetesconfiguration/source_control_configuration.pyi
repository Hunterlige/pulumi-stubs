

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SourceControlConfigurationArgs', 'SourceControlConfiguration']
@pulumi.input_type
class SourceControlConfigurationArgs:
    def __init__(__self__, *, cluster_name: pulumi.Input[_builtins.str], cluster_resource_name: pulumi.Input[_builtins.str], cluster_rp: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], configuration_protected_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_helm_operator: Optional[pulumi.Input[_builtins.bool]] = ..., helm_operator_properties: Optional[pulumi.Input[HelmOperatorPropertiesArgs]] = ..., operator_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., operator_namespace: Optional[pulumi.Input[_builtins.str]] = ..., operator_params: Optional[pulumi.Input[_builtins.str]] = ..., operator_scope: Optional[pulumi.Input[Union[_builtins.str, OperatorScopeType]]] = ..., operator_type: Optional[pulumi.Input[Union[_builtins.str, OperatorType]]] = ..., repository_url: Optional[pulumi.Input[_builtins.str]] = ..., source_control_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., ssh_known_hosts_contents: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterResourceName")
    def cluster_resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_resource_name.setter
    def cluster_resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterRp")
    def cluster_rp(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_rp.setter
    def cluster_rp(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationProtectedSettings")
    def configuration_protected_settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @configuration_protected_settings.setter
    def configuration_protected_settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHelmOperator")
    def enable_helm_operator(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_helm_operator.setter
    def enable_helm_operator(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="helmOperatorProperties")
    def helm_operator_properties(self) -> Optional[pulumi.Input[HelmOperatorPropertiesArgs]]:
        
        ...
    
    @helm_operator_properties.setter
    def helm_operator_properties(self, value: Optional[pulumi.Input[HelmOperatorPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorInstanceName")
    def operator_instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operator_instance_name.setter
    def operator_instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorNamespace")
    def operator_namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operator_namespace.setter
    def operator_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorParams")
    def operator_params(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operator_params.setter
    def operator_params(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorScope")
    def operator_scope(self) -> Optional[pulumi.Input[Union[_builtins.str, OperatorScopeType]]]:
        
        ...
    
    @operator_scope.setter
    def operator_scope(self, value: Optional[pulumi.Input[Union[_builtins.str, OperatorScopeType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OperatorType]]]:
        
        ...
    
    @operator_type.setter
    def operator_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OperatorType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceControlConfigurationName")
    def source_control_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_control_configuration_name.setter
    def source_control_configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshKnownHostsContents")
    def ssh_known_hosts_contents(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssh_known_hosts_contents.setter
    def ssh_known_hosts_contents(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SourceControlConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_rp: Optional[pulumi.Input[_builtins.str]] = ..., configuration_protected_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_helm_operator: Optional[pulumi.Input[_builtins.bool]] = ..., helm_operator_properties: Optional[pulumi.Input[Union[HelmOperatorPropertiesArgs, HelmOperatorPropertiesArgsDict]]] = ..., operator_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., operator_namespace: Optional[pulumi.Input[_builtins.str]] = ..., operator_params: Optional[pulumi.Input[_builtins.str]] = ..., operator_scope: Optional[pulumi.Input[Union[_builtins.str, OperatorScopeType]]] = ..., operator_type: Optional[pulumi.Input[Union[_builtins.str, OperatorType]]] = ..., repository_url: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source_control_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., ssh_known_hosts_contents: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SourceControlConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SourceControlConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> pulumi.Output[outputs.ComplianceStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationProtectedSettings")
    def configuration_protected_settings(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHelmOperator")
    def enable_helm_operator(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="helmOperatorProperties")
    def helm_operator_properties(self) -> pulumi.Output[Optional[outputs.HelmOperatorPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorInstanceName")
    def operator_instance_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorNamespace")
    def operator_namespace(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorParams")
    def operator_params(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorScope")
    def operator_scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryPublicKey")
    def repository_public_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshKnownHostsContents")
    def ssh_known_hosts_contents(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


