

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
__all__ = ['SQuotaPreferenceArgs', 'SQuotaPreference']
@pulumi.input_type
class SQuotaPreferenceArgs:
    def __init__(__self__, *, quota_config: pulumi.Input[SQuotaPreferenceQuotaConfigArgs], contact_email: Optional[pulumi.Input[_builtins.str]] = ..., dimensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ignore_safety_checks: Optional[pulumi.Input[_builtins.str]] = ..., justification: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., quota_id: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaConfig")
    def quota_config(self) -> pulumi.Input[SQuotaPreferenceQuotaConfigArgs]:
        
        ...
    
    @quota_config.setter
    def quota_config(self, value: pulumi.Input[SQuotaPreferenceQuotaConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactEmail")
    def contact_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_email.setter
    def contact_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreSafetyChecks")
    def ignore_safety_checks(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ignore_safety_checks.setter
    def ignore_safety_checks(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def justification(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @justification.setter
    def justification(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @quota_id.setter
    def quota_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SQuotaPreferenceState:
    def __init__(__self__, *, contact_email: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dimensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., ignore_safety_checks: Optional[pulumi.Input[_builtins.str]] = ..., justification: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., quota_config: Optional[pulumi.Input[SQuotaPreferenceQuotaConfigArgs]] = ..., quota_id: Optional[pulumi.Input[_builtins.str]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactEmail")
    def contact_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_email.setter
    def contact_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def dimensions(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreSafetyChecks")
    def ignore_safety_checks(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ignore_safety_checks.setter
    def ignore_safety_checks(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def justification(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @justification.setter
    def justification(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaConfig")
    def quota_config(self) -> Optional[pulumi.Input[SQuotaPreferenceQuotaConfigArgs]]:
        
        ...
    
    @quota_config.setter
    def quota_config(self, value: Optional[pulumi.Input[SQuotaPreferenceQuotaConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @quota_id.setter
    def quota_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:cloudquota/sQuotaPreference:SQuotaPreference")
class SQuotaPreference(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., contact_email: Optional[pulumi.Input[_builtins.str]] = ..., dimensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ignore_safety_checks: Optional[pulumi.Input[_builtins.str]] = ..., justification: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., quota_config: Optional[pulumi.Input[Union[SQuotaPreferenceQuotaConfigArgs, SQuotaPreferenceQuotaConfigArgsDict]]] = ..., quota_id: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SQuotaPreferenceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., contact_email: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dimensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., ignore_safety_checks: Optional[pulumi.Input[_builtins.str]] = ..., justification: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., quota_config: Optional[pulumi.Input[Union[SQuotaPreferenceQuotaConfigArgs, SQuotaPreferenceQuotaConfigArgsDict]]] = ..., quota_id: Optional[pulumi.Input[_builtins.str]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> SQuotaPreference:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactEmail")
    def contact_email(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreSafetyChecks")
    def ignore_safety_checks(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def justification(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaConfig")
    def quota_config(self) -> pulumi.Output[outputs.SQuotaPreferenceQuotaConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


