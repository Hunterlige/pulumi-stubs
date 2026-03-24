

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
__all__ = ['VpcBlockPublicAccessOptionsArgs', 'VpcBlockPublicAccessOptions']
@pulumi.input_type
class VpcBlockPublicAccessOptionsArgs:
    def __init__(__self__, *, internet_gateway_block_mode: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[VpcBlockPublicAccessOptionsTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGatewayBlockMode")
    def internet_gateway_block_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @internet_gateway_block_mode.setter
    def internet_gateway_block_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[VpcBlockPublicAccessOptionsTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[VpcBlockPublicAccessOptionsTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _VpcBlockPublicAccessOptionsState:
    def __init__(__self__, *, aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., aws_region: Optional[pulumi.Input[_builtins.str]] = ..., internet_gateway_block_mode: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[VpcBlockPublicAccessOptionsTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_region.setter
    def aws_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGatewayBlockMode")
    def internet_gateway_block_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @internet_gateway_block_mode.setter
    def internet_gateway_block_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[VpcBlockPublicAccessOptionsTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[VpcBlockPublicAccessOptionsTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VpcBlockPublicAccessOptions(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., internet_gateway_block_mode: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[VpcBlockPublicAccessOptionsTimeoutsArgs, VpcBlockPublicAccessOptionsTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcBlockPublicAccessOptionsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., aws_region: Optional[pulumi.Input[_builtins.str]] = ..., internet_gateway_block_mode: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[VpcBlockPublicAccessOptionsTimeoutsArgs, VpcBlockPublicAccessOptionsTimeoutsArgsDict]]] = ...) -> VpcBlockPublicAccessOptions:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGatewayBlockMode")
    def internet_gateway_block_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.VpcBlockPublicAccessOptionsTimeouts]]:
        ...
    


