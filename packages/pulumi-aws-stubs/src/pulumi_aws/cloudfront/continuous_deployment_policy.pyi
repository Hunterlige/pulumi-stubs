

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
__all__ = ['ContinuousDeploymentPolicyArgs', 'ContinuousDeploymentPolicy']
@pulumi.input_type
class ContinuousDeploymentPolicyArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], staging_distribution_dns_names: pulumi.Input[ContinuousDeploymentPolicyStagingDistributionDnsNamesArgs], traffic_config: Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingDistributionDnsNames")
    def staging_distribution_dns_names(self) -> pulumi.Input[ContinuousDeploymentPolicyStagingDistributionDnsNamesArgs]:
        
        ...
    
    @staging_distribution_dns_names.setter
    def staging_distribution_dns_names(self, value: pulumi.Input[ContinuousDeploymentPolicyStagingDistributionDnsNamesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficConfig")
    def traffic_config(self) -> Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigArgs]]:
        
        ...
    
    @traffic_config.setter
    def traffic_config(self, value: Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ContinuousDeploymentPolicyState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_time: Optional[pulumi.Input[_builtins.str]] = ..., staging_distribution_dns_names: Optional[pulumi.Input[ContinuousDeploymentPolicyStagingDistributionDnsNamesArgs]] = ..., traffic_config: Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingDistributionDnsNames")
    def staging_distribution_dns_names(self) -> Optional[pulumi.Input[ContinuousDeploymentPolicyStagingDistributionDnsNamesArgs]]:
        
        ...
    
    @staging_distribution_dns_names.setter
    def staging_distribution_dns_names(self, value: Optional[pulumi.Input[ContinuousDeploymentPolicyStagingDistributionDnsNamesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficConfig")
    def traffic_config(self) -> Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigArgs]]:
        
        ...
    
    @traffic_config.setter
    def traffic_config(self, value: Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ContinuousDeploymentPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., staging_distribution_dns_names: Optional[pulumi.Input[Union[ContinuousDeploymentPolicyStagingDistributionDnsNamesArgs, ContinuousDeploymentPolicyStagingDistributionDnsNamesArgsDict]]] = ..., traffic_config: Optional[pulumi.Input[Union[ContinuousDeploymentPolicyTrafficConfigArgs, ContinuousDeploymentPolicyTrafficConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ContinuousDeploymentPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_time: Optional[pulumi.Input[_builtins.str]] = ..., staging_distribution_dns_names: Optional[pulumi.Input[Union[ContinuousDeploymentPolicyStagingDistributionDnsNamesArgs, ContinuousDeploymentPolicyStagingDistributionDnsNamesArgsDict]]] = ..., traffic_config: Optional[pulumi.Input[Union[ContinuousDeploymentPolicyTrafficConfigArgs, ContinuousDeploymentPolicyTrafficConfigArgsDict]]] = ...) -> ContinuousDeploymentPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingDistributionDnsNames")
    def staging_distribution_dns_names(self) -> pulumi.Output[outputs.ContinuousDeploymentPolicyStagingDistributionDnsNames]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficConfig")
    def traffic_config(self) -> pulumi.Output[Optional[outputs.ContinuousDeploymentPolicyTrafficConfig]]:
        
        ...
    


