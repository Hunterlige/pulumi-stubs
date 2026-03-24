

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
__all__ = ['AccessPolicyAssociationArgs', 'AccessPolicyAssociation']
@pulumi.input_type
class AccessPolicyAssociationArgs:
    def __init__(__self__, *, access_scope: pulumi.Input[AccessPolicyAssociationAccessScopeArgs], cluster_name: pulumi.Input[_builtins.str], policy_arn: pulumi.Input[_builtins.str], principal_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessScope")
    def access_scope(self) -> pulumi.Input[AccessPolicyAssociationAccessScopeArgs]:
        
        ...
    
    @access_scope.setter
    def access_scope(self, value: pulumi.Input[AccessPolicyAssociationAccessScopeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_arn.setter
    def policy_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @principal_arn.setter
    def principal_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AccessPolicyAssociationState:
    def __init__(__self__, *, access_scope: Optional[pulumi.Input[AccessPolicyAssociationAccessScopeArgs]] = ..., associated_at: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., modified_at: Optional[pulumi.Input[_builtins.str]] = ..., policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., principal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessScope")
    def access_scope(self) -> Optional[pulumi.Input[AccessPolicyAssociationAccessScopeArgs]]:
        
        ...
    
    @access_scope.setter
    def access_scope(self, value: Optional[pulumi.Input[AccessPolicyAssociationAccessScopeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedAt")
    def associated_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @associated_at.setter
    def associated_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @modified_at.setter
    def modified_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_arn.setter
    def policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_arn.setter
    def principal_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AccessPolicyAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_scope: Optional[pulumi.Input[Union[AccessPolicyAssociationAccessScopeArgs, AccessPolicyAssociationAccessScopeArgsDict]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., principal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccessPolicyAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_scope: Optional[pulumi.Input[Union[AccessPolicyAssociationAccessScopeArgs, AccessPolicyAssociationAccessScopeArgsDict]]] = ..., associated_at: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., modified_at: Optional[pulumi.Input[_builtins.str]] = ..., policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., principal_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> AccessPolicyAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessScope")
    def access_scope(self) -> pulumi.Output[outputs.AccessPolicyAssociationAccessScope]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedAt")
    def associated_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


