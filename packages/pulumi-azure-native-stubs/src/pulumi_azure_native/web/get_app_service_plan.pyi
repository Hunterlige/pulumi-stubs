

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAppServicePlanResult', 'AwaitableGetAppServicePlanResult', 'get_app_service_plan', 'get_app_service_plan_output']
@pulumi.output_type
class GetAppServicePlanResult:
    
    def __init__(__self__, async_scaling_enabled=..., azure_api_version=..., elastic_scale_enabled=..., extended_location=..., free_offer_expiration_time=..., geo_region=..., hosting_environment_profile=..., hyper_v=..., id=..., is_spot=..., is_xenon=..., kind=..., kube_environment_profile=..., location=..., maximum_elastic_worker_count=..., maximum_number_of_workers=..., name=..., number_of_sites=..., number_of_workers=..., per_site_scaling=..., provisioning_state=..., reserved=..., resource_group=..., sku=..., spot_expiration_time=..., status=..., subscription=..., tags=..., target_worker_count=..., target_worker_size_id=..., type=..., worker_tier_name=..., zone_redundant=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncScalingEnabled")
    def async_scaling_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticScaleEnabled")
    def elastic_scale_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="freeOfferExpirationTime")
    def free_offer_expiration_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoRegion")
    def geo_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostingEnvironmentProfile")
    def hosting_environment_profile(self) -> Optional[outputs.HostingEnvironmentProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hyperV")
    def hyper_v(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSpot")
    def is_spot(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isXenon")
    def is_xenon(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeEnvironmentProfile")
    def kube_environment_profile(self) -> Optional[outputs.KubeEnvironmentProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumElasticWorkerCount")
    def maximum_elastic_worker_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumNumberOfWorkers")
    def maximum_number_of_workers(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfSites")
    def number_of_sites(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perSiteScaling")
    def per_site_scaling(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reserved(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuDescriptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotExpirationTime")
    def spot_expiration_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscription(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetWorkerCount")
    def target_worker_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetWorkerSizeId")
    def target_worker_size_id(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerTierName")
    def worker_tier_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[_builtins.bool]:
        
        ...
    


class AwaitableGetAppServicePlanResult(GetAppServicePlanResult):
    def __await__(self): # -> Generator[Never, Any, GetAppServicePlanResult]:
        ...
    


def get_app_service_plan(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAppServicePlanResult:
    
    ...

def get_app_service_plan_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAppServicePlanResult]:
    
    ...

