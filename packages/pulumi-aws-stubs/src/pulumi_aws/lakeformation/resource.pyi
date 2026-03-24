

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResourceArgs', 'Resource']
@pulumi.input_type
class ResourceArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str], hybrid_access_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., use_service_linked_role: Optional[pulumi.Input[_builtins.bool]] = ..., with_federation: Optional[pulumi.Input[_builtins.bool]] = ..., with_privileged_access: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridAccessEnabled")
    def hybrid_access_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @hybrid_access_enabled.setter
    def hybrid_access_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useServiceLinkedRole")
    def use_service_linked_role(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_service_linked_role.setter
    def use_service_linked_role(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="withFederation")
    def with_federation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @with_federation.setter
    def with_federation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="withPrivilegedAccess")
    def with_privileged_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @with_privileged_access.setter
    def with_privileged_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _ResourceState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_access_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., last_modified: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., use_service_linked_role: Optional[pulumi.Input[_builtins.bool]] = ..., with_federation: Optional[pulumi.Input[_builtins.bool]] = ..., with_privileged_access: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridAccessEnabled")
    def hybrid_access_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @hybrid_access_enabled.setter
    def hybrid_access_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified.setter
    def last_modified(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useServiceLinkedRole")
    def use_service_linked_role(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_service_linked_role.setter
    def use_service_linked_role(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="withFederation")
    def with_federation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @with_federation.setter
    def with_federation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="withPrivilegedAccess")
    def with_privileged_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @with_privileged_access.setter
    def with_privileged_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("aws:lakeformation/resource:Resource")
class Resource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_access_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., use_service_linked_role: Optional[pulumi.Input[_builtins.bool]] = ..., with_federation: Optional[pulumi.Input[_builtins.bool]] = ..., with_privileged_access: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., hybrid_access_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., last_modified: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., use_service_linked_role: Optional[pulumi.Input[_builtins.bool]] = ..., with_federation: Optional[pulumi.Input[_builtins.bool]] = ..., with_privileged_access: Optional[pulumi.Input[_builtins.bool]] = ...) -> Resource:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridAccessEnabled")
    def hybrid_access_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useServiceLinkedRole")
    def use_service_linked_role(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="withFederation")
    def with_federation(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="withPrivilegedAccess")
    def with_privileged_access(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    


