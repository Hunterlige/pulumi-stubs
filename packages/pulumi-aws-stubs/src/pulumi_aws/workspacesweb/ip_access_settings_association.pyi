

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IpAccessSettingsAssociationArgs', 'IpAccessSettingsAssociation']
@pulumi.input_type
class IpAccessSettingsAssociationArgs:
    def __init__(__self__, *, ip_access_settings_arn: pulumi.Input[_builtins.str], portal_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAccessSettingsArn")
    def ip_access_settings_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_access_settings_arn.setter
    def ip_access_settings_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @portal_arn.setter
    def portal_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _IpAccessSettingsAssociationState:
    def __init__(__self__, *, ip_access_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAccessSettingsArn")
    def ip_access_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_access_settings_arn.setter
    def ip_access_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @portal_arn.setter
    def portal_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class IpAccessSettingsAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., ip_access_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IpAccessSettingsAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., ip_access_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> IpAccessSettingsAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAccessSettingsArn")
    def ip_access_settings_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


