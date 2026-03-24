

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EncryptionControlArgs', 'EncryptionControl']
@pulumi.input_type
class EncryptionControlArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str], vpc_id: pulumi.Input[_builtins.str], egress_only_internet_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., elastic_file_system_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., internet_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., lambda_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[EncryptionControlTimeoutsArgs]] = ..., virtual_private_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., vpc_lattice_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_exclusion: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayExclusion")
    def egress_only_internet_gateway_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @egress_only_internet_gateway_exclusion.setter
    def egress_only_internet_gateway_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticFileSystemExclusion")
    def elastic_file_system_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @elastic_file_system_exclusion.setter
    def elastic_file_system_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGatewayExclusion")
    def internet_gateway_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @internet_gateway_exclusion.setter
    def internet_gateway_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaExclusion")
    def lambda_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lambda_exclusion.setter
    def lambda_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayExclusion")
    def nat_gateway_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nat_gateway_exclusion.setter
    def nat_gateway_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[EncryptionControlTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[EncryptionControlTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualPrivateGatewayExclusion")
    def virtual_private_gateway_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_private_gateway_exclusion.setter
    def virtual_private_gateway_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLatticeExclusion")
    def vpc_lattice_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_lattice_exclusion.setter
    def vpc_lattice_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringExclusion")
    def vpc_peering_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_peering_exclusion.setter
    def vpc_peering_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _EncryptionControlState:
    def __init__(__self__, *, egress_only_internet_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., elastic_file_system_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., internet_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., lambda_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_exclusions: Optional[pulumi.Input[EncryptionControlResourceExclusionsArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_message: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[EncryptionControlTimeoutsArgs]] = ..., virtual_private_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_lattice_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_exclusion: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayExclusion")
    def egress_only_internet_gateway_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @egress_only_internet_gateway_exclusion.setter
    def egress_only_internet_gateway_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticFileSystemExclusion")
    def elastic_file_system_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @elastic_file_system_exclusion.setter
    def elastic_file_system_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGatewayExclusion")
    def internet_gateway_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @internet_gateway_exclusion.setter
    def internet_gateway_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaExclusion")
    def lambda_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lambda_exclusion.setter
    def lambda_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayExclusion")
    def nat_gateway_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nat_gateway_exclusion.setter
    def nat_gateway_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceExclusions")
    def resource_exclusions(self) -> Optional[pulumi.Input[EncryptionControlResourceExclusionsArgs]]:
        
        ...
    
    @resource_exclusions.setter
    def resource_exclusions(self, value: Optional[pulumi.Input[EncryptionControlResourceExclusionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[EncryptionControlTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[EncryptionControlTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualPrivateGatewayExclusion")
    def virtual_private_gateway_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_private_gateway_exclusion.setter
    def virtual_private_gateway_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLatticeExclusion")
    def vpc_lattice_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_lattice_exclusion.setter
    def vpc_lattice_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringExclusion")
    def vpc_peering_exclusion(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_peering_exclusion.setter
    def vpc_peering_exclusion(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/encryptionControl:EncryptionControl")
class EncryptionControl(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., egress_only_internet_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., elastic_file_system_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., internet_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., lambda_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[EncryptionControlTimeoutsArgs, EncryptionControlTimeoutsArgsDict]]] = ..., virtual_private_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_lattice_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EncryptionControlArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., egress_only_internet_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., elastic_file_system_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., internet_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., lambda_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_exclusions: Optional[pulumi.Input[Union[EncryptionControlResourceExclusionsArgs, EncryptionControlResourceExclusionsArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_message: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[EncryptionControlTimeoutsArgs, EncryptionControlTimeoutsArgsDict]]] = ..., virtual_private_gateway_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_lattice_exclusion: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_exclusion: Optional[pulumi.Input[_builtins.str]] = ...) -> EncryptionControl:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressOnlyInternetGatewayExclusion")
    def egress_only_internet_gateway_exclusion(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticFileSystemExclusion")
    def elastic_file_system_exclusion(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGatewayExclusion")
    def internet_gateway_exclusion(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaExclusion")
    def lambda_exclusion(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayExclusion")
    def nat_gateway_exclusion(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceExclusions")
    def resource_exclusions(self) -> pulumi.Output[outputs.EncryptionControlResourceExclusions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Output[_builtins.str]:
        
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
    def timeouts(self) -> pulumi.Output[Optional[outputs.EncryptionControlTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualPrivateGatewayExclusion")
    def virtual_private_gateway_exclusion(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLatticeExclusion")
    def vpc_lattice_exclusion(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringExclusion")
    def vpc_peering_exclusion(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


