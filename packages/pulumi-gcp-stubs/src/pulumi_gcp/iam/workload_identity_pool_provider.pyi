

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkloadIdentityPoolProviderArgs', 'WorkloadIdentityPoolProvider']
@pulumi.input_type
class WorkloadIdentityPoolProviderArgs:
    def __init__(__self__, *, workload_identity_pool_id: pulumi.Input[_builtins.str], workload_identity_pool_provider_id: pulumi.Input[_builtins.str], attribute_condition: Optional[pulumi.Input[_builtins.str]] = ..., attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., aws: Optional[pulumi.Input[WorkloadIdentityPoolProviderAwsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., oidc: Optional[pulumi.Input[WorkloadIdentityPoolProviderOidcArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., saml: Optional[pulumi.Input[WorkloadIdentityPoolProviderSamlArgs]] = ..., x509: Optional[pulumi.Input[WorkloadIdentityPoolProviderX509Args]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workload_identity_pool_id.setter
    def workload_identity_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolProviderId")
    def workload_identity_pool_provider_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workload_identity_pool_provider_id.setter
    def workload_identity_pool_provider_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeCondition")
    def attribute_condition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attribute_condition.setter
    def attribute_condition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @attribute_mapping.setter
    def attribute_mapping(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def aws(self) -> Optional[pulumi.Input[WorkloadIdentityPoolProviderAwsArgs]]:
        
        ...
    
    @aws.setter
    def aws(self, value: Optional[pulumi.Input[WorkloadIdentityPoolProviderAwsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def oidc(self) -> Optional[pulumi.Input[WorkloadIdentityPoolProviderOidcArgs]]:
        
        ...
    
    @oidc.setter
    def oidc(self, value: Optional[pulumi.Input[WorkloadIdentityPoolProviderOidcArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def saml(self) -> Optional[pulumi.Input[WorkloadIdentityPoolProviderSamlArgs]]:
        
        ...
    
    @saml.setter
    def saml(self, value: Optional[pulumi.Input[WorkloadIdentityPoolProviderSamlArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def x509(self) -> Optional[pulumi.Input[WorkloadIdentityPoolProviderX509Args]]:
        
        ...
    
    @x509.setter
    def x509(self, value: Optional[pulumi.Input[WorkloadIdentityPoolProviderX509Args]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkloadIdentityPoolProviderState:
    def __init__(__self__, *, attribute_condition: Optional[pulumi.Input[_builtins.str]] = ..., attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., aws: Optional[pulumi.Input[WorkloadIdentityPoolProviderAwsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., oidc: Optional[pulumi.Input[WorkloadIdentityPoolProviderOidcArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., saml: Optional[pulumi.Input[WorkloadIdentityPoolProviderSamlArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_pool_provider_id: Optional[pulumi.Input[_builtins.str]] = ..., x509: Optional[pulumi.Input[WorkloadIdentityPoolProviderX509Args]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeCondition")
    def attribute_condition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attribute_condition.setter
    def attribute_condition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @attribute_mapping.setter
    def attribute_mapping(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def aws(self) -> Optional[pulumi.Input[WorkloadIdentityPoolProviderAwsArgs]]:
        
        ...
    
    @aws.setter
    def aws(self, value: Optional[pulumi.Input[WorkloadIdentityPoolProviderAwsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def oidc(self) -> Optional[pulumi.Input[WorkloadIdentityPoolProviderOidcArgs]]:
        
        ...
    
    @oidc.setter
    def oidc(self, value: Optional[pulumi.Input[WorkloadIdentityPoolProviderOidcArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def saml(self) -> Optional[pulumi.Input[WorkloadIdentityPoolProviderSamlArgs]]:
        
        ...
    
    @saml.setter
    def saml(self, value: Optional[pulumi.Input[WorkloadIdentityPoolProviderSamlArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workload_identity_pool_id.setter
    def workload_identity_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolProviderId")
    def workload_identity_pool_provider_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workload_identity_pool_provider_id.setter
    def workload_identity_pool_provider_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def x509(self) -> Optional[pulumi.Input[WorkloadIdentityPoolProviderX509Args]]:
        
        ...
    
    @x509.setter
    def x509(self, value: Optional[pulumi.Input[WorkloadIdentityPoolProviderX509Args]]): # -> None:
        ...
    


@pulumi.type_token(...)
class WorkloadIdentityPoolProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attribute_condition: Optional[pulumi.Input[_builtins.str]] = ..., attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., aws: Optional[pulumi.Input[Union[WorkloadIdentityPoolProviderAwsArgs, WorkloadIdentityPoolProviderAwsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., oidc: Optional[pulumi.Input[Union[WorkloadIdentityPoolProviderOidcArgs, WorkloadIdentityPoolProviderOidcArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., saml: Optional[pulumi.Input[Union[WorkloadIdentityPoolProviderSamlArgs, WorkloadIdentityPoolProviderSamlArgsDict]]] = ..., workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_pool_provider_id: Optional[pulumi.Input[_builtins.str]] = ..., x509: Optional[pulumi.Input[Union[WorkloadIdentityPoolProviderX509Args, WorkloadIdentityPoolProviderX509ArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkloadIdentityPoolProviderArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., attribute_condition: Optional[pulumi.Input[_builtins.str]] = ..., attribute_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., aws: Optional[pulumi.Input[Union[WorkloadIdentityPoolProviderAwsArgs, WorkloadIdentityPoolProviderAwsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., oidc: Optional[pulumi.Input[Union[WorkloadIdentityPoolProviderOidcArgs, WorkloadIdentityPoolProviderOidcArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., saml: Optional[pulumi.Input[Union[WorkloadIdentityPoolProviderSamlArgs, WorkloadIdentityPoolProviderSamlArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., workload_identity_pool_provider_id: Optional[pulumi.Input[_builtins.str]] = ..., x509: Optional[pulumi.Input[Union[WorkloadIdentityPoolProviderX509Args, WorkloadIdentityPoolProviderX509ArgsDict]]] = ...) -> WorkloadIdentityPoolProvider:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeCondition")
    def attribute_condition(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeMapping")
    def attribute_mapping(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aws(self) -> pulumi.Output[Optional[outputs.WorkloadIdentityPoolProviderAws]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def oidc(self) -> pulumi.Output[Optional[outputs.WorkloadIdentityPoolProviderOidc]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def saml(self) -> pulumi.Output[Optional[outputs.WorkloadIdentityPoolProviderSaml]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolProviderId")
    def workload_identity_pool_provider_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def x509(self) -> pulumi.Output[Optional[outputs.WorkloadIdentityPoolProviderX509]]:
        
        ...
    


