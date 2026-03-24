

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ZoneArgs', 'Zone']
@pulumi.input_type
class ZoneArgs:
    def __init__(__self__, *, comment: Optional[pulumi.Input[_builtins.str]] = ..., delegation_set_id: Optional[pulumi.Input[_builtins.str]] = ..., enable_accelerated_recovery: Optional[pulumi.Input[_builtins.bool]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[ZoneVpcArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegationSetId")
    def delegation_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delegation_set_id.setter
    def delegation_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedRecovery")
    def enable_accelerated_recovery(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_accelerated_recovery.setter
    def enable_accelerated_recovery(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ZoneVpcArgs]]]]:
        
        ...
    
    @vpcs.setter
    def vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ZoneVpcArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ZoneState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., delegation_set_id: Optional[pulumi.Input[_builtins.str]] = ..., enable_accelerated_recovery: Optional[pulumi.Input[_builtins.bool]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., primary_name_server: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[ZoneVpcArgs]]]] = ..., zone_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegationSetId")
    def delegation_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delegation_set_id.setter
    def delegation_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedRecovery")
    def enable_accelerated_recovery(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_accelerated_recovery.setter
    def enable_accelerated_recovery(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @name_servers.setter
    def name_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryNameServer")
    def primary_name_server(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_name_server.setter
    def primary_name_server(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ZoneVpcArgs]]]]:
        
        ...
    
    @vpcs.setter
    def vpcs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ZoneVpcArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:route53/zone:Zone")
class Zone(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., delegation_set_id: Optional[pulumi.Input[_builtins.str]] = ..., enable_accelerated_recovery: Optional[pulumi.Input[_builtins.bool]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ZoneVpcArgs, ZoneVpcArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ZoneArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., comment: Optional[pulumi.Input[_builtins.str]] = ..., delegation_set_id: Optional[pulumi.Input[_builtins.str]] = ..., enable_accelerated_recovery: Optional[pulumi.Input[_builtins.bool]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., primary_name_server: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ZoneVpcArgs, ZoneVpcArgsDict]]]]] = ..., zone_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Zone:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegationSetId")
    def delegation_set_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedRecovery")
    def enable_accelerated_recovery(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryNameServer")
    def primary_name_server(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpcs(self) -> pulumi.Output[Optional[Sequence[outputs.ZoneVpc]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


