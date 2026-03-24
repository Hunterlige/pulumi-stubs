

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RepositoryPermissionsPolicyArgs', 'RepositoryPermissionsPolicy']
@pulumi.input_type
class RepositoryPermissionsPolicyArgs:
    def __init__(__self__, *, domain: pulumi.Input[_builtins.str], policy_document: pulumi.Input[_builtins.str], repository: pulumi.Input[_builtins.str], domain_owner: Optional[pulumi.Input[_builtins.str]] = ..., policy_revision: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_document.setter
    def policy_document(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository.setter
    def repository(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainOwner")
    def domain_owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_owner.setter
    def domain_owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyRevision")
    def policy_revision(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_revision.setter
    def policy_revision(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RepositoryPermissionsPolicyState:
    def __init__(__self__, *, domain: Optional[pulumi.Input[_builtins.str]] = ..., domain_owner: Optional[pulumi.Input[_builtins.str]] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., policy_revision: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainOwner")
    def domain_owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_owner.setter
    def domain_owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyRevision")
    def policy_revision(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_revision.setter
    def policy_revision(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RepositoryPermissionsPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., domain_owner: Optional[pulumi.Input[_builtins.str]] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., policy_revision: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RepositoryPermissionsPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., domain_owner: Optional[pulumi.Input[_builtins.str]] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., policy_revision: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> RepositoryPermissionsPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainOwner")
    def domain_owner(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyRevision")
    def policy_revision(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


