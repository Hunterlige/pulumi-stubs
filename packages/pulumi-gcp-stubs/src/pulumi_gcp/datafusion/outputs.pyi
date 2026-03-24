

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceAccelerator', 'InstanceCryptoKeyConfig', 'InstanceEventPublishConfig', 'InstanceNetworkConfig', 'InstanceNetworkConfigPrivateServiceConnectConfig']
@pulumi.output_type
class InstanceAccelerator(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_type: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstanceCryptoKeyConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_reference: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyReference")
    def key_reference(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstanceEventPublishConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool, topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstanceNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_type: Optional[_builtins.str] = ..., ip_allocation: Optional[_builtins.str] = ..., network: Optional[_builtins.str] = ..., private_service_connect_config: Optional[outputs.InstanceNetworkConfigPrivateServiceConnectConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAllocation")
    def ip_allocation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateServiceConnectConfig")
    def private_service_connect_config(self) -> Optional[outputs.InstanceNetworkConfigPrivateServiceConnectConfig]:
        
        ...
    


@pulumi.output_type
class InstanceNetworkConfigPrivateServiceConnectConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, effective_unreachable_cidr_block: Optional[_builtins.str] = ..., network_attachment: Optional[_builtins.str] = ..., unreachable_cidr_block: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveUnreachableCidrBlock")
    def effective_unreachable_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unreachableCidrBlock")
    def unreachable_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    


