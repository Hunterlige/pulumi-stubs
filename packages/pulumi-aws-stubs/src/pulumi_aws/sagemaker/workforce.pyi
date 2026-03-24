

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkforceArgs', 'Workforce']
@pulumi.input_type
class WorkforceArgs:
    def __init__(__self__, *, workforce_name: pulumi.Input[_builtins.str], cognito_config: Optional[pulumi.Input[WorkforceCognitoConfigArgs]] = ..., oidc_config: Optional[pulumi.Input[WorkforceOidcConfigArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_ip_config: Optional[pulumi.Input[WorkforceSourceIpConfigArgs]] = ..., workforce_vpc_config: Optional[pulumi.Input[WorkforceWorkforceVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforceName")
    def workforce_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workforce_name.setter
    def workforce_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoConfig")
    def cognito_config(self) -> Optional[pulumi.Input[WorkforceCognitoConfigArgs]]:
        
        ...
    
    @cognito_config.setter
    def cognito_config(self, value: Optional[pulumi.Input[WorkforceCognitoConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcConfig")
    def oidc_config(self) -> Optional[pulumi.Input[WorkforceOidcConfigArgs]]:
        
        ...
    
    @oidc_config.setter
    def oidc_config(self, value: Optional[pulumi.Input[WorkforceOidcConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIpConfig")
    def source_ip_config(self) -> Optional[pulumi.Input[WorkforceSourceIpConfigArgs]]:
        
        ...
    
    @source_ip_config.setter
    def source_ip_config(self, value: Optional[pulumi.Input[WorkforceSourceIpConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforceVpcConfig")
    def workforce_vpc_config(self) -> Optional[pulumi.Input[WorkforceWorkforceVpcConfigArgs]]:
        
        ...
    
    @workforce_vpc_config.setter
    def workforce_vpc_config(self, value: Optional[pulumi.Input[WorkforceWorkforceVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkforceState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., cognito_config: Optional[pulumi.Input[WorkforceCognitoConfigArgs]] = ..., oidc_config: Optional[pulumi.Input[WorkforceOidcConfigArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_ip_config: Optional[pulumi.Input[WorkforceSourceIpConfigArgs]] = ..., subdomain: Optional[pulumi.Input[_builtins.str]] = ..., workforce_name: Optional[pulumi.Input[_builtins.str]] = ..., workforce_vpc_config: Optional[pulumi.Input[WorkforceWorkforceVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoConfig")
    def cognito_config(self) -> Optional[pulumi.Input[WorkforceCognitoConfigArgs]]:
        
        ...
    
    @cognito_config.setter
    def cognito_config(self, value: Optional[pulumi.Input[WorkforceCognitoConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcConfig")
    def oidc_config(self) -> Optional[pulumi.Input[WorkforceOidcConfigArgs]]:
        
        ...
    
    @oidc_config.setter
    def oidc_config(self, value: Optional[pulumi.Input[WorkforceOidcConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIpConfig")
    def source_ip_config(self) -> Optional[pulumi.Input[WorkforceSourceIpConfigArgs]]:
        
        ...
    
    @source_ip_config.setter
    def source_ip_config(self, value: Optional[pulumi.Input[WorkforceSourceIpConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdomain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subdomain.setter
    def subdomain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforceName")
    def workforce_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workforce_name.setter
    def workforce_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforceVpcConfig")
    def workforce_vpc_config(self) -> Optional[pulumi.Input[WorkforceWorkforceVpcConfigArgs]]:
        
        ...
    
    @workforce_vpc_config.setter
    def workforce_vpc_config(self, value: Optional[pulumi.Input[WorkforceWorkforceVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:sagemaker/workforce:Workforce")
class Workforce(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cognito_config: Optional[pulumi.Input[Union[WorkforceCognitoConfigArgs, WorkforceCognitoConfigArgsDict]]] = ..., oidc_config: Optional[pulumi.Input[Union[WorkforceOidcConfigArgs, WorkforceOidcConfigArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_ip_config: Optional[pulumi.Input[Union[WorkforceSourceIpConfigArgs, WorkforceSourceIpConfigArgsDict]]] = ..., workforce_name: Optional[pulumi.Input[_builtins.str]] = ..., workforce_vpc_config: Optional[pulumi.Input[Union[WorkforceWorkforceVpcConfigArgs, WorkforceWorkforceVpcConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkforceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cognito_config: Optional[pulumi.Input[Union[WorkforceCognitoConfigArgs, WorkforceCognitoConfigArgsDict]]] = ..., oidc_config: Optional[pulumi.Input[Union[WorkforceOidcConfigArgs, WorkforceOidcConfigArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_ip_config: Optional[pulumi.Input[Union[WorkforceSourceIpConfigArgs, WorkforceSourceIpConfigArgsDict]]] = ..., subdomain: Optional[pulumi.Input[_builtins.str]] = ..., workforce_name: Optional[pulumi.Input[_builtins.str]] = ..., workforce_vpc_config: Optional[pulumi.Input[Union[WorkforceWorkforceVpcConfigArgs, WorkforceWorkforceVpcConfigArgsDict]]] = ...) -> Workforce:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoConfig")
    def cognito_config(self) -> pulumi.Output[Optional[outputs.WorkforceCognitoConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcConfig")
    def oidc_config(self) -> pulumi.Output[Optional[outputs.WorkforceOidcConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIpConfig")
    def source_ip_config(self) -> pulumi.Output[outputs.WorkforceSourceIpConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdomain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforceName")
    def workforce_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforceVpcConfig")
    def workforce_vpc_config(self) -> pulumi.Output[Optional[outputs.WorkforceWorkforceVpcConfig]]:
        
        ...
    


