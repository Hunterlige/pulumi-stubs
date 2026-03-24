

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
__all__ = ['IdcApplicationArgs', 'IdcApplication']
@pulumi.input_type
class IdcApplicationArgs:
    def __init__(__self__, *, iam_role_arn: pulumi.Input[_builtins.str], idc_display_name: pulumi.Input[_builtins.str], idc_instance_arn: pulumi.Input[_builtins.str], redshift_idc_application_name: pulumi.Input[_builtins.str], application_type: Optional[pulumi.Input[_builtins.str]] = ..., authorized_token_issuer: Optional[pulumi.Input[IdcApplicationAuthorizedTokenIssuerArgs]] = ..., identity_namespace: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_integration: Optional[pulumi.Input[IdcApplicationServiceIntegrationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcDisplayName")
    def idc_display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @idc_display_name.setter
    def idc_display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcInstanceArn")
    def idc_instance_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @idc_instance_arn.setter
    def idc_instance_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redshiftIdcApplicationName")
    def redshift_idc_application_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @redshift_idc_application_name.setter
    def redshift_idc_application_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_type.setter
    def application_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedTokenIssuer")
    def authorized_token_issuer(self) -> Optional[pulumi.Input[IdcApplicationAuthorizedTokenIssuerArgs]]:
        
        ...
    
    @authorized_token_issuer.setter
    def authorized_token_issuer(self, value: Optional[pulumi.Input[IdcApplicationAuthorizedTokenIssuerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityNamespace")
    def identity_namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_namespace.setter
    def identity_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIntegration")
    def service_integration(self) -> Optional[pulumi.Input[IdcApplicationServiceIntegrationArgs]]:
        
        ...
    
    @service_integration.setter
    def service_integration(self, value: Optional[pulumi.Input[IdcApplicationServiceIntegrationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _IdcApplicationState:
    def __init__(__self__, *, application_type: Optional[pulumi.Input[_builtins.str]] = ..., authorized_token_issuer: Optional[pulumi.Input[IdcApplicationAuthorizedTokenIssuerArgs]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., idc_display_name: Optional[pulumi.Input[_builtins.str]] = ..., idc_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., idc_managed_application_arn: Optional[pulumi.Input[_builtins.str]] = ..., identity_namespace: Optional[pulumi.Input[_builtins.str]] = ..., redshift_idc_application_arn: Optional[pulumi.Input[_builtins.str]] = ..., redshift_idc_application_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_integration: Optional[pulumi.Input[IdcApplicationServiceIntegrationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_type.setter
    def application_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedTokenIssuer")
    def authorized_token_issuer(self) -> Optional[pulumi.Input[IdcApplicationAuthorizedTokenIssuerArgs]]:
        
        ...
    
    @authorized_token_issuer.setter
    def authorized_token_issuer(self, value: Optional[pulumi.Input[IdcApplicationAuthorizedTokenIssuerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcDisplayName")
    def idc_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @idc_display_name.setter
    def idc_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcInstanceArn")
    def idc_instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @idc_instance_arn.setter
    def idc_instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcManagedApplicationArn")
    def idc_managed_application_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @idc_managed_application_arn.setter
    def idc_managed_application_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityNamespace")
    def identity_namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_namespace.setter
    def identity_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redshiftIdcApplicationArn")
    def redshift_idc_application_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redshift_idc_application_arn.setter
    def redshift_idc_application_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redshiftIdcApplicationName")
    def redshift_idc_application_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redshift_idc_application_name.setter
    def redshift_idc_application_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIntegration")
    def service_integration(self) -> Optional[pulumi.Input[IdcApplicationServiceIntegrationArgs]]:
        
        ...
    
    @service_integration.setter
    def service_integration(self, value: Optional[pulumi.Input[IdcApplicationServiceIntegrationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:redshift/idcApplication:IdcApplication")
class IdcApplication(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_type: Optional[pulumi.Input[_builtins.str]] = ..., authorized_token_issuer: Optional[pulumi.Input[Union[IdcApplicationAuthorizedTokenIssuerArgs, IdcApplicationAuthorizedTokenIssuerArgsDict]]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., idc_display_name: Optional[pulumi.Input[_builtins.str]] = ..., idc_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., identity_namespace: Optional[pulumi.Input[_builtins.str]] = ..., redshift_idc_application_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_integration: Optional[pulumi.Input[Union[IdcApplicationServiceIntegrationArgs, IdcApplicationServiceIntegrationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IdcApplicationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_type: Optional[pulumi.Input[_builtins.str]] = ..., authorized_token_issuer: Optional[pulumi.Input[Union[IdcApplicationAuthorizedTokenIssuerArgs, IdcApplicationAuthorizedTokenIssuerArgsDict]]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., idc_display_name: Optional[pulumi.Input[_builtins.str]] = ..., idc_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., idc_managed_application_arn: Optional[pulumi.Input[_builtins.str]] = ..., identity_namespace: Optional[pulumi.Input[_builtins.str]] = ..., redshift_idc_application_arn: Optional[pulumi.Input[_builtins.str]] = ..., redshift_idc_application_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_integration: Optional[pulumi.Input[Union[IdcApplicationServiceIntegrationArgs, IdcApplicationServiceIntegrationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> IdcApplication:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedTokenIssuer")
    def authorized_token_issuer(self) -> pulumi.Output[Optional[outputs.IdcApplicationAuthorizedTokenIssuer]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcDisplayName")
    def idc_display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcInstanceArn")
    def idc_instance_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idcManagedApplicationArn")
    def idc_managed_application_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityNamespace")
    def identity_namespace(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redshiftIdcApplicationArn")
    def redshift_idc_application_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redshiftIdcApplicationName")
    def redshift_idc_application_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceIntegration")
    def service_integration(self) -> pulumi.Output[Optional[outputs.IdcApplicationServiceIntegration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    


