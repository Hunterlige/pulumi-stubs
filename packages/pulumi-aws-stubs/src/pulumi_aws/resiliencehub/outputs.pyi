

import builtins as _builtins
import sys
import pulumi
from typing import Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResiliencyPolicyPolicy', 'ResiliencyPolicyPolicyAz', 'ResiliencyPolicyPolicyHardware', 'ResiliencyPolicyPolicyRegion', 'ResiliencyPolicyPolicySoftware', 'ResiliencyPolicyTimeouts']
@pulumi.output_type
class ResiliencyPolicyPolicy(dict):
    def __init__(__self__, *, az: Optional[outputs.ResiliencyPolicyPolicyAz] = ..., hardware: Optional[outputs.ResiliencyPolicyPolicyHardware] = ..., region: Optional[outputs.ResiliencyPolicyPolicyRegion] = ..., software: Optional[outputs.ResiliencyPolicyPolicySoftware] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def az(self) -> Optional[outputs.ResiliencyPolicyPolicyAz]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hardware(self) -> Optional[outputs.ResiliencyPolicyPolicyHardware]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[outputs.ResiliencyPolicyPolicyRegion]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def software(self) -> Optional[outputs.ResiliencyPolicyPolicySoftware]:
        
        ...
    


@pulumi.output_type
class ResiliencyPolicyPolicyAz(dict):
    def __init__(__self__, *, rpo: _builtins.str, rto: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rto(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ResiliencyPolicyPolicyHardware(dict):
    def __init__(__self__, *, rpo: _builtins.str, rto: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rto(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ResiliencyPolicyPolicyRegion(dict):
    def __init__(__self__, *, rpo: Optional[_builtins.str] = ..., rto: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rto(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResiliencyPolicyPolicySoftware(dict):
    def __init__(__self__, *, rpo: _builtins.str, rto: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rto(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ResiliencyPolicyTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


