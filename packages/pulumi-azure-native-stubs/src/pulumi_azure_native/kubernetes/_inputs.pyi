

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AadProfileArgs', 'AadProfileArgsDict', 'ArcAgentProfileArgs', 'ArcAgentProfileArgsDict', 'ConnectedClusterIdentityArgs', 'ConnectedClusterIdentityArgsDict', 'SystemComponentArgs', 'SystemComponentArgsDict']
class AadProfileArgsDict(TypedDict):
    
    admin_group_object_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enable_azure_rbac: NotRequired[pulumi.Input[_builtins.bool]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AadProfileArgs:
    def __init__(__self__, *, admin_group_object_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enable_azure_rbac: Optional[pulumi.Input[_builtins.bool]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminGroupObjectIDs")
    def admin_group_object_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @admin_group_object_ids.setter
    def admin_group_object_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAzureRBAC")
    def enable_azure_rbac(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_azure_rbac.setter
    def enable_azure_rbac(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantID")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ArcAgentProfileArgsDict(TypedDict):
    
    agent_auto_upgrade: NotRequired[pulumi.Input[Union[_builtins.str, AutoUpgradeOptions]]]
    desired_agent_version: NotRequired[pulumi.Input[_builtins.str]]
    system_components: NotRequired[pulumi.Input[Sequence[pulumi.Input[SystemComponentArgsDict]]]]


@pulumi.input_type
class ArcAgentProfileArgs:
    def __init__(__self__, *, agent_auto_upgrade: Optional[pulumi.Input[Union[_builtins.str, AutoUpgradeOptions]]] = ..., desired_agent_version: Optional[pulumi.Input[_builtins.str]] = ..., system_components: Optional[pulumi.Input[Sequence[pulumi.Input[SystemComponentArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentAutoUpgrade")
    def agent_auto_upgrade(self) -> Optional[pulumi.Input[Union[_builtins.str, AutoUpgradeOptions]]]:
        
        ...
    
    @agent_auto_upgrade.setter
    def agent_auto_upgrade(self, value: Optional[pulumi.Input[Union[_builtins.str, AutoUpgradeOptions]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredAgentVersion")
    def desired_agent_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_agent_version.setter
    def desired_agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemComponents")
    def system_components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SystemComponentArgs]]]]:
        
        ...
    
    @system_components.setter
    def system_components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SystemComponentArgs]]]]): # -> None:
        ...
    


class ConnectedClusterIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[ResourceIdentityType]


@pulumi.input_type
class ConnectedClusterIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[ResourceIdentityType]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[ResourceIdentityType]): # -> None:
        ...
    


class SystemComponentArgsDict(TypedDict):
    
    major_version: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    user_specified_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SystemComponentArgs:
    def __init__(__self__, *, major_version: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., user_specified_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="majorVersion")
    def major_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @major_version.setter
    def major_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSpecifiedVersion")
    def user_specified_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_specified_version.setter
    def user_specified_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


