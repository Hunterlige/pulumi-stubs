

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LicenseAssociationArgs', 'LicenseAssociation']
@pulumi.input_type
class LicenseAssociationArgs:
    def __init__(__self__, *, license_type: pulumi.Input[_builtins.str], workspace_id: pulumi.Input[_builtins.str], grafana_token: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @license_type.setter
    def license_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grafanaToken")
    def grafana_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @grafana_token.setter
    def grafana_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _LicenseAssociationState:
    def __init__(__self__, *, free_trial_expiration: Optional[pulumi.Input[_builtins.str]] = ..., grafana_token: Optional[pulumi.Input[_builtins.str]] = ..., license_expiration: Optional[pulumi.Input[_builtins.str]] = ..., license_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="freeTrialExpiration")
    def free_trial_expiration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @free_trial_expiration.setter
    def free_trial_expiration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grafanaToken")
    def grafana_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @grafana_token.setter
    def grafana_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseExpiration")
    def license_expiration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_expiration.setter
    def license_expiration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_type.setter
    def license_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:grafana/licenseAssociation:LicenseAssociation")
class LicenseAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., grafana_token: Optional[pulumi.Input[_builtins.str]] = ..., license_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LicenseAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., free_trial_expiration: Optional[pulumi.Input[_builtins.str]] = ..., grafana_token: Optional[pulumi.Input[_builtins.str]] = ..., license_expiration: Optional[pulumi.Input[_builtins.str]] = ..., license_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ...) -> LicenseAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="freeTrialExpiration")
    def free_trial_expiration(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grafanaToken")
    def grafana_token(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseExpiration")
    def license_expiration(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


