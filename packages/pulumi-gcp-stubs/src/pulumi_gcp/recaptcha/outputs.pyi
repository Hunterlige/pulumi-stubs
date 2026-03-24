

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EnterpriseKeyAndroidSettings', 'EnterpriseKeyIosSettings', 'EnterpriseKeyTestingOptions', 'EnterpriseKeyWafSettings', 'EnterpriseKeyWebSettings']
@pulumi.output_type
class EnterpriseKeyAndroidSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_all_package_names: Optional[_builtins.bool] = ..., allowed_package_names: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAllPackageNames")
    def allow_all_package_names(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPackageNames")
    def allowed_package_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class EnterpriseKeyIosSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_all_bundle_ids: Optional[_builtins.bool] = ..., allowed_bundle_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAllBundleIds")
    def allow_all_bundle_ids(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedBundleIds")
    def allowed_bundle_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class EnterpriseKeyTestingOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, testing_challenge: Optional[_builtins.str] = ..., testing_score: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testingChallenge")
    def testing_challenge(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testingScore")
    def testing_score(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class EnterpriseKeyWafSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, waf_feature: _builtins.str, waf_service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wafFeature")
    def waf_feature(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wafService")
    def waf_service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EnterpriseKeyWebSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, integration_type: _builtins.str, allow_all_domains: Optional[_builtins.bool] = ..., allow_amp_traffic: Optional[_builtins.bool] = ..., allowed_domains: Optional[Sequence[_builtins.str]] = ..., challenge_security_preference: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAllDomains")
    def allow_all_domains(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAmpTraffic")
    def allow_amp_traffic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedDomains")
    def allowed_domains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="challengeSecurityPreference")
    def challenge_security_preference(self) -> Optional[_builtins.str]:
        
        ...
    


