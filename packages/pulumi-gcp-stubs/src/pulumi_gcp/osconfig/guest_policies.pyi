

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GuestPoliciesArgs', 'GuestPolicies']
@pulumi.input_type
class GuestPoliciesArgs:
    def __init__(__self__, *, assignment: pulumi.Input[GuestPoliciesAssignmentArgs], guest_policy_id: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., package_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageRepositoryArgs]]]] = ..., packages: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., recipes: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assignment(self) -> pulumi.Input[GuestPoliciesAssignmentArgs]:
        
        ...
    
    @assignment.setter
    def assignment(self, value: pulumi.Input[GuestPoliciesAssignmentArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestPolicyId")
    def guest_policy_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @guest_policy_id.setter
    def guest_policy_id(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageRepositories")
    def package_repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageRepositoryArgs]]]]:
        
        ...
    
    @package_repositories.setter
    def package_repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageRepositoryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def packages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageArgs]]]]:
        
        ...
    
    @packages.setter
    def packages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageArgs]]]]): # -> None:
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
    def recipes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeArgs]]]]:
        
        ...
    
    @recipes.setter
    def recipes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _GuestPoliciesState:
    def __init__(__self__, *, assignment: Optional[pulumi.Input[GuestPoliciesAssignmentArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., guest_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., package_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageRepositoryArgs]]]] = ..., packages: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., recipes: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeArgs]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assignment(self) -> Optional[pulumi.Input[GuestPoliciesAssignmentArgs]]:
        
        ...
    
    @assignment.setter
    def assignment(self, value: Optional[pulumi.Input[GuestPoliciesAssignmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestPolicyId")
    def guest_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @guest_policy_id.setter
    def guest_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageRepositories")
    def package_repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageRepositoryArgs]]]]:
        
        ...
    
    @package_repositories.setter
    def package_repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageRepositoryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def packages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageArgs]]]]:
        
        ...
    
    @packages.setter
    def packages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesPackageArgs]]]]): # -> None:
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
    def recipes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeArgs]]]]:
        
        ...
    
    @recipes.setter
    def recipes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GuestPoliciesRecipeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:osconfig/guestPolicies:GuestPolicies")
class GuestPolicies(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assignment: Optional[pulumi.Input[Union[GuestPoliciesAssignmentArgs, GuestPoliciesAssignmentArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., guest_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., package_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GuestPoliciesPackageRepositoryArgs, GuestPoliciesPackageRepositoryArgsDict]]]]] = ..., packages: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GuestPoliciesPackageArgs, GuestPoliciesPackageArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., recipes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GuestPoliciesRecipeArgs, GuestPoliciesRecipeArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GuestPoliciesArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., assignment: Optional[pulumi.Input[Union[GuestPoliciesAssignmentArgs, GuestPoliciesAssignmentArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., guest_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., package_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GuestPoliciesPackageRepositoryArgs, GuestPoliciesPackageRepositoryArgsDict]]]]] = ..., packages: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GuestPoliciesPackageArgs, GuestPoliciesPackageArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., recipes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GuestPoliciesRecipeArgs, GuestPoliciesRecipeArgsDict]]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> GuestPolicies:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assignment(self) -> pulumi.Output[outputs.GuestPoliciesAssignment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestPolicyId")
    def guest_policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageRepositories")
    def package_repositories(self) -> pulumi.Output[Optional[Sequence[outputs.GuestPoliciesPackageRepository]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def packages(self) -> pulumi.Output[Optional[Sequence[outputs.GuestPoliciesPackage]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recipes(self) -> pulumi.Output[Optional[Sequence[outputs.GuestPoliciesRecipe]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


