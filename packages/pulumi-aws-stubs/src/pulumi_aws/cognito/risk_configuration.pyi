

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
__all__ = ['RiskConfigurationArgs', 'RiskConfiguration']
@pulumi.input_type
class RiskConfigurationArgs:
    def __init__(__self__, *, user_pool_id: pulumi.Input[_builtins.str], account_takeover_risk_configuration: Optional[pulumi.Input[RiskConfigurationAccountTakeoverRiskConfigurationArgs]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., compromised_credentials_risk_configuration: Optional[pulumi.Input[RiskConfigurationCompromisedCredentialsRiskConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., risk_exception_configuration: Optional[pulumi.Input[RiskConfigurationRiskExceptionConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountTakeoverRiskConfiguration")
    def account_takeover_risk_configuration(self) -> Optional[pulumi.Input[RiskConfigurationAccountTakeoverRiskConfigurationArgs]]:
        
        ...
    
    @account_takeover_risk_configuration.setter
    def account_takeover_risk_configuration(self, value: Optional[pulumi.Input[RiskConfigurationAccountTakeoverRiskConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compromisedCredentialsRiskConfiguration")
    def compromised_credentials_risk_configuration(self) -> Optional[pulumi.Input[RiskConfigurationCompromisedCredentialsRiskConfigurationArgs]]:
        
        ...
    
    @compromised_credentials_risk_configuration.setter
    def compromised_credentials_risk_configuration(self, value: Optional[pulumi.Input[RiskConfigurationCompromisedCredentialsRiskConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="riskExceptionConfiguration")
    def risk_exception_configuration(self) -> Optional[pulumi.Input[RiskConfigurationRiskExceptionConfigurationArgs]]:
        
        ...
    
    @risk_exception_configuration.setter
    def risk_exception_configuration(self, value: Optional[pulumi.Input[RiskConfigurationRiskExceptionConfigurationArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _RiskConfigurationState:
    def __init__(__self__, *, account_takeover_risk_configuration: Optional[pulumi.Input[RiskConfigurationAccountTakeoverRiskConfigurationArgs]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., compromised_credentials_risk_configuration: Optional[pulumi.Input[RiskConfigurationCompromisedCredentialsRiskConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., risk_exception_configuration: Optional[pulumi.Input[RiskConfigurationRiskExceptionConfigurationArgs]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountTakeoverRiskConfiguration")
    def account_takeover_risk_configuration(self) -> Optional[pulumi.Input[RiskConfigurationAccountTakeoverRiskConfigurationArgs]]:
        
        ...
    
    @account_takeover_risk_configuration.setter
    def account_takeover_risk_configuration(self, value: Optional[pulumi.Input[RiskConfigurationAccountTakeoverRiskConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compromisedCredentialsRiskConfiguration")
    def compromised_credentials_risk_configuration(self) -> Optional[pulumi.Input[RiskConfigurationCompromisedCredentialsRiskConfigurationArgs]]:
        
        ...
    
    @compromised_credentials_risk_configuration.setter
    def compromised_credentials_risk_configuration(self, value: Optional[pulumi.Input[RiskConfigurationCompromisedCredentialsRiskConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="riskExceptionConfiguration")
    def risk_exception_configuration(self) -> Optional[pulumi.Input[RiskConfigurationRiskExceptionConfigurationArgs]]:
        
        ...
    
    @risk_exception_configuration.setter
    def risk_exception_configuration(self, value: Optional[pulumi.Input[RiskConfigurationRiskExceptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cognito/riskConfiguration:RiskConfiguration")
class RiskConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_takeover_risk_configuration: Optional[pulumi.Input[Union[RiskConfigurationAccountTakeoverRiskConfigurationArgs, RiskConfigurationAccountTakeoverRiskConfigurationArgsDict]]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., compromised_credentials_risk_configuration: Optional[pulumi.Input[Union[RiskConfigurationCompromisedCredentialsRiskConfigurationArgs, RiskConfigurationCompromisedCredentialsRiskConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., risk_exception_configuration: Optional[pulumi.Input[Union[RiskConfigurationRiskExceptionConfigurationArgs, RiskConfigurationRiskExceptionConfigurationArgsDict]]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RiskConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., account_takeover_risk_configuration: Optional[pulumi.Input[Union[RiskConfigurationAccountTakeoverRiskConfigurationArgs, RiskConfigurationAccountTakeoverRiskConfigurationArgsDict]]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., compromised_credentials_risk_configuration: Optional[pulumi.Input[Union[RiskConfigurationCompromisedCredentialsRiskConfigurationArgs, RiskConfigurationCompromisedCredentialsRiskConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., risk_exception_configuration: Optional[pulumi.Input[Union[RiskConfigurationRiskExceptionConfigurationArgs, RiskConfigurationRiskExceptionConfigurationArgsDict]]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ...) -> RiskConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountTakeoverRiskConfiguration")
    def account_takeover_risk_configuration(self) -> pulumi.Output[Optional[outputs.RiskConfigurationAccountTakeoverRiskConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compromisedCredentialsRiskConfiguration")
    def compromised_credentials_risk_configuration(self) -> pulumi.Output[Optional[outputs.RiskConfigurationCompromisedCredentialsRiskConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="riskExceptionConfiguration")
    def risk_exception_configuration(self) -> pulumi.Output[Optional[outputs.RiskConfigurationRiskExceptionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


