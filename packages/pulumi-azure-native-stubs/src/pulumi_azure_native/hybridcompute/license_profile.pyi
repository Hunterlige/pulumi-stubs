

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LicenseProfileArgs', 'LicenseProfile']
@pulumi.input_type
class LicenseProfileArgs:
    def __init__(__self__, *, machine_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], assigned_license: Optional[pulumi.Input[_builtins.str]] = ..., license_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., product_features: Optional[pulumi.Input[Sequence[pulumi.Input[ProductFeatureArgs]]]] = ..., product_type: Optional[pulumi.Input[Union[_builtins.str, LicenseProfileProductType]]] = ..., software_assurance_customer: Optional[pulumi.Input[_builtins.bool]] = ..., subscription_status: Optional[pulumi.Input[Union[_builtins.str, LicenseProfileSubscriptionStatus]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @machine_name.setter
    def machine_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedLicense")
    def assigned_license(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assigned_license.setter
    def assigned_license(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseProfileName")
    def license_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_profile_name.setter
    def license_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFeatures")
    def product_features(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProductFeatureArgs]]]]:
        
        ...
    
    @product_features.setter
    def product_features(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ProductFeatureArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productType")
    def product_type(self) -> Optional[pulumi.Input[Union[_builtins.str, LicenseProfileProductType]]]:
        
        ...
    
    @product_type.setter
    def product_type(self, value: Optional[pulumi.Input[Union[_builtins.str, LicenseProfileProductType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceCustomer")
    def software_assurance_customer(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @software_assurance_customer.setter
    def software_assurance_customer(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionStatus")
    def subscription_status(self) -> Optional[pulumi.Input[Union[_builtins.str, LicenseProfileSubscriptionStatus]]]:
        
        ...
    
    @subscription_status.setter
    def subscription_status(self, value: Optional[pulumi.Input[Union[_builtins.str, LicenseProfileSubscriptionStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:hybridcompute:LicenseProfile")
class LicenseProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assigned_license: Optional[pulumi.Input[_builtins.str]] = ..., license_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., machine_name: Optional[pulumi.Input[_builtins.str]] = ..., product_features: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ProductFeatureArgs, ProductFeatureArgsDict]]]]] = ..., product_type: Optional[pulumi.Input[Union[_builtins.str, LicenseProfileProductType]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., software_assurance_customer: Optional[pulumi.Input[_builtins.bool]] = ..., subscription_status: Optional[pulumi.Input[Union[_builtins.str, LicenseProfileSubscriptionStatus]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LicenseProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> LicenseProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedLicense")
    def assigned_license(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedLicenseImmutableId")
    def assigned_license_immutable_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingEndDate")
    def billing_end_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingStartDate")
    def billing_start_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disenrollmentDate")
    def disenrollment_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enrollmentDate")
    def enrollment_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> pulumi.Output[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="esuEligibility")
    def esu_eligibility(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="esuKeyState")
    def esu_key_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="esuKeys")
    def esu_keys(self) -> pulumi.Output[Sequence[outputs.EsuKeyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFeatures")
    def product_features(self) -> pulumi.Output[Optional[Sequence[outputs.ProductFeatureResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productType")
    def product_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverType")
    def server_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareAssuranceCustomer")
    def software_assurance_customer(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionStatus")
    def subscription_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


